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


In our world collecting data is extremely inexpensive but processing it requires large, parallel computations, often on clusters of machines. That's what Apache Spark was built for.Apache Spark is a unified computing engine and a set of libraries for parallel data processing on computer clusters that supports programming languages like R, Python, Java and Scala and libraries ranging from SQL to streaming and machine learning and runs everywhere from a laptop to a cluster of thousands of servers making it easy to scale up to big data processing or incredibly large scale.

Unified: Spark is designed to support a wide range of data analytics tasks over the same computing engine and with a consistent set of APIs. -> Real world data analytics tasks tend to combine many different processing types and libraries. 
Consistent Composable APIs: you can use to build an application out of smaller pieces or out of existing libraries. It also makes it easy for you to write your own analytics libraries on top. Spark's APIs are also designed to enable high performance by optimizing across the different libraries and functions composed together in a user program.#Example_1: if you load data using SQL query and then evaluate a machine learning model over it using Spark's ML library, the engine can combine these steps into a one scan over the data. Thus, the combination of general APIs and high-performance execution, no matter how you combine them, makes Spark a powerful platform for interactive, and production applications.#Example_2: Web developers benefit from unified frameworks such as Node.js or Django

Computing Engine:  Spark handles loading data from storage systems and performing computation on it, not being a permanent storage as the end itself. You can use Spark with a wide variety of storage systems such as Azure Storage and Amazon S3, distributed file systems such as Apache Hadoop, key-value stores such as Apache Cassandra and message buses such as Apache Kafka. However, Spark does not store data long-term itself.

Libraries: builds on Spark's design as a unified engine to provide a unified API for common data analysis tasks. Spark supports standard libraries and external libraries. Spark includes libraries for SQL, and structured data SparkSQL, machine learning (MLlib), stream processing (Spark Streaming and the newer Structured Streaming), and graph analytics (GraphX). Beyond these libraries there are a hundreds of open source external libraries. (spark-packages.org)
Parallel Processing: processing of program instructions by dividing them among multiple processors with the objective of running a program in less time. 

Running Spark -  Spark runs on the JVM (Java Virtual Machine) so you need to install Java to run it. If you want to use the Python API, you will also need a Python interpreter. If you want to use R, you will need a version of R on your machine. 
Launching Spark's Interactive Console

Python
Scala

SQL
|||||||||||
Cloud
./bin/pyspark
./bin/spark-shell
./bin/spark-sql
|||||||||||
Databrick's Community Edition

after you have done that type "spark" and press Enter. You will see the "SparkSession" object printed 
after you have done that type "spark" and press Enter. You will see the "SparkSession" object printed 

|||||||||||
data used in this book: https://github.com/databricks/Spark-The-Definitive-Guide

The SparkSession: You can control your Spark Application through a driver process called the SparkSession. The SparkSession is the way Spark executes user-defined manipulations across the cluster. There is a one-to-one correspondance between a SparkSession and a SparkApplication.
Spark's Basic ArchitectureProblem: one computer works well for watching movies or working with spreadsheet software. However, there are things a computer is not powerful enough to perform - e.g data processing. Single machines do not have the power and resources to perform computations on huge amounts of information or the user does not have time to wait for the computation to finish. Solution ->A cluster or group, of computers, pools the resources of many machines together, giving us the ability to use all the cumulative resources as if they were a single computer. A group of machines alone is not powerful, you need a framework to coordinate work across them - Spark does just that! - Coordinating and managing the execution of tasks on data across a cluster of computers.The cluster of machines that Spark uses to execute tasks is managed by a cluster manager. 
YARN or Mesos or Spark's standalone cluster manager. We then submit Spark Applications to these cluster managers

Spark Application (Architecture of a Spark Application)Spark applications consist of a drives process and a set of executor processes.

