| Service Name | Provider | Layer | Type | Purpose/Role | Key Attributes | Confidence |
|---|---|---|---|---|---|---|
| AWS Cloud | AWS | Cross-cutting | Environment | Overarching cloud environment | N/A | High |
| Availability Zone | AWS | Cross-cutting | Foundational | Logical datacenter for high availability | N/A | High |
| VPC | AWS | Cross-cutting | Networking | Isolated virtual network | CIDR: 10.0.0.0/16 | High |
| Internet Gateway | AWS | Cross-cutting | Networking | Connects VPC to the internet | N/A | High |
| Router | AWS | Cross-cutting | Networking | Handles routing within the VPC | N/A | High |
| Public subnet | AWS | Cross-cutting | Networking | Subnet for public-facing resources | CIDR: 10.0.128.0/20 | High |
| Private subnet | AWS | Cross-cutting | Networking | Subnet for internal/private resources | CIDR: 10.0.0.0/19 | High |
| Route table | AWS | Cross-cutting | Networking | Defines network routes for subnets | Routes to 172.16.0.0/0, 172.16.1.0, 172.16.2.0 | High |
| Network ACL | AWS | Cross-cutting | Security | Stateless network traffic filtering for subnets | N/A | High |
| Security group | AWS | Cross-cutting | Security | Stateful instance-level traffic filtering | N/A | High |
| DSS Automation Node | AWS | Application | Compute | Custom application/compute instance | Located in Public subnet | High |
| DSS Design Node | AWS | Application | Compute | Custom application/compute instance | Located in Public subnet | High |
| DSS API Deployer | AWS | Presentation | Compute | Custom application/API deployment endpoint | Located in Public subnet | High |
| Amazon Redshift | AWS | Data | Data Warehouse | Scalable data warehousing | Located in Private subnet | High |
| Amazon EMR | AWS | Application | Big Data | Managed Hadoop framework for big data processing | Located in Private subnet; CIDR: 10.0.0.0/19 | High |
| Amazon Elastic Kubernetes Service | AWS | Application | Container Orchestration | Managed Kubernetes service | Located in Private subnet | High |
| AWS Identity and Access Management | AWS | Cross-cutting | Security | Manages access to AWS resources | N/A | High |
| Amazon Simple Storage Service | AWS | Data | Storage | Scalable object storage for data lakes/archives | N/A | High |
| AWS Glue | AWS | Application | ETL/Data Integration | Serverless data integration and ETL service | N/A | High |
| Amazon Athena | AWS | Data | Analytics | Interactive query service for S3 data | N/A | High |
| Amazon SageMaker | AWS | Application | Machine Learning | ML model building, training, and deployment | N/A | High |
| Amazon Rekognition | AWS | Application | Machine Learning | Image and video analysis service | N/A | High |
| Amazon Comprehend | AWS | Application | Machine Learning | Natural Language Processing (NLP) service | N/A | High |

| Gaps | Layer | Missing Component | Description | Confidence |
|---|---|---|---|---|
| Load Balancing | Application | Load Balancer (ALB/NLB) | No explicit load balancer for public-facing services (e.g., DSS API Deployer, Automation/Design Nodes) is depicted, which is common for distributing traffic and ensuring high availability. | Medium |
| Monitoring | Cross-cutting | CloudWatch / CloudTrail | No explicit monitoring or logging services are shown for operational visibility. | High |
| DNS Resolution | Cross-cutting | Route 53 | No explicit DNS service is shown for domain management or internal resolution. | High |