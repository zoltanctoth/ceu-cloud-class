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

## The Spark DataFrame and SQL API

### Fundamental concepts:
Spark is a distributed programming model in which the user specifies transformations. These transformations build up a directed acyclic graph (DAG) of transformations and action. An action begins the process of execution that graph of instructions, as a single job, by breaking it down into stages and tasks to execute across the cluster. The logical structures that we manipulate with transformations and actions are DataFrames and Datasets. To create a new DataFrame or Dataset, you call a transformation. To start computation or convert to native language types, you call an action.

### Structured API Overview
Structured APIs are a tool for manipulating all sorts of data, from unstructured log files to semi-structured CSV files and highly structured Parquet (Apache Parquet is a columnar storage format available to any project in the Hadoop ecosystem, regardless of the choice of data processing framework, data model or programming language) files. These APIs refer to three core types of distributed collection APIs:
- Datasets
- DataFrames
- SQL Tables and Views

Majority of the Structured APIs apply to both batch and streaming computation. This means that when you work with the Structured APIs, it should be simple to migrate from batch to streaming or vice versa with little to no effort. Structured APIs are the fundamental abstraction used to write the majority of data flows. 

#### DataFrames and Datasets
DataFrames and Datasets are distributed table-like collection with well-defined rows and columns. Each column must have the same number of rows as all the other columns although you can use null to specify the absence of a value and each column has type information that must be consistent for every row in the collection. To Spark, DataFrames and Datasets represent immutable, lazily evaluated plans(transformations) that specify what operations to apply to data residing at a location to generate some output. When we perform an action on a DataFrame, we instruct Spark to perform the actual transformations and return the results. These represent plans of how to manipulate rows and columns to compute the user's desired result. 

**Schema:** defines the column names and types of a DataFrame. You can define schemas manually or read a schema from a data source. Schemas consist of types meaning that you need a way of specifying what lies where.


Spark is effectively a programming language of its own. Spark uses an engine called Catalyst:
**Catalyst:** maintains its own type information through the planning and processing of work. This opens up execution optimizations. 

#### Structured APIs


|DataFrame| DataSet |
|--|--|
| untyped (Spark maintains them completely)  | typed (checks whether types conform to the specification at compile time.) Only available to JVM based languages Scala and Java. |


DataFrames are Datasets of **Type Row.** The "Row" type is Spark's internal representation of its optimized in-memory format for computation. To Spark in Python and R there is no such thing as a Dataset, everything is a DataFrame and therefore we always operate on that optimized format.

#### Overview of Structured API Execution
- Write DataFrame/Dataset/SQL Code
- If valid code, Spark converts this to a Logical Plan
- Spark transforms this Logical Plan, checking for optimizations along the way
- Spark then executes this Physical Plan on the cluster

