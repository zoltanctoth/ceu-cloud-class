---
layout: default
---
[Home](./README.md).
[Internet](./internet.md).
[Cloud Computing](./cloud_computing.md).
[Serverless](./serverless.md).
[AWS](./aws.md).
[Spark DataFrame & SQL API](./sparkAPI.md).
[Spark Internals](./spark_internals.md).
[Advanced Optimizations in Spark](spark_optimizations.md).

### Using AWS programatically

// in the making, this is just a draft


### IAM - Identity Access Management
IAM allows you to manage users and their level of access to the AWS console
Features:
Centralized control of your AWS account
Shared access to your AWS account
Granular Permissions (limit people's permissions)
Identity Federation (You can use Active Directory, FB, Linkedin -> your users can log into the console using these)
Multi-factor Authentication
Provides temporary access for users / devices / services where necessary
Allows you to set up your own password rotation policy
Integrates with many different AWS Services
Supports PCI DSS Compliance (Credit card details must be compliant)

### Terminology
| Users       | Groups         | Policies |Roles
|:-------------|:------------------|:-------------|:------------------|
|End Users such as people, employees of an organization etc.| Collection of users in the group will inherit the permission of the group | Made up of "Policy Documents". JSON format. They give you permissions to what a User/Group/Role us able to do | You create roles and assign them to AWS resources |


### IAM Continued:
IAM is universal - it does not apply to regions!
The "Root Account" is the account created when first setup your AWS account. It has complete Admin access
New users have no permissions when first created
New users are assigned Access Key ID and Secret Access Keys when first created
-> These are not the same as passwords; you cannot use these to login to the console. You can use this to access AWS via APIs and the Command Line 
You only get to see this once!! If you lose them, you have to regenerate them!
You can create and customize your own password rotation policies

### Create Billing Alarm
Check if the region is correct (billing alarm is region specific)
Billing alarm is found under CloudWatch


### Amazon S3 - Stands for Simple Storage Service
S3 provides secure, durable, highly scalable object storage. Store and retrieve any amount of data from anywhere on the web
Safe place to store your files
Object-based storage up to 5TB (Objects consist of: KEY - name of the object, VALUE - data that is made up of a sequence of bits, VERSION ID - important for versioning, S3 allows you to have multiple versions of your files, METADATA - data about data you are storing, SUBRESOURCES - access control lists torrent)
Unlimited storage
Files are stored in Buckets -> folder in which you store your files.
Buckets must be unique globally. When you create a bucket it gets a web address. That's why it has to be unique.
When you upload to S3, you will receive HTTP 200 code if successful

### Data Consistency for S3
Read  after Write consistency for PUTS of new objects
If you upload a file you are able to read it immediately, you are able to rad it straight after writing to it -> you are doing a PUT of that object into S3
Eventual consistency for overwrite PUTS and DELETES
If you update that object / delete == eventual consistency
If you udate an existing file/ delete a file and read it immediately you may get the older version or not. Changes to objects can take some time to propagate. 

### S3 Guarantees:
Built for 99.99% availability for the S3 platform
99.0 % availability for Amazon Guarantee
Amazon guarantees 99.999999999% durability for S3 information (11 9s!)

### S3 Features
Tiered Storage Available
Lifecycle Management 
Versioning
Encryption
MFA Delete
Secure your Data using Access Control Lists and Bucket Policy
S3 Storage Classes
S3 STANDARD
S3 - IA
S3 ONE ZONE - IA
99.99% availability
99.999999999% durability
stored redundantly across multiple devices in multiple facilities and is designed to sustain the loss of 2 facilities concurrently.
Infrequently Accesses
For data that is accessed less frequently but requires rapid access when needed. Lower fee than S3 but you are charged for retrieval fee.
For when you want a lower cost option for infrequently accessed data, but do not require the multiple Availability Zone data resilience. Stored in one Availability Zone.

S3 - INTELLIGENT TIERING
S3 - GLACIER
S3 - GLACIER DEEP ARCHIVE
Designed to optimize costs by automatically moving data to the most cost-effective access tier without performance impact or operational overhead.
Secure, durable, and low cost storage class for data archiving. You can reliably store any amount of data at costs  that are competitive with or cheaper than on-premise solutions. Retrieval times configurable from minutes to hours. 
S3's lowest-cost storage class where a retrieval time of 12 hours is acceptable.
S3 Charges
Storage
Requests
Storage Management Pricing
Data Transfer Pricing
Transfer Acceleration: fast, easy, secure transfer of files over long distances between end-users and an S3 bucket. Takes advantage of CloudFront's globally distributed edge locations. As the data arrives at an edge location, data is routed to Amazon S3 over an optimized network path.
Cross Region Replication Pricing: When you upload an object to US_EAST 1 and cross region replication is turned on, the object will be replicated automatically to your bucket in Sydnie. 

S3 is not suitable to install an operating system / database on, because it is object based storage.
You can turn on MFA Delete - to delete files they need MFA.


### S3 Security and Encryption
By default all newly created buckets are private. You can set up access to your buckets using 1: bucket policies (bucket level), 2: Access Control Lists (ACL) - individual objects.
S3 buckets: can be configured to create Access Logs, which log all requests made to the S3 bucket. This can be sent to another bucket and even to another bucket in another account.

### Encryption in Transit is achieved by:
https -> secured
Always achieved by SSL/TLS
Encrypt at Rest (source side) is achieved by:
- S3 Management Keys - SSE-SB
- AWS Key Management Service, Managed Keys - SSE-KMS
- Server Side Encryption with Customer Provided Keys - SSE-C
Client Side Encryption
S3 Version Control - Great back-up tool
