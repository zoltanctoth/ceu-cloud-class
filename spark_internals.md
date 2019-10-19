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

## Spark Internals

**The SparkSession:** You can control your Spark Application through a driver process called the SparkSession. The SparkSession is the way Spark executes user-defined manipulations across the cluster. There is a one-to-one correspondance between a SparkSession and a SparkApplication.

**Spark Application** (Architecture of a Spark Application)
- Spark applications consist of a **drives process** and a set of **executor processes**.


| Driver Process    | Executor Processes   |
| :------------- | :----------: | 
| Heart of a Spark Application, maintains all relevant information during the lifetime of the application. Runs on your main() function, sits on a node in the cluster, and is responsible for: - Maintaining information about the Spark Application - Responding to a user's program or input analyzing, distributing and scheduling work across the executors | Responsible for actually carrying out the work that the (<-) driver assigns them. Each executor is responsible for: - Executing code assigned to it by the driver - Reporting the state of the computation on that executor back to the driver node.| 

![driver_executor](Images/SparkOverview/driver_executor_spark.png)

- Driver is on the left, four executors on the right. It demonstrates how the cluster manager controls physical machines and allocates resources to Spark Applications. This can be one of three cluster managers ( YARN, Mesos, Spark's standalone cluster manager). This means that there can be multiple Spark Applications running on a cluster at the same time.

> Note: Spark, in addition to a cluster mode, also has a local mode. The driver and the executor are simply processes, this means they can live on the same machine or different machines. Local Mode - Driver and executor run as threads on your individual computer in stead of a cluster.

- Spark employs a cluster manager that keeps track of the resources available
- The driver process is responsible for executing the driver program's commands across the executor to complete a given task
- The executor only runs Spark code. However, the driver can be driven from a number of different languages through Spark's Language APIs

**Spark's Language APIs:** make it possible to run Spark code using programming languages. Spark presents 'core concepts' in every language; these concepts are then translated into Spark code that runs on the cluster of machines. 
