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


### IAM - Identity Access Management

- IAM allows you to manage users and their level of access to the AWS console
- **Features:**
  - Centralized control of your AWS account
  - Shared access to your AWS account
  - Granular Permissions (limit people's permissions)
  - Identity Federation (You can use Active Directory, FB, Linkedin -> your users can log into the console using these)
  - Multi-factor Authentication
  - Provides temporary access for users / devices / services where necessary
  - Allows you to set up your own password rotation policy
  - Integrates with many different AWS Services
  - Supports PCI DSS Compliance (Credit card details must be compliant)


### Terminology

| Users       | Groups         | Policies |Roles
|:-------------|:------------------|:-------------|
|End Users such as people, employees of an organization etc.| Collection of users in the group will inherit the permission of the group | Made up of "Policy Documents". JSON format. They give you permissions to what a User/Group/Role us able to do | You create roles and assign them to AWS resources |


### IAM Continued:

- IAM is universal - it does not apply to regions!
- The "Root Account" is the account created when first setup your AWS account. It has complete Admin access
- New users have no permissions when first created
- New users are assigned Access Key ID and Secret Access Keys when first created -> These are not the same as passwords; you cannot use these to login to the console. You can use this to access AWS via APIs and the Command Line 
- You only get to see this once!! If you lose them, you have to regenerate them!
- You can create and customize your own password rotation policies

### Create Billing Alarm
- Check if the region is correct (billing alarm is region specific)
- Billing alarm is found under CloudWatch


### Amazon S3 - Stands for Simple Storage Service
- S3 provides secure, durable, highly scalable object storage. 
- Store and retrieve any amount of data from anywhere on the web
- Safe place to store your files
  - Object-based storage up to 5TB (Objects consist of: KEY - name of the object, VALUE - data that is made up of a sequence of bits, VERSION ID - important for versioning, S3 allows you to have multiple versions of your files, METADATA - data about data you are storing, SUBRESOURCES - access control lists torrent)
- Unlimited storage
- **Files are stored in Buckets -> folder in which you store your files.**
- **Buckets must be unique globally.** When you create a bucket it gets a web address. That's why it has to be unique.
- When you upload to S3, you will receive HTTP 200 code if successful

### Data Consistency for S3
- Read  after Write consistency for PUTS of new objects
  - If you upload a file you are able to read it immediately, you are able to read it straight after writing to it -> you are doing a PUT of that object into S3
- Eventual consistency for overwrite PUTS and DELETES
- If you update that object / delete == eventual consistency
- If you udate an existing file/ delete a file and read it immediately you may get the older version or not. Changes to objects can take some time to propagate. 

### S3 Guarantees:
- Built for 99.99% availability for the S3 platform
- 99.0 % availability for Amazon Guarantee
- Amazon guarantees 99.999999999% durability for S3 information (Tip: 11 9s!)

### S3 Features Overview:
- Tiered Storage Available
- Lifecycle Management 
- Versioning
- Encryption
- MFA Delete
- Secure your Data using Access Control Lists and Bucket Policy


### S3 Storage Classes

| S3 STANDARD       | S3 - IA         | S3 ONE ZONE - IA |
|:-------------|:------------------|:-------------|
|99.99% availability 99.999999999% durability stored redundantly across multiple devices in multiple facilities and is designed to sustain the loss of 2 facilities concurrently. | Infrequently Accesses: For data that is accessed less frequently but requires rapid access when needed. Lower fee than S3 but you are charged for retrieval fee.| For when you want a lower cost option for infrequently accessed data, but do not require the multiple Availability Zone data resilience. Stored in one Availability Zone.| 



| S3 - INTELLIGENT TIERING  | S3 - GLACIER       | S3 - GLACIER DEEP ARCHIVE |
|:-----------------|:-----------------|:-----------------|
|Designed to optimize costs by automatically moving data to the most cost-effective access tier without performance impact or operational overhead.| Secure, durable, and low cost storage class for data archiving. You can reliably store any amount of data at costs  that are competitive with or cheaper than on-premise solutions. Retrieval times configurable from minutes to hours | S3's lowest-cost storage class where a retrieval time of 12 hours is acceptable.| 


### S3 Charges for:
- Storage
- Requests
- Storage Management Pricing
- Data Transfer Pricing
- Transfer Acceleration: fast, easy, secure transfer of files over long distances between end-users and an S3 bucket. Takes advantage of CloudFront's globally distributed edge locations. As the data arrives at an edge location, data is routed to Amazon S3 over an optimized network path
- Cross Region Replication Pricing: When you upload an object to US_EAST 1 and cross region replication is turned on, the object will be replicated automatically to your bucket in Sydnie. 
- S3 is not suitable to install an operating system / database on, because it is object based storage.
You can turn on MFA Delete - to delete files they need MFA.

### S3 Security and Encryption
- By default all newly created buckets are private. 
- You can set up access to your buckets using 
  - 1: bucket policies (bucket level)
  - 2: Access Control Lists (ACL) - individual objects
- S3 buckets: can be configured to create Access Logs, which log all requests made to the S3 bucket. This can be sent to another bucket and even to another bucket in another account.

### Encryption in Transit is achieved by:
- https -> secured
- Always achieved by SSL/TLS
- Encrypt at Rest (source side) is achieved by:
  - S3 Management Keys - SSE-SB
  - AWS Key Management Service, Managed Keys - SSE-KMS
  - Server Side Encryption with Customer Provided Keys - SSE-C
- Client Side Encryption
- S3 Version Control - Great back-up tool


### S3 Version Control - Great back-up tool
Using Versioning with S3:
- Stores all versions of an object (including all writes and deletes of an object)
- Great backup tool
- Once enabled, versioning cannot be disabled, only suspended
- Integrates with Lifecycle Rules
- Versioning's MFA Delete capability, which uses multi-factor authentication can provide additional layer of security.
  - Note: Uploading the same file again (different version) will reset it to private
- Lifecycle Management and Glacier
- Lifecycle Rule automates transitioning your object to different tiers of storage
- You can use it to permanently delete your objects as well
- Can be used in conjunction with versioning
- Can be applied to current versions and previous versions

### Cross Region Replication
- Cross Region Replication requires versioning enabled on the source and destination buckets
- If you put a delete marker in your original bucket it is not going to replicate that market
- If you delete your latest version it is not going to replicate "delete" in cross region bucket
- Regions must be unique
- Files in an existing bucket are not replicated automatically
- All subsequent updates files will be replicated
- Delete markers are not replicated
- Deleting individual versions will not be replicated

### Transfer Acceleration
- S3 Transfer Acceleration utilizes the CloudFront Edge Network to accelerate your uploads to S3. Instead of uploading directly to your S3 bucket you can use a distinct URL to upload directly to an edge location which will then transfer that file to S3. 
- You will get a distinct URL to upload.

### CloudFront (Global)
- A Content Delivery Network (CDN) is a system of distributed servers (network) that delivers webpages and other web content to a user based on the geographical locations of the user, the origin of the webpage and the content deliver server.
**Key Terminology:**
- Edge Location: Location where content will be cached. This is separate to a Region/AZ (Availability Zone)
- Origin: The origin of all the files that the CDN will distribute. This can be an S3 Bucket, an EC2 instance, an Elastic Load Balancer, or Route 53. CloudFront can be used to deliver your entire website including dynamic/static,  streaming and interactive content - using a global network of edge locations. Requests for your content are automatically routed to the nearest edge location, so content is delivered with the best possible performance.

- Two Types of CloudFront Distributions:
  - 1: Web Distribution: Used for websites
  - 2: RTMP: Used for media streaming
- Edge Locations are not just READ only, you can write to them too. (e.g put objects to them)
- Objects are cached for the Time of the TTL (Time To Live)
- You can clear/invalidate cached objects, but you will be charged
- CloudFront has 2 distributions: Web and RTMP
- Invalidation: no longer available on the edge locations
(First you have to disable CloudFront distribution the you can delete it)

### Storage Gateway:
Storage Gateway is a service that connects an on-premise softwaer appliance with cloud-based storage to provide seamless and secure integration between an organization's on premises IT environment and AWS' storage infrastructure. The service enables you to securely store data to the AWS Cloud for scalable and cost effective storage.

**Your Data Center -> Storage Gateway -> Replicate Data -> AWS**

- AWS Storage Gateway's software appliance is available for download as a VM (virtual image) that you install on a host in your datacenter. Storage Gateway supports VMware ESX / Microsoft Hyper-V
- Once the gateway is installed and associated with your AWS account through the activation process, you can use the AWS Management Console to create the storage gateway options.

Storage Gateways:
  - 1: File Gateway (NPS)
  - 2: Volume Gateway (iSCSI)
    - stored volumes, cached volumes
  - 3: Tape Gateway (VTL)


# EC2 (Elastic Cloud Compute)

AWS EC2 is a web service that provides re-sizable compute capacity in the cloud. EC2 reduces the time required to obtain and boot new server instances to minutes, allowing you to quickly scale capacity, both up and down, as your computing requirements change.

EC2 has changed the economics of cloud computing by allowing you to pay only for capacity that your actually use. EC2 provides developers the tools to build failure resistant applications and isolate themselves from common failure scenarios.

## Pricing Options

### On Demand

Allows you to pay a fixed rate by the hour (or by the second) with no commitment.

**_Use Cases_**

- Perfect for users that want the low cost and flexibility of EC2 without any of the up front payment or long term commitment
- Applications with short term, spiky or unpredictable workloads that cannot be interrupted
- Applications being developed or tested on EC2 for the first time

### Reserved

Provides you with a capacity reservation, and offer a significant discount on the hourly charge for an instance. 1 year or 3 year terms.

**_Use Cases_**

- Applications with steady state or predictable usage
- Applications that require reserved capacity
- Users can make up front payments to reduce their total computing costs even further
  - Standard RIs (Up to 75% off on-demand)
  - Convertible RIs (Up to 54% off on-demand) feature the capability to change the attributes of the RI as long as the exchange results in the creation of Reserved Instances of equal or greater value. Ability to go from CPU intensive instance to Memory intensive.
  - Scheduled RIs are available to launch within the time window you reserve. This option allows you to match your capacity reservation to predictable recurring schedule that only requires a fraction of a day, a week, or a month.

### Spot

Enables you to bid whatever price you want for an instance capacity, providing for even greater savings if your applications have flexible start and end times.

**Use Cases**

- Applications that have flexible start and end times
- Applications that are only feasible at very low compute prices
- Used for single compute instances to save on costs compared to 9-5 during the week.
- Users with an urgent need for a large amount of additional computing capacity.

### Dedicated Hosts

Physical EC2 server dedicated for your use. Dedicated Hosts can help you reduce costs by allowing you to use your existing server-bound software licenses.

**Use Cases**

- Useful for regulatory requirements that may not support multi-tenant virtualization.
- Great for licensing which does not support multi-tenancy or cloud deployments
- Can be purchased On-Demand (hourly).
- Can be purchased as a Reservation for up to 70% off the On-Demand price.

## EC2 Instance Types

**_No need to memorize for associate exams_**

| Family | Specialty                     | Use Cases                       |
| :------:|:-----------------------------:| :------------------------------:|
| F1     | Field Programmable Gate Array | Genomics research, financial analytics, real-time video processing, big data etc|
| I3      | High Speed Storage            | NoSQL DBs, Datawarehousing |
| G3      | Graphics Intensive            | Video Encoding / 3D Application Streaming|
| H1      | High Disk Throughput          | MapReduce-based workloads, distributed file systems such as HDFS and MapR-FS |
| T2      | Lowest Cost General Purpose   | Web Servers / Small DBs |
| D2      | Dense Storage                 | Fileservers / Data Warehousing / Hadoop |
| R4      | Memory Optimization           | Memory Intensive Apps/DBs |
| M5      | General Purpose               | Application Servers |
| C5      | Compute Optimized             | CPU Intensive Apps / DBs |
| P3      | Graphics / General Purpose GPU | Machine Learning, Bit Coin Mining etc |
| X1      | Memory Optimized               | SAP HANA / Apache Spark |


**How to remember EC2 instance types F.I.G.H.T.D.R.M.C.P.X (after 2017 reinvent):**
  - **_F_** - FGPA
  - **_I_** - IOPS
  - **_G_** - Graphics
  - **_H_** - High Disk Throughput
  - **_T_** - Cheap General Purpose (think T2 Micro)
  - **_D_** - Density
  - **_R_** - Ram
  - **_M_** - Main choice for general purpose applications
  - **_C_** - Compute
  - **_P_** - Graphics(Pics)
  - **_X_** - Extreme Memory

## EBS - Elastic Block Storage

Amazon EBS allows you to create storage volumes and attach them Amazon EC2 instances. Once attached, you can create a file system on top of theses volumes, run a database, or use them in any other way you would use a block device. EBS volumes are placed in a specific Availability Zone, where they are automatically replicated to protect you from the failure of a single component.

_TLDR; A disk in the cloud that you attach to your EC2 instances_

### EBS Volume Types

- General Purpose SSD (GP2)
  - General purpose, balances both price and performance.
  - Ratio of 3 IOPS per GB with up to 10,000 IOPS and the ability to burst up to 3000 IOPS for extended periods of time for volumes at 3334 GB and above
- Provisioned IOPS SSD (IO1)
  - Designed for I/O intensive applications such as large relational or NoSQL databases.
  - Use if you need more than 10,000 IOPS
  - Provision up to 20,000 IOPS per volume
  - Super high performance
- Throughput Optimized HDD (ST1)
  - Big Data
  - Data warehouses
  - Log processing
  - Cannot be a boot volume
- Cold HDD (SC1)
  - Lowest cost storage for infrequently accessed workloads
  - File server
  - Cannot be a boot volume
- Magnetic (Standard)
  - Lowest cost per GB of all EBS volume types that is bootable. Magnetic volumes are ideal for workloads where data is accessed infrequently, and applications where the lowest storage cost is important

## Let's get our hands dirty! Launch an EC2 instance lab!

### Summary

- Termination protection is turned off by default, you **MUST** turn it on.
- On an EBS-backed instance, the default action is for the root EBS volume to be deleted when the instance is terminated
- EBS Root Volume of you DEFAULT AMI's cannot be encrypted. You can also use a third party tool (such as bit locker) to encrypt the root volume, or this can be done when creating AMI's (future lab) in the AWS console or using the API.
- Additional volumes can be encrypted.

## Security Groups

### What is a Security Group?

A security group is a virtual firewall that's controlling traffic to your EC2 instance. When you first launch as EC2 instance you associate it to 1 or more instances. You have the ability to add rules to these security groups that allows traffic to or from these instances.

### Security Groups - General

1. Any security group rules apply immediately
2. Security groups are **_STATEFUL_**. Inbound rules automatically add outbound rules
3. All traffic is blocked by default and included through the rules. Whitelist
4. All outbound traffic is allowed
5. You can have multiple EC2 instances within a security group.
6. You can have multiple security groups attached to EC2 instances.
7. You cannot block specific IP addresses using Security Groups, use Network Access Control Lists.
8. You can specify allow rules, but not deny rules.

## RAID, Volumes & Snapshots

### RAID - Redundant Array of Independent Disks

- RAID 0 - Striped, no redundancy, good performance. If one fails, you lose all
- RAID 1 - Mirrored, redundant. If one fails, others available
- RAID 5 - Good for reads, bad for writes, AWS does not recommend ever putting RAID 5's on EBS. Strongly discouraged.
- RAID 10 - Striping & Mirrored, good redundancy, good performance.

#### How can I take a Snapshot of a RAID Array?

- **Problem** - Taking a snapshot excludes the data held in cache by applications and the OS. This doesn't really matter on single volume, however when using multiple volumes in a RAID Array, this can be a problem due to interdependencies of the array.

- **Solution** - Take an application specific snapshot.
  - Stop application from writing to disk.
  - Flush all caches to the disk.
  - How can we do this?
    - Freeze the file system
    - Unmount the RAID Array
    - Shutting down the associated EC2 instance.

## Create an AMI lab - Volumes vs. Snapshots

### Snapshots of Root Device Volumes

- To create a snapshot for Amazon EBS volumes that server as root devices, you should stop the instance before taking the snapshot.

### Security

- Snapshots of encrypted volumes are encrypted automatically
- Volumes restored from encrypted snapshots are encrypted automatically.
- You can share snapshots, but only if they are unencrypted.
  - Said snapshots can be shared with other AWS accounts of made public

## AMI Types

### What should you select your AMI based on?

- Region
- OS
- Architecture
- Launch Permissions
- Storage for the Root Device (Root Device Volume)
  - Instance Store (Ephemeral Store)
  - EBS Backed Volumes

### EBS vs. Instance Store

All AMIs are categorized as either backed by Amazon EBS or backed by instance store.

**_For EBS Volumes:_**

The root device for an instance launched from the AMI is an Amazon EBS volume created from an Amazon EBS snapshot.

**_For Instance Store Volumes:_**

The root device for an instance launched from the AMI is an instance store volume created from a template stored in Amazon S3.

## Elastic Load Balancers

### What is a load balancer?

A virtual appliance that balances the load of HTTP traffic etc. of your web application/web servers.

### Types of Load Balancers

- Application Load Balancers
- Network Load Balancers
- Classic Load Balancers

### Application Load Balancer _(Intelligent)_

Best suited for load balancing of HTTP(S) traffic. They operate at Layer 7 (OSI) and are application aware. The are intelligent, and you can create advanced request routing, sending specified requests to specific web servers.

### Network Load Balancer _(Performance)_

Best suited for load balancing of TCP traffic where extreme performance is required. Operating at the connection level (Layer 4), Network Load Balancers are capable of handling millions of requests per second, while maintaining ultra-low latencies.

### Classic Load Balancer _(OG, Legacy Load Balancer)_

Used to load balance HTTP(S) applications and use Layer 7-specific features, such as X-Forwarded and stick-sessions. You can use strict Layer 4 load balancing for applications that rely purely on the TCP protocol.

### 504 Error

- If no response or timeout, the ELB (Elastic Load Balancer) responds with status code 504.
- Internal Server Error type - DB Layer or Web Server Layer.
- Solution: Identify issue where failing and scale up or out where possible.

## Placement Groups (Exam MUST KNOW!!)

### Two Types of Placement Groups

**Clustered Placement Group**

A cluster placement group is a grouping of instances within a **single** Availability Zone. Placement groups are recommended for applications that need low network latency, high network throughput, or both.

_NOTE: Only a certain number instances can be launched in to a Clustered Placement Group._

**Spread Placement Group**

Opposite of a Clustered Placement Group. A Spread Placement Group is a group of instances that are each placed on distinct underlying hardware. Spread Placement Groups are recommended for applications that have a small number of critical instances that should be kept separate from each other.

## EFS (Elastic File System)

AWS EFS is file storage service for AWS EC2 instances. Amazon EFS is easy to use and provides a simple interface that allows you to create and configure file systems quickly and easily. With AWS EFS, storage capacity is elastic, growing and shrinking automatically as you add and remove files, so your applications have the storage they need, when they need it.

### EFS Features

- Supports the Network File System version 4 (NFSv4) protocol
- You only pay for the storage you use (no pre-provisioning required)
- Can scale up to the petabytes
- Can support thousands of concurrent NFS connections
- Data is stored across multiple AZ's within a region
- Read After Write Consistency

## Lambda

### What is Lambda?

AWS Lambda is a compute service where you can upload your code and create Lambda function. AWS Lambda takes care of provisioning and managing the servers that you use to run the code. Worry free from OS, patching, scaling, etc.

**Use Cases**

- As an event-driven compute service where AWS Lambda runs your code in response to events. These events could be changes to data in an Amazon S3 bucket or an Amazon DynamoDB table.

- As a compute service to run your code in response to HTTP requests using Amazon API Gateway or API calls made using AWS SDKs.

**Encapsulation of the following:**

- Data Centers
- Hardware
- Assembly Code/Protocols
- High Level languages
- Operation Systems
- Application Layer/AWS API's
- AWS Lambda

### Compatible Languages:

- C#
- Java
- Node.js
- Python

### How is Lambda priced?

- Number of requests
  - First 1m requests are free. $0.20 per 1m requests thereafter.

- Duration
  - Duration is calculated from the time your code begins execution until it returns or otherwise terminates, rounded up to the nearest 100ms. The price depends on the amount of memory you allocate to your function. You are charged $0.00001667 for every GB-second used.


### Why is Lambda cool?

- No SERVERS!!
- Continuous Scaling
- Super super super cheap