Driver Process (heart of a Spark Application, maintains all relevant information during the lifetime of the application.
Executor Processes
Runs of your main() function, sits on a node in the cluster, and is responsible for:
maintaining information about the Spark Application
Responding to a user's program or input
analyzing, distributing and scheduling work across the executors
Responsible for actually carrying out the work that the (<-) driver assigns them. Each executor is responsible for:
Executing code assigned to it by the driver 
Reporting the state of the computation on that executor BACK to the driver node.

Driver is on the left, four executors on the right.  It demonstrates how the cluster manager controls physical machines and allocates resources to Spark Applications. This can be one of three cluster managers ( YARN, Mesos, Spark's standalone cluster manager). This means that there can be multiple Spark Applications running on a cluster at the same time.
Note: Spark, in addition to a cluster mode, also has a local mode. The driver and the executor are simply processes, this means they can live on the same machine or different machines. Local Mode - Driver and executor run as threads on your individual computer in stead of a cluster.

[]Spark employs a cluster manager that keeps track of the resources available[x]The driver process is responsible for executing the driver program's commands across the executor to complete a given task.
The executor only runs Spark code. However, the driver can be driven from a number of different languages through Spark's Language APIs.Spark's Language APIs: make it possible to run Spark code using programming languages. Spark presents 'core concepts' in every language; these concepts are then translated into Spark code that runs on the cluster of machines. // If you use the Structured APIs, you can expect all languages to have similar performance characteristics.-> Scala, Java, Python, SQL, R


Represents the relationship between SparkSession and Spark's Language APIs.
When using Spark or Python, you don't write explicit JVM instructions; instead you write Python and R code that Spark translates into code that it then can run on the executor JVMs.

Spark's APIs: Spark has two fundamental sets of APIs: (1) low-level UNSTRUCTURED API (2) higher-level STRUCTURED API
DataFramesCreate a DataFrame with one column containing 1,000 rows with values from 0 to 999. This range of numbers represents a distributed collection. When run on a cluster, each part of this range of numbers exists on a different executor. This is Spark DataFrame
Python
Scala
Databricks/Excel - display()
myRange = spark.range(1000).toDF("number")


val myRange = spark.range(1000).toDF("number")


click to zoom!

DataFrame (core abstraction) is the most common Structured API and simply represents a table of data with rows and columns. The list the defines the columns and types within those columns is called a schema. DataFrame is like a spreadsheet with named columns, but a spreadsheet sits on a computer in a specific location whereas Spark DataFrame can span thousands of computers. 
# Pandas (Python) DataFrames and R DataFrames are converted to Spark DataFrames because originally they exist on one machine rather than multiple machines thanks to Spark's language interfaces.
PartitionsTo allow every executor to perform work in parallel, Spark breaks up the data into chunks called partitions. A Partition is a collection of rows that sit on one physical machine in your cluster. It represents how the data is physically distributed across the cluster of machine during execution. #If you have ONE partition Spark will have a parallelism of ONE even if you have thousands of executors. If you have MANY partitions but only ONE executor you will still have a parallelism of ONE because there is only ONE computation resource. You don't manipulate partitions manually, Spark decides how this will actually execute on the cluster. Low-level APIs do exist via RDDs though.
Transformations - ways of specifying different series of data manipulationIn Spark, the core data structures are immutable, meaning they cannot be changed after they are created. You use transformations to instruct Spark how you would like to modify what you want.
DAG = Execution Plan is a  (Directed Acyclic Graph) DAG of transformations. each resulting in a new immutable DataFrame.
Task: find all even numbers in current DataFrame:No output!  -> we specified only an abstract transformation and Spark does not act on transformations until we call an action.

Python
Scala
Databricks/Excel 
divisBy2 = myRange.where("number % 2 = 0")

val divisBy2 = myRange.where("number % 2 = 0")



There are two types of transformations:  Narrow dependencies and  Wide dependencies.
Narrow dependencies: each input partition will contribute to only one output partition. In the above code the "where" statement specifies a narrow dependency, where only one partition contributes to at most one output partition. (see the map, filter part of the picture).Automatically performs an operation called pipelining, meaning that if we specify multiple filters on DataFrames, they will all be performed in-memory.Wide dependencies: input partitions contributing to many output partitions. Also referred to as "Shuffle" whereby Spark will exchange partitions across the cluster. When we perform a shuffle, Spark writes the results to disk. 


Lazy EvaluationSpark waits until the very last moment to execute the graph of computation instructions. Spark will not modify data immediately when you express some operation, you build up a plan of transformations that you would like to apply to your source data.Spark optimizes the entire data flow from end to end.  Predicate Pushdown - Spark will attempt to move filtering of data as close to the source as possible to avoid loading unnecessary data into memory.DataFrames have a set of columns with an unspecified number of rows -> reading data is a transformation and is a lazy operation. Spark only peeks at a couple of rows to try guess what type each column should be. 
ActionsTransformations allow us to build up our logical transformation plan. To trigger the computation we run an action. Action instructs Spark to compute a result from a series of transformations. The simplest action is count, which gives us the total number of records in the DataFrame. There are three kinds of actions
Actions to view data in the console
Actions to collect data to native objects in the respective language
Actions to write to output data sources
Python
Scala
DataBricks



In specifying this action, we started a Spark job that runs our filter transformation (narrow transformation) then an aggregation (wide transformation) that performs the counts on a per partition basis, and then collect, which brings our result to a native object in the respective language. Spark UI: (for monitoring the progress of a job) Local mode: available on port 4040 of the driver node. http://localhost:4040Spark job: represents a set of transformations triggered by an individual action, and you can monitor that job from Spark UI



*** EXAMPLE ****data from github - flight data csv 2015 databricks schema inference - we want Spark to take a best guess at what the schema of our DataFrame should be. (CSV files are not completely structured)we will specify that the first row is the header
STEP 1: Load data
inferschema
header
Python
Scala
Databricks
flightData2015 = spark\.read\.option("inferSchema" , "true")\.option("header", "true")\.csv("/Users......csc")





val flightData2015 = spark.read.option("inferSchema" , "true").option("header", "true").csv("/Users......csc")







STEP 2: Perform a take action:
Python
Scala
Databricks
flightData2015.take(3)




STEP 3: Nothing happens when we call a sort beacuse it's just a transformation. But we can see the explain plan to see how Spark will execute it across the cluster . We can call an explain on any DataFrame object to see the DataFrame's lineage. Explain plans are read top to bottom, top being the end result  and bottom being the source of data.
Python
Scala
DataBricks
flightData2015.sort("count").explain()




STEP4: Set a configuration. By default when we perform a shuffle Spark outputs two hundred shuffle partitions. Let's see this value to five to reduce the number of output partitions from the shuffle.  
Python
Scala
DataBricks
spark.conf.set("spark.sql.shuffle.partitions", "5")flightData2015.sort("count").take(2) 

spark.conf.set("spark.sql.shuffle.partitions", "5")flightData2015.sort("count").take(2)
spark.conf.set("spark.sql.shuffle.partitions", "5")flightData2015.sort("count").take(2)


This picture illustrates the above operation -->

The logical plan of transformations that we build up defines a lineage for the DataFrame so that at any given point in time Spark knows how to recompute any partition by performing all of the operations it had before on the same input data.Functional Programming: where the same inputs always result in the same outputs when the transformations on that data stay constant.
DataFrames and SQL:Spark can run the same transformations regardless of the language, in the exact same way. With SparkSQL, you can register any DataFrame as a table and query it using pure SQL. There is no performance difference between writing SQL queries and DataFrame code.
You can make any DataFrame into a table or view with one simple method call
Python
Scala
Databricks

flightData2015.createOrReplaceTempView("flight_data_2015")
flightData2015.createOrReplaceTempView("flight_data_2015")

createOrReplaceTempView
...Now we can query the data into SQL.Function: spark.sql (hint: spark is the SparkSession variable that returns a new DataFrame)

Python
Scala
Databricks (py)
Note

sqlWay = spark.sql("""SELECT DEST_COUNTRY_NAME, count(1)FROM flight_data_2015GROUP BY DEST_COUNTRY_NAME""")
<br>dataFrameWay= flightData2015\.groupBy("DEST_COUNTRY_NAME")\.count()
<br>sqlWay.explain()dataFrameWay.explain()


val sqlWay = spark.sql("""SELECT DEST_COUNTRY_NAME, count(1)FROM flight_data_2015GROUP BY DEST_COUNTRY_NAME""")
<br>val dataFrameWay = flightData2015.groupBy('DEST_COUNTRY_NAME).count()
<br>sqlWay.explaindataFrameWay.explain


Notice that these plans compile to the exact same underlying plan


DataFrames and SQL in Spark have a huge number of manipulations available, there are hundreds of functions you can use and import to help resolve big data problems faster!
Python
Scala
Databricks

from pyspark.sql.functions import max
import org.apache.spark.sql.functions.max

IMPORT

Task/Example: Establish the maximum number of flights to and from any given location.
Python
Scala
Databricks

flightdata2015.select(max("count")).take(1)


import org.apache.spark.sql.functions.max

MAX
Task/Example 2: Find the top five destination countries in the data.

SQL Way
DataFrame Way 
#PythonmaxSql = spark.sql("""SELECT DEST_COUNTRY_NAME, sum(count) as destination_totalFROM flight_data_2015GROUP BY DEST_COUNTRY_NAMEORDER BY sum(count) DESCLIMIT 5""")maxSql.show()

//Scalaval maxSql = spark.sql("""SELECT DEST_COUNTRY_NAME, sum(count) as destination_totalFROM flight_data_2015GROUP BY DEST_COUNTRY_NAMEORDER BY sum(count) DESCLIMIT 5""")maxSql.show()



Python DataFrame WayStep 1: from pyspark.sql.functions import desc
Step 2flightData2015\.groupBy("DEST_COUNTRY_NAME")\.sum("count")\.withColumnRenamed("sum(count)", "destination_total")\.limit(5)\.show()

---Scala  DataFrame syntax:flightData2015.groupBy("DEST_COUNTRY_NAME").sum("count").withColumnRenamed("sum(count)", "destination_total").limit(5).show()


Explanation of the above code (steps)
Read in the data (Spark does not actually read it until an action is called)
Grouping - RelationalGroupedDataset, which is a fancy name fro DataFrame that has grouping specified but needs the user to specify an aggregation before it can be queried further. We just specified that we are going to be grouping by a key.
Specify the aggregation - used the 'sum' aggregation. This takes an input as a column name, the result of the sum method call is a new DataFrame. No computation has been performed still. This is simply another transformation. You can check the schema, but it won't know the type of each column
WithColumnRenaimed() - takes two arguments: the original column name, and the new column name -this is just another transformation
Sorts the data 
Then we specified a limit to not return the entire DataFrame
The last step is the action - the process of collecting the results begin
-> Now let's look at the explain plan:


Spark is composed of primitives - the lower-level APIs and the Structured APIs - and then a series of standard libraries for additional functionality.Spark's libraries support graph analysis to machine learning to streaming and integrations with a host of computing and storage systems.
Objectives: 
Running production applications with spark-submit
Dataset: type safe APIs for structured data
Structured Streaming
Machine Learning and advanced analytics
Spark's lower level RDD API
SparkR
The third-party package ecosystem

Running Production Applicationsspark submit - does one thing: it lets you send your application code to a cluster and launch it to execute there. Upon submission, the application will run until it exits or encounters an error. You can do this with Spark Standalone, Mesos and YARN.spark-submit offers several controls to specify the resources your application needs

Python
Scala
./bin/spark-submit \--master local \./examples/src/main/python/pi.py 10
./bin/spark-submit \--class org.apache.spark.examples.SparkPi \ --master local \./examples/jars/spark-example_2.11-2.2.0.jar 10
Datasets: Type-Safe Structured APIsDataset = type-safe version of Spark's structured API for writing statically typed code in Java and Scala. - not available in Python and R because these languages are dyynamically typed.Dataset API gives users the ability to assign a Java class too the records within a DataFrame and manipulate it as collection of typed objects. The APIs available on Datasets are type-safe meaning that you cannot accidentally view the objects in a Dataset as being of another class than the class you put in initially. This makes Datasets attractive for writing large applications.The Dataset class is parametrized with the type of object contained inside: Dataset <T> in Java and Dataset[T]  in Scala. For Example: Dataset [Person] will be guaranteed to contain objects of class Person. Benefit: you can use Datasets only when you need or want to.Dataset API is an extension to DataFrames that provides a type-safe, object-oriented programming interface. It is a strongly-typed, immutable collection of objects that are mapped to a relational schema.
At the core of the Dataset, API is a new concept called an encoder, which is responsible for converting between JVM objects and tabular representation. The tabular representation is stored using Spark internal Tungsten binary format, allowing for operations on serialized data and improved memory utilization. Spark 1.6 comes with support for automatically generating encoders for a wide variety of types, including primitive types (e.g. String, Integer, Long), Scala case classes, and Java Beans.
Dataset Features:-
Provides best of both RDD and Dataframe: RDD(functional programming, type safe), DataFrame (relational model, Query optimazation , Tungsten execution, sorting and shuffling)
Encoders: With the use of Encoders, it is easy to convert any JVM object into a Dataset, allowing users to work with both structured and unstructured data unlike Dataframe.
Programming Languages supported: Datasets API is currently only available in Scala and Java. Python and R are currently not supported in version 1.6. Python support is slated for version 2.0.
Type Safety: Datasets API provides compile time safety which was not available in Dataframes. In the example below, we can see how Dataset can operate on domain objects with compile lambda functions.

Example/Task: Drop down to lower level, perform type-safe coding and move higher up to SQL for more rapid analysis.

Scala
case class Flight(DEST_COUNTRY_NAME: String,ORIGIN_COUNTRY_NAME: String,count: BigInt)val flightsDF = spark.read.parquet("/data/flights-data/parquet/2010-summary.parquet/")val flights = flightsDF.as[Flight]
The advantage is that when you call collect or take on the Dataset, we are going to collect to objects of the proper type in the DataSet, not DataFrame Rows. This makes it easy to get type safety and safely perform manipulation in distributed and a local manner without code changes. 
Scala
flights.filter(flight_row => flight_row.ORIGIN_COUNTRY_NAME != "Canada").map(flight_row => flight_row).take(5)
Structured StreamingStructured Streaming is a high level API for stream processing. With Structured Streaming you can teake the same operations that you perform in batch mode (computer processing in which commands are input from a batch file, not interactively) using Spark's structured APIs and run them in a streaming fashion. This reduces latency and allows for incremental processing.  It allows you to rapidly and quickly extract value out of streaming systems with virtually no code changes. You can write your batch jobs as a way to prototype and then you can convert it to streaming job by incrementally processing data.
Sample of the data:  (retail-data/def-guide)

Step 1: analyze the data as a static dataset and create a DataFrame to do so. We'll also create a schema from this static dataset.

Python
Scala
Notes
staticDataFrame = spark.read.format("csv")\.option("header", "true")\.option("inferSchema", "true")\.load("/Users/mikepetridisz/Desktop/retail-data/by-day/*.csv")

val staticDataFrame = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load("/Users/mikepetridisz/Desktop/retail-data/by-day/*.csv")
Load the dataRetailBy dayDef Guide
Step 2: Add a total cost column and see on what days a customer spend the most. window() - will include all data from each day in the aggregation. It's simply a window over the time-series column in our data. This is a helpful tool for manipulating date and timestamps because we can specify our requirements in a more human form via intervals, and Spark will group all of them together for us. 

Python
Scala
Notes
 
staticDataFrame.createOrReplaceTempView("retail_data")staticSchema = staticDataFrame.schema
from pyspark.sql.functions import window, column, desc, col
staticDataFrame\.selectExpr( "CustomerId", "(UnitPrice * Quantity) as total_cost", "InvoiceDate")\ .groupBy(col("CustomerId"), window(col("InvoiceDate"), "1 day"))\.sum("total_cost")\.show(5)


import org.apache.spark.sql.functions.{window, column, desc, coll}
Null values represent the fact that we don't have a customer Id for some transactions. 
Step 3: take a look at the streaming code:

Python
Scala
Notes
streamingDataFrame = spark.readStream\.schema(staticSchema)\.option("maxFilesPerTrigger", 1)\.format("csv")\.option("header", "true")\.load("/data/retail-data/by-day/*.csv")
streamingDataFrame.isStreaming



Let's perform a summation now:







Machine Learning and Advanced AnalyticsMLlib allows for preprocessing, munging, training of models and making predictions at scale on data.You can use models trained in MLlib to make predictions in Structured Streaming. Standark Algorithm: K-meansK-means clustering algorithm: clustering algorithm in which 'K' centers are randomly assigned within the data. The point closest to that point are then assigned to a class and the center of the assigned points is computed.This center point is called centroid. We then label the points closest to that centroid, to the centroid's class, and shift the centroid to the new center of that cluster of points. We repeat this process for a finite set of iterations or until convergence (our center points stop changing.)










K-means clustering does not work well if the data is noisy or there are overlapping data. Unsupervised.

Applications of K-means clustering:
Telephone companies use K-means clustering algorithm to place towers so that all its users receive optimum signal strenght
Police stations use K means clustering so that patrol vehicles are stationed across the area so that the areas of high crime rates are in the vicinity of the patrol van
Hospital care chains open a series of emergency care wards while considering accident prone areas in the region 
Can also be used for market segmentation, price spend behaviors and customer need segmentation and also used in computer vision

Advantages of K-means clusteringK-means speed>hierarchical clustering speed if K is smallK-means will produce tighter clusters than hierarchical clustering
Disadvantages of K-means clusteringDifficulty in comparing quality of the clusters produced Fixed number of clusters can make it difficult to predict what K should be Strong sensitivity to outliers and noise Does not work well in non-circular cluster shape Low capability to pass the local optimum
Machine learning algorithms in MLlib require that data is represented as numerical values. Our current data is represented by a variety of different types including time stamps, integers and strings. Therefore, we need to transform this data into some numerical representation. So we will use several DataFrame transformations to manipulate out date data.




Key concepts:Spark is a distributed programming model in which the user specifies transformations. These transformations build up a directed acyclic graph of transformations and action. An action begins the process of execution that graph of instructions, as a single job, by breaking it down into stages and tasks to execute across the cluster. The logical structures that we manipulate with transformations and actions are DataFrames and Datasets. To create a new DataFrame or Dataset, you call a transformation. To start computation or convert to native language types, you call an action.


Fundamental concepts:Spark is a distributed programming model in which the user specifies transformations. These transformations build up a directed acyclic graph of transformations and action. An action begins the process of execution that graph of instructions, as a single job, by breaking it down into stages and tasks to execute across the cluster. The logical structures that we manipulate with transformations and actions are DataFrames and Datasets. To create a new DataFrame or Dataset, you call a transformation. To start computation or convert to native language types, you call an action. Structured API OverviewStructured APIs are a tool for manipulating all sorts of data, from unstructured log files to semi-structured CSV files and highly structured Parquet (Apache Parquet is a columnar storage format available to any project in the Hadoop ecosystem, regardless of the choice of data processing framework, data model or programming language) files. These APIs refer to three core types of distributed collection APIs:
Datasets
DataFrames
SQL Tables and Views
Majority of the Structured APIs apply to both batch and streaming computation. This means that when you work with the Structured APIs, it should be simple to migrate from batch to streaming or vice versa with little to no effort.  Structured APIs are the fundamental abstraction used to write the majority of data flows.  DataFrames and DatasetsDataFrames and Datasets are distributed table-like collection with well-defined rows and columns. Each column must have the same number of rows as all the other columns although you can use null to specify the absence of a value and each column has type information that must be consistent for every row in the collection. To Spark, DataFrames and Datasets represent immutable, lazily evaluated plans(transformations) that specify what operations to apply to data residing at a location to generate some output. When we perform an action on a DataFrame, we instruct Spark to perform the actual transformations and return the results. These represent plans of how to manipulate rows and columns to compute the user's desired result.  Tables and views - like a DataFrame, but we execute SQL against them instead of DataFrame code.  Schema - defines the column names and types of a DataFrame. You can define schemas manually or read a schema from a data source. Schemas consist of types meaning that you need a way of specifying what lies where. Overview of Structured Spark TypesSpark is effectively a programming language of its own. Spark uses an engine called Catalyst. Catalyst - maintains its own type information through the planning and processing of work. This opens up execution optimizations.Even if we use Spark's Structured APIs from Python or R, the majority of our manipulations will operate strictly on Spark types not Python types.  
 This addition operation happens because Spark will convert an expression written in an input language to Spark's internal Catalyst representation of that same type information. It then will operate on that internal representation.  DataFrames VS Datasets
STRUCTURED APIs

DataFrames
Datasets
untyped(Spark maintains them completely)
typed(checks whether types conform to the specification at compile time.)Only available to JVM based languages Scala and Java.
DataFrames are Datasets of Type Row. The "Row" type is Spark's internal representation of its optimized in-memory format for computation. To Spark in Python and R there is no such thing as a Dataset, everything is a DataFrame and therefore we always operate on that optimized format. //WATCH! - Spark Catalyst Engine talks by Josh Rosen and Herman van Hovell
KEY Takeaway: When you use DataFrames, you are taking advantage of Spark's optimized internal format.
Columns: represent a simple type like an integer or string or complex type like an array or map or null values. Rows: record of data. 

Spark Types(Spark documentation - get updated time to time)
Overview of Structured API Execution
Write DataFrame/Dataset/SQL Code
If valid code, converts this to a Logical Plan
Spark . transforms this Logical Plan, checking for optimizations along the way
Spark then executes this Physical Plan (RDD Manipulations) on the cluster

The code we write gets submitted to Spark either through console or via a submitted job. This code passes through the Catalyst Optimizer, which decides how the code should be executed and lays out a plan for doing so before, finally, the code is run and the result is returned to the user.

Logical Planning
Physical Planning 
The first phase takes user code and converts it into a logical plan (optimized version of the user's set of expressions)It does this by converting user code into an unresolved logical plan. The plan is unresolved because although your code might be valid, the tables and columns that it refers to might or might not exist. Spark uses the catalog, a repository of all table and DataFrame information to resolve columns and tables in the analyzer. The analyzer might reject the unresolved logical plan if the required column name does not exist in the catalog. If the analyzer can resolve it, the result is passed through the Catalyst Optimizer, a collection of rules that attempt to optimize the logical plan by pushing down predicates or selections. Packages can extend the Catalyst to include their own rules for domain-specific optimizations.

After creating the optimized logical plan, Spark begins the physical planning process. The physical plan - often called SPark plan - specifies how the logical plan will execute on the cluster by generating different physical execution strategies and comparing them through a cost model. Upon selecting a physical plan Spark runs all of this code over RDDs.


Basic Structured OperationsDataFrame consists of a series of records that are of type Row and a number of columns that represent a computation expression that can perform on each individual record in the Dataset. Schemas define the name as well as the type of data in each column. Partitioning of the DataFrame defines the layout of the DataFrame or Dataset's physical distribution across the cluster. The partitioning scheme defines how that is allocated.
Creating a DataFrame:
Python
Scala
df = spark.read.format("json").load("/Users/mikepetridisz/Desktop/json/2015-summary.json")
val df = spark.read.format("json").load("/Users/mikepetridisz/Desktop/json/2015-summary.json")
printSchemadf.printSchema() # A schema is a StructType made up of a number of fields, StructFields, that have a name, type, a boolean flag (null values/missing values), metadata (metadata used in Machine Learning)
printSchemadf.printSchema()
<br><br><br><br><br><br><br><br><br>
 myManualScheme = StructType([
... StructField("DEST_COUNTRY_NAME", StringType(), True),
... StructField("ORIGIN_COUNTRY_NAME", StringType(), True),
... StructField("count", LongType(), False, metadata={"hello":"world"})
... ])
>>> df = spark.read.format("json").schema(myManualScheme)\
... .load("/Users/mikepetridisz/Desktop/json/2015-summary.json")

Columns and ExpressionsExpressions - when you select, remove manipulate columns from DataFrames
Creating a Column
Python
Scala
NOTE
from pyspark.sql.functions import cal, columncol("someColumnName")column("someColumnName")
import org.apache.spark.sql.functions.{col, column}col("someColumnName")column("someColumnName")--other way:scala> $"myColumn"scala>'myColumn
col()  or column function

Explicit Column References if you need to refer to a specific DataFrame's column, you can use the col method on the specific DataFrame. This can be useful when performing a join and need to refer to a specific column in one DataFrame that might share the same name with another column in the joined DataFrame. ExpressionsColumns are expressions. An expression is a set of transformations on one or more values in a record in a DataFrame. An expression created via the expr function is just a DataFrame column reference.expr("someCol") is equivalent to col("someCol") Columns as ExpressionsWhen using an expression, the expr function can actually parse transformations and column references from a string and can subsequently be passed into further transformations.Key takeaways:
Columns are just expressions
Columns and transformations of those columns compile to the same logical plan as parsed expressions.
Example:DataFrame Code
SQL code
#You can write expressions as DataFrame code or SQL code and get the exact same performance characteristics.
Accessing a DataFrame's ColumnsprintSchema or:spark.read.format("json").load("/Users/mikepetridisz/Desktop/json/2015-summary.json").columns Records and RowsEach row in a DataFrame is a singlerecord as an object type Row. Spark manipulates Row objects using column expressions in order to produce usable values. 

Creating Rows
Python
Scala
Note
from pyspark.sql import RowmyRow = Row("Hello", None, 1, False)

import org.apache.spark.sql.Rowval myRow = Row("Hello", null, 1, false)
Creating RowsImporting RowsAccessing data in rows 
DataFrame Transformations
We can add rows or columns
We can remove rows and columns
We can transform a row into a column or vice versa
We can change the order of rows based on the values in columns
 Creating DataFrames on the fly
Python
Scala
from pyspark.sql import Rowfrom pyspark.sql.types import StructField, StructType, StringType, LongType myManualSchema = StructType([StructField("some", StringType(), True),StructField("col", StringType(), True),StructField("names", LongType(), False)])myRow = ("hello", None, 1)myDf = spark.createDataFrame([myRow], myManualSchema)myDf.show()
  
import org.apache.spark.sql.Rowimport org.apache.spark.sql.types.{ StructField, StructType, StringType, LongType} val myManualSchema = new StructType(Array(new StructField("some", StringType, true),new StructField("col", StringType, true),new StructField("names", LongType, false)))val myRow = Seq(Row("hello", None, 1L))val myRDD = spark.sparkContext.parallelize(myRows)val myDf = spark.createDataFrame(myRDD, myManualSchema)myDf.show()val myDf = Seq(("Hello", 2, 1L)).toDF("col1","col2", "col3")myDf.show()
Select and SelectExpr
allows you to do the DataFrame equivalent of SQL queries on a table of data
SQL
Python
Scala
Note
SELECT DEST_COUNTRY_NAME FROM dfTable LIMIT 2
df.select("DEST_COUNTRY_NAME").show(2)

df.select("DEST_COUNTRY_NAME").show(2)
Use the select method and pass in the column names as strings with  which you would like to work
SELECT DEST_COUNTRY_NAME, ORIGIN_COUNTRY_NAME FROM dfTable LIMIT 2
df.select("DEST_COUNTRY_NAME", "ORIGIN_COUNTRY_NAME").show(2)

df.select("DEST_COUNTRY_NAME", "ORIGIN_COUNTRY_NAME").show(2)
you can select multiple columns

you can refer to columns in a number of different waysdf.select(expr("DEST_COUNTRY_NAME"),col("DEST_COUNTRY_NAME"),column("DEST_COUNTRY_NAME"))\.show(2)



AS and alias - change the name using the AS and alias keywords
SQL
Python
Scala
Note
SELECT DEST_COUNTRY_NAME as destination FROM dfTable LIMIT 2
df.select(expr("DEST_COUNTRY_NAME AS destination").alias("DEST_COUNTRY_NAME")).show(2)

df.select("DEST_COUNTRY_NAME").show(2)
change the name of the columnAS

df.select(expr("DEST_COUNTRY_NAME AS destination").alias("DEST_COUNTRY_NAME")).show(2))

df.select(expr("DEST_COUNTRY_NAME AS destination").alias("DEST_COUNTRY_NAME")).show(2)
aliaschange the column name back to its original name
SELECT *, (DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as withinCountryFROM dfTableLIMIT 2
df.selectExpr("*","(DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as withinCountry")\.show(2)

df.selectExpr("*","(DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as withinCountry").show(2)
add a new column withinCountry to DataFrame that specifies whether the destination and origin are the same
SELECT act(count), count(distinct(DEST_COUNTRY_NAME)) FROM dfTable LIMIT 2
df.selectExpr("avg(count)", "count(distinct(DEST_COUNTRY_NAME))").show(2)


df.selectExpr("avg(count)", "count(distinct(DEST_COUNTRY_NAME))").show(2)
Aggregations


Converting to Spark TypesSometimes we need to pass explicit values into Spark that aren't a new column but are just a value.The was we do this is through literals. This is a translation from a given programming language's literal value to one that Spark understands. Literals are expressions.
SQL
Python
Scala
Note
SELECT *, 1 as One FROM dfTable LIMIT2
from pyspark.sql.functions import litdf.select(expr("*"),lit(1).alias("One")).show(2)

import org.apache.spark.sql.functions.litdf.select(expr("*"),lit(1).as("One")).show(2)


Adding Columns
SQL
Python
Scala
Note
SELECT *, 1 as numberOne FROM dfTable LIMIT2
df.withColumn("numberOne", lit(1)).show(2)

df.withColumn("numberOne", lit(1)).show(2)
formal way of adding a column

df.withColumn("withinCountry", expr("ORIGIN_COUNTRY_NAME == DEST_COUNTRY_NAME"))\.show(2)

df.withColumn("withinCOuntry", expr("ORIGIN_COUNTRY_NAME == DEST_COUNTRY_NAME"))\.show(2)
Boolean expression for when the original country is the same as the Destination Country
 

df.withColumn("Destination", expr("DEST_COUNTRY_NAME").columns

NOTICE that withColumn function takes two arguments; the column name and the expression that will create the value for that given row in the DataFrame. We can also rename a column this way. (SQL syntax is the same as previously so it is not here now.
Renaming ColumnswithColumnRenamed method
SQL
Python
Scala
Note

df.withColumnRenamed("DEST_COUNTRY_NAME", "dest").columns

df.withColumnRenamed("DEST_COUNTRY_NAME", "dest").columns
rename columnsname of the string = first argumentstring = second argument
Reserved Characters and Keywordslike spaces or dashes in column names. Handling these means escaping column names appropriately. We do this by using backtick ("`")
SQL
Python
Scala
Note

dfWithLongColName = df.withColumn("This Long Column-Name",expr("ORIGIN)COUNTRY_NAME")
import org.apache.spark.sql.functions.exprval dfWithLongColName = df.withColumn("this Long Column-Name",expr("ORIGIN_COUNTRY_NAME"))
Could not run this nor understand this part! - Need to come back & Check!

dfWithLongColName.selectExpr(" This Long Column-Name "," This Long Column-Name as `new col`")\.show(2)


set spark.sql.caseSensitive true


Case Sensitivity 

df.drop("ORIGIN_COUNTRY_NAME").columns

Removing Columns

dfWithLongColName.drop("ORIGIN_COUNTRY_NAME", "DEST_COUNTRY_NAME")

Removing multiple columns
SELECT *, cast(count as long) AS count2 FROM dfTable
df.withColumn("count2", col("count").cast("long"))



Change Column's Type (cast)
SELECT * FROM dfTable WHERE count < 2 LIMIT 2
df.filter(col("count") < 2).show(2)



Filtering Rows - evaluates to true or false. You can use where or filter an they both will perform the same operation.
SELECT * FROM dfTable WHERE count < 2 AND ORIGIN_COUNTRY_NAME != "Croatia LIMIT 2
df.where(col("count") < 2).where(col("ORIGIN_COUNTRY_NAME") != "Croatia")\.show(2)


df.where(col("count") < 2).where(col("ORIGIN_COUNTRY_NAME") != "Croatia").show(2)
Multiple filters you can put multiple filters into the same expression. It's not always useful because Spark automatically performs all filtering operations at the same time regardless of the filter ordering. This optimization is called PIPELINING. This means that if you want to specify multiple AND filters, just chain them sequentially and let Spark handle the rest.
SELECT COUNT(DISTINCT(ORIGIN_COUNTRY_NAME,  DEST_COUNTRY_NAME) FROM dfTable
df.select("ORIGIN_COUNTRY_NAME", "DEST_COUNTRY_NAME").distinct().count()



df.select("ORIGIN_COUNTRY_NAME", "DEST_COUNTRY_NAME").distinct().count()
Getting unique Rowsextract unique or distinct values. These values van be in one or more columns. distinct method allws us to duplicate any rows that are in the DataFrame. 

seed = 5withReplacement = Falsefraction = 0.5df.sample(withReplacement, fraction, seed).count()

val seed = 5val withReplacement = Falseval fraction = 0.5df.sample(withReplacement, fraction, seed).count()
sample method - sample some random records from your DataFrame.

dataFrames = df.randomSplit([0.25, 0.75], seed)dataFrames[0].count() > dataFrames[1].count()

val dataFrames = df.randomSplit(Array(0.25, 0.75), seed)dataFrames(0).count() > dataFrames(1).count()
Random Splits can be useful when you need to break up your DataFrame.  It cannot guarantee that all records are in one of the DataFrames from which you are sampling. This is often used with machine learning.

from pyspark.sql import Rowschema = df.schemanewRows = [Row("New Country", "Other Country", 5),Row("New Country 2", "Other Country 3", 1),]parallelizeRows = spark.sparkContext.parallelize(newRows)newDF = spark.createDataFrame(parallelizeRows, schema) df.union(newDF)\.where("count =1")\.where(col("ORIGIN_COUNTRY_NAME") != "United States")\.show() 
 

Concentrating and Appending Rows (Union)

df.sort("count").show(5)df.orderBy("count", "DEST_COUNTRY_NAME").show(5)df.orderBy(col("count"), col("DEST_COUNTRY_NAME")).show(5)

df.sort("count").show(5)df.orderBy("count", "DEST_COUNTRY_NAME").show(5)df.orderBy(col("count"), col("DEST_COUNTRY_NAME")).show(5)
Sorting Rows sort and orderBy do the samethe default is sort in ascending order

to more explicitly specify sort direction, you need to use asc and desc functions if operating on a column. 

from pyspark.sql.functions import asc, descdf.orderBy(expr("count desc")).show(2)df.orderBy(col("count").desc(),  col("DEST_COUNTRY_NAME").asc()).show(2)


(sort)to more explicitly specify sort direction, you need to use asc and desc functions if operating on a column. 
Advanced tip is to use asc_nulls_first, desc_nulls_first, asc_nulls_last, or _desc_nulls_last
SELECT * FROM dfTable LIMIT 6
df.limit(5).show()
df.limit(5).show()
LimitRestrict what you extract from the dataframe
SELECT * FROM dfTable ORDER BY count desc LIMIT 6
df.orderBy(expr("count")).asc().limit(6).show()
df.orderBy(expr("count")).asc().limit(6).show()


df.rdd.getNumPartitions()df.repartition(5)

Repartition based on a columns name df.repartition(5, col("DEST_COUNTRY_NAME"))
df.rdd.getNumPartitions()df.repartition(5)
Repartition partition the data according to some frequently filtered columns, which control the physical layout of data across the cluster including the partitioning scheme and the number of partitions. 
Repartition will incur a full shuffle of the data, regardless of whether one is necessary. This means that you should typically only repartition when the future number of partitions os greater than your current number of partitions or when you are looking to partition by a set of columns. 

df.repartition(5, col("DEST_COUNTRY_NAME")).coalesce(2)
df.repartition(5, col("DEST_COUNTRY_NAME")).coalesce(2)
Coalescewill not incur a full shuffle and will try to combine partitions. This operation will shuffle your data into five partitions based on the destination country name and then coalesce them without a full shuffle.

collectDF=df.limit(10)collectDF.take(5) #works with an integer countcollectDF.show() #this prints it out nicelycollectDF.show(5, False)collectDF.collect()

val collectDF=df.limit(10)collectDF.take(5)collectDF.show()collectDF.show(5, False)collectDF.collect()
Collecting Rows to the DriverSpark maintains the state of the cluster in the driver. There are times when you want to collect some of the data to the driver in order to manipulate it on your local machine.
collect gets all the data from the entire Dataframetake selects the first N rows show prints out a number of rows nicely.

collectDF.toLocalIterator()

Iterate over the entire dataset. The method is called toLocalIterator that collects partitions to the driver as an iterator. Iterates over the entire dataset partition by partition in a serial manner


Working with Different Types of DataObjectives
Booleans
Numbers
Strings
Dates and Timestamps
Handling Null
Complex Types
User Defined Functions
 Where to look for APIs?DataFrame (Dataset) Methods: DataFrame is just a Dataset of Row types, so you will look at the Dataset methods available at: http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.DatasetDataFrameStatFunctions: http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.DataFrameStatFunctionsDataFrameNaFunctions http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.DataFrameNaFunctionsColumn methods: http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.ColumnFunctions: http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.functions$Dataset: http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Dataset
DataFrame used here => by-day/2010.12.01.csv
SQL
Python
Scala
Notes

>>> df = spark.read.format("csv")\
... .option("header", "true")\
... .option("inferSchema", "true")\
... .load("/Users/mikepetridisz/Desktop/retail-data/by-day/2010-12-01.csv")
>>> df.printSchema()
>>> df.createOrReplaceTempView("dfTable")
 




Load data
no equivalent function necessary in SQL
from pyspark.sql.functions import litdf.select(lit(5), lit("five"), lit(5.0))

import org.apache.spark.sql.functions.litdf.select(lit(5), lit("five"), lit(5.0))
convert to spart typesconvert native types to spark types.
We do this by using the lit function

from pyspark.sql.functions import coldf.where(col("InvoiceNo") != 536365)\.select("InvoiceNo", "Description")\.show(5, False)
  ORdf.where("InvoiceNo == 536365")\.show(5, false)
df.where(col("InvoiceNo") === 536365).select("InvoiceNo", "Description").show(5, False)
Working with BooleansBoolean statements consist of four elements: and, or, true, false
SELECT * FROM dfTable WHERE StockCode in ("DOT") AND (UnitPrice >600 OR instr(Description, "POSTAGE") >= 1
from pyspark.sql.functions import instrpriceFilter = col("UnitPrice") > 600descripFilter = instr(df.Description, "POSTAGE") >= 1df.where(df.StockCode.isin("DOT")).where(priceFilter | descripFilter).show()


val priceFilter = col("UnitPrice") > 600val descripFilter = col("Description").contains( "POSTAGE")df.where(df.StockCode.isin("DOT")).where(priceFilter | descripFilter).show() 

SELECT UnitPrice, (StockCode = 'DOT' AND(UnitPrice > 600 OR instr(Description, "POSTAGE") >= 1)) as isExpensiveFROM dfTableWHERE (StockCode = 'DOT' AND(UnitPrice > 600 OR instr(Description, "POSTAGE") >= 1))
from pyspark.sql.functions import instrDOTCodeFilter = col("StockCode") == "DOT"priceFilter = col("UnitPrice") > 600descripFilter = instr(col("Description"), "POSTAGE") >= 1df.withColumn("isExpensive", DOTCodeFilter & (priceFilter | descripFilter))\.where("isExpensive")\.select("unitPrice", "isExpensive").show(5)


To specify a DataFrame, you can also just specify a Boolean column

df.where(col("Description").eqNullSafe("hello")).show()

df.where(col("Description").eqNullSafe("hello")).show()
Null safe equivalence test:df.where(col("Description").eqNullSafe("hello")).show()
if there is a null in the data, we need to treat things differently. the above example shows how we can tackle it.

Working with Numbersafter filtering the most common thing in big data is counting things. 
SQL
Python
Scala
Note
SELECT customerId, (POWER((Quantity * UnitPrice), 2.0) +5) as realQuantity FROM dfTable
from pyspark.sql.functions import pow, exprfabricatedQuantity = pow(col("Quantity") * col("UnitPrice"), 2) +5df.select(expr("CustomerId"), fabricatedQuantity.alias("realQuantity")).show(2)

val fabricatedQuantity = pow(col("Quantity") * col("UnitPrice"), 2) +5df.select(expr("CustomerId"), fabricatedQuantity.alias("realQuantity")).show(2)
Let's imagine that we found out that we misrecorded the quantity in our retail dataset and the true quantity is equal to the ((current quantity * the unit price)^2 +5) pow function (raises a column to the expressed power
SELECT round (2.5), bround(2.5)
from pyspark.sql.functions import lit, round, brounddf.select(round(lit("2.5")), bround(lit("2.5"))).show(2)

import org.apache.spark.functions.litdf.select(round(lit("2.5")), bround(lit("2.5"))).show(2)

Roundingexample round to 1 decimal places
SELECT corr(Quantity, UnitPrice) FROM dfTable
from pyspark.sql.functions import corrdf.stat.corr("Quantity", "UnitPrice")df.select(corr("Quantity", "UnitPrice")).show()

import org.apache.spark.functions.{corr}df.stat.corr("Quantity", "UnitPrice")df.select(corr("Quantity", "UnitPrice")).show()
Compute the correlation of two columns. e.g to see if cheaper things are typically bought in greater quantities. 


df.describe().show()

df.describe().show()
Summary Statistics for a column or a set of columns. 
describe method. This takes all numeric columns and calculate the count, mean, standard deviation, min, max.You should use this for viewing the console because the schema might change in the future.

from pyspark.sql.functions import count, mean, stddev_pop, min, max


if you need exact numbers you can also perform this aggregation yourself by importing the functions and applying them to the columns that you need.
These are the statistical functions available in the StatFunctions Package. 

colName = "UnitPrice"quantileProbs = [0.5]relError = 0.05df.stat.approxQuantile("UnitPrice", quantileProbs, relError)


val colName = "UnitPrice"val quantileProbs = [0.5]val relError = 0.05df.stat.approxQuantile("UnitPrice", quantileProbs, relError)
You can calculate exact or approximate quantiles of your data using the approxQuantile method.

df.stat.crosstab("StockCode", "Quantity").show()
 df.stat.freqItems(["StockCode", "Quantity"]).show()

df.stat.crosstab("StockCode", "Quantity").show()
















 df.stat.freqItems(["StockCode", "Quantity"]).show()
cross-tabulation or frequent item pairs this output will be large!!!!!

from pyspark.sql.functions import monotonically_increasing_iddf.select(monotonically_increasing_id()).show(2) 

df.select(monotonically_increasing_id()).show(2)
Add unique ID to reach Row by usingmonotonically_increasing_id function


Working with Strings
SQL
Python
Scala
Notes
 SELECT initcap(Description) FROM dfTable
from pyspark.sql.functions import initcap
df.select(initcap(col("Description"))).show()



df.select(initcap(col("Description"))).show(2, false)
initcap - capitalize every word in a given string when that word is separated from another by a space
SELECT Description, lower(Description), Ipper(lower(Description)) FROM dfTable
from pyspark.sql.functions import lower, upperdf.select(col("Description"),lower(col("Description")),upper(lower(col("Description")))).show(2)


cast string in uppercase / lowercase
SELECTltrim(lit('     HELLOOOOO     '),rtrim(lit('     HELLOOOOO     '), lpad(lit(' HELLOOOOO     '),2, ' ')FROM dfTable
from pyspark.sql.functions import lit, trim, ltrim, rtrim, lpad, rpaddf.select(ltrim(lit("     HELLOOOOO     ")).alias("ltrim"),rtrim(lit("     HELLOOOOO     ")).alias("rtrim"),trim(lit("     HELLOOOOO     ")).alias("trim"),lpad(lit("HELLOOOOO     "),2, " ").alias("lpad"),rpad(lit("HELLOOOOO"), 10, "").alias("rpad")).show(2) 

import.... df.select(ltrim(lit("     HELLOOOOO     ")).alias("ltrim"),rtrim(lit("     HELLOOOOO     ")).alias("rtrim"),trim(lit("     HELLOOOOO     ")).alias("trim"),lpad(lit("HELLOOOOO     "),2, " ").alias("lpad"),rpad(lit("HELLOOOOO"), 10, "").alias("rpad")).show(2)
Adding/removing spaces around a stringlpadltrimrpadrtrimtrim If lpad and rpad takes a number less than the length of the string it will always remove values from the right side of the string
regex_replace(Description, 'BLACK|WHITE|RED|BLUE', 'COLOR') as color)clean, DescriptionFROM dfTable
from pyspark.sql.functions import regexp_replace regex_string = "BLACK|WHITE|RED|BLUE"df.select(regexp_replace(col("Description"), regex_string, "COLOR").alias("color_clean"), col("Description")).show(2)


Regular Expressions-replacing all mentions of a string with another value-searching for the existence of one stringThis is done with a tool called regular expressions (regexes)used to extract values from a string or replace them with some other valuesregexo_extractregexp_replace 
SELECT translate(Description, 'LEET', '1337'), Description FROM dfTable
from pyspark.sql.functions import translatedf.select(translate(col("Description"), "LEET", "1337"), col("Description")).show(2) 

from pyspark.sql.functions import translatedf.select(translate(col("Description"), "LEET", "1337"), col("Description")).show(2)
Replacing given characters with other characterstranslate function
SELECT regexp_extract(Description, 'BLACK|WHITE|RED|BLUE)', 1),Description FROM dfTable
from pyspark.sql.functions import regexp_extractextract_str ="(BLACK|WHITE|RED|BLUE)"df.select(regexp_extract(col("Description"), extract_str, 1).alias("color_clean"),  col("Description")).show(2) 


pull out the first mentioned color
SELECT  Description FROM dfTableWHERE instr(Description, 'BLACK') >= OR instr(Description, 'WHITE') >= 1
from pyspark.sql.functions import instrcontainsBlack = instr(col("Description"), "BLACK") >=1containsWhite = instr(col("Description"), "WHITE") >=1df.withColumn("hasSimpleColor", containsBlack | containsWhite)\.where("hasSimpleColor")\.select("Description").show(3, False)


contains methodcheck for values existence - this will return a Booleaninstr

from pyspark.sql.functions import expr, locatesimpleColors = ["black", "white", "red", "green", "blue"]def color_locator(column, color_string):  return locate(color_string.upper(), column)\.cast("boolean")\.alias("is_" + c)selectedColumns = [color_locator(df.Description, c) for c in simpleColors]selectedColumns.append(expr("*"))df.select(*selectedColumns).where(expr("is_white OR is_red"))\.select("Description").show(3, False)

problem


Working with Dates and TimestampsDates - focus exclusively on calendar datestimestamps - both date and time information included TimeStampType class supports only second-level precision, which means that if you are going to be working with milliseconds or microseconds you will need to work around this problem by potentially operating on them as longs,Important to be explicit when parsing or converting to ensure that there are no issues in doing so.Conforms to java standards when working with dates and timestamps.
SQL
Python
Scala
Notes

from pyspark.sql.functions import current_date, current_timestampdateDF = spark.range(10)\.withColumn("today", current_date())\.withColumn("now", current_timestamp())dateDF.createOrReplaceTempView("dataTable")dateDF.printSchema()



SELECT date_sub(today, 5), date_add(today_5) FROM dateTable
from pyspark.sql.functions import date_add, date_subdateDF.select(date_sub(col("today"),5), date_add(col("today"), 5)).show(1)


Now subtract five days from today
SELECT to_date('2016-01-01'), months_between('2016-01-01', '2017-01-01'),datediff('2016-01-01', '2017-01-01')FROM dateTable
from pyspark.sql.functions import datediff, months_between, to_datedateDF.withColumn("week_ago", date_sub(col("today"),7))\.select(datediff(col("week_ago"), col("today"))).show(1)dateDF.select(to_date(lit("2016-01-01")).alias("start"), to_date(lit("2017-05-22")).alias("end"))\.select(months_between(col("start"), col("end"))).show(1)


Difference between two datesdatediff functionit will return the number of days in between two dates
to_date function - allows you to convert a string to a date, optionally with a specified format. 

from pyspark.sql.functions import to_date, litspark.range(5).withColumn("date", lit("2017-01-01"))\.select(to_date(col("date"))).show(1)


if Spark cannot parse the date it will return nulltricky situation for bugs because some data might match the correct format. 

dateDF.select(to_date(lit("2016-20-12")), to_date(lit("2017-12-11"))).show(1) 
 

Notice that this date appears as Dec 11 instead of the correct day Nov 12. Spark doesn't throw an error because it cannot know whether the days are mixed up or that specific row is incorrect.
Let's fix this pipeline! --->
SELECT to_date(date, 'yyyy-dd-MM'), to_date(date2, 'yyyy-dd-MM'), to_date(date) FROM dataTable2
from pyspark.sql.functions import to_datedateFormat = "yyyy-dd-MM"cleanDateDF = spark.range(1).select(to_date(lit("2017-12-11"), dateFormat).alias("date"),  to_date(lit("2017-20-12"), dateFormat).alias("date2"))cleanDateDF.createOrReplaceTempView("dateTable2")

--->The first step is to remember that we need to specify our date format according to the Java SimpleDateFormat standard.We use two functions:to_dateto_timestampthe former optionally expects a format whereas the latter requires one.
SELECT to)timestamp(date, 'yyyy-dd-MM'), to_timestamp(date2, 'yyyy-dd-MM') FROM dateTable2
from pyspark.sql.functions import to_timestampcleanDateDF.select(to_timestamp(col("date"), dateFormat)).show()


to_timestamp

cleanDateDF.filter(col("date2") > "'2017-12-12'").show()


after we have our date or timestamp into the correct format and type comparing between them is easy. We just need to make sure that either use a date/timestamp type or specify our string according to the right format of yyyy-MM-dd if we are comparing a date


Working with Nulls in Datayou should always use null to represent missing or empty data in your DataFrames. Spark can optimize working with null values more than it can if you use empty strings or other values.use the .nasubpackage on a DataFrame  Fundamental concepts:Spark is a distributed programming model in which the user specifies transformations. These transformations build up a directed acyclic graph of transformations and action. An action begins the process of execution that graph of instructions, as a single job, by breaking it down into stages and tasks to execute across the cluster. The logical structures that we manipulate with transformations and actions are DataFrames and Datasets. To create a new DataFrame or Dataset, you call a transformation. To start computation or convert to native language types, you call an action. Structured API OverviewStructured APIs are a tool for manipulating all sorts of data, from unstructured log files to semi-structured CSV files and highly structured Parquet (Apache Parquet is a columnar storage format available to any project in the Hadoop ecosystem, regardless of the choice of data processing framework, data model or programming language) files. These APIs refer to three core types of distributed collection APIs:
Datasets
DataFrames
SQL Tables and Views
Majority of the Structured APIs apply to both batch and streaming computation. This means that when you work with the Structured APIs, it should be simple to migrate from batch to streaming or vice versa with little to no effort.  Structured APIs are the fundamental abstraction used to write the majority of data flows.  DataFrames and DatasetsDataFrames and Datasets are distributed table-like collection with well-defined rows and columns. Each column must have the same number of rows as all the other columns although you can use null to specify the absence of a value and each column has type information that must be consistent for every row in the collection. To Spark, DataFrames and Datasets represent immutable, lazily evaluated plans(transformations) that specify what operations to apply to data residing at a location to generate some output. When we perform an action on a DataFrame, we instruct Spark to perform the actual transformations and return the results. These represent plans of how to manipulate rows and columns to compute the user's desired result.  Tables and views - like a DataFrame, but we execute SQL against them instead of DataFrame code.  Schema - defines the column names and types of a DataFrame. You can define schemas manually or read a schema from a data source. Schemas consist of types meaning that you need a way of specifying what lies where. Overview of Structured Spark TypesSpark is effectively a programming language of its own. Spark uses an engine called Catalyst. Catalyst - maintains its own type information through the planning and processing of work. This opens up execution optimizations.Even if we use Spark's Structured APIs from Python or R, the majority of our manipulations will operate strictly on Spark types not Python types.  
 This addition operation happens because Spark will convert an expression written in an input language to Spark's internal Catalyst representation of that same type information. It then will operate on that internal representation.  DataFrames VS Datasets
STRUCTURED APIs

DataFrames
Datasets
untyped(Spark maintains them completely)
typed(checks whether types conform to the specification at compile time.)Only available to JVM based languages Scala and Java.
DataFrames are Datasets of Type Row. The "Row" type is Spark's internal representation of its optimized in-memory format for computation. To Spark in Python and R there is no such thing as a Dataset, everything is a DataFrame and therefore we always operate on that optimized format. //WATCH! - Spark Catalyst Engine talks by Josh Rosen and Herman van Hovell
KEY Takeaway: When you use DataFrames, you are taking advantage of Spark's optimized internal format.
Columns: represent a simple type like an integer or string or complex type like an array or map or null values. Rows: record of data. 

Spark Types(Spark documentation - get updated time to time)
Overview of Structured API Execution
Write DataFrame/Dataset/SQL Code
If valid code, converts this to a Logical Plan
Spark . transforms this Logical Plan, checking for optimizations along the way
Spark then executes this Physical Plan (RDD Manipulations) on the cluster

The code we write gets submitted to Spark either through console or via a submitted job. This code passes through the Catalyst Optimizer, which decides how the code should be executed and lays out a plan for doing so before, finally, the code is run and the result is returned to the user.

Logical Planning
Physical Planning 
The first phase takes user code and converts it into a logical plan (optimized version of the user's set of expressions)It does this by converting user code into an unresolved logical plan. The plan is unresolved because although your code might be valid, the tables and columns that it refers to might or might not exist. Spark uses the catalog, a repository of all table and DataFrame information to resolve columns and tables in the analyzer. The analyzer might reject the unresolved logical plan if the required column name does not exist in the catalog. If the analyzer can resolve it, the result is passed through the Catalyst Optimizer, a collection of rules that attempt to optimize the logical plan by pushing down predicates or selections. Packages can extend the Catalyst to include their own rules for domain-specific optimizations.

After creating the optimized logical plan, Spark begins the physical planning process. The physical plan - often called SPark plan - specifies how the logical plan will execute on the cluster by generating different physical execution strategies and comparing them through a cost model. Upon selecting a physical plan Spark runs all of this code over RDDs.


Basic Structured OperationsDataFrame consists of a series of records that are of type Row and a number of columns that represent a computation expression that can perform on each individual record in the Dataset. Schemas define the name as well as the type of data in each column. Partitioning of the DataFrame defines the layout of the DataFrame or Dataset's physical distribution across the cluster. The partitioning scheme defines how that is allocated.
Creating a DataFrame:
Python
Scala
df = spark.read.format("json").load("/Users/mikepetridisz/Desktop/json/2015-summary.json")
val df = spark.read.format("json").load("/Users/mikepetridisz/Desktop/json/2015-summary.json")
printSchemadf.printSchema() # A schema is a StructType made up of a number of fields, StructFields, that have a name, type, a boolean flag (null values/missing values), metadata (metadata used in Machine Learning)
printSchemadf.printSchema()
<br><br><br><br><br><br><br><br><br>
 myManualScheme = StructType([
... StructField("DEST_COUNTRY_NAME", StringType(), True),
... StructField("ORIGIN_COUNTRY_NAME", StringType(), True),
... StructField("count", LongType(), False, metadata={"hello":"world"})
... ])
>>> df = spark.read.format("json").schema(myManualScheme)\
... .load("/Users/mikepetridisz/Desktop/json/2015-summary.json")

Columns and ExpressionsExpressions - when you select, remove manipulate columns from DataFrames
Creating a Column
Python
Scala
NOTE
from pyspark.sql.functions import cal, columncol("someColumnName")column("someColumnName")
import org.apache.spark.sql.functions.{col, column}col("someColumnName")column("someColumnName")--other way:scala> $"myColumn"scala>'myColumn
col()  or column function

Explicit Column References if you need to refer to a specific DataFrame's column, you can use the col method on the specific DataFrame. This can be useful when performing a join and need to refer to a specific column in one DataFrame that might share the same name with another column in the joined DataFrame. ExpressionsColumns are expressions. An expression is a set of transformations on one or more values in a record in a DataFrame. An expression created via the expr function is just a DataFrame column reference.expr("someCol") is equivalent to col("someCol") Columns as ExpressionsWhen using an expression, the expr function can actually parse transformations and column references from a string and can subsequently be passed into further transformations.Key takeaways:
Columns are just expressions
Columns and transformations of those columns compile to the same logical plan as parsed expressions.
Example:DataFrame Code
SQL code
#You can write expressions as DataFrame code or SQL code and get the exact same performance characteristics.
Accessing a DataFrame's ColumnsprintSchema or:spark.read.format("json").load("/Users/mikepetridisz/Desktop/json/2015-summary.json").columns Records and RowsEach row in a DataFrame is a singlerecord as an object type Row. Spark manipulates Row objects using column expressions in order to produce usable values. 

Creating Rows
Python
Scala
Note
from pyspark.sql import RowmyRow = Row("Hello", None, 1, False)

import org.apache.spark.sql.Rowval myRow = Row("Hello", null, 1, false)
Creating RowsImporting RowsAccessing data in rows 
DataFrame Transformations
We can add rows or columns
We can remove rows and columns
We can transform a row into a column or vice versa
We can change the order of rows based on the values in columns
 Creating DataFrames on the fly
Python
Scala
from pyspark.sql import Rowfrom pyspark.sql.types import StructField, StructType, StringType, LongType myManualSchema = StructType([StructField("some", StringType(), True),StructField("col", StringType(), True),StructField("names", LongType(), False)])myRow = ("hello", None, 1)myDf = spark.createDataFrame([myRow], myManualSchema)myDf.show()
  
import org.apache.spark.sql.Rowimport org.apache.spark.sql.types.{ StructField, StructType, StringType, LongType} val myManualSchema = new StructType(Array(new StructField("some", StringType, true),new StructField("col", StringType, true),new StructField("names", LongType, false)))val myRow = Seq(Row("hello", None, 1L))val myRDD = spark.sparkContext.parallelize(myRows)val myDf = spark.createDataFrame(myRDD, myManualSchema)myDf.show()val myDf = Seq(("Hello", 2, 1L)).toDF("col1","col2", "col3")myDf.show()
Select and SelectExpr
allows you to do the DataFrame equivalent of SQL queries on a table of data
SQL
Python
Scala
Note
SELECT DEST_COUNTRY_NAME FROM dfTable LIMIT 2
df.select("DEST_COUNTRY_NAME").show(2)

df.select("DEST_COUNTRY_NAME").show(2)
Use the select method and pass in the column names as strings with  which you would like to work
SELECT DEST_COUNTRY_NAME, ORIGIN_COUNTRY_NAME FROM dfTable LIMIT 2
df.select("DEST_COUNTRY_NAME", "ORIGIN_COUNTRY_NAME").show(2)

df.select("DEST_COUNTRY_NAME", "ORIGIN_COUNTRY_NAME").show(2)
you can select multiple columns

you can refer to columns in a number of different waysdf.select(expr("DEST_COUNTRY_NAME"),col("DEST_COUNTRY_NAME"),column("DEST_COUNTRY_NAME"))\.show(2)



AS and alias - change the name using the AS and alias keywords
SQL
Python
Scala
Note
SELECT DEST_COUNTRY_NAME as destination FROM dfTable LIMIT 2
df.select(expr("DEST_COUNTRY_NAME AS destination").alias("DEST_COUNTRY_NAME")).show(2)

df.select("DEST_COUNTRY_NAME").show(2)
change the name of the columnAS

df.select(expr("DEST_COUNTRY_NAME AS destination").alias("DEST_COUNTRY_NAME")).show(2))

df.select(expr("DEST_COUNTRY_NAME AS destination").alias("DEST_COUNTRY_NAME")).show(2)
aliaschange the column name back to its original name
SELECT *, (DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as withinCountryFROM dfTableLIMIT 2
df.selectExpr("*","(DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as withinCountry")\.show(2)

df.selectExpr("*","(DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as withinCountry").show(2)
add a new column withinCountry to DataFrame that specifies whether the destination and origin are the same
SELECT act(count), count(distinct(DEST_COUNTRY_NAME)) FROM dfTable LIMIT 2
df.selectExpr("avg(count)", "count(distinct(DEST_COUNTRY_NAME))").show(2)


df.selectExpr("avg(count)", "count(distinct(DEST_COUNTRY_NAME))").show(2)
Aggregations


Converting to Spark TypesSometimes we need to pass explicit values into Spark that aren't a new column but are just a value.The was we do this is through literals. This is a translation from a given programming language's literal value to one that Spark understands. Literals are expressions.
SQL
Python
Scala
Note
SELECT *, 1 as One FROM dfTable LIMIT2
from pyspark.sql.functions import litdf.select(expr("*"),lit(1).alias("One")).show(2)

import org.apache.spark.sql.functions.litdf.select(expr("*"),lit(1).as("One")).show(2)


Adding Columns
SQL
Python
Scala
Note
SELECT *, 1 as numberOne FROM dfTable LIMIT2
df.withColumn("numberOne", lit(1)).show(2)

df.withColumn("numberOne", lit(1)).show(2)
formal way of adding a column

df.withColumn("withinCountry", expr("ORIGIN_COUNTRY_NAME == DEST_COUNTRY_NAME"))\.show(2)

df.withColumn("withinCOuntry", expr("ORIGIN_COUNTRY_NAME == DEST_COUNTRY_NAME"))\.show(2)
Boolean expression for when the original country is the same as the Destination Country
 

df.withColumn("Destination", expr("DEST_COUNTRY_NAME").columns

NOTICE that withColumn function takes two arguments; the column name and the expression that will create the value for that given row in the DataFrame. We can also rename a column this way. (SQL syntax is the same as previously so it is not here now.
Renaming ColumnswithColumnRenamed method
SQL
Python
Scala
Note

df.withColumnRenamed("DEST_COUNTRY_NAME", "dest").columns

df.withColumnRenamed("DEST_COUNTRY_NAME", "dest").columns
rename columnsname of the string = first argumentstring = second argument
Reserved Characters and Keywordslike spaces or dashes in column names. Handling these means escaping column names appropriately. We do this by using backtick ("`")
SQL
Python
Scala
Note

dfWithLongColName = df.withColumn("This Long Column-Name",expr("ORIGIN)COUNTRY_NAME")
import org.apache.spark.sql.functions.exprval dfWithLongColName = df.withColumn("this Long Column-Name",expr("ORIGIN_COUNTRY_NAME"))
Could not run this nor understand this part! - Need to come back & Check!

dfWithLongColName.selectExpr(" This Long Column-Name "," This Long Column-Name as `new col`")\.show(2)


set spark.sql.caseSensitive true


Case Sensitivity 

df.drop("ORIGIN_COUNTRY_NAME").columns

Removing Columns

dfWithLongColName.drop("ORIGIN_COUNTRY_NAME", "DEST_COUNTRY_NAME")

Removing multiple columns
SELECT *, cast(count as long) AS count2 FROM dfTable
df.withColumn("count2", col("count").cast("long"))



Change Column's Type (cast)
SELECT * FROM dfTable WHERE count < 2 LIMIT 2
df.filter(col("count") < 2).show(2)



Filtering Rows - evaluates to true or false. You can use where or filter an they both will perform the same operation.
SELECT * FROM dfTable WHERE count < 2 AND ORIGIN_COUNTRY_NAME != "Croatia LIMIT 2
df.where(col("count") < 2).where(col("ORIGIN_COUNTRY_NAME") != "Croatia")\.show(2)


df.where(col("count") < 2).where(col("ORIGIN_COUNTRY_NAME") != "Croatia").show(2)
Multiple filters you can put multiple filters into the same expression. It's not always useful because Spark automatically performs all filtering operations at the same time regardless of the filter ordering. This optimization is called PIPELINING. This means that if you want to specify multiple AND filters, just chain them sequentially and let Spark handle the rest.
SELECT COUNT(DISTINCT(ORIGIN_COUNTRY_NAME,  DEST_COUNTRY_NAME) FROM dfTable
df.select("ORIGIN_COUNTRY_NAME", "DEST_COUNTRY_NAME").distinct().count()



df.select("ORIGIN_COUNTRY_NAME", "DEST_COUNTRY_NAME").distinct().count()
Getting unique Rowsextract unique or distinct values. These values van be in one or more columns. distinct method allws us to duplicate any rows that are in the DataFrame. 

seed = 5withReplacement = Falsefraction = 0.5df.sample(withReplacement, fraction, seed).count()

val seed = 5val withReplacement = Falseval fraction = 0.5df.sample(withReplacement, fraction, seed).count()
sample method - sample some random records from your DataFrame.

dataFrames = df.randomSplit([0.25, 0.75], seed)dataFrames[0].count() > dataFrames[1].count()

val dataFrames = df.randomSplit(Array(0.25, 0.75), seed)dataFrames(0).count() > dataFrames(1).count()
Random Splits can be useful when you need to break up your DataFrame.  It cannot guarantee that all records are in one of the DataFrames from which you are sampling. This is often used with machine learning.

from pyspark.sql import Rowschema = df.schemanewRows = [Row("New Country", "Other Country", 5),Row("New Country 2", "Other Country 3", 1),]parallelizeRows = spark.sparkContext.parallelize(newRows)newDF = spark.createDataFrame(parallelizeRows, schema) df.union(newDF)\.where("count =1")\.where(col("ORIGIN_COUNTRY_NAME") != "United States")\.show() 
 

Concentrating and Appending Rows (Union)

df.sort("count").show(5)df.orderBy("count", "DEST_COUNTRY_NAME").show(5)df.orderBy(col("count"), col("DEST_COUNTRY_NAME")).show(5)

df.sort("count").show(5)df.orderBy("count", "DEST_COUNTRY_NAME").show(5)df.orderBy(col("count"), col("DEST_COUNTRY_NAME")).show(5)
Sorting Rows sort and orderBy do the samethe default is sort in ascending order

to more explicitly specify sort direction, you need to use asc and desc functions if operating on a column. 

from pyspark.sql.functions import asc, descdf.orderBy(expr("count desc")).show(2)df.orderBy(col("count").desc(),  col("DEST_COUNTRY_NAME").asc()).show(2)


(sort)to more explicitly specify sort direction, you need to use asc and desc functions if operating on a column. 
Advanced tip is to use asc_nulls_first, desc_nulls_first, asc_nulls_last, or _desc_nulls_last
SELECT * FROM dfTable LIMIT 6
df.limit(5).show()
df.limit(5).show()
LimitRestrict what you extract from the dataframe
SELECT * FROM dfTable ORDER BY count desc LIMIT 6
df.orderBy(expr("count")).asc().limit(6).show()
df.orderBy(expr("count")).asc().limit(6).show()


df.rdd.getNumPartitions()df.repartition(5)

Repartition based on a columns name df.repartition(5, col("DEST_COUNTRY_NAME"))
df.rdd.getNumPartitions()df.repartition(5)
Repartition partition the data according to some frequently filtered columns, which control the physical layout of data across the cluster including the partitioning scheme and the number of partitions. 
Repartition will incur a full shuffle of the data, regardless of whether one is necessary. This means that you should typically only repartition when the future number of partitions os greater than your current number of partitions or when you are looking to partition by a set of columns. 

df.repartition(5, col("DEST_COUNTRY_NAME")).coalesce(2)
df.repartition(5, col("DEST_COUNTRY_NAME")).coalesce(2)
Coalescewill not incur a full shuffle and will try to combine partitions. This operation will shuffle your data into five partitions based on the destination country name and then coalesce them without a full shuffle.

collectDF=df.limit(10)collectDF.take(5) #works with an integer countcollectDF.show() #this prints it out nicelycollectDF.show(5, False)collectDF.collect()

val collectDF=df.limit(10)collectDF.take(5)collectDF.show()collectDF.show(5, False)collectDF.collect()
Collecting Rows to the DriverSpark maintains the state of the cluster in the driver. There are times when you want to collect some of the data to the driver in order to manipulate it on your local machine.
collect gets all the data from the entire Dataframetake selects the first N rows show prints out a number of rows nicely.

collectDF.toLocalIterator()

Iterate over the entire dataset. The method is called toLocalIterator that collects partitions to the driver as an iterator. Iterates over the entire dataset partition by partition in a serial manner


Working with Different Types of DataObjectives
Booleans
Numbers
Strings
Dates and Timestamps
Handling Null
Complex Types
User Defined Functions
 Where to look for APIs?DataFrame (Dataset) Methods: DataFrame is just a Dataset of Row types, so you will look at the Dataset methods available at: http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.DatasetDataFrameStatFunctions: http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.DataFrameStatFunctionsDataFrameNaFunctions http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.DataFrameNaFunctionsColumn methods: http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.ColumnFunctions: http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.functions$Dataset: http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Dataset
DataFrame used here => by-day/2010.12.01.csv
SQL
Python
Scala
Notes

>>> df = spark.read.format("csv")\
... .option("header", "true")\
... .option("inferSchema", "true")\
... .load("/Users/mikepetridisz/Desktop/retail-data/by-day/2010-12-01.csv")
>>> df.printSchema()
>>> df.createOrReplaceTempView("dfTable")
 




Load data
no equivalent function necessary in SQL
from pyspark.sql.functions import litdf.select(lit(5), lit("five"), lit(5.0))

import org.apache.spark.sql.functions.litdf.select(lit(5), lit("five"), lit(5.0))
convert to spart typesconvert native types to spark types.
We do this by using the lit function

from pyspark.sql.functions import coldf.where(col("InvoiceNo") != 536365)\.select("InvoiceNo", "Description")\.show(5, False)
  ORdf.where("InvoiceNo == 536365")\.show(5, false)
df.where(col("InvoiceNo") === 536365).select("InvoiceNo", "Description").show(5, False)
Working with BooleansBoolean statements consist of four elements: and, or, true, false
SELECT * FROM dfTable WHERE StockCode in ("DOT") AND (UnitPrice >600 OR instr(Description, "POSTAGE") >= 1
from pyspark.sql.functions import instrpriceFilter = col("UnitPrice") > 600descripFilter = instr(df.Description, "POSTAGE") >= 1df.where(df.StockCode.isin("DOT")).where(priceFilter | descripFilter).show()


val priceFilter = col("UnitPrice") > 600val descripFilter = col("Description").contains( "POSTAGE")df.where(df.StockCode.isin("DOT")).where(priceFilter | descripFilter).show() 

SELECT UnitPrice, (StockCode = 'DOT' AND(UnitPrice > 600 OR instr(Description, "POSTAGE") >= 1)) as isExpensiveFROM dfTableWHERE (StockCode = 'DOT' AND(UnitPrice > 600 OR instr(Description, "POSTAGE") >= 1))
from pyspark.sql.functions import instrDOTCodeFilter = col("StockCode") == "DOT"priceFilter = col("UnitPrice") > 600descripFilter = instr(col("Description"), "POSTAGE") >= 1df.withColumn("isExpensive", DOTCodeFilter & (priceFilter | descripFilter))\.where("isExpensive")\.select("unitPrice", "isExpensive").show(5)


To specify a DataFrame, you can also just specify a Boolean column

df.where(col("Description").eqNullSafe("hello")).show()

df.where(col("Description").eqNullSafe("hello")).show()
Null safe equivalence test:df.where(col("Description").eqNullSafe("hello")).show()
if there is a null in the data, we need to treat things differently. the above example shows how we can tackle it.

Working with Numbersafter filtering the most common thing in big data is counting things. 
SQL
Python
Scala
Note
SELECT customerId, (POWER((Quantity * UnitPrice), 2.0) +5) as realQuantity FROM dfTable
from pyspark.sql.functions import pow, exprfabricatedQuantity = pow(col("Quantity") * col("UnitPrice"), 2) +5df.select(expr("CustomerId"), fabricatedQuantity.alias("realQuantity")).show(2)

val fabricatedQuantity = pow(col("Quantity") * col("UnitPrice"), 2) +5df.select(expr("CustomerId"), fabricatedQuantity.alias("realQuantity")).show(2)
Let's imagine that we found out that we misrecorded the quantity in our retail dataset and the true quantity is equal to the ((current quantity * the unit price)^2 +5) pow function (raises a column to the expressed power
SELECT round (2.5), bround(2.5)
from pyspark.sql.functions import lit, round, brounddf.select(round(lit("2.5")), bround(lit("2.5"))).show(2)

import org.apache.spark.functions.litdf.select(round(lit("2.5")), bround(lit("2.5"))).show(2)

Roundingexample round to 1 decimal places
SELECT corr(Quantity, UnitPrice) FROM dfTable
from pyspark.sql.functions import corrdf.stat.corr("Quantity", "UnitPrice")df.select(corr("Quantity", "UnitPrice")).show()

import org.apache.spark.functions.{corr}df.stat.corr("Quantity", "UnitPrice")df.select(corr("Quantity", "UnitPrice")).show()
Compute the correlation of two columns. e.g to see if cheaper things are typically bought in greater quantities. 


df.describe().show()

df.describe().show()
Summary Statistics for a column or a set of columns. 
describe method. This takes all numeric columns and calculate the count, mean, standard deviation, min, max.You should use this for viewing the console because the schema might change in the future.

from pyspark.sql.functions import count, mean, stddev_pop, min, max


if you need exact numbers you can also perform this aggregation yourself by importing the functions and applying them to the columns that you need.
These are the statistical functions available in the StatFunctions Package. 

colName = "UnitPrice"quantileProbs = [0.5]relError = 0.05df.stat.approxQuantile("UnitPrice", quantileProbs, relError)


val colName = "UnitPrice"val quantileProbs = [0.5]val relError = 0.05df.stat.approxQuantile("UnitPrice", quantileProbs, relError)
You can calculate exact or approximate quantiles of your data using the approxQuantile method.

df.stat.crosstab("StockCode", "Quantity").show()
 df.stat.freqItems(["StockCode", "Quantity"]).show()

df.stat.crosstab("StockCode", "Quantity").show()
















 df.stat.freqItems(["StockCode", "Quantity"]).show()
cross-tabulation or frequent item pairs this output will be large!!!!!

from pyspark.sql.functions import monotonically_increasing_iddf.select(monotonically_increasing_id()).show(2) 

df.select(monotonically_increasing_id()).show(2)
Add unique ID to reach Row by usingmonotonically_increasing_id function


Working with Strings
SQL
Python
Scala
Notes
 SELECT initcap(Description) FROM dfTable
from pyspark.sql.functions import initcap
df.select(initcap(col("Description"))).show()



df.select(initcap(col("Description"))).show(2, false)
initcap - capitalize every word in a given string when that word is separated from another by a space
SELECT Description, lower(Description), Ipper(lower(Description)) FROM dfTable
from pyspark.sql.functions import lower, upperdf.select(col("Description"),lower(col("Description")),upper(lower(col("Description")))).show(2)


cast string in uppercase / lowercase
SELECTltrim(lit('     HELLOOOOO     '),rtrim(lit('     HELLOOOOO     '), lpad(lit(' HELLOOOOO     '),2, ' ')FROM dfTable
from pyspark.sql.functions import lit, trim, ltrim, rtrim, lpad, rpaddf.select(ltrim(lit("     HELLOOOOO     ")).alias("ltrim"),rtrim(lit("     HELLOOOOO     ")).alias("rtrim"),trim(lit("     HELLOOOOO     ")).alias("trim"),lpad(lit("HELLOOOOO     "),2, " ").alias("lpad"),rpad(lit("HELLOOOOO"), 10, "").alias("rpad")).show(2) 

import.... df.select(ltrim(lit("     HELLOOOOO     ")).alias("ltrim"),rtrim(lit("     HELLOOOOO     ")).alias("rtrim"),trim(lit("     HELLOOOOO     ")).alias("trim"),lpad(lit("HELLOOOOO     "),2, " ").alias("lpad"),rpad(lit("HELLOOOOO"), 10, "").alias("rpad")).show(2)
Adding/removing spaces around a stringlpadltrimrpadrtrimtrim If lpad and rpad takes a number less than the length of the string it will always remove values from the right side of the string
regex_replace(Description, 'BLACK|WHITE|RED|BLUE', 'COLOR') as color)clean, DescriptionFROM dfTable
from pyspark.sql.functions import regexp_replace regex_string = "BLACK|WHITE|RED|BLUE"df.select(regexp_replace(col("Description"), regex_string, "COLOR").alias("color_clean"), col("Description")).show(2)


Regular Expressions-replacing all mentions of a string with another value-searching for the existence of one stringThis is done with a tool called regular expressions (regexes)used to extract values from a string or replace them with some other valuesregexo_extractregexp_replace 
SELECT translate(Description, 'LEET', '1337'), Description FROM dfTable
from pyspark.sql.functions import translatedf.select(translate(col("Description"), "LEET", "1337"), col("Description")).show(2) 

from pyspark.sql.functions import translatedf.select(translate(col("Description"), "LEET", "1337"), col("Description")).show(2)
Replacing given characters with other characterstranslate function
SELECT regexp_extract(Description, 'BLACK|WHITE|RED|BLUE)', 1),Description FROM dfTable
from pyspark.sql.functions import regexp_extractextract_str ="(BLACK|WHITE|RED|BLUE)"df.select(regexp_extract(col("Description"), extract_str, 1).alias("color_clean"),  col("Description")).show(2) 


pull out the first mentioned color
SELECT  Description FROM dfTableWHERE instr(Description, 'BLACK') >= OR instr(Description, 'WHITE') >= 1
from pyspark.sql.functions import instrcontainsBlack = instr(col("Description"), "BLACK") >=1containsWhite = instr(col("Description"), "WHITE") >=1df.withColumn("hasSimpleColor", containsBlack | containsWhite)\.where("hasSimpleColor")\.select("Description").show(3, False)


contains methodcheck for values existence - this will return a Booleaninstr

from pyspark.sql.functions import expr, locatesimpleColors = ["black", "white", "red", "green", "blue"]def color_locator(column, color_string):  return locate(color_string.upper(), column)\.cast("boolean")\.alias("is_" + c)selectedColumns = [color_locator(df.Description, c) for c in simpleColors]selectedColumns.append(expr("*"))df.select(*selectedColumns).where(expr("is_white OR is_red"))\.select("Description").show(3, False)

problem


Working with Dates and TimestampsDates - focus exclusively on calendar datestimestamps - both date and time information included TimeStampType class supports only second-level precision, which means that if you are going to be working with milliseconds or microseconds you will need to work around this problem by potentially operating on them as longs,Important to be explicit when parsing or converting to ensure that there are no issues in doing so.Conforms to java standards when working with dates and timestamps.
SQL
Python
Scala
Notes

from pyspark.sql.functions import current_date, current_timestampdateDF = spark.range(10)\.withColumn("today", current_date())\.withColumn("now", current_timestamp())dateDF.createOrReplaceTempView("dataTable")dateDF.printSchema()



SELECT date_sub(today, 5), date_add(today_5) FROM dateTable
from pyspark.sql.functions import date_add, date_subdateDF.select(date_sub(col("today"),5), date_add(col("today"), 5)).show(1)


Now subtract five days from today
SELECT to_date('2016-01-01'), months_between('2016-01-01', '2017-01-01'),datediff('2016-01-01', '2017-01-01')FROM dateTable
from pyspark.sql.functions import datediff, months_between, to_datedateDF.withColumn("week_ago", date_sub(col("today"),7))\.select(datediff(col("week_ago"), col("today"))).show(1)dateDF.select(to_date(lit("2016-01-01")).alias("start"), to_date(lit("2017-05-22")).alias("end"))\.select(months_between(col("start"), col("end"))).show(1)


Difference between two datesdatediff functionit will return the number of days in between two dates
to_date function - allows you to convert a string to a date, optionally with a specified format. 

from pyspark.sql.functions import to_date, litspark.range(5).withColumn("date", lit("2017-01-01"))\.select(to_date(col("date"))).show(1)


if Spark cannot parse the date it will return nulltricky situation for bugs because some data might match the correct format. 

dateDF.select(to_date(lit("2016-20-12")), to_date(lit("2017-12-11"))).show(1) 
 

Notice that this date appears as Dec 11 instead of the correct day Nov 12. Spark doesn't throw an error because it cannot know whether the days are mixed up or that specific row is incorrect.
Let's fix this pipeline! --->
SELECT to_date(date, 'yyyy-dd-MM'), to_date(date2, 'yyyy-dd-MM'), to_date(date) FROM dataTable2
from pyspark.sql.functions import to_datedateFormat = "yyyy-dd-MM"cleanDateDF = spark.range(1).select(to_date(lit("2017-12-11"), dateFormat).alias("date"),  to_date(lit("2017-20-12"), dateFormat).alias("date2"))cleanDateDF.createOrReplaceTempView("dateTable2")

--->The first step is to remember that we need to specify our date format according to the Java SimpleDateFormat standard.We use two functions:to_dateto_timestampthe former optionally expects a format whereas the latter requires one.
SELECT to)timestamp(date, 'yyyy-dd-MM'), to_timestamp(date2, 'yyyy-dd-MM') FROM dateTable2
from pyspark.sql.functions import to_timestampcleanDateDF.select(to_timestamp(col("date"), dateFormat)).show()


to_timestamp

cleanDateDF.filter(col("date2") > "'2017-12-12'").show()


after we have our date or timestamp into the correct format and type comparing between them is easy. We just need to make sure that either use a date/timestamp type or specify our string according to the right format of yyyy-MM-dd if we are comparing a date


Working with Nulls in Datayou should always use null to represent missing or empty data in your DataFrames. Spark can optimize working with null values more than it can if you use empty strings or other values.use the .nasubpackage on a DataFrame                      