#### Logical Planning
The first phase takes user code and converts it into a logical plan (optimized version of the user's set of expressions)
It does this by converting user code into an unresolved logical plan. The plan is unresolved because although your code might be valid, the tables and columns that it refers to might or might not exist. Spark uses the catalog, a repository of all table and DataFrame information to resolve columns and tables in the analyzer. The analyzer might reject the unresolved logical plan if the required column name does not exist in the catalog. If the analyzer can resolve it, the result is passed through the Catalyst Optimizer, a collection of rules that attempt to optimize the logical plan by pushing down predicates or selections. Packages can extend the Catalyst to include their own rules for domain-specific optimizations.

#### Physical Planning
After creating the optimized logical plan, Spark begins the physical planning process. The physical plan - often called Spark plan - specifies how the logical plan will execute on the cluster by generating different physical execution strategies and comparing them through a cost model. (Upon selecting a physical plan Spark runs all of this code over RDDs.)

#### Basic Structured Operations
DataFrame consists of a series of records that are of type Row and a number of columns that represent a computation expression that can perform on each individual record in the Dataset. Schemas define the name as well as the type of data in each column. Partitioning of the DataFrame defines the layout of the DataFrame or Dataset's physical distribution across the cluster. The partitioning scheme defines how that is allocated.

#### DataFrame

**Create DataFrame:**
```
df = spark.read.format("json/csv/..").load("Some/path")
```
**Print Schema:**
```
printSchema
df.printSchema()
```

#### Columns and Expressions
- Expressions - when you select, remove manipulate columns from DataFrames

**Create Column:**
```
from pyspark.sql.functions import col, column
col("someColumnName")
column("someColumnName")
```

*Explicit Column References*
- If you need to refer to a specific DataFrame's column, you can use the col method on the specific DataFrame. This can be useful when performing a join and need to refer to a specific column in one DataFrame that might share the same name with another column in the joined DataFrame.

*Expressions*
- Columns are expressions. An expression is a set of transformations on one or more values in a record in a DataFrame. 
An expression created via the expr function is just a DataFrame column reference.
expr("someCol") is equivalent to col("someCol")

*Columns as Expressions*
- When using an expression, the `expr()` can actually parse transformations and column references from a string and can subsequently be passed into further transformations.

**Key takeaways:**
- Columns are just expressions
- Columns and transformations of those columns compile to the same logical plan as parsed expressions.

#### Records and Rows
- Each row in a DataFrame is a single  record as an object type Row. 
- Spark manipulates Row objects using column expressions in order to produce usable values. 

**Create Rows:**
```
from pyspark.sql import Row
myRow = Row("Hello", None, 1, False)
```
*DataFrame Transformations*
- We can add rows or columns
- We can remove rows and columns
- We can transform a row into a column or vice versa
- We can change the order of rows based on the values in columns

### DataFrame Operations 

**Reading Data:**
```
df = spark.read \
  .option("header", True) \
  .option("sep", ",") \
  .option("inferSchema", True) \
  .csv("PATH/file.csv") 
```

**Show**
Parameters:
- show(5) - Show only 5 rows
- show(5, False) - Show only 5 rows and don't truncate the columns
- show(5, 55) - Show only 5 rows and truncate the columns 55 the columns

```
df.show(15, True)
```

**Display**
Display is a fully featured utility available in the Databricks environment. It can:
- Show our Dataframe in a tabular format
- Plot numerical columns
- Display Python / Scala / Java arrays

```
display(df)
```

**Columns - select**
```
display(
  df.select("column3", "column7")
)
```

```
selected_df = df.select(df.column3, df.column7)
```

**Drop**
```
df.drop("id")
```

**Limit**
If we only need the first N rows of a Dataframe, we can use limit:
```
df.limit(3).show(10)
```

**Count**
count will return the number of elements in our Dataframe

#### Creating DataFrames on the fly

```
from pyspark.sql import Row
from pyspark.sql.types import StructField, StructType, StringType, LongType

myManualSchema = StructType([
StructField("some", StringType(), True),
StructField("col", StringType(), True),
StructField("names", LongType(), False)
])
myRow = ("hello", None, 1)
myDf = spark.createDataFrame([myRow], myManualSchema)
myDf.show()
```

**Adding columns**
- allows you to do the DataFrame equivalent of SQL queries on a table of data
- withColumn
```
df.withColumn("somecolumnsName", lit(1)).show(2)
```

**Renaming columns**
- withColumnRenamed method
```
df.withColumn("somecolumnsName", lit(1)).show(2)
```

**Sorting Rows**
- `sort` and `orderBy` do the same
- the default is sort in ascending order
- to more explicitly specify sort direction, you need to use asc and desc functions if operating on a column. 
```
from pyspark.sql.functions import asc, desc
df.orderBy(expr("count desc")).show(2)
df.orderBy(col("count").desc(),  col("ColName").asc()).show(2)
```

**Limit**
- Restrict what you extract from the dataframe
```
df.limit(5).show()
```


#### Working with Different Types of Data

**Objectives**
- Booleans
- Numbers
- Strings
- Dates and Timestamps
- Handling Null
- Complex Types
- User Defined Functions

**Where to look for APIs?**
DataFrame (Dataset) Methods: DataFrame is just a Dataset of Row types, so you will look at the Dataset methods available at: http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Dataset
DataFrameStatFunctions: http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.DataFrameStatFunctions
DataFrameNaFunctions http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.DataFrameNaFunctions
Column methods: http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Column
Functions: http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.functions$
Dataset: http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Dataset


#### Joins
Joins bring together a large number of different datasets. It helps avoid OutOfMemory issues and solve problems.

**Join Expressions**
- Join expressions determine whether two rows should join
A join brings together two sets of data, the left and the right, by comparing the value of one or more keys of the left and right and evaluating the result of a join expression that determines whether Spark should bring together the left set of data with the right set of data. 

**Join types**
- The join type determines what should be in the result set. 

- Inner joins (keep rows with keys that exist in the left and right datasets)
- Outer joins (keep rows with keys in either the left or right datasets)
- Left outer joins (keep rows with keys in the left dataset)
- Right outer joins (keep rows with keys in the right dataset)
- Left semi joins (keep the rows in the left, and only the left, dataset where the key appears in the right dataset)
- Left anti joins (keep the rows in the left, and only the left, dataset where they dos not appear in the right dataset)
- Natural joins (perform a join by implicitly matching the columns between the two datasets with the same names)
- Cross (or cartesian) joins (match every row in the left dataset with every row in the right dataset)

**Create a simple dataset:**
```
person = spark.createDataFrame([
(0, "Bill Chambers", 0, [100]),
(1, "Matei Zaharia", 1, [500, 250, 100]),
(2, "Michael Armbrust", 1, [250, 100])])\
.toDF("id", "name", "graduate_program", "spark_status")
graduateProgram = spark.createDataFrame([
(0, "Masters", "School of Information", "UC Berkeley"),
(2, "Masters", "EECS", "UC Berkeley"),
(1, "Ph.D.", "EECS", "UC Berkeley")])\
.toDF("id", "degree", "department", "school")
sparkStatus = spark.createDataFrame([
(500, "Vice President"),
(250, "PMC Member"),
(100, "Contributor")])\
.toDF("id", "status")
```
**Register these tables:**
``` 
person.createOrReplaceTempView("person")
graduateProgram.createOrReplaceTempView("graduateProgram")
sparkStatus.createOrReplaceTempView("sparkStatus")
```

**Inner Joins**
- Evaluate the keys in both of the DataFrames or tables and include only the rows that evaluate to true. Join graduateProgram DataFrame with the person DataFrame.
```
joinExpression = person["graduate_program"] == graduateProgram['id']
#keys don't exist in both DataFrames so the following expression results in zero values.
wrongJoinExpression = person["name"] == graduateProgram["school"]
person.join(graduateProgram, joinExpression).show()
```
*We can also specify this explicitly by passing in a third parameter, the joinType.*
```
joinType = "inner"
person.join(graduateProgram, joinExpression, joinType).show()
```

**Outer Joins**
- Evaluate the keys in both of the DataFrames or tables and includes (and joins together) the rows that evaluate to true or false. If there is no equivalent row in either the left or right DataFrame, Spark will insert null.
```
joinType = "outer"
person.join(graduateProgram, joinExpression, joinType).show()
```

**Left Outer Joins**
- Left outer joins evaluate the keys in both of the DataFrames or tables and includes all rows from the left DataFrame as well as any rows in the right DataFrame that have a match in the left DataFrame. If there is no equivalent row in the right DataFrame, Spark will insert null.
```
joinType = "left_outer"
graduateProgram.join(person, joinExpression, joinType).show()
```

**Right Outer Joins**
- Right outer joins evaluate the keys in both of the DataFrames or tables and includes all rows from the right DataFrame as well as any rows in the left DataFrame that have a match in the right DataFrame. If there is no equivalent row in the left DataFrame, Spark will insert null.
```
joinType = "right_outer"
person.join(graduateProgram, joinExpression, joinType).show()
```

**Left Semi Joins**
- Semi joins do not actually include any values from the right DataFrame. They only compare values to see if the value exists in the second DataFrame. If the value does exist, those rows will be kept in the result, even if there are duplicate keys in the left DataFrame. Think of left semi joins as filters on a DataFrame, as opposed to the function of a conventional join.
```
joinType = "left_semi"
graduateProgram.join(person, joinExpression, joinType).show()
```

**Left Anti Joins**
- Left anti joins are the opposite of left semi joins. Like left semi joins, they do not actually include any values from the right DataFrame. They only compare values to see if the value exists in the second DataFrame. However, rather than keeping the values that exist in the second DataFrame, they keep only the values that do not have a corresponding key in the second DataFrame. Like a NOT IN SQL style filter.
```
joinType = "left_anti"
graduateProgram.join(person, joinExpression, joinType).show()
```

**Cross (Cartesian) Joins**
- Cross-joins are inner joins that do not specify a predicate. Cross joins will join every single row in the left DataFrame to ever single row in the right DataFrame. This will cause an absolute explosion in the number of rows contained in the resulting DataFrame. If you have 1,000 rows in each DataFrame, the cross join of these will result in 1,000,000 (1,000 x 1,000) rows. For this reason, you must very explicitly state that you want a cross-join by using the following special syntax:
```
joinType = "cross"
graduateProgram.join(person, joinExpression, joinType).show()
```

#### Challenges When Using Joins
**Joins on Complex Types**
- Any expression is a valid join expression, assuming that it returns a Boolean.

**Handling Duplicate Column Names**
In a DataFrame, each column has a unique ID within Spark’s SQL Engine, Catalyst. This unique ID is purely internal and not something that you can directly reference. This makes it quite difficult to refer to a specific column when you have a DataFrame with duplicate column names.
*This can occur in two distinct situations:*
- The join expression that you specify does not remove one key from one of the input DataFrames and the keys have the same column name
- Two columns on which you are not performing the join on have the same name

Note: If you partition your data correctly prior to a join, you can end up with much more efficient execution because even if a shuffle is planned, if data from two different DataFrames is already located on the same machine, Spark can avoid the shuffle.

#### Data Sources
- **JSON:** JSON objects have structure, and JavaScript (on which JSON is based) has at least basic types. This makes it easier to work with
- **Parquet**: Parquet is an open source column-oriented data store that provides a variety of storage optimizations, especially for analytics workloads. It provides columnar compression, which saves storage space and allows for reading individual columns instead of entire files. It is the default file format. Writing data out to Parquet for long-term storage because reading from a parquet file will always be more efficient than JSON or CSV. Another advantage of Parquet is that it supports complex types. 
- **ORC**: ORC is a self-describing, type-aware columnar file format designed for Hadoop workloads. It is optimized for large streaming reads, but with integrated support for finding required rows quickly. ORC has no options for reading in data because Spark understands the file format well.
- **JDBC/ODBC Connections**
- **Plain Text Files** Each line in the file becomes a record in the DataFrame. 
- **CSV:** Commma-Separated Values. Each line represents a single record, and commas separate each field within a record. 

**Community-created Data Sources**
- Cassandra
- HBase
- MongoDB
- AWS Redshift
- XML

#### The Structure of the Data Sources API
**Reading data:**
`DataFrameReader.format(...).option("key", "value").schema(...).load()`
#`format` is optional because Spark will use the parquet format by default
#`.option` allows you to set key value configurations to parameterize how you will read data
#`schema` is optional if the data source provides a schema or if intend to use schema inference. 

The foundation for reading data in Spark is the DataFrameReader. We access this through the SparkSession via the read attribute: `spark.read`
After we have a DataFrame reader, we specify several values: 
the format (1)
the schema (2)
the read mode (3)
a series of options (4)

Example: 
```
spark.read.format("csv")
.option("mode", "FAILFAST")
.option("inferSchema", "true")
.option("path", "path/to/file(s)")
.schema(someSchema)
.load()
```

**Read Mode**
Reading data from an external source naturally entails encountering malformed data, especially when working with only semi-structured data sources. Read modes specify what will happen when Spark does come across malformed records.


#### Basics of Writing Data
The foundation for writing data is quite similar to that of reading data. Instead of the `DataFrameReader`, we have the `DataFrameWriter`. Because we always need to write out some given data source, we access the `DataFrameWriter` on a per DataFrame basis via the write attribute: dataFrame.write
 
*Specify three values:* the format, a series of options, and the save mode. At a minimum, you must supply a path. 
Example:
```
dataframe.write.format("csv")
.option("mode", "OVERWRITE")
.option("dateFormat", "yyyy-MM-dd")
.option("path", "path/to/file(s)")
.save()
```

#### Save Mode
- Save modes specify what will happen if Spark finds data at the specified location. The default is errorIfExists. This means that if Spark finds data at the location to which you’re writing, it will fail the write immediately.


## SparkSQL
With SparkSQL you can:
- Run SQL queries against views or tables organized into databases
- Use system functions of define user functions and analyze query plans in order to optimize their workloads
  - You can choose to express some of your data manipulations in SQL and others in DataFrames and they will compile to the same underlying code

#### What is SQL?
- Structured Query Language
- Domain-specific language (A domain-specific language is created specifically to solve problems in a particular domain and is not intended to be able to solve problems outside it (although that may be technically possible). 
  - In contrast, general-purpose languages are created to solve problems in many domains.)
- For expressing relational operations over data, it is used in all relational databases.

#### Spark SQL
*The power of Spark SQL derives from:*
- SQL analysts can take advantage of Spark’s computation abilities by plugging into the Thrift Server or Spark’s SQL interface
- Data engineers and scientists can use Spark SQL where appropriate in any data flow. 
  - This unifying API allows for data to be extracted with SQL, manipulated as a DataFrame, passed into one of Spark MLlibs large scale machine learning algorithms, written out to another data source and everything in between.

- Spark SQL is intended to operate as a online analytic processing (OLAP) database. This means that it is not intended to perform very extremely-low-latency queries. 

| OLAP (Online Analytic Processing) | OLTP (Online Transaction Processing)    | 
| :------------- | :----------: | 
|  Deals with Historical Data or Archival Data. OLAP is characterized by relatively low volume of transactions. Queries are often very complex and involve aggregations. For OLAP systems a response time is an effectiveness measure. OLAP applications are widely used by Data Mining techniques. In OLAP database there is aggregated, historical data, stored in multi-dimensional schemas (usually star schema). Sometime query need to access large amount of data in Management records like what was the profit of your company in last year. | Is involved in the operation of a particular system. OLTP is characterized by a large number of short on-line transactions (INSERT, UPDATE, DELETE). The main emphasis for OLTP systems is put on very fast query processing, maintaining data integrity in multi-access environments and an effectiveness measured by number of transactions per second. In OLTP database there is detailed and current data, and schema used to store transactional databases is the entity model (usually 3NF). It involves Queries accessing individual record like Update your Email in Company database.   | 

 
#### Spark SQL CLI
- You can make Spark SQL queries in local mode from the command line. It cannot communicate with the Thrift JDBC server. To start Spark SQL CLI, run the following in the spark directory: 
`./bin/spark-sql`
- It is also possible to execute sql in an ad hoc manner via any of Spark's language by calling the method "sql" on the SparkSession object.
`spark.sql("SELECT 1 + 1").show()`

Note: **You can completely interoperate between SQL and DataFrames e.g you can create a DataFrame, manipulate it with SQL, and then manipulate it again as a DataFrame.**

**Convert DataFrame to SQL:**
```
spark.read.json("/data.json")\
.createOrReplaceTempView("some_sql_view") 
```

#### Catalog
The highest level abstraction in Spark SQL is the Catalog. The Catalog is an abstraction for the storage of metadata about the data stored in your tables as well as other helpful things like databases, tables, functions, and views. The catalog is available in the org.apache.spark.sql.catalog.Catalog package and contains a number of helpful functions for doing things like listing tables, databases, and functions. We will talk about all of these things shortly It’s very self explanatory to users, so we will omit the code samples here but it’s really just another programmatic interface to Spark SQL. This chapter shows only the SQL being executed; thus, keep in mind if you’re using the programmatic interface that you need to wrap everything in a spark.sql function call to execute the relevant code.

#### Tables
To do anything useful with Spark SQL you first need to define tables. Tables are a structure of data against which you run commands. We can join tables, filter them, aggregate them, and perform different manipulations.
The core difference between tables and DataFrames is that you define DataFrames in a scope of a programming language, whereas you define tables within a database. This means that when you create a table (assuming you never changed the database), it will belong to the default database. 

**In Spark 2.X, tables always contain data. There is no notion of a temporary table: these are just views that do not contain data.  This is important because if you go to drop a table, you can risk losing the data when doing so.**

#### Spark-Managed Tables
- There are managed tables and unmanaged tables. 
- When you define a table from files on disk, you are defining an unmanaged table. 
- When you use saveAsTable on a DataFrame you are creating a managed table for which Spark will keep track of all the relevant information for you. 
- This will read your table and write it out to a new location in Spark format. 
- You can see this reflected in the new explain plan. 
    - In the explain plan you will also notice that this writes to the default Hive warehouse location. You can set this by setting the spark.sql.warehouse.dir configuration to the directory of your choosing when you create your SparkSession.
    
**Tables store two important information:**
- data within the tables
- data about the tables, that is, metadata

#### Views
Now that you created a table, another thing that you can define is a view. 
A view specifies a set of transformations on top of an existing table—basically just saved query plans, which can be convenient for organizing or reusing your query logic. Spark has several different notions of views. Views can be global, set to a database, or per session.

#### Creating Views
To an end user, views are displayed as tables, except rather than rewriting all of the data to a new location, they simply perform a transformation on the source data at query time. This might be a filter, select, or potentially an even larger GROUP BY or ROLLUP.

**Views**
A view specifies a set of transformations on top of an existing table—basically just saved query plans, which can be convenient for organizing or reusing your query logic. Spark has several different notions of views. Views can be global, set to a database, or per session.

**Creating Views**
To an end user, views are displayed as tables, except rather than rewriting all of the data to a new location, they simply perform a transformation on the source data at query time. This might be a filter, select, or potentially an even larger GROUP BY or ROLLUP.


* * *

#### Sourcers/Credits:
To be completed



### Introduction
   > Spark SQL is a component on top of Spark Core that introduces a new data  abstraction  called SchemaRDD, which provides support for structured and semi-structured data.Spark SQL is to execute SQL queries written using either a basic SQL syntax or HiveQL. Spark SQL can also be used to read data from an existing Hive installation.It provides a programming abstraction called DataFrame and can act as distributed SQL query engine.
> Spark’s interface for working with structured and semi structured data. Structured data is any data that has a    schema—that is, a known set of fields for each record. When you have this type of data, Spark SQL makes it both  easier and more efficient to load and query.There are several ways to interact with Spark SQL including SQL, the DataFrames API and the Datasets API. When computing a result the same execution engine is used, independent of which API/language you are using to express the computation.

#### Create SQL Context

> To create a basic SQLContext, all you need is a SparkContext.

```scala

val sc = SparkCommon.sparkContext
val sqlContext = new org.apache.spark.sql.SQLContext(sc)

```

##### Basic Query 
> Spark SQL can load JSON files and infer the schema based on that data. Here is the code to load the json files, register the data in the temp table called "Cars1" and print out the schema based on that.
> To make a query against a table, we call the sql() method on the SQLContext. The first thing we need to do is tell Spark SQL about some data to query. In this case we will load some Cars data from JSON, and give it a name by
registering it as a “Cars1” so we can query it with SQL.

> Here we are using  JSON document named _cars.json_ with the following content and generate a table based on the schema in the JSON document.

```scala
[{"itemNo" : 1, "name" : "ferrari", "speed" : 259 , "weight": 800},  {"itemNo" : 2, "name" : "jaguar", "speed" : 274 , "weight":998},  {"itemNo" : 3, "name" : "mercedes", "speed" : 340 , "weight": 1800},  {"itemNo" : 4, "name" : "audi", "speed" : 345 , "weight": 875},  {"itemNo" : 5, "name" : "lamborghini", "speed" : 355 , "weight": 1490},{"itemNo" : 6, "name" : "chevrolet", "speed" : 260 , "weight": 900},  {"itemNo" : 7, "name" : "ford", "speed" : 250 , "weight": 1061},  {"itemNo" : 8, "name" : "porche", "speed" : 320 , "weight": 1490},  {"itemNo" : 9, "name" : "bmw", "speed" : 325 , "weight": 1190},  {"itemNo" : 10, "name" : "mercedes-benz", "speed" : 312 , "weight": 1567}]


```

```scala
object BasicQueryExample {

  val sc = SparkCommon.sparkContext
  val sqlContext = new org.apache.spark.sql.SQLContext(sc)

  def main(args: Array[String]) {

    import sqlContext.implicits._

    val input = sqlContext.read.json("src/main/resources/cars1.json")

    input.registerTempTable("Cars1")


    val result = sqlContext.sql("SELECT * FROM Cars1")

    result.show()
 }

}

case class Cars1(name: String)


```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/sqldata.png)


