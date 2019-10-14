---
layout: default
---
[Home](./README.md).
[Internet](./internet.md).
[Cloud Computing](./cloud_computing.md).
[Serverless](./serverless.md).
[AWS](./aws.md).
[Spark Overview](./spark_overview.md).
[Spark DataFrame & SQL API](./sparkAPI.md).
[Spark Internals](./spark_internals.md).
[Advanced Optimizations in Spark](spark_optimizations.md).
[Help/Resources](./resources.md).

## Using AWS programatically

## Table of Contents

* * *

## Part 1. Preamble, Regions, Availability Zones (AZ), Edge Locations

#### Preamble
Cloud computing allows users to quickly access an arbitrary amount of compute resources from a distance without the need to buy or maintain hardware themselves. There are many cloud computing services. This note describes the use of the Amazon Web Services ([AWS](http://aws.amazon.com/)) and its resources. However, the fundamental concepts covered here will generally apply to other cloud computing services such as [Google Cloud](https://cloud.google.com/), [Digital Ocean](https://www.digitalocean.com/), [Microsoft Azure](https://azure.microsoft.com/), [etc.](http://cloud-computing.softwareinsider.com/), though with substantial differences in jargon used by each provider.

#### Glossary and abbreviations
- [AWS](http://aws.amazon.com/) - Amazon Web Services. A collection of cloud computing services provided by Amazon. 
- [EC2](http://aws.amazon.com/ec2/) - Elastic Compute. A particular AWS service that provides 'resizable cloud hosting services'. This service allows you to configure and rent computers to meet you compute needs on an as needed basis.
- [EBS](http://aws.amazon.com/ebs/) - Elastic Block Storage. A data storage solution offered through the EC2 service. This service allows you to rent disk storage and associate that storage with your compute resources. EBS volumes are generally backed by SSD devices. EBS volumes can only be directly attached to a single EC2 instance at a time.
- [S3](http://aws.amazon.com/s3/) - Simple storage service. A storage service that is cheaper than EBS and allows for storage of larger amounts of data with some drawbacks [compared to EBS](http://www.tomsitpro.com/articles/cost-of-the-cloud-book,2-694-2.html). S3 volumes store data as objects that are accessed by an API or command line interface or other application designed to work with S3. EBS volumes on the other hand can be mounted as if they were a local disk drive associated with the Instance..
- [SSD](http://en.wikipedia.org/wiki/Solid-state_drive) - Solid state drive. A particular type of storage hardware that is generally faster and more expensive than traditional hard drives.
- [HDD](http://en.wikipedia.org/wiki/Hard_disk_drive) - Hard disk drive. A particular type of storage hardware that is generally cheaper and larger but slower than SSD. HDD drives are traditional hard drives that access data on a spinning magnetic disk.
- [Ephemeral storage](http://stackoverflow.com/questions/11566223/what-data-is-stored-in-ephemeral-storage-of-amazon-ec2-instance) - Also known as Instance Store storage. Data storage associated with an EC2 instance that is local to the host computer. This storage *does not persist* when the instance is stopped or terminated. In other words, anything you store in this way will be lost if the system is stopped or terminated. Instance store volumes may be backed by SSD or HDD devices.

### Regions

**AWS Region** is a physical, geographical area or location, consisting of 2 or more Availability Zones.

**_Current regions across the world:_**

- US East (N. Virginia) - `us-east-1`
- US East (Ohio) - `us-east-2`
- US West (Northern California) - `us-west-1`
- US West (Oregon) - `us-west-2`
- Canada (Central) - `ca-central-1`
- EU (Frankfurt) - `eu-central-1`
- EU (Ireland) - `eu-west-1`
- EU (London) - `eu-west-2`
- EU (Paris) - `eu-west-3`
- Asia Pacific (Tokyo) - `ap-northeast-1`
- Asia Pacific (Seoul) - `ap-northeast-2`
- Asia Pacific (Osaka-Local) - `ap-northeast-3`
- Asia Pacific (Singapore) - `ap-southeast-1`
- Asia Pacific (Sydney) - `ap-southeast-2`
- Asia Pacific (Mumbai) - `ap-south-1`
- South America (Sao Paulo) - `sa-east-1`

### Availability-Zones

- **AWS Availability Zones** are one or more discrete data centers, each with redundant power, networking and connectivity housed in separate facilities. Deploying your application across multiple Availability Zones is useful for redundancy, low latency and fault tolerance.

**_Regions with multiple Availability Zones:_**

- US East
  - Ohio (3)
  - North Virginia (6)
- US West
  - Oregon (3)
  - Northern California (3)
- Canada
  - Central (3)
- South America
  - Sao Paulo (3)
- Europe
  - Ireland (3)
  - Frankfurt (3)
  - London (3)
  - Paris (3)
- Asia Pacific
  - Singapore (3)
  - Seoul (2)
  - Tokyo (4)
  - Mumbai (2)
  - Sydney (3)
  - Beijing (2)
  - Ningxia (2)
  
#### Availability Zones Video
  
[![AZ](assets/AZ.png)](https://www.youtube.com/watch?v=ET_CSqdGsYg "Availability Zones")

### Edge Locations

- **AWS Edge Locations** are locations around the world meant for caching content, enhancing the user experience, reducing latency. Edge locations are specifically used by AWS Cloudfront and AWS CDN. Every Region is has its own set Availability Zone's and Edge Locations.

## Part 1. AWS Services Overview

**Compute:**
-    `EC2` - Elastic Compute Cloud
-    `EC2 Container Services` - Containerization Docker
-    `Elastic Beanstalk` - Plug and Play - for developers
-    `Lambda (server less)` - Code/Functions uploaded to the cloud to run at different points
-    `Lightsail` - Plug and Play
-    `Batch` - Batch computing in the cloud

**Storage:**
-    `S3` - Simple Storage Service - object based storage - buckets
-    `EFS` - Elastic File System
-    `Glacier` - Data Archival 
-    `Snowball` - Large amounts of data to aws data center
-    `Storage gateway` - VM installed in datacenter or office - replicate info to S3

**Databases:**
-    `RDS` - Relation Database Service - postgres, mysql, oracle
-    `DynamoDB` - Non-Relational DB
-    `Elasticache` - Cache Things from DB
-    `Redshift` - Data Warehousing Business Intelligence, complex queries
    
**Migration:**
-    `AWS Migration Hub` - tracking service for moving to aws
-    `Application Discover Service` - track applications and dependency
-    `Database Migration Service` - migrate db from on premise to AWS
-    `Server Migration Service` - migrate server to AWS cloud
-    `Snowball` - in between storage and migration

**Networking and Content Delivery:**
-    `VPC (highlight)` - Amazon virtual private cloud - virtual datacenter - configure avail zones, firewall, network acl etc.
-    `Cloudfront` - AWS content delivery network, store assets specific regions around the world
-    `Route 53` - AWS DNS service - lookup ip to get ipv4 and ipv6 address
-    `API Gateway` - Serverless way of creating own api
-    `Direct Connect` - Dedicated line from office directly into amazon, connects to VPC

**Developer Tools:**
-    `Codestart` - project management, CI toolchain, collaborate
-    `Codecommit` - store code, like github    
-    `Codebuild` - compile and run tests, produce package
-    `Code deploy` - deployment service to ec2 instance
-    `Codepipeline` - automate and visualize steps to release software
-    `X-ray` - debug and analyze server less application
-    `Cloud9` - IDE environment in browser

**Management tools:**
-    `Cloudwatch` - Monitoring service
-    `Cloudformation` - solutions architect specific - scripting infrastructure - turn infrastructure to code
-    `Cloudtrail` - log changes to aws environment
-    `Config` - monitors config of aws environment
-    `Opswork` - similar to elastic beanstalk - chef and puppet to automate environments
-    `Service Catalog` - manage a catalog of IT services
-    `Systems manager` - interface for managing aws resources - group resources
-    `Trusted Advisor` - advice around security, advice for aws services and resources, accountant like
-    `Managed Services` - manage service for aws cloud

**Media Services:**
-    `Elastic transcoder` - takes media and resizes on different devices
-    `Media convert` - file based video transcoding with broadcast grade features
-    `Media live` - broadcast grade live video processing service. tv internet connected multiscreen
-    `Media Package` - protect content over internet 
-    `Media Store` - media storage, optimized for media
-    `Media Tailor` - target advertising into video streams with out harming broadcast

**Machine Learning:**
-    `Sage maker` - easy for deep learning when coding for environment
-    `Comprehend` - sentiment analysis on products. good or bad?
-    `Deep lens` - computer vision on camera, recognition, physical piece of hardware
-    `Lex` - powers alexa, AI 
-    `Machine Learning` - throw dataset to AWS cloud and predict outcome
-    `Polly` - text to speech, voices sound real, accents
-    `Rekognition` - upload file, tells you what is in the file
-    `Amazon translate` - translate to other langs
-    `Amazon transcribe` - hard of hearing, speech recognition, speech to text

**Analytics:**
-    `Athena` - SQL queries ins S3 buckets, serverless
-    `EMR` - elastic map reduce - processing large amounts of data, chops data up for analysis
-    `Cloudsearch` - search service
-    `Elastic Search service` - search service
-    `Kinesis` - solutions architect highlight, ingesting large amounts data
-    `Kinesis Video streams` - ingesting streams and analyze    
-    `Quicksight` - business intelligence tool
-    `Datapipeline` - moving data between different services
-    `Glue` - ETL (extract transform load)

**Security Identity and Compliance:**
-    `IAM` - identity access management
-    `Cognito` - device authentication, oath, after authenticated, use aws services
-    `Guard Duty` - monitor for malicious activity
-    `Inspector` - install on vm or instances, test against it, schedule
-    `Macie` - Scan s3 buckets and looks for sensitive info and alert
-    `Certificate Manager` - ssl cert for free, manage ssl cert
-    `Cloud HSM` - cloud hardware security module - dedicate bits of hardware to store keys to authenticated
-    `Directory Service` - integration ms active service to aws services
-    `WAF` - web application firewall - at application layer to stop attacks, XSS, sql injection
-    `Shield` - by default for cloud front - ddos mitigation, prevent ddos attacks
-    `Artifact` - portal to download aws client reports, manage agreements 

**Mobile Services:**
-    `Mobile hub` - management console for mobile app for aws services
-    `AWS Pinpoint` - targeted push notifications
-    `AWS Appsync` - atomically updates data in web or mobile in real time
-    `Device Farm` - test apps on real device, iOS, android
-    `Mobile Analytics` - analytics service for mobile

**AR/VR:**
-    `Sumerian` - tools to create environment, super new

**Application Integration:**
-    `Step functions` - manage lambda functions and ways to go through it
-    `Amazon MQ` - message queue
-    `SNS` - notification services
-    `SQS` - decouple infrastructure, queue
-    `SWF` - workflow job creation

**Customer Engagement:**
-    `Connect` - contact center as a service, call center
-    `Simple Email Service` - email service, send grid, mailchimp

**Business Productivity:**
-    `Alexa for business` - manager for business needs
-    `Amazon chime` - google hangouts like
-    `Work Docs` - dropbox for AWS
-    `Work Mail` - Office 365 like
   
**Desktop and App streaming:**
-    `Workspaces` - VDI solution, run OS in aws cloud
-    `App stream 2.0` - streaming application to desktop of device
    
**IOT:**
-    `iOT` - devices sending sensor information
-    `iOT Device Management` - device management
-    `Amazon FreeRTOS` - OS for microcontrollers
-    `Greengrass` - ?? 

**Game Development:**
-    `Gamelift` - service to develop games

* * *

## What Services Will Be Tested On The Exam?
- `S3`
- `Glacier`
- `EC2`
- `EBS`


* * *

## Part 2

### Amazon S3 - Stands for Simple Storage Service
- S3 provides secure, durable, highly scalable object storage. 
- Store and retrieve any amount of data from anywhere on the web
- Safe place to store your files
  - Object-based storage up to 5TB (Objects consist of: KEY - name of the object, VALUE - data that is made up of a sequence of bits, VERSION ID - important for versioning, S3 allows you to have multiple versions of your files, METADATA - data about data you are storing, SUBRESOURCES - access control lists torrent)
- Unlimited storage
- **Files are stored in Buckets -> folder in which you store your files.**
- **Buckets must be unique globally.** When you create a bucket it gets a web address. That's why it has to be unique.
- When you upload to S3, you will receive HTTP 200 code if successful

#### Video 1 - S3 Basics
[![S3](assets/S3.png)](https://www.youtube.com/watch?v=f9hXcxHnQuE "S3 Basics")

#### Video 2 - S3 Netflix [High Level] Demo
[![S3Netflix](assets/S3Netflix.png)](https://www.youtube.com/watch?v=06AQA3xXXLA "How Netflix uses AWS")


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

* * *

## Part 3

### EC2 - Elastic Cloud Compute

AWS EC2 is a web service that provides re-sizable compute capacity in the cloud. EC2 reduces the time required to obtain and boot new server instances to minutes, allowing you to quickly scale capacity, both up and down, as your computing requirements change.

EC2 has changed the economics of cloud computing by allowing you to pay only for capacity that your actually use. EC2 provides developers the tools to build failure resistant applications and isolate themselves from common failure scenarios.

#### How Netflix uses AWS EC2 Video
[![EC2Netflix](assets/EC2Netflix.png)](https://www.youtube.com/watch?v=izyqJPl9wW8 "EC2 Netflix Video")

#### EC2 Basics Video
[![EC2](assets/EC2.png)](https://www.youtube.com/watch?v=dO1X7QG_4xw&t=3s "EC2 Basics Video")

### Pricing Options

#### On Demand

- Allows you to pay a fixed rate by the hour (or by the second) with no commitment.

**_Use Cases_**

- Perfect for users that want the low cost and flexibility of EC2 without any of the up front payment or long term commitment
- Applications with short term, spiky or unpredictable workloads that cannot be interrupted
- Applications being developed or tested on EC2 for the first time

#### Reserved

Provides you with a capacity reservation, and offer a significant discount on the hourly charge for an instance. 1 year or 3 year terms.

**_Use Cases_**

- Applications with steady state or predictable usage
- Applications that require reserved capacity
- Users can make up front payments to reduce their total computing costs even further
  - Standard RIs (Up to 75% off on-demand)
  - Convertible RIs (Up to 54% off on-demand) feature the capability to change the attributes of the RI as long as the exchange results in the creation of Reserved Instances of equal or greater value. Ability to go from CPU intensive instance to Memory intensive.
  - Scheduled RIs are available to launch within the time window you reserve. This option allows you to match your capacity reservation to predictable recurring schedule that only requires a fraction of a day, a week, or a month.

#### Spot

Enables you to bid whatever price you want for an instance capacity, providing for even greater savings if your applications have flexible start and end times.

**Use Cases**

- Applications that have flexible start and end times
- Applications that are only feasible at very low compute prices
- Used for single compute instances to save on costs compared to 9-5 during the week.
- Users with an urgent need for a large amount of additional computing capacity.

#### Dedicated Hosts

Physical EC2 server dedicated for your use. Dedicated Hosts can help you reduce costs by allowing you to use your existing server-bound software licenses.

**Use Cases**

- Useful for regulatory requirements that may not support multi-tenant virtualization.
- Great for licensing which does not support multi-tenancy or cloud deployments
- Can be purchased On-Demand (hourly).
- Can be purchased as a Reservation for up to 70% off the On-Demand price.

### EC2 Instance Types

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


**How to remember EC2 instance types F.I.G.H.T.D.R.M.C.P.X**
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

* * *

## Part 4

### EBS - Elastic Block Storage

Amazon EBS allows you to create storage volumes and attach them Amazon EC2 instances. Once attached, you can create a file system on top of theses volumes, run a database, or use them in any other way you would use a block device. EBS volumes are placed in a specific Availability Zone, where they are automatically replicated to protect you from the failure of a single component.

`_TLDR; A disk in the cloud that you attach to your EC2 instances_`

#### Elastic Block Store (EBS) Video
[![EBS](assets/EBS.png)](https://www.youtube.com/watch?v=S0gzrxsVQHo "Elastic Block Store (EBS)")


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


* * *

## Part 6 - Launching an EC2 Instance

#### What do I need to perform this tutorial?
- A computer with access to the internet, a Web Browser, and a command line terminal application (e.g. `Terminal` on a Mac, `putty` on Windows, etc.)
- We are going to access the Amazon EC2 console in your web browser and use it to configure and rent a remote computer from Amazon. 
- We are then going to log into that computer from the command line using a terminal application. 
    - The computer you are working on can be almost anything and could be running Windows, Mac OSX, or Linux. 
 - The computer that we configure and rent from Amazon will be a Linux machine (though there are many other possibilities). - - You will use the terminal application on your computer to remotely log into this computer. 
 - The Amazon AWS computer you rent will be physically located somewhere that is likely far away from you. 
 - Depending on the `Region` you select in Amazon AWS it could be physically located in one of several large compute warehouses in the North America, South America, Europe or Asia.   

***
**Google Data Center, The Dalles, Oregon ([source](http://en.wikipedia.org/wiki/File:Google_Data_Center,_The_Dalles.jpg)):**
![Image of a data center](Images/AWS/DataCenter.jpg)

- Since we are going to create an Amazon instance that is running a Linux operating system you will need to learn the basics of working at a Linux command line. You will also need to become familiar with basic fundamentals of Linux system administration.
 
### Creating an account
- In order to use AWS for the first time, you will need to create an account. 
- In order to create and run instances as described, you will need to associate a credit card with that account for billing purposes. Refer to the sections below on how billing works, how to estimate costs, and how to ensure that you have properly shut down everything that you could be billed for. 

* * *
**To run this tutorial as it is described should cost at most a few dollars.**
* * *

### Logging into the AWS console
- To log into AWS, go to [aws.amazon.com](http://aws.amazon.com/) and hit the [Sign In to the Console](https://console.aws.amazon.com/console/home) button as shown below. 
- If needed, create an account and activate it by associating a credit card. 
- Once you are logged in, select `EC2` from the list of Amazon Web Services. This tutorial is entirely focused on `EC2` (with some mention of `S3`) so the `EC2` console will be the starting point for many of the activities described below.

***
**AWS home:**
![AWS-Home](Images/AWS/AWS-Home.png)
***
**AWS log in:**
![AWS-Login](Images/AWS/AWS-Login.png)
***
**List of AWS services (select EC2 for this tutorial):**
![AWS-Services](Images/AWS/AWS-Services.png)
***
**The AWS EC2 dashboard:**
![AWS-EC2-Dashboard](Images/AWS/AWS-EC2-Dashboard.png)
***

### What is a Region?
- As discussed before, an AWS `Region` is set of compute resources that Amazon maintains (each like the `Data Center` image shown above). 
- Each `Region` corresponds to a physical warehouse of compute hardware (computers, storage, networking, etc.). 
- At the time of writing there are 8 regions: `(US East (N.Virginia)`, `US West (Oregon)`, `US West (N. California)`, `EU (Ireland)`, `EU (Frankfurt)`, `Asia Pacific (Singapore)`, `Asia Pacific (Tokyo)`, `Asia Pacific (Sydney)`, and `South America (Sao Paulo)`.
- When you are logged into the AWS EC2 console you are always operating in one of these 8 regions. 
- The current region is shown in the upper right corner of the console between the `User` menu and `Support` menu. 
- It is important to pay attention to what region you are using for several reasons. First, when you launch an EC2 instance, this happens in a specific region. 
  - If you switch regions later, you will not see this instance. 
  - To find info in the console you will have to switch back to the region where that instance was created. 
    - The same reasoning applies for EBS volumes, AMIs, and other resources. 
    - These are tracked within a region. Second, the cost to use many AWS resources varies by region. 
    - Third, since each region is located in a different part of the world, this may influence network performance when you are accessing the instance and especially if you need to transfer large amounts of data in or out. 
    - For example, if you are working in the US and you are going to be uploading RNA-seq data to EC2 instances, it probably does not make sense to create those instances in `Asia Pacific (Sydney)`. 
- Generally you should choose a region that is close to you or your users. 
  - But cost is also a consideration. 
  - It is important to be aware of regions when it comes to billing because if you are using resources in multiple regions it is easy to lose track of what you have running and you might wind up paying for something that you forgot to shut down. 
- We will discuss billing and cost in further detail below.

***
**The `Region` menu in the EC2 console:**
![AWS-EC2-Regions](Images/AWS/AWS-EC2-Regions.png)
***

### How much does it cost to use AWS EC2 resources?
- Estimating the cost to use AWS resources can get complicated.  
- For the most part when you launch an EC2 instance or create an EBS or S3 volume, you are renting and reserving that resource. 
- You will generally be charged for as long as you reserve that resource regardless of how you use it. 
  - For example, if you rent an 8-core machine with 1Tb of disk, and 64Gb of RAM, once you start that machine you will be charged an hourly rate for as long as it is running. 
    - Even if you do not use it much. 
    - Even if you do not log into it at all! 
    - You have reserved it, it is being run for you, that resource can not be rented to someone else, so you must pay for it. 
- To get a sense of how much a particular resource costs, spend some time examining the [AWS EC2 Pricing](http://aws.amazon.com/ec2/pricing/) list. 
- Remember that `Region` can influence cost, so once you decide on the type of resources you need you should compare the cost of that resource across multiple regions. 
- The pricing list is an extremely long page, broken down into several major categories: 
- `Free Tier` (light weight resources you can experiment with for free) 
- `On-Demand Instances` (rent by the hour, as we do in this tutorial)
- `Reserved Instances` (get a discount by renting longer term)
- `Reserved Instance Volume Discounts` (get further discounts by being an enterprise scale user)
- `Spot Instances` (bid for unused Amazon EC2 capacity in an open market)
- `Data transfer` (moving data in and out of EC2)
- `EBS-Optimized Instances` (for high performance file I/O)
- `Amazon Elastic Block Store` (rent storage volumes separately from Instances)
-  etc.  
- Amazon provides a [Monthly Calculator](http://calculator.s3.amazonaws.com/index.html) to help you predict what your costs might look like.

- In this explanatory section, we are going to use an `On-Demand Instance`. 
    - Let look more closely at that section of the [pricing list](http://aws.amazon.com/ec2/pricing/) by referring to the example screenshot below. 
    - Note that we have selected `US West (Oregon)` as our region and we are looking at the `General Purpose` section of the table and assuming that we will launch a `Linux` instance. 
    - These tables enumerate the features of various computer configurations that you can rent by the hour. 
    - Consider a particular instance type in this table, for example `m3.xlarge`.  
    - For this instance, we are told the number of CPUs that will be available on the machine (4), the amount of memory (15 GiB), the storage that will be pre-configured (2 x 80GB SSD drives), and the cost per hour to rent this machine ($0.140 per Hour).  
    - Note how much jargon is used in these tables.
      - Memory is reported in GiB and storage is reported in GB ([1GiB ≈ 1.074GB](http://en.wikipedia.org/wiki/Gibibyte)). 
      - For the number of CPUs we are told both the number of vCPUs (virtual CPUs) and ECUs ([Elastic Compute Units](http://aws.amazon.com/ec2/faqs/#What_is_an_EC2_Compute_Unit_and_why_did_you_introduce_it)). 
      - A virtual CPU is a reference to the number of physical CPUs that are available on the machine. 
      - It is referred to as `virtual` because we are actually creating a [virtual machine](http://en.wikipedia.org/wiki/Virtual_machine) when we create an EC2 instance. 
      - This virtualization allows Amazon to create a set of smaller virtual computers of varying specifications from larger phyiscal computers that they maintain. 
      - An ECU is a unit of computing that is meant to allow more accurate comparisons between machines that might have different generations of CPUs, recognizing that not all CPUs are created equally. 
      - The storage descriptions for EC2 instances may use the terms: `EBS only`, `SSD`, and `HDD`.  
- We will discuss EBS (Elastic Block Storage) in more detail below, but briefly EBS allows us to define one or more storage volumes of almost any size we wish. The hardware details of that storage will be handled for us behind the scenes. 
- EBS volumes exist independently of an EC2 machine and can be moved from one machine to another and the contents can be stored and attached to multiple EC2 instances over time (though only one instance at a time). 
- `SSD` refers to a solid state drive that is associated with the machine. 
- `HDD` refers to a hard disk drive that is associated with the machine. 
- `SSD` drives tend to be higher performance than `HDD` but also more expensive per unit of storage space. 
- When an instance indicates that it has `2 x 40 SSD` this means that is has two solid state drives, and each are 40GB in size.  
- The `SSD` and `HDD` drives associated with each instance and described in the pricing list are considered `ephemeral`. 
- We will discuss this important concept in more detail below.     

***
**An example AWS EC2 price list:**
![AWS-EC2-PriceList](Images/AWS/AWS-EC2-PriceList.png)
***

### How does billing work?

- Generally you get an accounting of usage and cost on a 30 day cycle. 
- You can get more detailed information on your account by going to the `Billing and Cost Management` section of the `User` menu in the EC2 console
- You can also refer to the [billing section](http://aws.amazon.com/ec2/faqs/#Billing) of the EC2 FAQ page. 

- Briefly, Amazon describes billing as follows:

> You pay only for what you use and there is no minimum fee. Pricing is per instance-hour consumed for each instance type. Partial instance-hours consumed are billed as full hours. There is no Data Transfer charge between two Amazon Web Services within the same region (i.e. between Amazon EC2 US West and another AWS service in the US West). Data transferred between AWS services in different regions will be charged as Internet Data Transfer on both sides of the transfer. Usage for other Amazon Web Services is billed separately from Amazon EC2. Billing commences when Amazon EC2 initiates the boot sequence of an AMI instance. Billing ends when the instance terminates, which could occur through a web services command, by running “shutdown -h”, or through instance failure. Instance-hours are billed for any time your instances are in a “running” state. If you no longer wish to be charged for your instance, you must "stop" or "terminate" the instance to avoid being billed for additional instance-hours. Billing starts when an instance transitions into the running state.

- This sounds simple but it tends to be more complicated than this. 
- EBS usage is billed separately from EC2 resources, even though the two are often intricately linked. 
  - For example, the root volume on a Linux Instance often exists as an EBS volume. 
  - You will be charged for this whether the system is running or stopped. 
  - Similarly, if you have an EC2 instance with an extra EBS volume(s) attached to it, you will be charged for this storage even when the EC2 instance is stopped. 
  - When you terminate the instance, associated EBS volumes may or may not be automatically destroyed. 
  - This behavior depends on how you configured the instance. 
    - We will discuss this configuration in further detail below. 
  - Similarly, if you create a `Snapshot` of your instance, this gets saved to EBS storage and you will be charged for these as long as they exist. 
  - When you create an AMI to save the state of your instance for later, this is stored as a `Snapshot`.  
  - The good news is that small EBS volumes are very cheap and by default the root volume for most instances is small (usually 8GB).

- If you choose an instance type with pre-configured storage or you attach EBS volumes for storage but set them to be deleted upon termination of the instance, and you never create any `Snapshots` or save the instance as an `AMI`, when you terminate that instance, all costs associated with it will be gone. 
- The cost will therefore be the hourly rate from the [pricing list](http://aws.amazon.com/ec2/pricing/) multiplied by the number of hours it was running rounded up to closest whole hour.

- In the `Billing and Cost Management` section of the EC2 console you can create billing alerts that will warn you of ongoing costs. 
- If you find that you are being charged a monthly fee but you are not intentionally using any resources, you should follow these steps. 
- Log into the AWS EC2 console. 
  - Now, *for each AWS Region*, determine the following; Are there any?:
    - `Running Instances`? 
    - `Volumes`? `
    - 'Elastic IPs`?
    - `Snapshots`?  
    - If any of these values are greater than 0, in *any one or more regions*, you are likely being billed monthly for resources that Amazon is reserving for you until told otherwise. 
    - If you terminate or delete all of these items, your monthly bill should return to $0.

### Necessary steps for launching an Instance
- In the following sections we are going to launch an example instance, configure it in the AWS EC2 console, discuss some of the important concepts of this configuration and log into the instance once it is running. 
- In each case, screenshots from an example instance will be shown and discussed. 
- To get started, make sure you are logged into AWS and go to the `EC2 dashboard`. 
- To start using EC2 we will launch a virtual server running the latest stable version of the Ubuntu operating system. 
- We will decide on the basic hardware for this server, configure storage that will be available on it, configure its security, and so on. 
- Once it is running we will log into this server and perform some additional exercises and configuration. 
- To get started press the blue `Launch Instance` button. 
- Remember that you are launching this instance in a particular `Region`. 
- In the following example we launched an instance in `US East (N. Virginia)`. (Pick the closest to your location)

***
**Launching an instance:**
![AWS-EC2-LaunchInstance](Images/AWS/AWS-EC2-LaunchInstance.png)
***

### Step 1. Choosing an AMI 
- An [AMI](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) or `Amazon Machine Instance` is a template for launching an instance.  
- The AMI includes a template for a pre-configured root volume that contains an operating system (e.g. Ubuntu Linux, Windows, etc.)
- The AMI also includes basic configuration of storage volumes that will be available within an instance
- The first step to launching an instance is to select an AMI. 
- Refer to the screenshot below. 
- There are four main options when selecting an AMI: 
- `Quick Start`
- `My AMIs`
- `AWS Marketplace`
- `Community AMIs`
- In the `Quick Start` list we will select an Ubuntu AMI as our starting point
- The `Quick Start` AMIs section is a relatively short list of basic systems that have been chosen by Amazon as common starting points
- These have some degree of "official" support and testing on AWS
- The `My AMIs` section contains AMIs that you have created youself, perhaps using a `Quick Start` or `Community AMI` as a starting point
- For example, you might start with an Ubuntu AMI and install all of the bioinformatics software and other infrastructure you need to run an analysis pipeline
- You could then store this configured machine as an AMI to save your work
- Having an AMI allows you to share a complete system configuration, and to fire up a cluster of identical instances that are ready to go
- The `AWS Marketplace` contains AMIs where a company (often a software company) has configured a machine for certain applications
- You can browse through this section to get an idea what kinds applications are available
- Finally, the `Community AMI` section contains thousands of AMIs created by users around the world
- These AMIs are specific to each `Region` so if someone tells you about an AMI they want to share, be sure to search for it in the correct region
- If you create you own AMI and you want to share it with others, you can 'publish' it to the community
- It will still appear in you `My AMIs` section, but it will also then appear and be searchable in the `Community AMI` section.

- For this tutorial we will select the following AMI from the `Quick Start` list: `ami-9a562df2`
- This number is a unique ID for the AMI
- The full length description for this AMI is `Ubuntu Server 14.04 LTS (HVM), SSD Volume Type`
- We are also told that the `Root device type` is `EBS` and the `Virtualization type` is `HVM`
- `Ubuntu Server 14.04 LTS`, refers to the version of the Ubuntu OS
- This version is also known as Ubuntu '[Trusty Tahr](http://en.wikipedia.org/wiki/List_of_Ubuntu_releases#Ubuntu_14.04_LTS_.28Trusty_Tahr.29)'
- We are told that the `Root device type` of the AMI is `EBS`
- We will discuss storage in more detail but this means that the AMI is configured so that the `root volume` of the operating system will be installed on an EBS volume
- In practical terms, this means that information stored on the root volume, including the OS itself will persist if we stop the instance (i.e. the root volume is *not* ephemeral)
- The term `HVM` refers to a type of virtualization technologythat will be used by the instance, the other common type being `PV`
- A detailed discussion of virtualizition technology is outside of the scope of this tutorial but you can learn more details here: [Linux AMI virtualization types](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/virtualization_types.html) and [Ubuntu PV vs HVM](http://stackoverflow.com/questions/22130214/amazon-ec2-ubuntupv-or-ubuntuhvm). 
- On balance, the `HVM` option is now perhaps recommended over the `PV` option. Once you are ready to proceed, press the blue `Select` button next to the Ubuntu Server description.

***
**Step 1. Choose an Amazon Machine Image (AMI):**
![AWS-EC2-ChooseAnAMI](Images/AWS/AWS-EC2-ChooseAnAMI.png)
***

### Step 2. Choosing an Instance Type
- Once an AMI is selected, the next step is to choose an instance type
- In simple terms, in the previous step we decided on the operating system we want to run (Ubuntu v14.04), and now we need to chose the hardware that it will run on
- Refer to the following screenshot for this discussion
  - Note that in this example, we have selected `General purpose` in the drop down filter
  - This leaves us 7 choices for hardware configuration. 
  - Note that the price per hour for each of these options is not listed here
    - To get the price, note the instance type name (e.g. `m3.large`) and refer back to the [EC2 pricing list](http://aws.amazon.com/ec2/pricing/)
- At the time of writing, an `m3.large` instance in `US East (N. Virginia)` rented on an `On Demand` basis costs $0.140 per Hour
- We discussed many of the details described in this table of instance types in the pricing discussion above
- Briefly, we are given a series of options that differ in their number of CPUs, memory, pre-configured storage, network performance, etc.
- To view more or less details you can adjust this table using the `Show/Hide Columns option`
- In the example depicted below we have selected the `m3.large` option with 2 CPUs, 7.5 GiB of memory, a single 32GB SSD `Instance Storage` volume, and moderate network performance
- Once you are ready, proceed to the next step by pressing the `Next: Configure Instance Details` button

***
**Step 2. Choose an Instance Type:**
![AWS-EC2-ChooseAnInstanceType](Images/AWS/AWS-EC2-ChooseAnInstanceType.png)
***

### Step 3. Configuring Instance Details
- Once an instance type is selected the next step is to configure the instance details
- This step in the launch-an-instance procedure introduces many advanced concepts that will be covered only briefly here
- To learn more about each of the options available in this step you can mouse over the `i` symbol beside each
- For the most part, leaving all of these options at their default value will be fine
- Refer to the following screenshot while we discuss a few of these options briefly
- Using the `Number of instances` option you could launch multiple instances of the same AMI with the same hardware configurations at the same time
- However, in our example, only one instance will be launched
- You also have the option to attempt to negotiate a cheaper rental by using the [Request Spot Instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) option
- The `Shutdown behavior` option determines what will happen if you shutdown the instance from within the AMI (e.g. by issuing a `sudo shutdown` command in ubuntu linux)
- To prevent accidental termination of your instance, you may want to set this option to `Stop`
- You can also help to prevent accidental termination of your instance by using the `Enable termination protection` option
- These options can also adjusted later for any instance in the console
- Once you are ready, proceed to the next step by pressing the `Next: Add Storage` button

***
**Step 3. Configure Instance Details:**
![AWS-EC2-ConfigureInstanceDetails](Images/AWS/AWS-EC2-ConfigureInstanceDetails.png)
***

### Step 4. Adding Storage
- The next step is to configure the disk/storage that will be available in the instance
- The starting point of this page depends on what instance type we selected in Step 2
  - Remember that we selected an instance type with an EBS root volume (during AMI selection) and an additional 1 x 32 GB SSD drive
  - These two volumes are summarized in the `Add Storage` view
  - The first volume is 8 GiB.  This is the root volume where the operating system will exist
  - It is set to be deleted on termination of the instance but we could chose to keep it as well
  - The second row of the table shows as `instance store 0`. This is the 32 GiB SSD drive (though confusingly, the size is not shown here)
- Our two volumes are projected to be attached to the instance as `/dev/sda` and `/dev/sdb`. Sometimes this does not exactly match what we see inside the instance because device mapping behavior depends on the operating system
- Since the second volume is an `Instance Store` device, it is akin to a drive physically attached to the computer we are renting
- This should ensure high performance, but it is important to remember that such volumes are `ephemeral` and the contents will not persist if the instance is stopped or destroyed
- To demonstrate the difference, lets use the `Add New Volume` button to add a third volume to our instance (see Step 4b screenshot below)
- Choose `EBS` as the `Type`, set the device to `/dev/sdc`, give it a size of 500 GiB, and set the volume type to `General Purpose (SSD)`
- Now when we log into the instance we will expect to find three distinct storage volumes/devises. 

***
**Step 4a. Add Storage:**
![AWS-EC2-AddStorage1](Images/AWS/AWS-EC2-AddStorage1.png)
***

**Step 4b. Add additional Storage:**
![AWS-EC2-AddStorage2](Images/AWS/AWS-EC2-AddStorage2.png)
***

### Storage volume options 

#### What is ephemeral or `Instance Store` storage? What is `EBS` storage? Which is the better option for `Root device type`?
- An `EBS` ([elastic block storage](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)) volume can be linked to single instance
- `EBS` volumes can be set to persist even if the instance is destroyed
- They could therefore later be reassigned to a different instance
- In the context of bioinformatics analysis, you might decide to write your analysis results to an EBS volume
- Once analysis was complete you could then shut down the instance to save money but keep your results indefinitely on the EBS volume
- The [Instance Store](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) volumes are considered 'ephemeral' or transient
  - Therefore, you must be careful when storing data to these volumes because if the machine is stopped or terminated, the data will be unrecoverable
- Instance store volumes are created from disks that are physically attached to the host computer while EBS volumes are created from disk arrays in the same `Availability Zone` but are not physically attached to the host computer
- Instead the host computer accesses EBS volumes over a network
- EBS volumes can be added at will to an existing instance
  - On the other hand, Instance Store volumes can only be added or configured when the instance is created

- The `Root device type` refers to the type of volume used to store the operating system itself
- This is usually a small volume (often 8 GiB) that can be either `EBS` or `Instance Store` type
- This type option can be selected during the choice of AMI or when configuring storage during setup of the AMI
- Once you launch the AMI though you can not change the `Root device type`
- There are [pros and cons](http://stackoverflow.com/questions/3630506/benefits-of-ebs-vs-instance-store-and-vice-versa) to both `EBS` and `Instance Store` for the root device type
- The `Instance Store` type may have a performance advantage but the `EBS` type is more flexible and safer from the perspective of accidental data loss
- For a beginniner just starting to use AWS, we recommend `EBS`
- A bioinformatics analysis instance might use an `EBS` volume for `Root device type`, use an `Instance Store` volume for `/tmp` where all temporary files and staging of data will occur, and use an additional `EBS` volume to store the final results
- Notice that this is how we have configured the example instance in this tutorial
- You can examine the types of volumes for an existing Instance in the EC2 dashboard by selecting a running Instance and examining the `Root device type` value
- Once you are ready, proceed to the next step by pressing the `Next: Tag Instance` button

### Step 5. Tagging the Instance
- As you start to have a large number of instances running or saved you may want to start assigning `Tags` to these instances to help track their usage and billing details
- Try creating a `Tag` as a simple key/value pair
- In the example below we created a `name` tag with a value of `AWS Tutorial`
- Once you are ready, proceed to the next step by pressing the `Next: Configure Security Group` button

***
**Step 5. Tag Instance:**
![AWS-EC2-TagInstance](Images/AWS/AWS-EC2-TagInstance.png)
***

### Step 6. Configuring a Security Group:
- A `Security Group` controls how services and users can access your instance once it is running
- When you launch a new instance you can choose to configure a new Security Group and use it or select one that you created previously
- You can also select a `default` security group
- The purpose of Security Group settings is to determine what Inbound and Outbound network traffic will be allowed on the instance
- Since Inbound traffic could be coming from anyone (including those with malicious intentions) it is highly recommended that most incoming traffic be blocked and only certain incoming services be allowed on an as needed basis
- In the example below we created a Security Group called `AWS-Tutorial` that only allows incoming traffic of two types:
  - `SSH` (over port 22) 
  - `HTTP` (over port 80)
- The first rule, will allow us to log into our instance remotely using the SSH protocol
- The second rule, will allow us to set up a web server on the instance and access web content remotely using a web browser
- Both of these rules could be made significantly more secure by limiting access to only certain IP addresses
  - For example, if you will access your AWS instances only from your university you could limit access to your universities IP address (or a range of addresses)
- You can reconfigure the `Security Group` settings at any time, but they will not take effect until the instance has been rebooted
- Create two Incoming rules that match those in the screenshot and name your new security group
- Once you are ready, proceed to the next step by pressing the `Review and Launch` button

***
**Step 6. Configure Security Group:**
![AWS-EC2-ConfigureSecurityGroup](Images/AWS/AWS-EC2-ConfigureSecurityGroup.png)
***

### Step 7. Reviewing the Instance before Launch
- At this stage you will be presented with a final summary describing the configuration of your instance
- Some warnings may appear
- A conservative security warning is often presented here if you have allowed any broad Incoming access to the instance
- Once you are ready, proceed to the next step by pressing the `Launch` button

***
**Step 7. Review Instance Launch:**
![AWS-EC2-ReviewInstanceLaunch](Images/AWS/AWS-EC2-ReviewInstanceLaunch.png)
***

### Step 8. Assigning a Key Pair
- You will now be presented with a final, but very important configuration step, assignment of a `Key Pair`
- A Key Pair consists of two keys, a `public key` and a `private key`
- The `public key` will be stored in AWS. The `private key` will will be presented to you on creation and it *must be saved by you* to allow you to log into your instance later
- If this is your first instance you will have to `Create a new key pair`
- In the example below we have chosen to create a new key pair called `AWS-Tutorial`
- Once the name is chosen, press the `Download Key Pair` button
- You will download a simple text file called `AWS-Tutorial.pem`
- Store this file somewhere on your computer (e.g. your home directory) and remember the location
- The contents of this file will contain an RSA key that should look something like this:

```
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAhEpF18lIUouMH8qia/BSB70vrQVq/mTTkiRbsACB78rzy3XGRMfvwUseIsGY
H6SDOAFrRlmTrAArH5A0t2TZ8PKrq7b9FtEAvMCeE7rWEiqBblAWiER0k1pbnIqyKJJCo1YRSUs0
oNMdvjB4CUylYraSsSNFYJG5gRwcNhBENLDVnDS79geQcPLu/JeEiJ9V+w+CCYAG40f7li/TuULr
rSy6Oq6jgn2Gy7rrHU7XHU5hcEvxuSeoLb8h/bH1N+cN/H7x3ipEjIDdA2ScCkRXum1V6/kTFQFq
vDG0lqoTlmTNKgDGpb+rdzJgOg/3QX4RSrX/c0W6aFkV9Ib/jQxT+wIDAQABAoIBADAvWXc6wpQG
bjiaN0T3mPlmqHnuEkWs9f8yLQ9TcACmvNwr/tbIuISAVu6z8zP7WSxKIAfU0twAh7SMcxclrdh8
m5kFIvRvlkQqKKnpENY3E0PZ+gsSXB/b9qhzQGdUtt8Fl3BJ61Z07016HA7PEyJ8e7v3q+p7ycTE
N2Zd0GocRIX8zxdRo9GS8ouS0QcFgNF8KblzlJ6Vs0gI7o7mIRZIm9vWkuR9Lp9uEPD2flUIvN3z
yRmY/FE/R1yc76Uq+g8eywifRAh+GFyyO8PmFoYRni4Ki6+tEIFaq5JauT0JJF66EZeZP8ZKoWm9
1K30Ucti2D5l8t+CpbBM5JxhmjECgYEAxz1ET42F1sBGYqNn5hmfjrRp+YF3EYz2awRSibOeerpJ
Bh1QZeB7/QD3wcB00XFiMu/3haP9xs4eesjSSug+1F59nyzDplNsybz1sYpUQwP9LjX0loUCIb8r
3O2VdLJ5ZJ9dfNgpStC/wi7kkr8xjK5XiHgP6DLk6+H1Lr2d+kMCgYEAqfpUseZ/sm1vYt80LlWI
r8ozsUmzuISRspGVUppyDD47Iyj/1mkiWnsFDDl07oBcFIUFIEd1rkJNB3gXKSr76kcY0X4lav7a
0dvse2T9PC/pLSFkax9UjVnydCN8ElyNoXI2wT5HuLDjjCmHBD/4E9ZOO201JICSbRxaykl17+kC
gYEAxRiWuxwFiqwq9Okxny856LIRJAIvB+2q17Mu84n8/OvL0YCuSBoKjf6nGcSJy6eevUUmV84i
/sho3o5Lek7F2NCg9RYTdjaRKAEGDNwK/0Cy9UPq8fwiX7/+ZE+jyg3EiQYeNaKhNqHLEQ3SkFkT
a1gMv7QGCG5QiAi/w71QyoECgYARcn+VDyrWXsNLK8wIYYE5QhESRpVrADiQUr84DmBcf1rEniW8
lWgQT4ZSHeexv300If9Hs+4RZ/7OIHaIJEBdaNTUVBV1KRm+5sscU15m+if+GOpc0Id2RuBLKYVH
wTZMdxPFvCXSgF2q+mxAdGx7ZMj88pW83HGrP3jWQLoZWQKBgQCX5jxy3QXlPpwDppqwKKBQ8cGn
YDDQHCeD5LhrVCUqo5DCobswzmGKU/xEqYsqlk/Mz1Zkvg4FbJwJDgQGkSyAu071NLi0O6w27dm+
UHuvF5mCDdAHWirFUBSiebxOpEQnkZ9IPXUUCSC6IQvPFbdGN8G3WjoER6Lw121Q4rJxGA==
-----END RSA PRIVATE KEY-----
```

- If this is not your first instance and you have already created a key pair, and *you still have that key file*, you can choose to use the existing key pair. 

***
**Step 8. Select an existing Key Pair or create a new Key Pair:**
![AWS-EC2-CreateKeyPair](Images/AWS/AWS-EC2-CreateKeyPair.png)
***

- To prepare for logging into our instance, lets create a directory on our own `local` computer (i.e. the one you are sitting at) and store the key file there
- Later we will use this file to log onto the AWS instance
- We are using a mac system
- To create a directory and move the key file we downloaded into that directory we can down the following in a Mac Terminal session:

```bash
mkdir ~/AWS-Tutorial
mv ~/Downloads/AWS-Tutorial.pem ~/AWS-Tutorial
cd ~/AWS-Tutorial
chmod 400 AWS-Tutorial.pem 
ls
```

- The `chmod 400 AWS-Tutorial.pem` command changes the permissions of your key file so that only you can read it
- This is an important security setting
- If you attempt to log into your instance using a key file with inappropriate permissions, the login command may fail
- So you should always perform this command on any new key file (or copy of such a file) before attempting to use it to log into an instance

### Step 9. Reviewing launch status
- Once you have launched your instance, you will be presented with yet another review page
- When you are ready, proceed to the next step by hitting the `View Instances` button

***
**Step 9. Review launch status:**
![AWS-EC2-LaunchStatus](Images/AWS/AWS-EC2-LaunchStatus.png)
***

### Step 10. Examining a new Instance in the EC2 Console
- You should now see the EC2 Console view for a new instance
- This view shows a table of all Instances you have created in the current `Region`
- When an instance is terminated it will remain visible in this table for a brief time and then will be automatically removed
- You should see a single entry that when selected looks much like the example below
- After a few minutes, your instance should achieve an `Instance State` of `running`
- Note the incredible wealth of information available both in the table and in the `Description` view below
- Much of the configuration we described above will be summarized here
- To work effectively with your instances you will need to become familiar with certain features of this EC2 console view
- For example, the `Name`, `Instance Type`, `AMI ID`, `Root device type`, `Root device`, and `Block devices` will help to remind you what kind of instance you configured
- In order to remotely log into the instance, the following items in the console will be relevant: `Instance State`, `Key Pair Name`, `Security Groups`, and `Public IP` (or `Public DNS`)
- Try to familiarize yourself with each of these features and how to find them in the console for each instance you have have running

- To modify an instance in the EC2 console you can select that instance (or a series instances) using the blue check boxes at the left
- You can then perform various tasks using the `Actions` menu
- You can also right click on a single instance to obtain a similar menu
- Before logging into this instance lets take a momemt to examine various important sections of the EC2 console in particular the `EC2 Dashboard`, `Volumes`, `Security Groups`, and `Key Pairs`
- In each of these views you should see new entities that correspond to the instance we just created

***
**Step 10. EC2 Console view of a new Instance:**
![AWS-EC2-Console](Images/AWS/AWS-EC2-Console.png)
***

**The EC2 dashboard should now show a running Instance, Volumes, etc.:**
![AWS-EC2-Dashboard2](Images/AWS/AWS-EC2-Dashboard2.png)
***

**Review new Volumes:**
![AWS-EC2-Volumes](Images/AWS/AWS-EC2-Volumes.png)
***

**Review new Security Groups:**
![AWS-EC2-SecurityGroups](Images/AWS/AWS-EC2-SecurityGroups.png)
***

**Review new Key Pairs:**
![AWS-EC2-KeyPairs](Images/AWS/AWS-EC2-KeyPairs.png)
***

### Step 11. Logging into an instance
- We are finally ready to log into our instance
- To do this, open a terminal session on your local computer (e.g. using `Mac Terminal` or `Windows Putty`)
- Change directories to the location where you stored your key file `AWS-Tutorial.pem`
- Now at the same time, view your instance in the EC2 console
- Make sure that the `Key pair name` for this instance matches the `.pem` key file
- Also, get the `Public IP` value from the console and use it instead of the example one below. Note that you could use the `Public DNS` value instead if you want

- Finally log in as follows:
```bash
cd ~/AWS-Tutorial
chmod 400 AWS-Tutorial.pem
ssh -i AWS-Tutorial.pem ubuntu@52.5.92.87
```

```In this example, we open a terminal command line session on our local computer. We moved to the location of my `.pem` key file. We then made sure the permissions of this file were set correctly using a `chmod` command. You only need to do this step once but there is no harm in doing it again. Then we executed an SSH command to remotely log into our AWS instance using the `Public IP` 52.5.92.87. Our SSH command included an option to use the `.pem` file to identify us as the owner of the instance. We logged into the instance as a user called `ubuntu` because that is a user that we know will be defined by default on all ubuntu systems. Once logged in you can create new users if you wish. If your login is successful, you should see something like that shown in the screenshot below.```


**Step 11. Log into Instance:**

* * *

### Trouble-shooting and advanced topics

### I cannot log into my EC2 instance, what might have gone wrong?
If you tried the above and it did not work there are several possible explanations. 
- First, check the `Instance State` of your instance in the EC2 console. Is it `running`? When you first start an instance it takes a few minutes to boot up. Similarly, if you reboot the instance for some reason, you will not be able to log into it until it comes back online. 
- Second, are you in a terminal session in the directory where you stored your `.pem` key file? 
- Third, is this the right key file? Each instance is associated with a single `Key Pair` and you must have the key file that was created when that `Key Pair` was created. If you delete a key file and later generate a new one, it will not work with instances that used an older `Key Pair` even if you name the file the same thing. 
- Fourth, have you set the permissions for your `.pem` key file correctly. Do not forget to run `chmod 400 *.pem` on your key file. 
- Fifth, did you remember to include the `-i key_file_name.pem` in your SSH command? 
- Sixth, did you remember to specify what user you want to log into the system as? You must include the `ubuntu@` (or other valid user name) before the IP address to log into an Ubuntu system by SSH. 
- Seventh, did you specify the correct IP address for the instance you want to log into. The value after `ubuntu@` must match the `Public DNS` or `Public IP` value that is shown in the AWS EC2 Console.  Note that there are also `private` versions of these two values. Only the `Public` version will work from your local computer.
- Eighth, does the `Security Group` used for the instance allow Incoming SSH Access? Make sure your `Security Group` has an entry for type `SSH`, protocol `TCP`, port `22`, from source `Anywhere`. If you have to change the `Security Group` settings to allow access, you will have to reboot the instance before they take effect.  

### How do storage volumes appear within a Linux instance on Amazon EC2?
- Now that you are logged in, you can investigate how the storage options you choose when creating the instance manifest inside an AWS Ubuntu instance
- First try using the command `df -h` to view existing storage devices that are mounted
- If you created a system exactly as decsribed above, you should see two devices (`/dev/xvda1` of 7.8G mounted as `/`) and (`/dev/xvdb` of 30G mounted as `/mnt`)
- These are the `EBS` root device volume and the ephemeral 30G `Instance Store` volume that come with the `m3.large` instance type we chose
- Remember that we also added another `EBS` volume that was 500 GiB in size. Where is that device? 
  - It is not currently mounted
  - To view all devices the system knows about you can do something like this command: `ls /dev/` or `ls -1 /dev/ | grep xvd`
  - You should now see three devices: `xvda`, `xvdb`, and `xvdc`
    - Lets format and mount the device `xvdc` to a new directory `data` as follows:

```bash
lsblk
cd /
sudo mkdir data
sudo mkfs -t ext4 /dev/xvdc
sudo mount /dev/xvdc /data
sudo chown -R ubuntu:ubuntu /data
df -h
lsblk
```

- NOTE: Refer to AWS docs [about using EBS Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html) for more details.

- Now the same `df -h` command we performed above should show a new volume `/dev/xvdc` mounted at `/data` of size 493G
- Note that in order to make this new mount persist when we reboot the machine we will have to add a mount line like this to the `/etc/fstab` file (e.g. by `sudo vim /etc/fstab`):
```
/dev/xvdc /data  auto  defaults,nobootwait 0 2
```

### Taking stock of compute resources within an Ubuntu Linux instance
- To examine other resources within the Ubuntu instance you should familiarize yourself with the command `top` (press `1` to show CPUs and `q` to exit)
- You can also learn about the system by examining `cat /proc/meminfo`, `cat /proc/cpuinfo`, and `lsb_release -a`.  

### Basic setup and administration of an Ubuntu Linux instance
- To update your Ubuntu OS to use the latest security patches etc. you can do the following:
```bash
sudo apt-get update
sudo apt-get upgrade
sudo reboot
```

### Setting up an Apache web server
- If you want to easily retrieve or share data created on your instance, one option is to start an Apache web service on the instance so that you can browse the contents of certain directories remotely in a web browser
- Note that when launching the instance our security group was configured to allow http access via port 80 so that this would work.

* Edit config to allow files to be served from outside /usr/share and /var/www
```
sudo vim /etc/apache2/apache2.conf
```

* Add the following content to apache2.conf
```
<Directory /home/ubuntu/>
       Options Indexes FollowSymLinks
       AllowOverride None
       Require all granted
</Directory>
```

* Edit vhost file
```
sudo vim /etc/apache2/sites-available/000-default.conf
```

* Change document root in 000-default.conf
```
DocumentRoot /home/ubuntu
```

* Restart apache
```
sudo service apache2 restart
```

- You should now be able to enter the `Public IP` or `Public DNS` in a web browser on your local computer and browse the contents of the `/home/ubuntu` directory on your AWS instance

### What is difference between the 'Start', 'Stop', 'Reboot', and 'Terminate' (Instance States)?
- From the AWS EC2 console, you can change the state of each of your instances
- The `Start` command will boot a system that has been powered down
- The `Stop` command will power down the instance and is similar to performing `sudo shutdown` from within the instance (if you have configured your instance that way during creation)
  - Do not forget that if you stop an instance with ephemeral `Instance Store` volumes, the contents of these volumes will be lost
- The `Reboot` command will simply reboot the machine
  - This is equivalent to using a `sudo reboot` command from within the instance
- The `Terminate` command will destroy the instance and any ephemeral `Instance Store` volumes associated with it
- If the root device is an EBS volume it may or may not be destroyed depending on how you configured the instance during creation
- If there were additional EBS volumes associated with the instance and you `Terminate` the instance, these may also be destroyed if you selected that option when they were being created
- Before terminating an instance you should think carefully about whether there is data you want to save and if so, how the volumes will behave on termination
- Similarly, if you want to destroy all components of an instance, including all associated volumes, you may need to terminate the instance and then separately destroy certain volumes 

### Tidying up and shutting down AWS resources
- Once you are done with this tutorial you should terminate or delete all resources that were created to ensure you are not charged
- Specifically you should remove: `Instances`, `Volumes` and `Snapshots`
- You may also decide to remove other entities that were created for demonstration purposes including: `Tags`, `AMIs`, `Security Groups`, and `Key Pairs`
- All of this can be done in the AWS EC2 console
- hen you are done, the `EC2 Dashboard` should show `0` for all resource types except `Security Groups` where a single default security configuration will remain

### Further reading (Optional)
- This is a basic introduction to AWS cloud computing that assumes all configuration of the instance will occur within the AWS EC2 console of your web browser and all configuration of the Ubuntu Linux system will occur by the user manually executing commands and perhaps saving the outcome as a cusom AMI
- For large scale computing and complex deployments of compute infrastructure on the cloud these methods will not be sustainable
- Here is a list of more advanced topics for discussion on how to move beyond the console and automate configuration of your system:
- Use of the [AWS command line interface (CLI)](http://aws.amazon.com/cli/)
- Use of the [AWS EC2 API](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/Welcome.html)a
- Use of [AWS SDKs](http://aws.amazon.com/tools/#SDKs)
- Use of [S3](http://aws.amazon.com/s3/) and [glacier](http://aws.amazon.com/glacier/)
- Use of [vagrant](https://www.vagrantup.com/) to launch AWS instances
- Use of [puppet](https://puppetlabs.com/puppet/what-is-puppet) to configure Linux systems




* * * 
### Practice Questions

#### What are the advantages of cloud computing?
** Answer
6 advantages: 
- Trade capital expense for variable expense
- Stop guessing about capacity
- Increase speed and agility
- Stop spending money running and maintaining data centers
- Go global in minutes

#### What are the types of cloud computing?

** Answer
- Infrastructure as a Service (IaaS)
- Platform as a Service (PaaS)
- Software as a Service (Software as a Service)

#### What are the models of computing deployment?

** Answer
- Public
- Hybrid
- On-premises

#### What is S3 and what does it mean?

** Answer
S3 stands for Simple Storage Service.
S3 is on object storage with a simple web interface to store and 
retrieve any amount of data from anywhere on the web. 

#### What are some usages of S3?

** Answer
You can use Amazon S3: 
- as primary storage for cloud-native applications
- as a bulk repository, or "data lake," for analytics
- as a target for backup and recovery and disaster recovery
- with serverless computing. 

#### What are the features of S3?

** Answer
**9 features:**

- Simple: easy-to-use web based management console + REST API
- Durable: your data is redundantly stored across multiple facilities and multiple devices in each facility
- Scalable: you can store as much data as you want and access it 
when needed.
- Secure: Amazon S3 supports data transfer over SSL and automatic encryption of your data once it is uploaded. You can also configure bucket policies to manage object permissions and control access to your data using IAM
- Available: designed for up to 99.99% availability of objects over a given year and is backed by the Amazon S3 Service Level Agreement ensuring that you can rely on it when needed. 
- Low cost: Using lifecycle policies, you can set policies to automatically migrate your data to Standard - Infrequent Access and Amazon Glacier as it ages to further reduce costs
- Simple data transfer: Amazon provides multiple options for
cloud data migration and makes it simple and cost-effective for you to move large volumes of data into or out of Amazon S3. You can choose from network-optimized, physical disk-based, or third-party connector methods for import to or export from Amazon S3
- Integrated: Amazon S3 is deeply integrated with other AWS services to make it easier to build solutions that use a range of AWS services
- Easy to manage: Amazon S3 Storage Management features allow you to take a data-driven approach to storage optimization, data security, and management efficiency. These enterprise-class capabilities give you data about your data, so you can manage your storage based on that personalized metadata.


#### What is AWS EC2?

** Answer
EC2 stands for Amazon Elastic Compute Cloud. 
It is a web service that provides secure, resizable =compute capacity= in the cloud. 
It is designed to make web-scale computing easier for developers.

#### What is a region?

** Answer
A Region is a physical location in the world where we have multiple Availability Zones (AZs).


#### What is an Availability Zones ?

** Answer
AZs consist of one or more discrete data centers, each with redundant power, networking,and connectivity, housed in separate facilities.

#### What is an Edge Location?

** Answer
Edge Locations are endpoints for AWS which are used for caching content. There are many more Edge Locations than Regions. Currently there are over 96 EL.* Question :drill:

#### What is the difference between a region, an Availability Zone and an Edge Location?

** Answer
- A region is a physical location in the World which consists of two or more Availability Zones.
- An AZ is one or more discrete data centers, each with redundant power, networking and connectivity, 
housed in separate facilities
- Edge locations are endpoints for AWS which are used for caching content.


#### What is IAM?

** Answer
Essentially, IAM allows you to manage users and their level of access to the AWS Console.


#### Critical terms of IAM?

** Answer
- Users - End Users (think people)
- Groups - A collection of Users under one set of permissions
- Roles - You create roles and can then be assign them to AWS resources
- Policies - A document that defines one (or more permissions). Can be attached to User/Group/Role.

#### Is IAM Global?

** Answer
Yes

#### What is the root account?

** Answer
This is the email address used to sign up in AWS.
Unlimited access to do things in the cloud.


#### Which permissions have new users when created?

** Answer
New users have NO permissions when first created

#### What is the difference between access keys and user/pass?

** Answer
You cannot use the Access Key ID and Secret Key to login in the console. You can use this to access AWS via the APIs and CLI however.

#### What is S3?

** Answer

S3 provides developpers and IT teams with secure, durable, highly-scalable object storage. Amazon S3 is easy to use, with a simple web service 
interface to store and retrieve any amount of data from anywhere on the web.


#### Size of the files on S3?

** Answer
From 0 Bytes to 5 TB

#### What is the data consistency model for S3?

** Answer
- Read after Write consistency for PUTS of new Objects
- Eventual Consistency for overwrite PUTS and DELETES (can take some time to propagate)

#### S3 is object based. What do objects consist of?

** Answer
- key (This is the name of the object)
- value (This is the data and is made up of a sequence of bytes)
- version ID (very important for versioning)
- metadata (data about data you are storing)
- subresources:
  - Access Control Lists
  - Torrent (not an exam topic)


#### What are the different Tiers/Classes of storage for S3?

** Answer
- S3 standard : 99.99% availability, 99.999999999% durability, stored redundantly across multiple devices in multiple facilities, and is 
designed to sustain the loss of 2 facilities concurrently. No retrieval fees

- S3 - IA (Infrequently Accessed) : For data that is accessed less frequently, but requires rapid access when needed. Lower fee than S3, but you are 
charged a retrieval fee.

- S3 One Zone - IA : want a lower cost option for infrequently accessed data, but do not require the multiple AZ data resilience.

- Glacier : Very cheap, but used for archival only. Expedited (higher fees less retrieval time -- within minutes),
 Standard (3-5 hours) or Bulk (5-12 hours).


#### S3 Charges?

** Answer
Charged for 
- Storagex
- Requests
- Storage Management Pricing (the tags you use on your data, added on the metadat of your files)
- Data Transfer Pricing (when you transfer data from one region to another)
- Transfer Acceleration

#### What is S3 Transfert Acceleration?

** Answer
Amazon S3 Transfert Acceleration enables fast, easy, and secure transferts of files over long distances between your end users and an S3 bucket. 

Transfert Acceleration takes advantage of Amazon CloudFront's globally distributed edge locations. As the data arrives at an edge location, data 
is routed to Amazon S3 over an optimized path.

#### What are the server side encryption options for S3?

** Answer
- SSE with Amazon S3 Managed Keys (SSE-S3)
- SSE with KMS (SSE-KMS)
- SSE with Customer Provided Keys (SSE-C)


#### What are the two options for controlling access to a S3 bucket?

** Answer
- Bucket ACL
- Bucket Policies

#### S3 Versioning characteristics?

** Answer
- Stores all versions of an object (including all writes and even if you delete an object)
- Great backup tool
- Once enabled, versioning cannot be disabled, only suspended
- Integrates with Lifecycles rules
- Versioning's MFA Delete capability, which uses multi-factor authentication, can be used to provide an additional layer of security.

#### Cross replication on S3?

** Answer
- Versioning must be enabled on both the source and destination buckets
- Regions must be unique
- Files in an existing bucket are not replicated automatically. All subsequent updated files will be replicated automatically.
- You cannot replicate to multiple buckets or use daisy chaining (at this time)
- Delete markers are replicated
- Deleting individual versions or delete markers will not be replicated

#### Lifecycle Management in S3?

** Answer
- Can be used in conjunction with versioning
- Can be applied to current versions and previous versions
- Following actions can now be done:
  - Transition to the Standard IA storage class
  - Archive to Glacier Storage Class
  - Permanently Delete

#### What are the two types of encryption on S3?

** Answer
- In Transit: when you are sending data to your bucket
  - SSL/TLS
- At Rest 
  - Server Side Encryption 
    - S3 Managed Keys - SSE-S3 each bucket is encrypted with a unique key Amazon encrypt the key itself with a master key that is regularly rotated.
      Amazon handles all the keys for you (AES 256)
    - AWS Key Management Service, Managed Keys - SSE-KMS Similar to SSE-S3 with some additional benefits s.a. who is decrypting what and when + option to manage the keys yourself.
    - Server Side Encryption with Customer Provided Keys - SSE-C where your manage your keys and AWS is responsible for the encryption and decryption.
  - Client Side Encryption
