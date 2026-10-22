import boto3
import io
import json
import os
from urllib.parse import unquote_plus

from PIL import Image, ImageOps, UnidentifiedImageError

s3 = boto3.client("s3")
rekognition = boto3.client("rekognition")

OUTPUT_BUCKET = os.environ["OUTPUT_BUCKET"]
MAX_SIZE = (300, 300)

def detect_image_labels(bucket, key):
    response = rekognition.detect_labels(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": key
            }
        },
        MaxLabels=10,
        MinConfidence=75
    )

    return [
        {
            "label": item["Name"],
            "confidence": round(item["Confidence"], 2)
        }
        for item in response["Labels"]
    ]

def lambda_handler(event, context):

    for record in event["Records"]:

        # 1. Identify the uploaded image
        source_bucket = record["s3"]["bucket"]["name"]
        object_key = unquote_plus(
            record["s3"]["object"]["key"]
        )

        print(f"Processing image: {object_key}")

        # 2. Download the original image from S3
        response = s3.get_object(
            Bucket=source_bucket,
            Key=object_key
        )

        original_bytes = response["Body"].read()

        # 3. Open and validate the image
        try:
            with Image.open(io.BytesIO(original_bytes)) as image:

                if image.format not in ("JPEG", "PNG"):
                    raise ValueError("Only JPEG and PNG images are supported")

                original_dimensions = image.size

                # Correct orientation using EXIF metadata
                image = ImageOps.exif_transpose(image)

                # 4. Resize without distorting the image
                image.thumbnail(MAX_SIZE)

                # Convert to RGB for JPEG output
                if image.mode in ("RGBA", "LA") or (
                    image.mode == "P" and "transparency" in image.info
                ):
                    image = image.convert("RGBA")

                    background = Image.new(
                        "RGB",
                        image.size,
                        (255, 255, 255)
                    )

                    background.paste(
                        image,
                        mask=image.getchannel("A")
                    )

                    image = background
                else:
                    image = image.convert("RGB")

                # 5. Save thumbnail in memory
                output_buffer = io.BytesIO()

                image.save(
                    output_buffer,
                    format="JPEG",
                    quality=80,
                    optimize=True
                )

                thumbnail_bytes = output_buffer.getvalue()
                thumbnail_dimensions = image.size

        except (UnidentifiedImageError, ValueError) as error:
            print(f"Invalid image: {object_key}: {error}")
            raise

        # 6. Create output filename
        filename = object_key.rsplit("/", 1)[-1]
        base_name = filename.rsplit(".", 1)[0]

        output_key = f"{base_name}_thumb.jpg"

        # 7. Upload thumbnail to output bucket
        s3.put_object(
            Bucket=OUTPUT_BUCKET,
            Key=output_key,
            Body=thumbnail_bytes,
            ContentType="image/jpeg"
        )

        # 8. Analyse the original image using Amazon Rekognition
        if os.environ.get("ENABLE_REKOGNITION", "false").lower() == "true":

            try:
                # Detect labels in the original image
                labels = detect_image_labels(
                    source_bucket,
                    object_key
                )

                # Prepare JSON metadata
                metadata = {
                    "product_image": object_key,
                    "thumbnail": output_key,
                    "detected_labels": labels
                }

                # Create JSON filename
                labels_key = f"{base_name}_labels.json"

                # Save JSON metadata to S3 output bucket
                s3.put_object(
                    Bucket=OUTPUT_BUCKET,
                    Key=labels_key,
                    Body=json.dumps(metadata, indent=4).encode("utf-8"),
                    ContentType="application/json"
                )

                # Log successful AI processing
                print(
                    json.dumps({
                        "status": "rekognition_success",
                        "image": object_key,
                        "labels_file": labels_key,
                        "ai_labels": labels
                    })
                )

            except Exception as error:
                print(
                    json.dumps({
                        "status": "rekognition_failed",
                        "image": object_key,
                        "error": str(error)
                    })
                )

        # 9. Log processing results
        reduction = (
            (1 - len(thumbnail_bytes) / len(original_bytes)) * 100
        )

        print(
            json.dumps({
                "status": "success",
                "source_image": object_key,
                "output_image": output_key,
                "original_dimensions": original_dimensions,
                "thumbnail_dimensions": thumbnail_dimensions,
                "original_bytes": len(original_bytes),
                "thumbnail_bytes": len(thumbnail_bytes),
                "size_reduction_percent": round(reduction, 2)
            })
        )

    return {
        "statusCode": 200,
        "body": json.dumps("Image processing completed")
    }