```scala

    val cars = sqlContext.sql("SELECT COUNT(*) FROM Cars1").collect().foreach(println)

```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/sql2.png)



```scala

    val result1 = sqlContext.sql("SELECT name, COUNT(*) AS cnt FROM Cars1 WHERE name <> '' GROUP BY name ORDER BY cnt DESC LIMIT 10")
      .collect().foreach(println)

```
![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/sql3.png)


### DataFrames

> A DataFrame is a distributed collection of data organized into named columns.DataFrames can be constructed from a wide array of sources such as: structured data files, tables in Hive, external databases, or existing RDDs.

#### Creating DataFrames

> A DataFrame is a distributed collection of data, which is organized into named columns. Conceptually, it is equivalent to relational tables with good optimization techniques.
> A DataFrame can be constructed from an array of different sources such as Hive tables, Structured Data files, external databases, or existing RDDs.
> Here we are using  JSON document named _cars.json_ with the following content and generate a table based on the schema in the JSON document.

```scala

[{"itemNo" : 1, "name" : "Ferrari", "speed" : 259 , "weight": 800},  {"itemNo" : 2, "name" : "Jaguar", "speed" : 274 , "weight":998},  {"itemNo" : 3, "name" : "Mercedes", "speed" : 340 , "weight": 1800},  {"itemNo" : 4, "name" : "Audi", "speed" : 345 , "weight": 875},  {"itemNo" : 5, "name" : "Lamborghini", "speed" : 355 , "weight": 1490}]


```

