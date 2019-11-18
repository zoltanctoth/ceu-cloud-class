---
layout: default
---
[Home](./README.md).
[Internet](./internet.md).
[Cloud Computing](./cloud_computing.md).
[Serverless](./serverless.md).
[AWS](./aws.md).

### Apache Spark Overview

#### Big Data 101
>The IDC estimated the size of the “digital universe” at 4.4 Zettabytes (1 Trillion Gigabytes) in 2013. It grows by 40% every year, and by 2020 the IDC expects it to be as large as 44 Zettabytes, amounting to a single bit of data for every star in the physical universe.

- We have a lot of data, and we aren’t getting rid of any of it. We need a way to store increasing amounts of data at scale
- Even if Excel could store that much data, not many desktop computers have enough hard drive space for that anyway.
- One computer works well for watching movies or working with spreadsheet software. However, there are things a computer is not powerful enough to perform - e.g data processing. Single machines do not have the power and resources to perform computations on huge amounts of information or the user does not have time to wait for the computation to finish

<p align="center"> 
<img src="https://i.stack.imgur.com/K2Glj.png" width="300">
</p>

- A cluster or group, of computers, pools the resources of many machines together, giving us the ability to use all the cumulative resources as if they were a single computer. 
- A group of machines alone is not powerful, you need a framework to coordinate work across them
- Spark does just that! - Coordinating and managing the execution of tasks on data across a cluster of computers.

<p align="center"> Thank the cosmos we have Spark! </p>

### Glossary 
#### To understand Spark, first familiarize yourself with these terms:
|     Glossary        |        Definition                                                                                                                                                                |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Cluster**             | A group of computers pooling the resources of many machines together, giving us the ability to use all the cumulative resources as if they were a single computer. YARN or Mesos or Spark's standalone cluster manager. We then submit Spark Applications to these cluster managers      |
| **Language APIs**        | Make it possible to run code using programming languages (Scala, Python, Java, R, SQL)                                                                                                             |
| **Computing Engine**     | Spark handles loading data from storage systems and performing computation on it, not being a permanent storage as the end itself. You can use Spark with a wide variety of storage systems such as Azure Storage and Amazon S3, distributed file systems such as Apache Hadoop, key-value stores such as Apache Cassandra and message buses such as Apache Kafka. However, Spark does not store data long-term itself.                                                        |
| **Unified**              | Spark is designed to support a wide range of data analytics tasks over the same computing engine and with a consistent set of APIs. Real world data analytics tasks tend to combine many different processing types and libraries.                                                                                            |
| **Libraries**            | Spark supports standard libraries and external libraries. Spark includes libraries for SQL, and structured data SparkSQL, machine learning (MLlib), stream processing (Spark Streaming and the newer Structured Streaming), and graph analytics (GraphX). Beyond these libraries there are a hundreds of open source external libraries. (spark-packages.org) |
| **Parallel Processing**  | Large problems divided into smaller ones, which can then be solved at the same time                                                                                    |

## ...Now, What's Spark?
>Apache Spark is a **unified** **computing engine** and a set of libraries for **parallel data processing** on computer **clusters** that supports programming languages like R, Python, Java and Scala and **libraries** ranging from SQL to streaming and machine learning and runs everywhere from a laptop to a cluster of thousands of servers making it easy to scale up to big data processing or incredibly large scale

<div style="text-align:center"><span>
<img src="https://ogirardot.files.wordpress.com/2015/05/future-of-spark.png" width="900"></span></div>
 
 - **Spark Core:** This is the heart of Spark, and is responsible for management functions such as task scheduling. Spark Core implements and depends upon a programming abstraction known as Resilient Distributed Datasets (RDDs), which is outside the scope of this class.
 
 - **Spark SQL:** This is Spark’s module for working with structured data, and it is designed to support workloads that combine familiar SQL database queries with more complicated, algorithm-based analytics. Spark SQL supports the open source Hive project, and its SQL-like HiveQL query syntax. Spark SQL also supports JDBC and ODBC connections, enabling a degree of integration with existing databases, data warehouses and business intelligence tools. JDBC connectors can also be used to integrate with Apache Drill, opening up access to an even broader range of data sources.
 
 - **Spark Streaming:** This module supports scalable and fault-tolerant processing of streaming data, and can integrate with established sources of data streams like Flume (optimized for data logs) and Kafka (optimized for distributed messaging). Spark Streaming’s design, and its use of Spark’s RDD abstraction, are meant to ensure that applications written for streaming data can be repurposed to analyze batches of historical data with little modification.
 
 - **MLlib:** This is Spark’s scalable machine learning library, which implements a set of commonly used machine learning and statistical algorithms. These include correlations and hypothesis testing, classification and regression, clustering, and principal component analysis.
 
 - **GraphX:** This module began life as a separate UC Berkeley research project, which was eventually donated to the Apache Spark project. GraphX supports analysis of and computation over graphs of data, and supports a version of graph processing’s Pregel API. GraphX includes a number of widely understood graph algorithms, including PageRank.

 
 ### Use cases
 |     Use cases                |                                                                                                                                                                |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Stream processing**            | This data arrives in a steady stream from multiple sources simultaneously. Streams of data related to financial transactions can be processed in real time to identify – and refuse – potentially fraudulent transactions.      |
