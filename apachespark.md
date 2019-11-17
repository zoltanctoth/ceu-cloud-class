---
layout: default
---
[Home](./README.md).
[Internet](./internet.md).
[Cloud Computing](./cloud_computing.md).
[Serverless](./serverless.md).
[AWS](./aws.md).

### Apache Spark Overview

## Big Data 101
>The IDC estimated the size of the “digital universe” at 4.4 Zettabytes (1 Trillion Gigabytes) in 2013. It grows by 40% every year, and by 2020 the IDC expects it to be as large as 44 Zettabytes, amounting to a single bit of data for every star in the physical universe. We have a lot of data, and we aren’t getting rid of any of it. We need a way to store increasing amounts of data at scale, with protections against data-loss stemming from hardware failure. 

Even if Excel could store that much data, not many desktop computers have enough hard drive space for that anyway. 

<img src="https://i.stack.imgur.com/K2Glj.png" width="300">

<p align="center"> Thank the cosmos we have Spark! </p>

#### To understand Spark, first familiarize yourself with these terms:
|     Glossary        |        Definition                                                                                                                                                                |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Cluster**             | A group of computers pooling the resources of many machines together, giving us the ability to use all the cumulative resources as if they were a single computer      |
| **Language APIs**        | Make it possible to run code using programming languages (Scala, Python, Java, R, SQL)                                                                                                             |
| **Computing Engine**     | Loads data from storage systems and performs computation on it, not being a permanent storage as the end itself                                                        |
| **Unified**              | Supports a wide range of data analytics tasks over the same computing engine                                                                                           |
| **Libraries**            | Spark includes libraries for SQL, and structured data SparkSQL, machine learning \(MLlib\), stream processing \(Structured Streaming\), and graph analytics \(GraphX\) |
| **Parallel Processing**  | Large problems divided into smaller ones, which can then be solved at the same time                                                                                    |

## ...Now, What's Spark?
>Apache Spark is a **unified** **computing engine** and a set of libraries for **parallel data processing** on computer **clusters** that supports programming languages like R, Python, Java and Scala and **libraries** ranging from SQL to streaming and machine learning and runs everywhere from a laptop to a cluster of thousands of servers making it easy to scale up to big data processing or incredibly large scale

<div style="text-align:center"><span>
<img src="https://ogirardot.files.wordpress.com/2015/05/future-of-spark.png" width="900"></span></div>
 
 - Spark Core: This is the heart of Spark, and is responsible for management functions such as task scheduling. Spark Core implements and depends upon a programming abstraction known as Resilient Distributed Datasets (RDDs), which is outside the scope of this class.
 
 - Spark SQL: This is Spark’s module for working with structured data, and it is designed to support workloads that combine familiar SQL database queries with more complicated, algorithm-based analytics. Spark SQL supports the open source Hive project, and its SQL-like HiveQL query syntax. Spark SQL also supports JDBC and ODBC connections, enabling a degree of integration with existing databases, data warehouses and business intelligence tools. JDBC connectors can also be used to integrate with Apache Drill, opening up access to an even broader range of data sources.
 
 - Spark Streaming: This module supports scalable and fault-tolerant processing of streaming data, and can integrate with established sources of data streams like Flume (optimized for data logs) and Kafka (optimized for distributed messaging). Spark Streaming’s design, and its use of Spark’s RDD abstraction, are meant to ensure that applications written for streaming data can be repurposed to analyze batches of historical data with little modification.
 
 - MLlib: This is Spark’s scalable machine learning library, which implements a set of commonly used machine learning and statistical algorithms. These include correlations and hypothesis testing, classification and regression, clustering, and principal component analysis.
 
 - Spark R: This module was added to the 1.4.x release of Apache Spark, providing data scientists and statisticians using R with a lightweight mechanism for calling upon Spark’s capabilities.
 
 - GraphX: This module began life as a separate UC Berkeley research project, which was eventually donated to the Apache Spark project. GraphX supports analysis of and computation over graphs of data, and supports a version of graph processing’s Pregel API. GraphX includes a number of widely understood graph algorithms, including PageRank.
 
 #### API Overview
The Spark API was optimized for manipulating data, with a design that reduced common data science tasks from hundreds or thousands of lines of code to only a few. For those familiar with a DataFrames API in other languages like R or pandas in Python, this API will make them feel right at home.
 
DataFrame API:
- Ability to scale from kilobytes of data on a single laptop to petabytes on a large cluster
- Support for a wide array of data formats and storage systems
- State-of-the-art optimization and code generation through the Spark SQL

Language APIs: 
- Python
- Java
- Scala
- R
- SQL

