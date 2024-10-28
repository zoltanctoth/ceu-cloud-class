# **Week 2 - AWS**

## **Using AWS programmatically**

### **Recap video***

[AWS EC2 Recap](https://youtu.be/6FfLocjBcNE)

### **Part 1. Preamble, Regions, Availability Zones (AZ), Edge Locations**

Cloud computing allows users to quickly access vast amounts of computing resources remotely, without the need to purchase or maintain hardware. There are many cloud providers offering these services; this lecture focuses on Amazon Web Services (AWS). The fundamental concepts we discuss, however, apply broadly to other providers, such as Google Cloud and Microsoft Azure, though the terminology may differ between platforms.

### Glossary and Abbreviations

- **AWS (Amazon Web Services)** - A collection of cloud computing services provided by Amazon.
- **EC2 (Elastic Compute Cloud)** - AWS service that provides resizable cloud hosting, allowing you to configure and rent virtual machines on an as-needed basis.
- **EBS (Elastic Block Storage)** - Persistent storage solution that integrates with EC2. EBS volumes are generally SSD-backed, providing reliable storage that can only be attached to a single EC2 instance at any given time.
- **S3 (Simple Storage Service)** - Cost-effective, large-scale storage solution. Unlike EBS, which allows direct attachment as a local drive, S3 stores data as objects accessed via an API or command-line interface. While suitable for massive datasets, S3 may have certain limitations compared to EBS, such as latency.
- **SSD (Solid State Drive)** - A type of fast, reliable storage hardware generally more expensive than traditional hard drives.
- **HDD (Hard Disk Drive)** - Traditional, spinning-disk storage, offering large capacity at lower cost, but with slower performance compared to SSDs.
- **Ephemeral Storage (Instance Store Storage)** - Temporary, local storage for EC2 instances that is wiped once the instance is stopped or terminated. Instance stores may use either SSD or HDD hardware.

---

## Regions

An **AWS Region** is a physical location worldwide, consisting of multiple Availability Zones (AZs). Each region operates independently to reduce latency and increase redundancy.

**Current AWS Regions and their identifiers:**

- **US East**
  - North Virginia - `us-east-1`
  - Ohio - `us-east-2`
- **US West**
  - Northern California - `us-west-1`
  - Oregon - `us-west-2`
- **Canada**
  - Central - `ca-central-1`
- **Europe**
  - Frankfurt - `eu-central-1`
  - Ireland - `eu-west-1`
  - London - `eu-west-2`
  - Paris - `eu-west-3`
- **Asia Pacific**
  - Tokyo - `ap-northeast-1`
  - Seoul - `ap-northeast-2`
  - Osaka-Local - `ap-northeast-3`
  - Singapore - `ap-southeast-1`
  - Sydney - `ap-southeast-2`
  - Mumbai - `ap-south-1`
- **South America**
  - São Paulo - `sa-east-1`

---

## Availability Zones (AZ)

**Availability Zones (AZs)** are distinct data centers within a region, each with independent power, networking, and connectivity to ensure high availability and fault tolerance. Distributing applications across multiple AZs provides redundancy and minimizes latency.

**Regions with Multiple Availability Zones:**

- **US East**
  - Ohio (3)
  - North Virginia (6)
- **US West**
  - Oregon (3)
  - Northern California (3)
- **Canada**
  - Central (3)
- **South America**
  - São Paulo (3)
- **Europe**
  - Ireland (3)
  - Frankfurt (3)
  - London (3)
  - Paris (3)
- **Asia Pacific**
  - Singapore (3)
  - Seoul (2)
  - Tokyo (4)
  - Mumbai (2)
  - Sydney (3)
  - Beijing (2)
  - Ningxia (2)

Deploying across multiple AZs within a region is crucial for fault tolerance and performance, as this setup reduces the risk of downtime due to individual data center failures.