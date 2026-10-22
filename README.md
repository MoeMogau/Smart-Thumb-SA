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
