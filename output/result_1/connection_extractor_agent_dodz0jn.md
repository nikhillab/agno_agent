| Source | Target | Relationship | Details |
|---|---|---|---|
| AWS Cloud | Availability Zone | contains | Logical grouping |
| Availability Zone | VPC | contains | Logical grouping |
| VPC | Public subnet | contains | CIDR 10.0.128.0/20 |
| VPC | Private subnet | contains | CIDR 10.0.0.0/19 |
| Public subnet | DSS Automation Node | hosts | |
| Public subnet | DSS Design Node | hosts | |
| Public subnet | DSS API Deployer | hosts | |
| Private subnet | Amazon Redshift | hosts | |
| Private subnet | Amazon EMR | hosts | |
| Private subnet | Amazon Elastic Kubernetes Service | hosts | |
| Internet gateway | Router | routes_traffic | Bidirectional |
| Router | Internet gateway | routes_traffic | Bidirectional |
| Router | Public subnet Route table | routes_traffic | Bidirectional |
| Public subnet Route table | Router | routes_traffic | Bidirectional |
| Router | Private subnet Route table | routes_traffic | Bidirectional |
| Private subnet Route table | Router | routes_traffic | Bidirectional |
| Public subnet | Network ACL | associated_with | |
| Private subnet | Network ACL | associated_with | |
| Public subnet | Route table | associated_with | |
| Private subnet | Route table | associated_with | |
| DSS Automation Node | Security group (Public) | secured_by | Bidirectional arrow with Security Group |
| DSS Design Node | Security group (Public) | secured_by | Bidirectional arrow with Security Group |
| DSS API Deployer | Security group (Public) | secured_by | Bidirectional arrow with Security Group |
| Amazon Redshift | Security group (Redshift) | secured_by | Bidirectional arrow with Security Group |
| Amazon EMR | Security group (EMR) | secured_by | Bidirectional arrow with Security Group |
| Amazon Elastic Kubernetes Service | Security group (EKS) | secured_by | Bidirectional arrow with Security Group |
| DSS Automation Node | AWS Identity and Access Management | connects_to | Unidirectional |
| DSS Design Node | Amazon Simple Storage Service (S3) | connects_to | Unidirectional |
| DSS API Deployer | AWS Glue | connects_to | Unidirectional |
| Amazon Redshift | Amazon Athena | connects_to | Unidirectional |
| Amazon EMR | Amazon SageMaker | connects_to | Unidirectional |
| Amazon Elastic Kubernetes Service | Amazon Rekognition | connects_to | Unidirectional |
| Amazon Elastic Kubernetes Service | Amazon Comprehend | connects_to | Unidirectional |

### Gaps

| Source | Target | Relationship | Details |
|---|---|---|---|
| DSS Automation Node | DSS Design Node / DSS API Deployer | missing_explicit_connection | No explicit communication arrows drawn between these closely related components within the same security group. |
| DSS Design Node | DSS Automation Node / DSS API Deployer | missing_explicit_connection | No explicit communication arrows drawn between these closely related components within the same security group. |
| DSS API Deployer | DSS Automation Node / DSS Design Node | missing_explicit_connection | No explicit communication arrows drawn between these closely related components within the same security group. |