```scala
package com.tutorial.sparksql

import com.tutorial.utils.SparkCommon

object CreatingDataFarmes {

  val sc = SparkCommon.sparkContext

  /**
    * Create a Scala Spark SQL Context.
    */
  val sqlContext = new org.apache.spark.sql.SQLContext(sc)

  def main(args: Array[String]) {
    /**
      * Create the DataFrame
      */
    val df = sqlContext.read.json("src/main/resources/cars.json")

    /**
      * Show the Data
      */
    df.show()

  }
}

```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/creatingdataframe.png)


#### DataFrame API Example Using Different types of Functionality

> Diiferent type of DataFrame operatios are :

##### Action:

> Action are operations (such as take, count, first, and so on) that return a value after running a computation on an DataFrame.

> Some Action Operation with examples:

###### show()

> If you want to see top 20 rows of DataFrame in a tabular form then use the following command.

```scala

carDataFrame.show()

```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/showdata.png)



###### show(n)

> If you want to see n  rows of DataFrame in a tabular form then use the following command.

```scala

carDataFrame.show(2)

```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/shown.png)

###### take()

> take(n) Returns the first n rows in the DataFrame.

```scala

carDataFrame.take(2).foreach(println)

```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/takedata.png)

###### count()

> Returns the number of rows.

