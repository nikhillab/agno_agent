| Service Name                     | Provider | Layer         | Type        | Purpose/Role                                                    | Key Attributes                                    | Confidence |
|----------------------------------|----------|---------------|-------------|-----------------------------------------------------------------|---------------------------------------------------|------------|
| AWS Amplify                      | AWS      | Presentation  | Development | Front-end web/mobile application development and hosting platform | Provides connectivity to backend services, hosting | High       |
| Amazon API Gateway               | AWS      | Presentation  | API         | Creates, publishes, maintains, monitors, and secures APIs       | Acts as an entry point for backend Lambda functions | High       |
| AWS Identity and Access Management | AWS      | Cross-cutting | Security    | Manages permissions for users and AWS services                  | Secures access to resources for services like Lambda and Amplify | High       |
| AWS Lambda                       | AWS      | Application   | Compute     | Serverless compute service for executing backend logic          | Event-driven function, triggered by API Gateway   | High       |
| Amazon DynamoDB                  | AWS      | Data          | Database    | NoSQL database for storing and retrieving application data      | Serverless, key-value and document database       | High       |

**Gaps**

| Gaps                         | Layer         | Description                                       | Confidence |
|------------------------------|---------------|---------------------------------------------------|------------|
| VPC/Networking details       | Cross-cutting | Specific VPC, Subnet, Security Group configurations are not depicted despite being fundamental to AWS deployments | Low        |
| Monitoring & Logging         | Cross-cutting | Common services like CloudWatch or CloudTrail are not explicitly shown for observability | Low        |
| Specific IAM Resources       | Cross-cutting | While IAM is a service, specific IAM Roles/Policies are not detailed for services like Lambda or API Gateway | Medium     |
| DNS/Domain Management        | Presentation  | No service like Route 53 is shown for managing custom domains for Amplify or API Gateway endpoints | Low        |