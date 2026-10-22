SmartThumb SA — Test Cases

SmartThumb SA was tested using five product categories and an invalid text file to verify image processing, AI labelling and error detection.

| Test              | Expected Outcome                 | Result              |
| ----------------- | -------------------------------- | ------------------- |
| Electronics       | Generate thumbnail and AI labels | Passed              |
| Footwear          | Generate thumbnail and AI labels | Passed              |
| Clothing          | Generate thumbnail and AI labels | Passed              |
| Furniture         | Generate thumbnail and AI labels | Passed              |
| Bag               | Generate thumbnail and AI labels | Passed              |
| Invalid text file | Detect unsupported input         | Detected and logged |
| S3 trigger        | Automatically invoke Lambda      | Passed              |
| Output storage    | Save thumbnail and JSON metadata | Passed              |

Validation Criteria
- Thumbnails limited to 300 × 300 pixels, preserving aspect ratio.
- AI-generated labels returned with confidence scores.
- Outputs stored in a separate S3 bucket.
- Processing results and errors recorded in CloudWatch.

Limitations
Testing covered a small sample of images. Further testing is required to establish reliability and performance benchmarks. Invalid-file detection was confirmed, but graceful error handling remains unverified.