```scala

carDataFrame.groupBy("speed").count().show()

```
![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/countdata.png)

###### head()

> head () is used to returns first row.

```scala

val resultHead = carDataFrame.head()

    println(resultHead.mkString(","))
```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/headdata.png)


###### head(n)

> head(n) returns first n rows.

```scala
val resultHeadNo = carDataFrame.head(3)

    println(resultHeadNo.mkString(","))
```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/headn.png)


###### first()

> Returns the first row.

```scala
 val resultFirst = carDataFrame.first()

    println("fist:" + resultFirst.mkString(","))

```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/firstdata.png)


###### collect()

> Returns an array that contains all of Rows in this DataFrame.

``` scala

val resultCollect = carDataFrame.collect()

    println(resultCollect.mkString(","))

```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/collectdata.png)


##### Basic DataFrame functions:

###### printSchema()

> If you want to see the Structure (Schema) of the DataFrame, then use the following command.

```scala

carDataFrame.printSchema()
```
![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/printschemadata.png)

###### toDF()

>  toDF() Returns a new DataFrame with columns renamed. It  can be quite convenient in conversion from a RDD of tuples into a DataFrame with meaningful names.

```scala

val car = sc.textFile("src/main/resources/fruits.txt")
      .map(_.split(","))
      .map(f => Fruit(f(0).trim.toInt, f(1), f(2).trim.toInt))
      .toDF().show()

```
![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/todfdata.png)

