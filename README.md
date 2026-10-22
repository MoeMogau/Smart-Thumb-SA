SmartThumb SA
Serverless Image Optimisation and AI-Powered Product Labelling on AWS

SmartThumb SA is an AWS-powered serverless application designed to help small businesses automate product-image processing and organisation.

Small businesses selling products through online marketplaces, social media and digital catalogues often need to manually resize, optimise and categorise product photographs. As their product catalogues grow, these repetitive tasks can become time-consuming and inefficient.

SmartThumb SA addresses this challenge by automatically processing product images when they are uploaded to Amazon S3.

The application uses AWS Lambda and Python's Pillow library to generate optimised thumbnails, while Amazon Rekognition analyses the original images and suggests AI-generated product labels.
The processed thumbnails and structured JSON metadata are stored in a separate Amazon S3 bucket, making them available for future integration with e-commerce platforms and product catalogues.

Objectives:

- Automate product-image processing using an event-driven serverless architecture.
- Generate thumbnails with maximum dimensions of 300 × 300 pixels while preserving aspect ratio.
- Reduce image file sizes to support efficient digital product listings.
- Use Amazon Rekognition to generate AI-assisted product labels.
- Apply AWS IAM permissions to secure access to cloud resources.
- Monitor application execution and errors using Amazon CloudWatch.
- Evaluate processing performance, reliability and estimated AWS operating costs.

AWS Services and Technologies Used:

 Service / Technology  Purpose                                                       
 
 Amazon S3             Stores original product images, thumbnails and JSON metadata. 
 AWS Lambda            Automatically processes uploaded images.                      
 Amazon Rekognition    Detects objects and generates AI-assisted product labels.     
 AWS IAM               Controls permissions between AWS services.                    
 Amazon CloudWatch     Captures execution logs, errors and performance metrics.      
 Python 3.12           Application programming language.                             
 Pillow                Image validation, resizing and optimisation.                  
 Boto3                 AWS SDK for Python used to interact with AWS services.

System Architecture
SmartThumb SA uses an event-driven, serverless AWS architecture. Product images are automatically processed when uploaded to a private Amazon S3 source bucket, eliminating the need for continuously running servers.

Processing Workflow:

1. Product Image Upload — Amazon S3
A user uploads a JPEG or PNG product photograph to the source S3 bucket. The bucket is private, and an `ObjectCreated` event notification automatically invokes AWS Lambda.

2. Image Processing — AWS Lambda and Pillow
The Lambda function retrieves the uploaded image using Boto3 and processes it using Python's Pillow library.

The function:
- Validates the image format.
- Corrects image orientation using EXIF metadata.
- Resizes the image to fit within 300 × 300 pixels while preserving its aspect ratio.
- Converts the processed image to JPEG format.
- Optimises the output using JPEG quality settings.

3. Thumbnail Storage — Amazon S3
The optimised thumbnail is saved in a separate private S3 output bucket using the naming convention:
`original_filename_thumb.jpg`, Separating the source and output buckets prevents generated thumbnails from triggering the processing function recursively.

4. AI-Powered Product Labelling — Amazon Rekognition
After thumbnail generation, the Lambda function invokes Amazon Rekognition's `DetectLabels` API to analyse the original product image & returns suggested labels and confidence scores. These are AI-generated suggestions rather than guaranteed product classifications.

The implementation uses:
- Maximum labels: `10`
- Minimum confidence: `75%`

5. JSON Metadata Generation
The Lambda function saves the detected labels as a JSON file in the output S3 bucket.

The metadata follows the naming convention:
`original_filename_labels.json`and Each metadata file includes:
- Original image filename.
- Generated thumbnail filename.
- AI-detected labels.
- Confidence scores.


6. Monitoring — Amazon CloudWatch
AWS Lambda automatically sends execution logs, execution-duration and memory-usage information to Amazon CloudWatch.

The application records information including:
- Original and thumbnail dimensions.
- Original and processed file sizes.
- Percentage image-size reduction.
- AI labelling results.
- Processing errors.

Security
AWS Identity and Access Management (IAM) controls access between services.

The Lambda execution role grants permissions required to read source images, write processed outputs, invoke Amazon Rekognition and publish execution logs. Both S3 buckets are private, and AWS credentials are not embedded in the application source code.

Deployment Instructions

1. Amazon S3: Create two private buckets for source images and processed outputs.
2. AWS IAM: Create a Lambda execution role with permissions to read source images, write outputs, invoke Rekognition and publish CloudWatch logs.
3. AWS Lambda: Create a Python 3.12 function with 512 MB memory and a 30-second timeout.
4. Dependencies: Package Pillow in a compatible Lambda layer and attach it to the function.
5. Environment Variables: Configure:
   * `OUTPUT_BUCKET` — Name of the destination S3 bucket.
   * `ENABLE_REKOGNITION` — Set to `true`.
6. S3 Trigger: Configure an `ObjectCreated` event notification on the source bucket to invoke Lambda.
7. Testing: Upload a JPEG or PNG image and verify that the thumbnail and JSON metadata appear in the output bucket.
8. Monitoring: Review execution logs in Amazon CloudWatch.

Create AWS resources in the same supported Region. AWS charges may apply.
