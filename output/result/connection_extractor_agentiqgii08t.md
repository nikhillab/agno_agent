| Source | Target | Relationship | Details |
|---|---|---|---|
| Users | AWS Amplify | connects_to | Frontend access, HTTPS |
| AWS Amplify | Amazon API Gateway | invokes | API calls |
| Amazon API Gateway | AWS Lambda | invokes | API integration, HTTPS |
| AWS Identity and Access Management | AWS Lambda | grants_permissions_to | IAM Role for execution |
| AWS Lambda | Amazon DynamoDB | connects_to | Data access, AWS SDK |