###### dtypes()

> Returns all column names and their data types as an array.

```scala

carDataFrame.dtypes.foreach(println)

```
![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/dtypesdata.png)

###### columns ()

> Returns all column names as an array.

```scala

carDataFrame.columns.foreach(println)

```
![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/columnsdata.png)

###### cache()

>  cache() explicitly to store the data into memory. Or data stored in a distributed way in the memory by default.

```scala
val resultCache = carDataFrame.filter(carDataFrame("speed") > 300)

    resultCache.cache().show()
```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/cachedata.png)




##### Data Frame operations:

###### sort()

> Returns a new DataFrame sorted by the given expressions.

```scala

carDataFrame.sort($"itemNo".desc).show()

```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/shortdata.png)

###### orderBy()

> Returns a new DataFrame sorted by the specified column(s).

```scala

carDataFrame.orderBy(desc("speed")).show()

```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/orderbydata.png)

###### groupBy()

> counting the number of cars who are of the same speed .

```scala

carDataFrame.groupBy("speed").count().show()

```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/groupbydata.png)

###### na()

> Returns a DataFrameNaFunctions for working with missing data.

```scala

carDataFrame.na.drop().show()

```
![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/nadata.png)


###### as()

> Returns a new DataFrame with an alias set.

```scala
carDataFrame.select(avg($"speed").as("avg_speed")).show()

```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/asdata.png)

###### alias()

> Returns a new DataFrame with an alias set. Same as `as`.


```scala

carDataFrame.select(avg($"weight").alias("avg_weight")).show()

```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/aliasdata.png)

###### select()

> To fetch speed-column among all columns from the DataFrame.

```scala

carDataFrame.select("speed").show()

```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/selectdata.png)

######  filter()

> filter the cars whose speed is greater than 300 (speed > 300).

```scala

carDataFrame.filter(carDataFrame("speed") > 300).show()

```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/filterdata.png)

###### where()


> Filters age using the given SQL expression.

```scala
carDataFrame.where($"speed" > 300).show()

```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/wheredata.png)


###### agg()

> Aggregates on the entire DataFrame without groups.

```scala

carDataFrame.agg(max($"speed")).show()

```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/aggdata.png)

###### limit()

> Returns a new DataFrame by taking the first n rows.The difference between this function and head is that head returns an array while limit returns a new DataFrame.

``` scala

carDataFrame1.limit(3).show()

```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/limit.png)

###### unionAll()

> Returns a new DataFrame containing union of rows in this frame and another frame.

```scala
carDataFrame.unionAll(empDataFrame2).show()


```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/unionalldata.png)

###### intersect()

> Returns a new DataFrame containing rows only in both this frame and another frame.

```scala

carDataFrame1.intersect(carDataFrame).show()
```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/intersectdata.png)

###### except()

> Returns a new DataFrame containing rows in this frame but not in another frame.

```scala

carDataFrame.except(carDataFrame1).show()

```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/exceptdata.png)



###### withColumn()

>  Returns a new DataFrame by adding a column or replacing the existing column that has the same name.

```scala

val coder: (Int => String) = (arg: Int) => {
      if (arg < 300) "slow" else "high"
    }

    val sqlfunc = udf(coder)

    carDataFrame.withColumn("First", sqlfunc(col("speed"))).show()


```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/withcolumndata.png)

###### withColumnRenamed()

> Returns a new DataFrame with a column renamed.

```scala

empDataFrame2.withColumnRenamed("id", "employeeId").show()
```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/withcolumnrenameddata.png)

###### drop()

> Returns a new DataFrame with a column dropped.

```scala

carDataFrame.drop("speed").show()

```
![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/dropdata.png)

###### dropDuplicates()

> Returns a new DataFrame that contains only the unique rows from this DataFrame.
> This is an alias for distinct.

```scala

carDataFrame.dropDuplicates().show()

```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/dropduplicates.png)

###### describe()

> describe returns a DataFrame containing information such as number of non-null entries (count),mean, standard deviation, and minimum and maximum value for each numerical column.

``` scala

carDataFrame.describe("speed").show()

```
![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/describe.png)



#### Interoperating with RDDs

>  SparkSQL supports two different  types methods for converting existing RDDs into DataFrames:


##### 1. Inferring the Schema using Reflection:


> The Scala interface for Spark SQL supports automatically converting an RDD containing case classes to a DataFrame.
> The case class defines the schema of the table.
> The names of the arguments to the case class are read using reflection and they become the names of the columns.
> RDD can be implicitly converted to a DataFrame and then be registered as a table.
> Tables can be used in subsequent SQL statements.