#### Data Pipelines
Spark’s power lies in its ability to combine very different techniques and processes together into a single, coherent, whole. Spark crosses boundaries between batch, streaming and interactive workflows in ways that make the user more productive.
Spark jobs perform multiple operations consecutively, in memory and only spilling to disk when required by memory limitations. In use cases such as ETL, these pipelines can become extremely rich and complex, combining large numbers of inputs and a wide range of processing steps into a unified whole that consistently delivers the desired result.
 
 
 
 - **Unified:** Spark is designed to support a wide range of data analytics tasks over the same computing engine and with a consistent set of APIs. 
-> Real world data analytics tasks tend to combine many different processing types and libraries. 

- **Consistent Composable APIs:** you can use to build an application out of smaller pieces or out of existing libraries. It also makes it easy for you to write your own analytics libraries on top. Spark's APIs are also designed to enable high performance by optimizing across the different libraries and functions composed together in a user program.
#Example_1: if you load data using SQL query and then evaluate a machine learning model over it using Spark's ML library, the engine can combine these steps into a one scan over the data. Thus, the combination of general APIs and high-performance execution, no matter how you combine them, makes Spark a powerful platform for interactive, and production applications.
#Example_2: Web developers benefit from unified frameworks such as Node.js or Django

- **Computing Engine:**  Spark handles loading data from storage systems and performing computation on it, not being a permanent storage as the end itself. You can use Spark with a wide variety of storage systems such as Azure Storage and Amazon S3, distributed file systems such as Apache Hadoop, key-value stores such as Apache Cassandra and message buses such as Apache Kafka. However, Spark does not store data long-term itself.

- **Libraries:** builds on Spark's design as a unified engine to provide a unified API for common data analysis tasks. Spark supports standard libraries and external libraries. Spark includes libraries for SQL, and structured data SparkSQL, machine learning (MLlib), stream processing (Spark Streaming and the newer Structured Streaming), and graph analytics (GraphX). Beyond these libraries there are a hundreds of open source external libraries. (spark-packages.org)

- **Parallel Processing:** processing of program instructions by dividing them among multiple processors with the objective of running a program in less time. 

### Launching Spark's Interactive Console

Spark runs on the **JVM (Java Virtual Machine)** so you need to install Java to run it. If you want to use the Python API, you will also need a Python interpreter. If you want to use R, you will need a version of R on your machine.

| Python   |      Scala      |  SQL |
|----------|:-------------:|------:|
| ./bin/pyspark | ./bin/spark-shell | ./bin/spark-sql |
| after you have done that type "spark" and press Enter. You will see the "SparkSession" object printed  |    after you have done that type "spark" and press Enter. You will see the "SparkSession" object printed    |   after you have done that type "spark" and press Enter. You will see the "SparkSession" object printed  |

-  **SparkSession:** You can control your Spark Application through a driver process called the SparkSession. The SparkSession is the way Spark executes user-defined manipulations across the cluster. There is a one-to-one correspondance between a SparkSession and a SparkApplication.

- **Spark's Basic Architecture**
*Problem:* one computer works well for watching movies or working with spreadsheet software. However, there are things a computer is not powerful enough to perform - e.g data processing. Single machines do not have the power and resources to perform computations on huge amounts of information or the user does not have time to wait for the computation to finish. 
*Solution:*
A cluster or group, of computers, pools the resources of many machines together, giving us the ability to use all the cumulative resources as if they were a single computer. A group of machines alone is not powerful, you need a framework to coordinate work across them - Spark does just that! - Coordinating and managing the execution of tasks on data across a cluster of computers.

**The cluster** of machines that Spark uses to execute tasks is managed by a cluster manager. 
YARN or Mesos or Spark's standalone cluster manager. We then submit Spark Applications to these cluster managers

**Spark Application** (Architecture of a Spark Application)
Spark applications consist of a **driver process** and a set of **executor processes.**

- **Driver Process** (heart of a Spark Application, maintains all relevant information during the lifetime of the application.
  - Runs of your main() function, sits on a node in the cluster, and is responsible for:
    - Maintaining information about the Spark Application
    - Responding to a user's program or input 
    - Analyzing, distributing and scheduling work across the executors
- **Executor Processes**
  - Responsible for actually carrying out the work that the (<-) driver assigns them. Each executor is responsible for:
    - Executing code assigned to it by the driver 
    - Reporting the state of the computation on that executor BACK to the driver node.
    
Driver is on the left, four executors on the right.  It demonstrates how the cluster manager controls physical machines and allocates resources to Spark Applications. This can be one of three cluster managers ( YARN, Mesos, Spark's standalone cluster manager). This means that there can be multiple Spark Applications running on a cluster at the same time.

Note: Spark, in addition to a cluster mode, also has a local mode. The driver and the executor are simply processes, this means they can live on the same machine or different machines. 
**Local Mode** - Driver and executor run as threads on your individual computer in stead of a cluster.
