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

## Spark Overview

### Apache Spark
- Collecting data is extremely inexpensive but processing it requires large, parallel computations, often on clusters of machines
    - That's what Apache Spark was built for

> Apache Spark is a unified computing engine and a set of libraries for parallel data processing on computer clusters that supports programming languages like R, Python, Java and Scala and libraries ranging from SQL to streaming and machine learning and runs everywhere from a laptop to a cluster of thousands of servers making it easy to scale up to big data processing or incredibly large scale.

  - **Unified:** Spark is designed to support a wide range of data analytics tasks over the same computing engine and with a consistent set of APIs as real world data analytics tasks tend to combine many different processing types and libraries
  
  - **Consistent Composable APIs:** you can use them to build an application out of smaller pieces or out of existing libraries. It also makes it easy for you to write your own analytics libraries on top. Spark's APIs are also designed to enable high performance by optimizing across the different libraries and functions composed together in a user program.
#Example_1: if you load data using SQL query and then evaluate a machine learning model over it using Spark's ML library, the engine can combine these steps into a one scan over the data. Thus, the combination of general APIs and high-performance execution, no matter how you combine them, makes Spark a powerful platform for interactive, and production applications.
#Example_2: Web developers benefit from unified frameworks such as Node.js or Django

  - **Computing Engine:**  Spark handles loading data from storage systems and performing computation on it, not being a permanent storage as the end itself. You can use Spark with a wide variety of storage systems such as Azure Storage and Amazon S3, distributed file systems such as Apache Hadoop, key-value stores such as Apache Cassandra and message buses such as Apache Kafka. However, Spark does not store data long-term itself.

  - **Libraries:** builds on Spark's design as a unified engine to provide a unified API for common data analysis tasks. Spark supports standard libraries and external libraries. Spark includes libraries for SQL, and structured data SparkSQL, machine learning (MLlib), stream processing (Spark Streaming and the newer Structured Streaming), and graph analytics (GraphX). Beyond these libraries there are a hundreds of open source external libraries. (spark-packages.org)

  - **Parallel Processing:** processing of program instructions by dividing them among multiple processors with the objective of running a program in less time. 

### Launching Spark

- Spark runs on both Windows and UNIX-like systems (e.g. Linux, Mac OS). All you need is to have java installed on your system PATH, or the JAVA_HOME environment variable pointing to a Java installation. If you want to use the Python API, you will need a Python interpreter. If you want to use R, you will need a version of R on your machine. 

**Launching Spark:**
Open the Terminal: 
**Python:** ```./bin/pyspark``` 
**Scala:** ```./bin/spark-shell```
**SQL:** ```./bin/spark-sql```

*After you have done that type "spark" and press Enter. You will see the "SparkSession" object printed*

**The SparkSession:** You can control your Spark Application through a driver process called the SparkSession. The SparkSession is the way Spark executes user-defined manipulations across the cluster. There is a one-to-one correspondance between a SparkSession and a SparkApplication.

  > One computer works well for watching movies or working with spreadsheet software. However, there are things a computer is not powerful enough to perform - e.g data processing. Single machines do not have the power and resources to perform computations on huge amounts of information or the user does not have time to wait for the computation to finish. 
  
**Cluster:** A cluster or group, of computers, pools the resources of many machines together, giving us the ability to use all the cumulative resources as if they were a single computer. A group of machines alone is not powerful, you need a framework to coordinate work across them - Spark does just that! - Coordinating and managing the execution of tasks on data across a cluster of computers. The cluster of machines that Spark uses to execute tasks is managed by a cluster manager. 
*YARN or Mesos or Spark's standalone cluster manager. We then submit Spark Applications to these cluster managers*

**Spark Application** (Architecture of a Spark Application)
- Spark applications consist of a **drives process** and a set of **executor processes**.


| Driver Process    | Executor Processes   |
| :------------- | :----------: | 
| Heart of a Spark Application, maintains all relevant information during the lifetime of the application. Runs on your main() function, sits on a node in the cluster, and is responsible for: - Maintaining information about the Spark Application - Responding to a user's program or input analyzing, distributing and scheduling work across the executors | Responsible for actually carrying out the work that the (<-) driver assigns them. Each executor is responsible for: - Executing code assigned to it by the driver - Reporting the state of the computation on that executor back to the driver node.| 

![driver_executor](Images/SparkOverview/driver_executor_spark.png =100x20)

- Driver is on the left, four executors on the right. It demonstrates how the cluster manager controls physical machines and allocates resources to Spark Applications. This can be one of three cluster managers ( YARN, Mesos, Spark's standalone cluster manager). This means that there can be multiple Spark Applications running on a cluster at the same time.

> Note: Spark, in addition to a cluster mode, also has a local mode. The driver and the executor are simply processes, this means they can live on the same machine or different machines. 
Local Mode - Driver and executor run as threads on your individual computer in stead of a cluster.