```scala

  def main(args: Array[String]) {

    /**
      * Create RDD and Apply Transformations
      */

    val fruits = sc.textFile("src/main/resources/fruits.txt")
      .map(_.split(","))
      .map(frt => Fruits(frt(0).trim.toInt, frt(1), frt(2).trim.toInt))
      .toDF()

    /**
      * Store the DataFrame Data in a Table
      */
    fruits.registerTempTable("fruits")

    /**
      * Select Query on DataFrame
      */
    val records = sqlContext.sql("SELECT * FROM fruits")


    /**
      * To see the result data of allrecords DataFrame
      */
    records.show()

  }
}

case class Fruits(id: Int, name: String, quantity: Int)
```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/inferringdataframe.png)


##### 2. Programmatically Specifying the Schema:

> Creating DataFrame is through programmatic interface that allows you to construct a schema and then apply it to an existing RDD.
> DataFrame can be created programmatically with three steps.
> We Create an RDD of Rows from an Original RDD.
> Create the schema represented by a StructType matching the structure of Rows in the RDD created in Step first.
> Apply the schema to the RDD of Rows via createDataFrame method provided by SQLContext.

```scala

object ProgrammaticallySchema {
  val sc = SparkCommon.sparkContext
  val schemaOptions = Map("header" -> "true", "inferSchema" -> "true")

  //sc is an existing SparkContext.
  val sqlContext = new org.apache.spark.sql.SQLContext(sc)

  def main(args: Array[String]) {

    // Create an RDD
    val fruit = sc.textFile("src/main/resources/fruits.txt")

    // The schema is encoded in a string
    val schemaString = "id name"

    // Generate the schema based on the string of schema
    val schema =
      StructType(
        schemaString.split(" ").map(fieldName => StructField(fieldName, StringType, true)))

    schema.foreach(println)

    // Convert records of the RDD (fruit) to Rows.
    val rowRDD = fruit.map(_.split(",")).map(p => Row(p(0), p(1).trim))

    rowRDD.foreach(println)

    // Apply the schema to the RDD.
    val fruitDataFrame = sqlContext.createDataFrame(rowRDD, schema)

    fruitDataFrame.foreach(println)

    // Register the DataFrames as a table.
    fruitDataFrame.registerTempTable("fruit")

    /**
      * SQL statements can be run by using the sql methods provided by sqlContext.
      */
    val results = sqlContext.sql("SELECT * FROM fruit")
    results.show()


  }


}



```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/programmaticallydata.png)






#### Data Sources
> Spark SQL supports a number of structured data sources. These sources include Hive tables, JSON, and Parquet files.Spark SQL supports operating on a variety of data sources through the DataFrame interface. A DataFrame can be operated on as normal RDDs and can also be registered as a temporary table. Registering a DataFrame as a table allows you to run SQL queries over its data.


##### DataFrame Operations in JSON file:

> Here we include some basic examples of structured data processing using DataFrames.
> As an example, the following creates a DataFrame based on the content of a JSON file.
> Read a JSON document named _cars.json_ with the following content and generate a table based on the schema in the JSON document.

```scala

[{"itemNo" : 1, "name" : "ferrari", "speed" : 259 , "weight": 800},  {"itemNo" : 2, "name" : "jaguar", "speed" : 274 , "weight":998},  {"itemNo" : 3, "name" : "mercedes", "speed" : 340 , "weight": 1800},  {"itemNo" : 4, "name" : "audi", "speed" : 345 , "weight": 875},  {"itemNo" : 5, "name" : "lamborghini", "speed" : 355 , "weight": 1490}]

```

```scala

object DataFrameOperations {

  val sc = SparkCommon.sparkContext

  /**
    * Use the following command to create SQLContext.
    */
  val ssc = SparkCommon.sparkSQLContext

  val schemaOptions = Map("header" -> "true", "inferSchema" -> "true")

  def main(args: Array[String]) {

    /**
      * Create the DataFrame
      */
    val cars = "src/main/resources/cars.json"

    /**
      * read the JSON document
      * Use the following command to read the JSON document named cars.json.
      * The data is shown as a table with the fields − itemNo, name, speed and weight.
      */
    val carDataFrame: DataFrame = ssc.read.format("json").options(schemaOptions).load(cars)

    /**
      * Show the Data
      * If you want to see the data in the DataFrame, then use the following command.
      */
    carDataFrame.show()

    /**
      * printSchema Method
      * If you want to see the Structure (Schema) of the DataFrame, then use the following command
      */
    carDataFrame.printSchema()

    /**
      * Select Method
      * Use the following command to fetch name-column among three columns from the DataFrame
      */
    carDataFrame.select("name").show()

    /**
      * Filter used to
      * cars whose speed is greater than 300 (speed > 300).
      */
    carDataFrame.filter(empDataFrame("speed") > 300).show()

    /**
      * groupBy Method
      * counting the number of cars who are of the same speed.
      */
    carDataFrame.groupBy("speed").count().show()


  }


}



```

##### Show the Data

> If you want to see the data in the DataFrame, then use the following command.

```scala

carDataFrame.show()
```
![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/show.png)

##### printSchema Method

> If you want to see the Structure (Schema) of the DataFrame, then use the following command

```scala
 carDataFrame.printSchema()

```
![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/schema.png)

##### Select Method

> Use the following command to fetch name-column among three columns from the DataFrame

```scala

carDataFrame.select("name").show()

``` 
![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/select.png)

##### Filter Method

> Use the following command to filter whose speed is greater than 300 (speed > 300)from the DataFrame

