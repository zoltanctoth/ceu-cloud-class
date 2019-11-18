---
layout: default
---
[Home](./README.md).
[Internet](./internet.md).
[Cloud Computing](./cloud_computing.md).
[Serverless](./serverless.md).
[AWS](./aws.md).

**Disclaimer:** Reading List - Matei Zaharia et al.: Spark, the Definitive Guide [book] (http://shop.oreilly.com/product/0636920034957.do) <- if you don't understand this summary, this book will be of help.

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

**optional (Windows)**
>Install Java 8.

>Configure your environment variables, JAVA_HOME and PATH to point to the path of jdk.

>To test java installation is complete, open command prompt type java -version and hit enter.

>Download and install Maven dependency manager

>Download and install Intellij IDEA which is an IDE.

>Download and install Python or Anaconda (in case you want to test Jupyter)

>Set an environment variable for your Python path PYTHONPATH=

>Download and install PyCharm

>Download winutils.exe and place it in a bin directory under a created Hadoop home directory. Set HADOOP_HOME = <> in environment variable.

>Download and extract this pre-built Spark package apache-spark-2.3.2

>Set SPARK_HOME and add SPARK_HOME\bin in PATH variable in environment variables.

>Run command: spark-shell

Spark runs on the **JVM (Java Virtual Machine)** so you need to install Java to run it. If you want to use the Python API, you will also need a Python interpreter. If you want to use R, you will need a version of R on your machine.

| Python   |      Scala      |  SQL |
|----------|:-------------:|------:|
| ./bin/pyspark | ./bin/spark-shell | ./bin/spark-sql |
| after you have done that type "spark" and press Enter. You will see the "SparkSession" object printed  |    after you have done that type "spark" and press Enter. You will see the "SparkSession" object printed    |   after you have done that type "spark" and press Enter. You will see the "SparkSession" object printed  |

-  **SparkSession:** You can control your Spark Application through a driver process called the SparkSession. The SparkSession is the way Spark executes user-defined manipulations across the cluster. There is a one-to-one correspondance between a SparkSession and a SparkApplication. SparkSession and Language APIs relationship: 

<p align="center"> 
<img src="https://www.oreilly.com/library/view/spark-the-definitive/9781491912201/assets/spdg_0202.png" width="400"></p>

- **Spark Application Architecture:** Spark applications consist of a **driver process** and a set of **executor processes.**

<p align="center"> 
<img src="https://izhangzhihao.github.io/assets/images/spark-01.png" width="400"></p>

Driver is on the left, four executors on the right.  It demonstrates how the cluster manager controls physical machines and allocates resources to Spark Applications. This can be one of three cluster managers ( YARN, Mesos, Spark's standalone cluster manager). This means that there can be multiple Spark Applications running on a cluster at the same time.

*Note: Spark, in addition to a cluster mode, also has a local mode. The driver and the executor are simply processes, this means they can live on the same machine or different machines. 
**Local Mode** - Driver and executor run as threads on your individual computer in stead of a cluster.*

| Driver Process   |      Executor Process      | 
|----------|:-------------:|
| The heart of a Spark Application, maintains all relevant information during the lifetime of the application. Runs of your main() function, sits on a node in the cluster, and is responsible for: Maintaining information about the Spark Application. Responding to a user's program or input. Analyzing, distributing and scheduling work across the executors | Responsible for actually carrying out the work that the (<-) driver assigns them. Each executor is responsible for: Executing code assigned to it by the driver. Reporting the state of the computation on that executor BACK to the driver node. |

**Key Takeaways:**
- Spark employs a cluster manager that keeps track of the resources available
- The driver process is responsible for executing the driver program's commands across the executor to complete a given task

The executor only runs Spark code. However, the driver can be driven from a number of different languages through Spark's Language APIs. (Scala, Java, Python, R)


 
 #### API Overview
Structured APIs are a tool for manipulating all sorts of data, from unstructured log files to semi-structured CSV files and highly structured Parquet (Apache Parquet is a columnar storage format available to any project in the Hadoop ecosystem, regardless of the choice of data processing framework, data model or programming language) files. These APIs refer to three core types of distributed collection APIs:

- **Datasets**
- **DataFrames**
- **SQL Tables and Views**


Majority of the Structured APIs apply to both batch and streaming computation. This means that when you work with the Structured APIs, it should be simple to migrate from batch to streaming or vice versa with little to no effort.  Structured APIs are the fundamental abstraction used to write the majority of data flows. 

### DataFrames
For those familiar with the DataFrames API in other languages like R or pandas in Python, this API will make them feel right at home. In this course, we are going to focus on the **DataFrame** API and skip Datasets & RDDs - but to explain DataFrames - we need to understand RDDs a little.

>A Dataframe is a distributed collection of rows under named columns. In simple terms, it looks like an Excel sheet with Column headers, or you can think of it as the equivalent to a table in a relational database or a DataFrame in R or Python.

<img src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/06/1-2.png">

*Note: A DataFrame is an abstraction on top of RDDs. An RDD is broken down into partitions and a DataFrame is an abstraction on top of RDDs hence DataFrame is also partitioned. DataFrames ultimately compile down to RDDs.*

DataFrames (and Datasets) are **distributed table-like collection with well-defined rows and columns**. Each column must have the same number of rows as all the other columns although you can use null to specify the absence of a value and each column has type information that must be consistent for every row in the collection. To Spark, DataFrames (and Datasets) represent **immutable, lazily evaluated plans(transformations)** that specify what operations to apply to data residing at a location to generate some output. When we perform an action on a DataFrame, we instruct Spark to perform the actual transformations and return the results. These represent plans of how to manipulate rows and columns to compute the user's desired result. 

- To allow every executor to perform work in parallel, Spark breaks up the data into chunks called partitions.
- A partition is a collection of rows that sit on one physical machine in your cluster
- A DataFrame’s partitions represent how the data is physically distributed across the cluster of machines during execution
- If you have one partition, Spark will have a parallelism of only one, even if you have thousands of executors
- If you have many partitions but only one executor, Spark will still have a parallelism of only one because there is only one computation resource.


**Transformations:**
- Transformations are the core of how you express your business logic using Spark. There are two types of transformations:
  - those that specify narrow dependencies, which are those for which each input partition will contribute to only one output partition
  - and those that specify wide dependencies (shuffles), where we have input partitions contributing to many output partitions
- Narrow transformations can be performed in-memory, whereas for shuffles, Spark writes the results to disk
- Spark will not act on transformations until we call an action, that's why we say that they are lazily evaluated
- Lazy evaluation means that Spark will wait until the very last moment to execute the graph of computation instructions

**Actions:**
- Transformations allow us to build up a logical transformation plan.
- To trigger the computation, we run an action. An action instructs Spark to compute a result from a series of transformations
  - There are three kinds of actions:

     - Actions to view data in the console
     - Actions to collect data to native objects in the respective language
     - Actions to write to output data sources
     
<p align="center"> 
<img src="https://4.bp.blogspot.com/-RDjf_UrR1Zo/W_5WzQIWuHI/AAAAAAAABGY/RbV9OnTBVhcO471mKcEwJqGMihCnHgR5ACLcBGAs/s1600/2.jpg" width="1000"></p>

### Overview of Structured API Execution
How is the code actually executed across a cluster? Here’s an overview of the steps:
- Write DataFrame/Dataset/SQL Code
- If valid code, Spark converts this to a Logical Plan
- Spark transforms this Logical Plan to a Physical Plan, checking for optimizations along the way
- Spark then executes this Physical Plan on the cluster

<p align="center"> 
<img src="https://i.stack.imgur.com/Y9oU5.png" width="600"></p>

<p align="center"> 
<img src="https://www.oreilly.com/library/view/spark-the-definitive/9781491912201/assets/spdg_0402.png" width="600"></p>

<p align="center"> 
<img src="https://www.oreilly.com/library/view/spark-the-definitive/9781491912201/assets/spdg_0403.png" width="600"></p>

### DataFrame Operations
a DataFrame consists of:
- A series of records (like rows in a table), that are of type Row
- A number of columns (like columns in a spreadsheet) that represent a computation expression that can be performed on each individual record in the Dataset

- **Schemas** define the name as well as the type of data in each column
  - A schema defines the column names and types of a DataFrame
  - We can either let a data source define the schema or we can define it explicitly ourselves
  - To check the schema: `df.printSchema()`
<p align="center"> 
<img src="https://www.edureka.co/blog/content/ver.1554792280/uploads/2019/04/schema-of-character-deaths-DataFrames-in-spark-Edureka.png" width="400"></p>
- A schema is a StructType made up of a number of fields, StructFields, that have a name, type, a Boolean flag which specifies whether that column can contain missing or null values, and, finally, users can optionally specify associated metadata with that column.

- **Partitioning** of the DataFrame defines the layout of the DataFrame or Dataset’s physical distribution across the cluster.
  - The partitioning scheme defines how that is allocated. You can set this to be based on values in a certain column or nondeterministically

#### Columns and Expressions
- Columns in Spark are similar to columns in a spreadsheet, R dataframe, or pandas DataFrame. You can select, manipulate, and remove columns from DataFrames and these operations are represented as expressions
- To construct columns we can use the `withColumn` function
```python
df.withColumn('newage',df['age']).show()
df.withColumn('half_age',df['age']/2).show()
```
#### Records and Rows
- In Spark, each row in a DataFrame is a single record. Spark represents this record as an object of type Row
- Spark manipulates Row objects using column expressions in order to produce usable values
- Row objects internally represent arrays of bytes
We can see a row by calling `first` or `head(1)` in a DataFrame

```python
df.first()
df.head(1)
```
#### DataFrame Transformations
- `select` allows you to do the DataFrame equivalent of SQL queries on a table of data:

```python
df.select("age").show(2)
```
- We can register the DataFrame as a SQL temporary view (It's thde equivalent of `SELECT AGE FROM PEOPLE LIMIT 2`)
```python
df.createOrReplaceTempView("people")
```

**Filtering Rows**
Example:
```python
df.filter( (df["Close"] < 200) | (df['Open'] > 200) ).show()
```

**Sorting Rows**
For sorting we can use `sort` and `orderBy` which function similarly:
```python
df.sort("Sales").show()
df.orderBy("Sales").show()
```

**Grouping**
```python
df.groupBy("Company")
df.groupBy("Company").count().show()
df.groupBy("Company").mean().show()
df.groupBy("Company").min().show()
```

#### DataFrame Aggregations
- Aggregating is the act of collecting something together and is a cornerstone of big data analytics. In an aggregation, you will specify a key or grouping and an aggregation function that specifies how you should transform one or more columns
- This function must produce one result for each group, given multiple input values. 

All aggregations are available as functions, most aggregation functions can be found here:
http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.functions$

- `count` function allows us to specify a specific column to count
```python
df.select(count("Sales")).show()
```

- `countdistinct` function gives us the number of unique groups
```python
from pyspark.sql.functions import countDistinct
df.select(countDistinct("Sales")).show()
```

#### Methods
http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.functions$
http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.DataFrameStatFunctions
http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Column
http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Dataset


### Joings
- Joins are an essential part of nearly all Spark workloads. Spark’s ability to talk to different data means that you gain the ability to tap into a variety of data sources across your company
- Whereas the join expression determines whether two rows should join, the join type determines what should be in the result set. There are a variety of different join types available in Spark for you to use such as (list not-exhaustive):

- Inner joins (keep rows with keys that exist in the left and right datasets)
- Outer joins (keep rows with keys in either the left or right datasets)
- Left outer joins (keep rows with keys in the left dataset)
- Right outer joins (keep rows with keys in the right dataset)


## Example
https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt

**A simple program that performs a word count on the collected works of Shakespeare**
```python
from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName('MyFirstStandaloneApp')
sc = SparkContext(conf=conf)
text_file = sc.textFile("./shakespeare.txt")
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
print ("Number of elements: " + str(counts.count()))
counts.saveAsTextFile("./shakespeareWordCount")
```

Sources:
To be finished

