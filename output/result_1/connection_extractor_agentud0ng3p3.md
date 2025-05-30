| Source | Target | Relationship | Details |
|---|---|---|---|
| AWS Cloud | Availability Zone | contains | |
| Availability Zone | VPC | contains | |
| VPC | Public subnet | contains | CIDR: 10.0.128.0/20 |
| VPC | Private subnet | contains | CIDR: 10.0.0.0/19 |
| Internet Gateway | Router | connects_to | Bidirectional |
| Router | Route table (Public) | routes_through | Bidirectional |
| Router | Public subnet | connects_to | Bidirectional |
| Public subnet | Network ACL (Public) | secured_by | |
| Public subnet | DSS Automation Node | hosts | |
| Public subnet | DSS Design Node | hosts | |
| Public subnet | DSS API Deployer | hosts | |
| DSS Automation Node | Security group (Public) | secured_by | |
| DSS Design Node | Security group (Public) | secured_by | |
| DSS API Deployer | Security group (Public) | secured_by | |
| Router | Route table (Private) | routes_through | Bidirectional |
| Router | Private subnet | connects_to | Bidirectional |
| Private subnet | Network ACL (Private) | secured_by | |
| Private subnet | Amazon Redshift | hosts | |
| Private subnet | Amazon EMR | hosts | |
| Private subnet | Amazon Elastic Kubernetes Service | hosts | |
| Amazon Redshift | Security group (Private Redshift) | secured_by | |
| Amazon EMR | Security group (Private EMR) | secured_by | |
| Amazon Elastic Kubernetes Service | Security group (Private EKS) | secured_by | |
| DSS Automation Node | DSS Design Node | connects_to | Implied application flow |
| DSS Design Node | DSS API Deployer | connects_to | Implied application flow |
| DSS Automation Node | DSS API Deployer | connects_to | Implied application flow |
| VPC | AWS Identity and Access Management | connects_to | HTTPS/TCP 443 |
| VPC | Amazon Simple Storage Service | connects_to | HTTPS/TCP 443 |
| VPC | AWS Glue | connects_to | HTTPS/TCP 443 |
| VPC | Amazon Athena | connects_to | HTTPS/TCP 443 |
| VPC | Amazon SageMaker | connects_to | HTTPS/TCP 443 |
| VPC | Amazon Rekognition | connects_to | HTTPS/TCP 443 |
| VPC | Amazon Comprehend | connects_to | HTTPS/TCP 443 |

---

**Gaps Table**

| Source | Target | Gap Type | Details |
|---|---|---|---|
| Private subnet components (Redshift, EMR, EKS) | External AWS Services (S3, Glue, Athena, SageMaker, Rekognition, Comprehend, IAM) | Missing Connectivity Detail | No explicit mechanism (e.g., NAT Gateway, VPC Endpoints) shown for private subnet resources to securely access external AWS services. |
| Public subnet components (DSS Nodes) | Private subnet components (Redshift, EMR, EKS) | Missing Connection | No explicit inter-subnet communication paths shown, which are often necessary in multi-tier architectures. |
| Security Group (Public) / (Private) | N/A | Missing Configuration Detail | Ingress/Egress rules (ports, protocols, source/destination CIDRs) are not specified. |
| Network ACL (Public) / (Private) | N/A | Missing Configuration Detail | Ingress/Egress rules (ports, protocols, source/destination CIDRs) are not specified. |