```scala

carDataFrame.filter(carDataFrame("speed") > 300).show()

``` 
![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/filterage.png)

##### DataFrame Operations in Text file:

> As an example, the following creates a DataFrame based on the content of a text file.
> Read a text document named _fruits.txt_ with the following content and generate a table based on the schema in the text document.

```scala
1, Grapes, 25
2, Guava, 28
3, Gooseberry, 39
4,  Raisins, 23
5, Naseberry, 23
```
```scala
 val fruits = sc.textFile("src/main/resources/fruits.txt")
      .map(_.split(","))
      .map(frt => Fruits(frt(0).trim.toInt, frt(1), frt(2).trim.toInt))
      .toDF()

    /**
      * Store the DataFrame Data in a Table
      */
    fruits.registerTempTable("fruits")

    /**
      * Select Query on DataFrame
      */
    val records = sqlContext.sql("SELECT * FROM fruits")


    /**
      * To see the result data of allrecords DataFrame
      */
    records.show()

  }
}

case class Fruits(id: Int, name: String, quantity: Int)
```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/text1.png)

##### DataFrame Operations in CSV file :

> As an example, the following creates a DataFrame based on the content of a CSV file.
> Read a csv document named _cars.csv_ with the following content and generate a table based on the schema in the csv document.

```scala
year,make,model,comment,blank
"2012","Tesla","S","No comment",

1997,Ford,E350,"Go get one now they are going fast",
2015,Chevy,Volt
```
```scala

object csvFile {

val sc = SparkCommon.sparkContext

val sqlContext = SparkCommon.sparkSQLContext

def main(args: Array[String]) {

val sqlContext = new SQLContext(sc)
val df = sqlContext.read
.format("com.databricks.spark.csv")
.option("header", "true") // Use first line of all files as header
.option("inferSchema", "true") // Automatically infer data types
.load("src/main/resources/cars.csv")
 df.show()
 df.printSchema()
    
val selectedData = df.select("year", "model")
selectedData.write
.format("com.databricks.spark.csv")
.option("header", "true")
.save(s"src/main/resources/${UUID.randomUUID()}")
  println("OK")

  }

}
```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/csv.png)


### Dataset

> Dataset is a new experimental interface that tries to provide the benefits of RDDs (strong typing, ability to use powerful lambda functions) with the benefits of Spark SQL’s optimized execution engine. Dataset can be constructed from JVM objects and then manipulated using functional transformations (map, flatMap, filter, etc.).

#### Creating Datasets:

> A Dataset is a strongly-typed, immutable collection of objects that are mapped to a relational schema.
> Datasets are similar to RDDs, however, instead of using Java Serialization they use a specialized Encoder to serialize the objects for processing or transmitting over the network.
> Dataset API is a new concept called an encoder, which is responsible for converting between JVM objects and tabular representation.
> Dataset support for automatically generating encoders for a wide variety of types, including primitive types (e.g. String, Integer, Long), Scala case classes, and Java Beans.
> Here we are using  text document named _test_file.txt_ with the following content and generate a table based on the schema in the text document.

```scala

JSON is a popular semistructured data format. The simplest way to load JSON data is
by loading the data as a text file and then mapping over the values with a JSON
parser. Likewise, we can use our preferred JSON serialization library to write out the
values to strings, which we can then write out.
 In Java and Scala we can also work
with JSON data using a custom Hadoop format.
 “JSON” on page 172 also shows how to
load JSON data with Spark SQL.

```

```scala
package com.tutorial.sparksql

import com.tutorial.utils.SparkCommon

object CreatingDatasets {

  val sc = SparkCommon.sparkContext
  val sqlContext = new org.apache.spark.sql.SQLContext(sc)

  def main(args: Array[String]) {

    import sqlContext.implicits._

    val lines = sqlContext.read.text("src/main/resources/test_file.txt").as[String]
    val words = lines
      .flatMap(_.split(" "))
      .filter(_ != "")
      .groupBy(_.toLowerCase)
      .count()
      .show()

  }
}


```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/creatingdataset.png)

#### Basic Opeartion 

>  Encoders are also created for case classes.

```scala
    case class Cars(name: String, kph: Long)
    val ds = Seq(Cars("lamborghini", 32)).toDS()
    ds.show()
```
![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/encoderdata.png)

> DataFrames can be converted to a Dataset by providing a class.
> Mapping will be done by name.
     
```scala

   case class Cars(name: String, kph: Long)

    val car = sqlContext.read.json("src/main/resources/cars.json").as[Cars]
    
    car.show()

```

![alt text](https://github.com/rklick-solutions/spark-tutorial/wiki/images/datasetclass.png)



--------------------------------------------

* https://github.com/vaquarkhan/vk-wiki-notes/wiki/Apache-Spark-SQL
* https://github.com/vaquarkhan/vk-wiki-notes/wiki/Apache-Spark-SQL-programming-guide-notes-1
* https://github.com/vaquarkhan/vk-wiki-notes/wiki/How-do-I-flatten-JSON-blobs-into-a-Data-Frame-using-Spark-Spark-SQL
* https://github.com/vaquarkhan/vk-wiki-notes/wiki/Problems-Spark-SQL-solves
* https://github.com/vaquarkhan/vk-wiki-notes/wiki/Spark-SQL-and-dataset-type
* https://github.com/vaquarkhan/vk-wiki-notes/wiki/Spark-SQL-links
* https://databricks.com/blog/2016/07/14/a-tale-of-three-apache-spark-apis-rdds-dataframes-and-datasets.html
* https://cwiki.apache.org/confluence/display/SPARK/Spark+SQL+Internals
* https://trongkhoanguyen.com/spark/spark-sql-internals/


