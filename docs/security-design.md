Security Design
SmartThumb SA implements AWS security best practices to protect uploaded images, processed thumbnails and AI-generated metadata.

1. Identity and Access Management (IAM)
* AWS Lambda uses a dedicated execution role: `SmartThumbLambdaExecutionRole`.
* Permissions are scoped to the services and resources required for image processing.
* No AWS access keys or credentials are hardcoded into the application.

2. Amazon S3 Security
* Source bucket: `smartthumb-*****`.
* Destination bucket: `smartthumb******`.
* Both buckets are private and do not require public access.
* Lambda reads images from the source bucket and writes processed thumbnails and JSON metadata to the destination bucket.

3. AWS Lambda Security
* Lambda accesses AWS services through its assigned IAM execution role.
* The function processes uploaded images without exposing a public application endpoint.
* Image processing is triggered automatically through Amazon S3 events.

4. Amazon Rekognition
* Lambda uses IAM permissions to invoke Amazon Rekognition's `DetectLabels` API.
* AI-generated labels and confidence scores are stored as JSON files in the destination S3 bucket.

5. Monitoring and Logging
* Amazon CloudWatch records Lambda execution logs and errors.
* Processing activity can be reviewed to identify failures and troubleshoot issues.

6. Security Improvements
Potential future enhancements include:
* Enforcing HTTPS-only requests through S3 bucket policies.
* Implementing additional file-type and upload-size validation.
* Configuring CloudWatch alarms for processing failures.
* Periodically reviewing IAM permissions and access logs.

In Conclusion
SmartThumb SA follows a security-focused serverless design by combining private S3 storage, IAM-based access control and CloudWatch monitoring.