| **Machine learning**        | Spark’s ability to store data in memory and rapidly run repeated queries makes it a good choice for training machine learning algorithms.                                                                                                           |
| **Interactive analytics**     | Business analysts and data scientists want to explore their data by asking a question and viewing the results. This interactive query process requires systems such as Spark that are able to respond and adapt quickly.                                                |
| **Data integration**              | Data produced by different systems across a business is rarely clean or consistent enough to simply and easily be combined for reporting or analysis. Spark is used to reduce the cost and time required for this ETL process.       | 


### Launching Spark's Interactive Console
You can grab Spark from here, altough we will use Databricks in this course: https://spark.apache.org/downloads.html

Spark runs on the **JVM (Java Virtual Machine)** so you need to install Java to run it. If you want to use the Python API, you will also need a Python interpreter. If you want to use R, you will need a version of R on your machine.

| Python   |      Scala      |  SQL |
|----------|:-------------:|------:|
| ./bin/pyspark | ./bin/spark-shell | ./bin/spark-sql |
| after you have done that type "spark" and press Enter. You will see the "SparkSession" object printed  |    after you have done that type "spark" and press Enter. You will see the "SparkSession" object printed    |   after you have done that type "spark" and press Enter. You will see the "SparkSession" object printed  |

-  **SparkSession:** You can control your Spark Application through a driver process called the SparkSession. The SparkSession is the way Spark executes user-defined manipulations across the cluster. There is a one-to-one correspondance between a SparkSession and a SparkApplication.

- **Spark Application:** Spark applications consist of a **driver process** and a set of **executor processes.**

<p align="center"> 
<img src="https://izhangzhihao.github.io/assets/images/spark-01.png" width="400"></p>

Driver is on the left, four executors on the right.  It demonstrates how the cluster manager controls physical machines and allocates resources to Spark Applications. This can be one of three cluster managers ( YARN, Mesos, Spark's standalone cluster manager). This means that there can be multiple Spark Applications running on a cluster at the same time.

*Note: Spark, in addition to a cluster mode, also has a local mode. The driver and the executor are simply processes, this means they can live on the same machine or different machines. 
**Local Mode** - Driver and executor run as threads on your individual computer in stead of a cluster.*

| Driver Process   |      Executor Process      | 
|----------|:-------------:|
| The heart of a Spark Application, maintains all relevant information during the lifetime of the application. Runs of your main() function, sits on a node in the cluster, and is responsible for: Maintaining information about the Spark Application. Responding to a user's program or input. Analyzing, distributing and scheduling work across the executors | Responsible for actually carrying out the work that the (<-) driver assigns them. Each executor is responsible for: Executing code assigned to it by the driver. Reporting the state of the computation on that executor BACK to the driver node. |
    
 
 #### API Overview
Structured APIs are a tool for manipulating all sorts of data, from unstructured log files to semi-structured CSV files and highly structured Parquet (Apache Parquet is a columnar storage format available to any project in the Hadoop ecosystem, regardless of the choice of data processing framework, data model or programming language) files. These APIs refer to three core types of distributed collection APIs:

- **Datasets**
- **DataFrames**
- **SQL Tables and Views**

Majority of the Structured APIs apply to both batch and streaming computation. This means that when you work with the Structured APIs, it should be simple to migrate from batch to streaming or vice versa with little to no effort.  Structured APIs are the fundamental abstraction used to write the majority of data flows. 
 
For those familiar with the DataFrames API in other languages like R or pandas in Python, this API will make them feel right at home. In this course, we are going to focus on the **DataFrame** API and skip Datasets & RDDs - but to explain DataFrames - we need to understand RDDs a little.

>A Dataframe is a distributed collection of rows under named columns. In simple terms, it looks like an Excel sheet with Column headers, or you can think of it as the equivalent to a table in a relational database or a DataFrame in R or Python.

<img src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/06/1-2.png">

*Note: A DataFrame is an abstraction on top of RDDs. An RDD is broken down into partitions and a DataFrame is an abstraction on top of RDDs hence DataFrame is also partitioned. DataFrames ultimately compile down to RDDs.*

DataFrames (and Datasets) are **distributed table-like collection with well-defined rows and columns**. Each column must have the same number of rows as all the other columns although you can use null to specify the absence of a value and each column has type information that must be consistent for every row in the collection. To Spark, DataFrames (and Datasets) represent **immutable, lazily evaluated plans(transformations)** that specify what operations to apply to data residing at a location to generate some output. When we perform an action on a DataFrame, we instruct Spark to perform the actual transformations and return the results. These represent plans of how to manipulate rows and columns to compute the user's desired result. 

#### Data Pipelines
Spark’s power lies in its ability to combine very different techniques and processes together into a single, coherent, whole. Spark crosses boundaries between batch, streaming and interactive workflows in ways that make the user more productive.
Spark jobs perform multiple operations consecutively, in memory and only spilling to disk when required by memory limitations. In use cases such as ETL, these pipelines can become extremely rich and complex, combining large numbers of inputs and a wide range of processing steps into a unified whole that consistently delivers the desired result.
