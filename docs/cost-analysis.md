Cost Analysis

SmartThumb SA uses a serverless, pay-as-you-go AWS architecture to minimise infrastructure costs.

AWS Services and Cost Considerations

| AWS Service        | Cost Consideration                           
| ------------------ | -------------------------------------------- 
| Amazon S3          | Storage, uploads, retrievals and requests    
| AWS Lambda         | Number of invocations and execution duration 
| Amazon Rekognition | Number of images analysed                    
| Amazon CloudWatch  | Log ingestion, storage and monitoring        
| AWS IAM            | No additional charge for IAM                 

Actual Testing Costs

As of **22 October 2026**, the AWS Billing Dashboard displayed an estimated cost of **$0.00** for the project testing period.

This amount is provisional because AWS billing data may take time to update.

Cost Optimisation
* Serverless services eliminate the need for continuously running servers.
* Lambda executes only when an image is uploaded.
* Images are resized to reduce storage requirements.
* IAM permissions restrict access to necessary resources.
* Amazon Rekognition can be disabled when AI labelling is unnecessary.

Essentially,
SmartThumb SA demonstrates a cost-efficient serverless architecture suitable for small businesses. Actual operating costs will depend on image volumes, storage usage, processing duration and AI recognition requests.
