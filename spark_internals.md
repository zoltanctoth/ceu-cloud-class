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
Production Applications

  

*   Spark Architecture 1
    

![](Production%20Applications.html.resources/IMG_3832.jpg)  

*   2 Spark Architecture 2
    

Spark breaks our code into a set of code and runs it in parallel. 

  

 Typical Spark Application Process Flow

Read Data from a Source 

Load it into Spark

Process the data

Hold intermediate Results

Write the results back to a destination

<- In this process you need a data structure to hold the data in Spark. We have 3 alternatives to hold data in Spark:  DataFrame, Dataset & RDD

DataFramers and Datasets are ultimately compiled down to an RDD.

*   Collection of Data: RDD holds data
    
*   Resilient: Fault tolerant
    
*   Distributed: Instead of keeping partitions on a single machine, Spark spreads them across the cluster
    
*   Partitioned: Breaks RDD into smaller chunks of data. These chunks are called partitions. 
    
*   Immutable: Once defined you cannot change them so Spark RDD is a Read-Only Data Structure.
    

  

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-03%20at%209.42.58%20PM.png)  

Parallel Processing in Apache Spark

We have 5 partitions here. I can give one partition to each executor and ask them to count the lines in the given partition. Then, I will take the counts back from these executors and sum them. 

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-03%20at%209.55.11%20PM.png)  

Execute the code to count the number of lines in the RDD. 

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-03%20at%209.55.54%20PM.png)  

Now check the Spark UI to check what happens under the hood. 

Here we see ONE job, ONE stage and FIVE tasks.

  

JOB: we asked for a count and Spark started a job. A job to calculate the count. 

  

TASK: Spark breaks this JOB into TASKS because we have FIVE partitions. One counting task per partition. A task if the smallest unit of work performed by the executor. 

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-03%20at%209.58.43%20PM.png)  

I ran it in local mode and had a single executor. Hence, all of these tasks are executed by the same executor. I had five tasks and the driver executed each of them. 

  

There are two main variables to control the number of parallelism in Apache Spark. 

*   The number of partitions
    
*   The number of executors
    

E.g: If you have ten partitions, you can achieve ten parallel processes at most. However if you have just two executors, all those ten partitions will be queued to those two executors. 

  

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-03%20at%2010.02.58%20PM.png)  

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-03%20at%2010.04.20%20PM.png)  

flistRDD - It is the data a.k.a collection

.count() \- function to execute on that data

  

The data is already partitioned and distributed over the executors. Then Spark runs the function on the partition that it has and return the result. 

  

  

  

That's how Spark breaks our code and execute it in parallel. This emphasizes the importance of functional programming. 

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-03%20at%2010.07.15%20PM.png)  

Line 1 loads a text file into an RDD. It it likely that I will get 1 or 2 partitions by default. However, if we want to have 5 partitions of this data file, we can specify it. 

  

Line 2 executes a map method on the first RDD and returns a new RDD. RDDs are immutable so we cannot modify the first RDD. Instead we take the first RDD, perform a map operation and create a new RDD. The map operation splits each line into an array of words. Hence, the new RDD is a collection of Arrays. 

  

Line 3 executes another map method over the arrayRDD. This time we generate a tuple. A key value pair. I am taking the first element of the array as my key. And the value if a hardcoded numeric one.  (I am trying to count the number of different files in each directory)

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-03%20at%2010.13.21%20PM.png)  

The new kvRDD looks like this

Once I have this RDD, I can easily count the number of files. 

  

Line 4: All I have to do is to group all the values by the key and sum up these 1s.

ReduceByKey, which means group by key and sum these 1s.

  

  

Line 5: Collect all the data back from the executors to the driver. 

Note

RDDs offer two types of operations: transformations and actions. 

The transformation operation creates a new RDD  from an existing RDD. 

The actions are performed to sent results back to the driver and hence they produce a non-distributed dataset.

  

Transformations are lazy - they don't compute results until an action is called. 

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-03%20at%2010.20.14%20PM.png)  

Spark completed this JOB with two stages. We had 5 partitions so I expected 5 tasks, but since we had 2 stages we had 10 tasks, meaning 2 stages \* 5 partitions = 10 tasks.  Five tasks for each stage. 

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-03%20at%2010.22.18%20PM.png)  

Check the Spark DAG.

It shows the whole process. 

  

Stage 0 - (textFile) = File Load

map - first map operation

map - second map operation

\=> Spark was able to complete all of these in a single stage!

  

Stage 1

For the reduceByKey function Spark created a new Stage. 

  

WHY?

Explanation below:

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-03%20at%2010.26.16%20PM.png)  

Here's the initial RDD. 

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-03%20at%2010.27.19%20PM.png)  

I created five partitions 

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-03%20at%2010.27.49%20PM.png)  

Spark assigned these partitions to five executors. 

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-03%20at%2010.29.29%20PM.png)  

Then I executed my first map operation.

(Read each line and split it into individual words). Executors will perform this function on the partition that hey hold. 

  

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-03%20at%2010.31.00%20PM.png)  

Then I did another map operation - create a key value pair for each row. So far so good, there is no need to send the data from one executor to another executor or the driver. There is no need for any data movement. Therefore, Spark was able to perform these functions in a single stage!

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-03%20at%2010.33.03%20PM.png)  

Then I wanted to group the whole dataset by the key and count the number of ones for each key. However, the keys are spread across the partitions. 

  

  

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-03%20at%2010.34.38%20PM.png)  

To accomplish this task, we need to repartition the data in a way that we get all the records for a single key in one partition.  

This new partitioning is based on the key. So the old partitions will send the data to the new partitions. 

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-03%20at%2010.36.15%20PM.png)  

This is a Shuffle and Sort activity, and Spark performs it on its own behind the scenes.

  

By doing do, Spark moves the data and creates new partitions. That's why it needs a new Stage.

  

WHENEVER THERE IS A NEED TO MOVE DATA  ACROSS EXECUTORS WE NEED A NEW STAGE! SPARK WILL THEN BREAK THE JOB INTO TO STAGES. 

  

when you do groupby or join operations, Spark will create a new stage. 

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-03%20at%2010.38.50%20PM.png)  

Finally, they send the results to the driver because we executed the .collect() method.

SUMMATION 

RDDs are the core of Spark. 

An action on an RDD triggers a job. 

Spark breaks the job into stages

The shuffle activity is a reason to break the job into stages. 

Each stage is executed in parallel tasks.

The number of parallel tasks is dependent on the number of partitions. 

The degree of parallelism is also dependent on the number of available executors. 

  

How Spark Runs on a Cluster

Structured APIs take a logical operation, break it up into a logical plan, and convert that to a physical plan that actually consists of RDD operations that execute across the cluster of machines. This note focuses on how Spark actually goes about executing this code.

  

Objectives

*   The architecture and components of a Spark Application
    
*   The lifecycle of a Spark Application inside and outside of Spark
    
*   Important low-level execution properties, such as pipelining
    
*   What it takes to run a Spark Application
    

  

The Architecture of a Spark Application

  

**The Spark driver**

The driver is the process “in the driver seat” of your Spark Application. It is the controller of the execution of a Spark Application and maintains all of the state of the Spark cluster (the state and tasks of the executors). It must interface with the cluster manager in order to actually get physical resources and launch executors. At the end of the day, this is just a process on a physical machine that is responsible for maintaining the state of the application running on the cluster.

  

The Spark executors

Spark executors are the processes that perform the tasks assigned by the Spark driver. Executors have one core responsibility - take the tasks assigned by the driver, run them, and report back their state (success or failure) and results. Each Spark Application has its own, separate executor processes.

  

The cluster manager

The cluster manager is responsible for maintaining a cluster of machines that will run your Spark Application(s). Somewhat confusingly, a cluster manager will have its own “driver” (sometimes called master) and “worker” abstractions. The core difference is that these are tied to physical machines rather than processes (as they are in Spark). 

Basic cluster setup:

(the machine on the left is the Cluster Manager Driver Node. The circles represent daemon processes running on and managing each of the individual worker nodes. So far in this image, there is no Spark Application running—these are just the processes from the cluster manager.)

  

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-02%20at%208.28.25%20PM.png)  

When it comes time to actually run a Spark Application, we request resources from the cluster manager to run it. Depending on how our application is configured, this can include a place to run the Spark driver or might be just resources for the executors for our Spark Application. Over the course of Spark Application execution, the cluster manager will be responsible for managing the underlying machines that our application is running on.

Spark supports three cluster managers: a simple built-in standalone cluster manager, Apache Mesos, and Hadoop YARN.

  

Execution Modes

An execution mode gives you the power to determine where the resources are physically located when you go to run your application. 

You have three modes to choose from:

1\. Cluster mode

Most common way of running Spark Applications. In cluster mode, a user submits a pre-compiled JAR, Python script, or R script to a cluster manager. The cluster manager then launches the driver process on a worker node inside the cluster, in addition to the executor processes. This means that the cluster manager is responsible for maintaining all Spark Application–related processes. 

  

Cluster manager placed our driver on a worker node and the executors on other worker nodes:

**![](Production%20Applications.html.resources/Screen%20Shot%202019-06-02%20at%208.32.15%20PM.png)  
**

  

2\. Client mode

Client mode is nearly the same as cluster mode except that the Spark driver remains on the client machine that submitted the application. This means that the client machine is responsible for maintaining the Spark driver process, and the cluster manager maintains the executor processes.

  

The driver is running on a machine outside of the cluster but that the workers are located on machines in the cluster:

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-02%20at%208.33.58%20PM.png)  

3\. Local mode

It runs the entire Spark Application on a single machine. It achieves parallelism through threads on that single machine. This is a common way to learn Spark, to test your applications, or experiment iteratively with local development. However, we do not recommend using local mode for running production applications.

\---

The Life Cycle of a Spark Application (Outside Spark)

Illustrated example of an application run with spark-submit

We assume that a cluster is already running with four nodes, a driver (not a Spark driver but cluster manager driver) and three worker nodes.

Step-by-step Spark Application life cycle from initialization to program exit:

Lines represent network communication

Darker arrows represent communication by Spark or Spark-related processes

Dashed lines represent more general communication (like cluster management communication)

  

STEP 1: Client Request

The first step is for you to submit an actual application. This will be a pre-compiled JAR or library. At this point, you are executing code on your local machine and you’re going to make a request to the cluster manager driver node (illustration). Here, we are explicitly asking for resources for the Spark driver process only. We assume that the cluster manager accepts this offer and places the driver onto a node in the cluster. The client process that submitted the original job exits and the application is off and running on the cluster.

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-02%20at%208.39.24%20PM.png)  

  

To do this:

Code

Note

./bin/spark-submit \\

\--class <main-class> \\

\--master <master-url> \\

\--deploy-mode cluster \\

\--conf <key>=<value> \\

... # other options

<application-jar> \\

\[application-arguments\]

Client Request

STEP 2: Driver Process

Now that the driver process has been placed on the cluster, it begins running user code. This code must include a SparkSession that initializes a Spark cluster (e.g., driver + executors). The SparkSession will subsequently communicate with the cluster manager (the darker line), asking it to launch Spark executor processes across the cluster (the lighter lines). The number of executors and their relevant configurations are set by the user via the command-line arguments in the original spark-submit call.

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-02%20at%208.43.40%20PM.png)  

The cluster manager responds by launching the executor processes (assuming all goes well) and sends the relevant information about their locations to the driver process. After everything is hooked up correctly, we have a “Spark Cluster”.

  

STEP 3: Execution

Now that we have a “Spark Cluster” Spark goes about its merry way executing code. The driver and the workers communicate among themselves, executing code and moving data around. The driver schedules tasks onto each worker, and each worker responds with the status of those tasks and success or failure. 

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-02%20at%208.45.47%20PM.png)  

  

STEP 4: Completion

After a Spark Application completes, the driver process exits with either success or failure. The cluster manager then shuts down the executors in that Spark cluster for the driver. At this point, you can see the success or failure of the Spark Application by asking the cluster manager for this information.

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-02%20at%208.46.37%20PM.png)  

  

The Life Cycle of a Spark Application (Inside Spark)

This is “user-code” (the actual code that you write that defines your Spark Application). Each application is made up of one or more Spark jobs. Spark jobs within an application are executed serially (unless you use threading to launch multiple actions in parallel).

  

STEP 1:

The SparkSession

The first step of any Spark Application is creating a SparkSession. In many interactive modes, this is done for you, but in an application, you must do it manually. Some of your legacy code might use the new SparkContext pattern. This should be avoided in favor of the builder method on the SparkSession, which more robustly instantiates the Spark and SQL Contexts and ensures that there is no context conflict, given that there might be multiple libraries trying to create a session in the same Spark Application:

  

Python

Scala

Note

Errors

from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").appName("Word Count")\\

.config("spark.some.config.option", "some-value")\\

.getOrCreate()

import org.apache.spark.sql.SparkSession

val spark = SparkSession.builder().appName("Databricks Spark Example")

.config("spark.sql.warehouse.dir", "/user/hive/warehouse")

.getOrCreate()

Creating a SparkSession

ERROR

ImportError: cannot import name 'SparkSession' from 'pyspark'

After you have a SparkSession, you should be able to run your Spark code. From the SparkSession, you can access all of low-level and legacy contexts and configurations accordingly, as well. 

STEP 2:

The SparkContext

A SparkContext object within the SparkSession represents the connection to the Spark cluster. This class is how you communicate with some of Spark’s lower-level API’s, such as RDDs. It is commonly stored as the variable sc in older examples and documentation. Through a SparkContext, you can create RDDs, accumulators, and broadcast variables, and you can run code on the cluster. For the most part, you should not need to explicitly initialize a SparkContext; you should just be able to access it through the SparkSession. If you do want to create it, you should create it in the most general way, through the getOrCreate method:

// in Scala

import org.apache.spark.SparkContext

val sc = SparkContext.getOrCreate()

  

How Spark Runs on a Cluster

Structured APIs take a logical operation, break it up into a logical plan, and convert that to a physical plan that actually consists of RDD operations that execute across the cluster of machines. This note focuses on how Spark actually goes about executing this code.

  

Objectives

*   The architecture and components of a Spark Application
    
*   The lifecycle of a Spark Application inside and outside of Spark
    
*   Important low-level execution properties, such as pipelining
    
*   What it takes to run a Spark Application
    

  

The Architecture of a Spark Application

  

**The Spark driver**

The driver is the process “in the driver seat” of your Spark Application. It is the controller of the execution of a Spark Application and maintains all of the state of the Spark cluster (the state and tasks of the executors). It must interface with the cluster manager in order to actually get physical resources and launch executors. At the end of the day, this is just a process on a physical machine that is responsible for maintaining the state of the application running on the cluster.

  

The Spark executors

Spark executors are the processes that perform the tasks assigned by the Spark driver. Executors have one core responsibility - take the tasks assigned by the driver, run them, and report back their state (success or failure) and results. Each Spark Application has its own, separate executor processes.

  

The cluster manager

The cluster manager is responsible for maintaining a cluster of machines that will run your Spark Application(s). Somewhat confusingly, a cluster manager will have its own “driver” (sometimes called master) and “worker” abstractions. The core difference is that these are tied to physical machines rather than processes (as they are in Spark). 

Basic cluster setup:

(the machine on the left is the Cluster Manager Driver Node. The circles represent daemon processes running on and managing each of the individual worker nodes. So far in this image, there is no Spark Application running—these are just the processes from the cluster manager.)

  

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-02%20at%208.28.25%20PM.png)  

When it comes time to actually run a Spark Application, we request resources from the cluster manager to run it. Depending on how our application is configured, this can include a place to run the Spark driver or might be just resources for the executors for our Spark Application. Over the course of Spark Application execution, the cluster manager will be responsible for managing the underlying machines that our application is running on.

Spark supports three cluster managers: a simple built-in standalone cluster manager, Apache Mesos, and Hadoop YARN.

  

Execution Modes

An execution mode gives you the power to determine where the resources are physically located when you go to run your application. 

You have three modes to choose from:

1\. Cluster mode

Most common way of running Spark Applications. In cluster mode, a user submits a pre-compiled JAR, Python script, or R script to a cluster manager. The cluster manager then launches the driver process on a worker node inside the cluster, in addition to the executor processes. This means that the cluster manager is responsible for maintaining all Spark Application–related processes. 

  

Cluster manager placed our driver on a worker node and the executors on other worker nodes:

**![](Production%20Applications.html.resources/Screen%20Shot%202019-06-02%20at%208.32.15%20PM.png)  
**

  

2\. Client mode

Client mode is nearly the same as cluster mode except that the Spark driver remains on the client machine that submitted the application. This means that the client machine is responsible for maintaining the Spark driver process, and the cluster manager maintains the executor processes.

  

The driver is running on a machine outside of the cluster but that the workers are located on machines in the cluster:

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-02%20at%208.33.58%20PM.png)  

3\. Local mode

It runs the entire Spark Application on a single machine. It achieves parallelism through threads on that single machine. This is a common way to learn Spark, to test your applications, or experiment iteratively with local development. However, we do not recommend using local mode for running production applications.

\---

The Life Cycle of a Spark Application (Outside Spark)

Illustrated example of an application run with spark-submit

We assume that a cluster is already running with four nodes, a driver (not a Spark driver but cluster manager driver) and three worker nodes.

Step-by-step Spark Application life cycle from initialization to program exit:

Lines represent network communication

Darker arrows represent communication by Spark or Spark-related processes

Dashed lines represent more general communication (like cluster management communication)

  

STEP 1: Client Request

The first step is for you to submit an actual application. This will be a pre-compiled JAR or library. At this point, you are executing code on your local machine and you’re going to make a request to the cluster manager driver node (illustration). Here, we are explicitly asking for resources for the Spark driver process only. We assume that the cluster manager accepts this offer and places the driver onto a node in the cluster. The client process that submitted the original job exits and the application is off and running on the cluster.

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-02%20at%208.39.24%20PM.png)  

  

To do this:

Code

Note

./bin/spark-submit \\

\--class <main-class> \\

\--master <master-url> \\

\--deploy-mode cluster \\

\--conf <key>=<value> \\

... # other options

<application-jar> \\

\[application-arguments\]

Client Request

STEP 2: Driver Process

Now that the driver process has been placed on the cluster, it begins running user code. This code must include a SparkSession that initializes a Spark cluster (e.g., driver + executors). The SparkSession will subsequently communicate with the cluster manager (the darker line), asking it to launch Spark executor processes across the cluster (the lighter lines). The number of executors and their relevant configurations are set by the user via the command-line arguments in the original spark-submit call.

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-02%20at%208.43.40%20PM.png)  

The cluster manager responds by launching the executor processes (assuming all goes well) and sends the relevant information about their locations to the driver process. After everything is hooked up correctly, we have a “Spark Cluster”.

  

STEP 3: Execution

Now that we have a “Spark Cluster” Spark goes about its merry way executing code. The driver and the workers communicate among themselves, executing code and moving data around. The driver schedules tasks onto each worker, and each worker responds with the status of those tasks and success or failure. 

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-02%20at%208.45.47%20PM.png)  

  

STEP 4: Completion

After a Spark Application completes, the driver process exits with either success or failure. The cluster manager then shuts down the executors in that Spark cluster for the driver. At this point, you can see the success or failure of the Spark Application by asking the cluster manager for this information.

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-02%20at%208.46.37%20PM.png)  

  

The Life Cycle of a Spark Application (Inside Spark)

This is “user-code” (the actual code that you write that defines your Spark Application). Each application is made up of one or more Spark jobs. Spark jobs within an application are executed serially (unless you use threading to launch multiple actions in parallel).

  

STEP 1:

The SparkSession

The first step of any Spark Application is creating a SparkSession. In many interactive modes, this is done for you, but in an application, you must do it manually. Some of your legacy code might use the new SparkContext pattern. This should be avoided in favor of the builder method on the SparkSession, which more robustly instantiates the Spark and SQL Contexts and ensures that there is no context conflict, given that there might be multiple libraries trying to create a session in the same Spark Application:

  

Python

Scala

Note

Errors

from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local").appName("Word Count")\\

.config("spark.some.config.option", "some-value")\\

.getOrCreate()

import org.apache.spark.sql.SparkSession

val spark = SparkSession.builder().appName("Databricks Spark Example")

.config("spark.sql.warehouse.dir", "/user/hive/warehouse")

.getOrCreate()

Creating a SparkSession

ERROR

ImportError: cannot import name 'SparkSession' from 'pyspark'

After you have a SparkSession, you should be able to run your Spark code. From the SparkSession, you can access all of low-level and legacy contexts and configurations accordingly, as well. 

STEP 2:

The SparkContext

A SparkContext object within the SparkSession represents the connection to the Spark cluster. This class is how you communicate with some of Spark’s lower-level API’s, such as RDDs. It is commonly stored as the variable sc in older examples and documentation. Through a SparkContext, you can create RDDs, accumulators, and broadcast variables, and you can run code on the cluster. For the most part, you should not need to explicitly initialize a SparkContext; you should just be able to access it through the SparkSession. If you do want to create it, you should create it in the most general way, through the getOrCreate method:

// in Scala

import org.apache.spark.SparkContext

val sc = SparkContext.getOrCreate()

  

  

Logical Instructions

Logical instructions and physical execution

#Example in Python

  

Python

Example

df1 = spark.range(2, 10000000, 2)

df2 = spark.range(2, 10000000, 4)

step1 = df1.repartition(5)

step12 = df2.repartition(6)

step2 = step1.selectExpr("id \* 5 as id")

step3 = step2.join(step12, \["id"\])

step4 = step3.selectExpr("sum(id)")

step4.collect() # Result: 2500000000000

  

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-03%20at%201.14.20%20AM.png)  

  

Do a three-step job: using a simple DataFrame, we’ll repartition it, perform a value-by-value manipulation, and then aggregate some values and collect the final result.

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-03%20at%201.15.42%20AM.png)  

Explain Plan

  

\->

to ground the understanding of the physical execution plan.

  

Spark UI: localhost:4040

A Spark job

In general, there should be **one Spark job for one action**. **Actions always return results.**

Each **job breaks down into a series of stages**, the number of **which depends on the number of shuffle operations** that need to take place.

The above job breaks down into the following stages and tasks:

• Stage 1 with 8 Tasks

• Stage 2 with 8 Tasks

• Stage 3 with 6 Tasks

• Stage 4 with 5 Tasks

• Stage 5 with 200 Tasks

• Stage 6 with 1 Task

  

Stages

Stages in Spark represent groups of tasks that can be executed together to compute the same operation on multiple machines.

In general, Spark will try to pack as much work as possible (i.e., as many transformations as possible inside your job) into the same stage, but the engine starts new stages after operations called shuffles.

A shuffle represents a physical repartitioning of the data---for example, sorting a DataFrame, or grouping data that was loaded from a file by key (which requires sending records with the same key to the same node).

This type of repartitioning requires coordinating across executors to move data around. Spark starts a new stage after each shuffle, and keeps track of what order the stages must run in to compute the final result.

  

In the job we looked at earlier, stage one and two correspond to the range that you perform in order to create DataFrames. By default when you create a DataFrame with range, it has eight partitions. The next step is the repartitioning. This changes the number of partitions by shuffling the data. These DataFrames are shuffled into six partitions and five partitions, corresponding to the number of tasks in stages three and four.

Stages three and four perform on each of those DataFrames and the end of the stage represents the join (a shuffle). Suddenly, we have 200 tasks. This is because of a Spark SQL configuration. The spark.sql.shuffle.partitions default value is 200, which means that when there is a shuffle performed during execution, it outputs 200 shuffle partitions by default. You can change this value, and the number of output partitions will change.

  

A good rule of thumb is that the number of partitions should be larger than the number of executors on your cluster, potentially by multiple factors depending on the workload. If you are running code on your local machine, it would behoove you to set this value lower because your local machine is unlikely to be able to execute that number of tasks in parallel. This is more of a default for a cluster in which there might be many more executor cores to use. Regardless of the number of partitions, that entire stage is computed in parallel. The final result aggregates those partitions individually, brings them all to a single partition before finally sending the final result to the driver.

  

Tasks

Stages in Spark consist of tasks. Each task corresponds to a combination of blocks of data and work to execute that runs on a single executor. If there is one big partition in our dataset, we will have one task. If there are 1,000 little partitions, we will have 1,000 tasks that can be executed in parallel. A task is just a unit of computation applied to a unit of data (the partition). Partitioning your data into a greater number of partitions means that more can be executed in parallel. This is not a panacea, but it is a simple place to begin with optimization.

  

Execution Details

Tasks and stages in Spark have some important properties that are worth reviewing before we close out this chapter. First, Spark automatically pipelines stages and tasks that can be done together, such as a map operation followed by another map operation. Second, for all shuffle operations, Spark writes the data to stable storage (e.g., disk), and can reuse it across multiple jobs. 

  

Pipelining

An important part of what makes Spark an “in-memory computation tool” is that unlike the tools that came before it (e.g., MapReduce), Spark performs as many steps as it can at one point in time before writing data to memory or disk. One of the key optimizations that Spark performs is pipelining, which occurs at and below the RDD level. With pipelining, any sequence of operations that feed data directly into each other, without needing to move it across nodes, is collapsed into a single stage of tasks that do all the operations together. For example, if you write an RDD-based program that does a map, then a filter, then another map, these will result in a single stage of tasks that immediately read each input record, pass it through the first map, pass it through the filter and pass it through the last map function if needed. This pipelined version of the computation is much faster than writing the intermediate results to memory or disk after each step. The same kind of pipelining happens for a DataFrame or SQL computation that does a select, filter and select. From a practical point of view, pipelining will be transparent to you as you write an application—the Spark runtime will automatically do it—but you will see it if you ever inspect your application through the Spark UI or through its log files, where you will see that multiple RDD or DataFrame operations were pipelined into a single stage.

  

Shuffle Persistence

The second property you’ll sometimes see is shuffle persistence. When Spark needs to run an operation that has to move data across nodes, such as a reduce-by-key operation (where input data for each key first needs to first be brought together from many odes), the engine can’t perform pipelining anymore, and instead it performs a cross-network shuffle. Spark always executes shuffles by first having the “source” tasks (those sending data) write shuffle files to their local disks during their execution stage. Then, the stage that does the grouping and reduction launches and runs tasks that fetch their corresponding records from each shuffle file and performs that computation (e.g., fetches and processes the data for a specific range of keys). Saving the shuffle files to disk lets Spark run this stage later in time than the source stage (e.g., if there are not enough executors to run both at the same time), and also lets the engine re-launch reduce tasks on failure without rerunning all the input tasks.

  

  

Deploying Spark

Explore the infrastructure you need in place for you and your team to be able to run Spark Applications:

• Cluster deployment choices

• Spark’s different cluster managers

• Deployment considerations and configuring deployments.

  

Detail about deploying Spark with actionable examples: [http://spark.apache.org/docs/latest/cluster-overview.html](http://spark.apache.org/docs/latest/cluster-overview.html)

  

Cluster managers:

• Standalone mode

• Hadoop YARN

• Apache Mesos

//Cluster managers maintain a set of machines onto which you can deploy Spark Applications. 

  

Where to Deploy Your Cluster to Run Spark Applications

There are two high-level options for where to deploy Spark clusters: deploy in an on-premises cluster or in the public cloud. 

  

1.  On-Premises Cluster Deployments
    

For organizations that already manage their own datacenters. An on-premises cluster gives you full control over the hardware used, enabling optimizing performance for your specific workload. 

Challenges, especially when it comes to data analytics workloads like Spark: Firstly, your cluster is fixed in size, whereas the resource demands of data analytics workloads are often elastic. eIf you make your cluster too small, it will be hard to launch the occasional very large analytics query or training job for a new machine learning model, whereas if you make it large, you will have resources sitting idle. Secondly, you need to select and operate your own storage system, such as a Hadoop file system or scalable key-value store. This includes setting up georeplication and disaster recovery if required. If you are going to deploy on-premises, the best way to combat the resource utilization problem is to use a cluster manager that allows you to run many Spark applications and dynamically reassign resources between them, or even allows non-Spark applications on the same cluster. All of Spark’s supported cluster managers allow multiple concurrent applications, but YARN and Mesos have better support for dynamic sharing and also additionally support non-Spark workloads. Handling resource sharing is likely going to be the biggest difference your users see day to day with Spark on-premise versus in the cloud: in public clouds, it’s easy to give each application its own cluster of exactly the required size for just the duration of that job. For storage, you have several different options, but covering all the trade-offs and operational details in depth would probably require its own book. The most common storage systems used for Spark are distributed file systems such as Hadoop’s HDFS and key-value stores such as Apache Cassandra. Streaming message bus systems such as Apache Kafka are also often used for ingesting data. All these systems have varying degrees of support for management, backup and georeplication, sometimes built into the system and sometimes only through third-party commercial tools. Before choosing a storage option, we recommend evaluating the performance of its Spark connector and evaluating the available management tools.

  

2.  Spark in the Cloud
    

The public cloud has several advantages when it comes to big data workloads. First, resources can belaunched and shut down elastically, so you can run that occasional “monster” job that takes hundreds of machines for a few hours without having to pay for them all the time. Even for normal operation, you can choose a different type of machine and cluster size for each application to optimize its cost-performance — for example, launch machines with Graphics Processing Units (GPUs) just for your deep learning jobs. Second, public clouds include low-cost, georeplicated storage that makes it easier to manage large amounts of data. Many companies looking to migrate to the cloud imagine they’ll run their applications in the same way that they run their on-premises clusters. All the major cloud providers (Amazon Web Services \[AWS\], Microsoft Azure, Google Cloud Platform \[GCP\], and IBM Bluemix) include managed Hadoop clusters for their customers, which provide HDFS for storage as well as Apache Spark. This is actually not a great way to run Spark in the cloud, however, because by using a fixed-size cluster and file system, you are not going to be able to take advantage of elasticity. Instead, it is generally a better idea to use global storage systems that are decoupled from a specific cluster, such as Amazon S3, Azure Blob Storage or Google Cloud Storage, and spin up machines dynamically for each Spark workload. With decoupled compute and storage, you will be able to pay for computing resources only when needed, scale them up dynamically, and mix different hardware types. Basically, keep in mind that running Spark in the cloud need not mean migrating an on-premises installation to virtual machines: you can run Spark natively against cloud storage to take full advantage of the elasticity, cost-saving and management tools of the cloud without having to manage an on-premise computing stack within your cloud environment. Several companies provide “cloud-native” Spark-based services, and all installations of Apache Spark can of course connect to cloud storage. Databricks is one example of a service provider built specifically for Spark in the cloud. Databricks provides a simple way to run Spark workloads without the heavy baggage a Hadoop insallation. The company provides a number of features for running Spark more efficiently in the cloud, such as auto-scaling, auto-termination of clusters, and optimized connectors to cloud storage, as well as a collaborative environment for working on notebooks and standalone jobs. If you run Spark in the cloud, much of the content in this chapter might not be relevant because you can often create a separate, short-lived Spark cluster for each job you execute. In that case, the standalone cluster manager is likely the easiest to use.However, you may still want to read this content if you’d like to share a longer-lived cluster among many applications, or to install Spark on virtual machines yourself.

  

Cluster Managers

Unless you are using a high-level managed service, you will have to decide on the cluster manager to use for Spark. 

Spark supported cluster managers: standalone clusters, Hadoop YARN and Mesos. 

  

1.  Standalone Mode Spark’s standalone cluster manageris a lightweight platform built specifically for Apache Spark workloads. Using it, you can run multiple Spark Applications on the same cluster. It also provides simple interfaces for doing so but can scale to large Spark workloads. The main disadvantage of the standalone mode is that it’s more limited than the other cluster managers — in particular, your cluster can only run Spark. It’s probably the best starting point if you just want to quickly get Spark running on a cluster, however, and you do not have experience using YARN or Mesos. Starting a standalone cluster requires provisioning the machines for doing so. That means starting them up, ensuring that they can talk to one another over the network, and getting the version of Spark you would like to run on those sets of machines. After that, there are two ways to start the cluster: by hand or using built-in launch scripts. Let’s first launch a cluster by hand. The first step is to start the master process on the machine that we want that to run on, using the following command: $SPARK\_HOME/sbin/start-master.sh When we run this command, the cluster manager master process will start up on that machine. Once started, the master prints out a [spark://HOST:PORT](spark://HOST:PORT) URI. You use thiswhen you start each of the worker nodes of the cluster, and you can use it as the master argument to your SparkSession on application initialization. You can also find this URI on the master’s web UI, which is [http://master-ip-address:8080](http://master-ip-address:8080/) by default. Withthat URI, start the worker nodes by logging in to each machine and running the following script using the URI you just received from the master node. The master machine must be available on the network of the worker nodes you are using, and the port must be open on the master node, as well. $SPARK\_HOME/sbin/start-slave.sh <master-spark-URI> As soon as you’ve run that on another machine, you have a Spark cluster running! This process is naturally a bit manual; thankfully there are scripts that can help to automate this process.
    

Cluster launch scripts

You can configure cluster launch scripts that can automate the launch of standalone clusters. To do this, create a file called conf/slaves in your Spark directory that will contain the hostnames of all the machines on which you intend to start Spark workers, one per line. If this file does not exist, everything will launch locally. When you go to actually start the cluster, the master machine will access each of the worker machines via Secure Shell (SSH). By default, SSH is run in parallel and requires that you configure password-less (using a private key) access. If you do not have a password-less setup, you can set the environment variable SPARK\_SSH\_FOREGROUND and serially provide a password for each worker. After you set up this file, you can launch or stop your cluster by using the following shell scripts, based on Hadoop’s deploy scripts, and available in $SPARK\_HOME/sbin:

\-$SPARK\_HOME/sbin/start-master.sh

Starts a master instance on the machine on which the script is executed.

$SPARK\_HOME/sbin/start-slaves.sh

Starts a slave instance on each machine specified in the conf/slaves file.

$SPARK\_HOME/sbin/start-slave.sh

Starts a slave instance on the machine on which the script is executed.

$SPARK\_HOME/sbin/start-all.sh

Starts both a master and a number of slaves as described earlier.

$SPARK\_HOME/sbin/stop-master.sh

Stops the master that was started via the bin/start-master.sh script.

$SPARK\_HOME/sbin/stop-slaves.sh

Stops all slave instances on the machines specified in the conf/slaves file.

$SPARK\_HOME/sbin/stop-all.sh Stops both the master and the slaves as described earlier.

  

Standalone cluster congurations 

Standalone clusters have a number of configurations that you can use to tune your application. These control everything from what happens to old files on each worker for terminated applications to the worker’s core and memory resources. These are controlled via environment variables or via application properties. Due to space limi‐ tations, we cannot include the entire configuration set here. Please see the relevant table on Standalone Environment Variables in the Spark documentation.

[http://spark.apache.org/docs/latest/spark-standalone.html#cluster-launch-scripts](http://spark.apache.org/docs/latest/spark-standalone.html#cluster-launch-scripts)

[http://spark.apache.org/docs/latest/index.html](http://spark.apache.org/docs/latest/index.html)

  

Submitting applications

After you create the cluster, you can submit applications to it using the spark:// URI of the maste. You can do this either on the master node itself or another machine using spark-submit.

  

2.  Spark on YARN
    

Hadoop YARN is a framework for job scheduling and cluster resource management. Even though Spark is often (mis)classified as a part of the “Hadoop Ecosystem,” in reality, Spark has little to do with Hadoop. Spark does natively support the Hadoop YARN cluster manager but it requires nothing from Hadoop itself. You can run your Spark jobs on Hadoop YARN by specifying the master as YARN in the spark-submit command-line arguments. Just like with standalone mode, there are a number of knobs that you are able to tune according to what you would like the cluster to do. The number of knobs is naturally larger than that of Spark’s standalone mode because Hadoop YARN is a generic scheduler for a large number of different execution frameworks. Setting up a YARN cluster is beyond the scope of this book, but there are some great books on the topic as well as managed services that can simplify this experience. Submitting applications When submitting applications to YARN, the core difference from other deployments is that --master will become yarn as opposed the the master node IP, as it is in stand‐ alone mode. Instead, Spark will find the YARN configuration files using the environ‐ ment variable HADOOP\_CONF\_DIR or YARN\_CONF\_DIR.

There are two deployment modes that you can use to launch Spark on YARN. Cluster mode has the spark driver as a process managed by the YARN cluster, and the client can exit after creating the application. In client mode, the driver will run in the client process and therefore YARN will be responsible only for granting executor resources to the application, not maintaining the master node. Also of note is that in cluster mode, Spark doesn’t necessarily run on the same machine on which you’re executing. Therefore libraries and external jars must be distributed manually or through the --jars command-line argument.

  

  

Configuring Spark on YARN Applications

Deploying Spark as YARN applications requires you to understand the variety of different configurations and their implications for your Spark applications. This section covers some of the basic configurations best practices and includes references to some of the important configuration for running your Spark applications.

Hadoop configurations

If you plan to read and write from HDFS using Spark, you need to include two Hadoop configuration files on Spark’s classpath: hdfs-site.xml, which provides default behaviors for the HDFS client; and core-site.xml, which sets the default file‐ system name. The location of these configuration files varies across Hadoop versions, but a common location is inside of /etc/hadoop/conf. Some tools create these configu‐ rations on the fly, as well, so it’s important to understand how your managed service might be deploying these, as well. To make these files visible to Spark, set HADOOP\_CONF\_DIR in $SPARK\_HOME/spark- env.sh to a location containing the configuration files or as a environment variable when you go to spark-submit your application.

Application properties for YARN 

There are a number of Hadoop-related configurations and things that come up that largely don’t have much to do with Spark, just running or securing YARN in a way that influences how Spark runs. Due to space limitations, we cannot include the configuration set here.

[http://spark.apache.org/docs/latest/running-on-yarn.html#configuration](http://spark.apache.org/docs/latest/running-on-yarn.html#configuration)

[http://spark.apache.org/docs/latest/index.html](http://spark.apache.org/docs/latest/index.html)

  

  

  

3.  Spark on Mesos
    

Apache Mesos is another clustering system that Spark can run on. A “fun fact” about Mesos is that the project was also started by many of the original authors of Spark, including one of the authors of this book. In the Mesos project’s own words  Apache Mesos abstracts CPU, memory, storage, and other compute resources away from machines (physical or virtual), enabling fault-tolerant and elastic distributed systems to easily be built and run effectively. For the most part, Mesos intends to be a datacenter scale-cluster manager that man‐ ages not just short-lived applications like Spark, but long-running applications like web applications or other resource interfaces. Mesos is the heaviest-weight cluster manager, simply because you might choose this cluster manager only if your organization already has a large-scale deployment of Mesos, but it makes for a good cluster

manager nonetheless. Mesos is a large piece of infrastructure, and unfortunately there’s simply too much information for us to cover how to deploy and maintain mesos clusters. There are many great books on the subject for that, including Dipa Dubhashi and Akhil Das’s Mastering Mesos, (O’Reilly, 2016). The goal here is to bring up some of the considerations that you’ll need to think about when running Spark Applications on Mesos. For instance, one common thing you will hear about Spark on Mesos is fine-grained versus coarse-grained mode. Historically Mesos supported a variety of different modes (fine-grained and coarse-grained), but at this point, it supports only coarse- grained scheduling (fine-grained has been deprecated). Coarse-grained mode means that each Spark executor runs as a single Mesos task. Spark executors are sized according to the following application properties:

• spark.executor.memory

• spark.executor.cores

• spark.cores.max/spark.executor.cores

Submitting applications

Submitting applications to a Mesos cluster is similar to doing so for Spark’s other cluster managers. For the most part you should favor cluster mode when using Mesos. Client mode requires some extra configuration on your part, especially with regard to distributing resources around the cluster. For instance, in client mode, the driver needs extra configuration information in spark-env.sh to work with Mesos. In spark-env.sh set some environment variables:

export MESOS\_NATIVE\_JAVA\_LIBRARY=<path to libmesos.so>

This path is typically <prex>/lib/libmesos.so where the prefix is /usr/local by default.On Mac OS X, the library is called libmesos.dylib instead of libmesos.so.

export SPARK\_EXECUTOR\_URI=<URL of spark-2.2.0.tar.gz uploaded above>

Finally, set the Spark Application property spark.executor.uri to <URL of spark-2.2.0.tar.gz>. Now, when starting a Spark application against the cluster,pass a mesos:// URL as the master when creating a SparkContex, and set that property as a parameter in your SparkConf variable or the initialization of a SparkSession.

Mesos configuration

[http://spark.apache.org/docs/latest/running-on-mesos.html#configuration](http://spark.apache.org/docs/latest/running-on-mesos.html#configuration)

[http://spark.apache.org/docs/latest/index.html](http://spark.apache.org/docs/latest/index.html)

  

Secure Deployment Configurations

Spark also provides some low-level ability to make your applications run more securely, especially in untrusted environments. Note that the majority of this setup will happen outside of Spark. These configurations are primarily network-based to help Spark run in a more secure manner. This means authentication, network encryption, and setting TLS and SSL configurations. Due to space limitations, we cannot include the entire configuration set here.

[http://spark.apache.org/docs/latest/configuration.html#security](http://spark.apache.org/docs/latest/configuration.html#security)

[http://spark.apache.org/docs/latest/index.html](http://spark.apache.org/docs/latest/index.html)

  

Cluster Networking Configurations

Just as shuffles are important, there can be some things worth tuning on the network. This can also be helpful when performing custom deployment configurations for your Spark clusters when you need to use proxies in between certain nodes. These should not be the first configurations you go to tune if you’re looking to increase. Spark’s performance, but may come up in custom deployment scenarios.Due to space limitations, we cannot include the entire configuration set here.

[http://spark.apache.org/docs/latest/configuration.html#networking](http://spark.apache.org/docs/latest/configuration.html#networking)

[http://spark.apache.org/docs/latest/index.html](http://spark.apache.org/docs/latest/index.html)

  

Application Scheduling

Spark has several facilities for scheduling resources between computations. First, recall that, as described earlier in the book, each Spark Application runs an independent set of executor processes. Cluster managers provide the facilities for scheduling across Spark applications. Second, within each Spark application, multiple jobs (i.e., Spark actions) may be running concurrently if they were submitted by different threads. This is common if your application is serving requests over the network. Spark includes a fair scheduler to schedule resources within each application. We introduced this topic in the previous chapter. If multiple users need to share your cluster and run different Spark Applications, there are different options to manage allocation, depending on the cluster manager. The simplest option, available on all cluster managers, is static partitioning of resources. With this approach, each application is given a maximum amount of resources that it can use, and holds onto those resources for the entire duration. In spark-submit there are a number of properties that you can set to control the resource allocation of a particular application. In addition, dynamic allocation (described later in this section) can be turned on to let applications scale up and down dynamically based on their current number of pending tasks. If, instead, you want users to be able to share memory and executor resources in a fine-grained manner, you can launch a single Spark Application and use thread scheduling within it to serve multiple requests in parallel.

  

Dynamic Allocation

If you would like to run multiple Spark Applications on the same cluster, Spark provides a mechanism to dynamically adjust the resources your application occupies

based on the workload. This means that your application can give resources back to the cluster if they are no longer used, and request them again later when there is demand. This feature is particularly useful if multiple applications share resources in your Spark cluster. This feature is disabled by default and available on all coarse-grained cluster managers; that is, standalone mode, YARN mode, and Mesos coarse-grained mode. There are two requirements for using this feature. First, your application must set spark.dynamicAllocation.enabled to true. Second, you must set up an external shuffle service on each worker node in the same cluster and set spark.shuffle.ser‐ vice.enabled to true in your application. The purpose of the external shuffle service is to allow executors to be removed without deleting shuffle files written by them. This is set up differently for each cluster manager. Due to space limitations, we cannot include the configuration set for dynamic allocation.

[http://spark.apache.org/docs/latest/job-scheduling.html#configuration-and-setup](http://spark.apache.org/docs/latest/job-scheduling.html#configuration-and-setup)

[http://spark.apache.org/docs/latest/job-scheduling.html#dynamic-resource-allocation](http://spark.apache.org/docs/latest/job-scheduling.html#dynamic-resource-allocation)

  

Miscellaneous Considerations

YARN is great for HDFS-based applications but is not commonly used for much else. Additionally, it’s not well designed to support the cloud, bacause it expects information to be available on HDFS. Also, compute and storage is largely coupled together, meaning that scaling your cluster involves scaling both storage and compute instead of just one or the other. Mesos does improve on this a bit conceptually and it supports a wide range of application types but it still requires pre-provisioning machines and, in some sense, requires buy-in at a much larger scale. For instance, it doesn’t really make sense to have a Mesos cluster for only running Spark Applications. Spark standalone mode is the lightest-weight cluster manager and is relatively simple to understand and take advantage of, but then you’re going to be building more application management infrastructure like that that you might get from using YARN or Mesos.

  

Another challenge is managing different Spark versions. You’re hands are largely tied if you want to try to run a variety of different applications running different Spark versions, and unless you use a well-managed service, you’re going to need to spend a fair amount of time either managing different setup scripts for different Spark serv‐ ices or removing the ability for your users to use a variety of different Spark applica‐ tions. Regardless of the cluster manager that you choose, you’re going to want to consider how you’re going to set up logging, store logs for future reference, and allow end users to debug their applications. These are more “out of the box” for YARN or Mesos and might need some tweaking if you’re using standalone. One thing you might want to consider—or that might influence your decision making—is maintaining a metastore in order to maintain metadata about your stored datasets, such as a table catalog. We saw how this comes up in Spark SQL when we are creating and maintaining tables. Maintaining an Apache Hive metastore, a topic beyond the scope of this book, might be something that’s worth doing to facilitate more productive, cross-application referencing to the same datasets.

  

Depending on your workload, it might be worth considering using Spark’s external shuffle service. Typically Spark stores shuffle blocks (shuffle output) on a local disk on that particular node. An external shuffle service allows for storing those shuffle blocks so that they are available to all executors, meaning that you can arbitrarily kill executors and still have their shuffle outputs available to other applications. Finally, you’re going to need to configure at least some basic monitoring solution and help users debug their Spark jobs running on their clusters. This is going to vary across cluster management options

  

IMPORTANT: [https://stackoverflow.com/questions/43802809/difference-between-sparkcontext-javasparkcontext-sqlcontext-and-sparksession](https://stackoverflow.com/questions/43802809/difference-between-sparkcontext-javasparkcontext-sqlcontext-and-sparksession)

  

  

Monitoring and Debugging

  

_Components of a Spark application that you can monitor_

**![](Production%20Applications.html.resources/Screen%20Shot%202019-06-09%20at%206.12.07%20PM.png)**

  

*   The Monitoring Landscape
    
    Spark Application and Jobs: Spark UI and Spark logs report information about the applications currently running at the level of concepts in Spark such as RDDs and query plans. 
    
      
    

*   JVM: Spark runs the executors in individual Java Virtual Machines (JVMs). Therefore, the next level of detail would be to monitor the individual virtual machines (VMs) to better understand how your code is running. This is particularly useful when you’re creating lots of objects through something like Datasets or Resilient Distributed Datasets (RDDs). JVM utilities such as jstack for providing stack traces, jmap for creating heap-dumps, jstat for reporting time–series statistics andjconsole for visually exploring various JVM properties are useful for those comfortable with JVM internals. You can also use a tool like jvisualvm to help profile Spark jobs. Some of this information is provided in the Spark UI, but for very low-level debugging, it might be worth using some of the aforementioned tools.
    
*   OS/Machine: The JVMs run on a host operating system (OS) and it’s well worth monitoring the state of those machines to ensure that they are healthy. This includes monitoring things like CPU, network, and IO. These are often reported in cluster-level monitoring solutions; however, there are more specific tools that you can use including dstat, iostat, and iotop.
    
*   Cluster: Naturally, we can monitor the cluster on which our Spark Application(s) will run. This might be a YARN, Mesos, or standalone cluster. Usually it’s pretty important to have some sort of monitoring solution here because, somewhat obviously, if your cluster is not working, you should probably know pretty quickly. Some popular cluster-level monitoring tools include Ganglia and Prometheus.
    

  

What to Monitor

You must monitor: 

1.  the processes running your application - at the level of CPU usage, memory usage etc.
    
2.  the query execution inside it, such as jobs and tasks.
    

  

Driver and Execution Processes

Driver - this is where all the state of your application lives - must run in a stable manner.

Spark has a configurable metrics system based on the Dropwizard Metrics Library. The metrics system is configured via a configuration file that Spark expects to be present at $SPARK\_HOME/conf/metrics.properties .   (A custom file location can be specified vi the spark.metrics.conf configuration property. These metrics can be output to a variety of different sinks including cluster monitoring solutions like Ganglia.

  

Queries, Jobs, Stages and Tasks

Spark Logs: Most powerful way to monitor Spark is through its log files. (Python won't be able to intergrrate directly with SPark's java-based logging library. Using Python's logging module or even a simple print statement will still print the results to standard error and make them easy to find. 

To change Spark's log level, run the following command:

spark.sparkContext.setLogLevel("INFO") .   ->This allows you to read the logs and if you use an application template you can log your own relevant information along with these logs allowing to inspect both your application and Spark. 

It's advised to collect logs over time to reference them in the future. - e.g when the application crashes and you want to debug why without access to the now-crashed application. You also may ship logs off the machine they were written on to hold onto them if a machine crashes or gets shut down. 

  

The Spark UI

Visual way to understand running applications as well as metrics about Spark workload at the Spark and JVM level. Every SparkContext running launches a  web UI, by default on port 4040. In local mode - navigate to [https://localhost:4040](https://localhost:4040/) to see the UI. If running multiple applications they will launch web UIs on increasing port numbers (4041, 4042...). Cluster managers will also link to each application's web UI from their own UI. 

  

![](Production%20Applications.html.resources/sparkuitabs.png)  

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-09%20at%206.13.09%20PM.png)

  

**Walkthrough**

  

**Python**

**Note - Walkthrough**

spark.read\\

.option("header", "true")\\

.csv("/data/retail-data/all/online-retail-dataset.csv")\\

.repartition(2)\\

.selectExpr("instr(Description, 'GLASS') >= 1 as is\_glass")\\

.groupBy("is\_glass")\\

.count()\\

.collect()

This results in three rows of various values. This code kicks off a SQL query.

  

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-09%20at%206.15.01%20PM.png)

The first thing you see is an **aggregate statistics** about this **query**:

Submitted Time: 2017/04/08 16:24:41

Duration: 2 s

Succeeded Jobs: 2

  

  

**Each blue box in these tabs represent a stage of ****Spark tasks**. **The entire group of these stages represent our Spark job.**

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-09%20at%206.18.24%20PM.png)

**Stage 1**

The box on top, labeled **WholeStateCodegen**, represents a **full scan of the CSV file**. The **box below** that represents a **shuffle** that we forced when we called repartition. This turned our original dataset (of a yet to be specified number of partitions) into two partitions.

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-09%20at%206.19.28%20PM.png)

**Stage 2**

**The next step is our projection (selecting/adding/filtering columns) and the aggrega****tion.**

The number of output rows is six. This conveniently lines up with the number of output rows multiplied by the number of partitions at aggregation time. This is because Spark performs an aggregation for each partition (in this case a hash-based aggregation) before shuffling the data around in preparation for the final stage.

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-09%20at%206.20.54%20PM.png)

**Stage 3**

The last stage is the aggregation of the sub-aggregations that happen on a per partition basis in the previous stage. We combine those two partitions in the the final three rows that are the output of our total query.

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-09%20at%206.22.03%20PM.png)

  

Our job breaks down into three stages.

Clicking the label for one of them takes to the details for a given stage.

  

The first stage has eight tasks. CSV files are splittable, and Spark broke up the work to be distributed relatively evenly between the different cores on the machine. This happens at the cluster level and points to an important optimization: how you store your files. The following stage has two tasks because we explicitly called a repartition to move the data into two partitions. The last stage has **200 tasks because the default ****shuffle partitions value is 200.**

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-09%20at%206.23.41%20PM.png)

Toward the top, notice the Summary Metrics section. This provides a synopsis of statistics regarding various metrics. What you want to be on the lookout for is uneven distributions of the values.

  

In the table at the bottom, we can also examine on a per-executor basis (one for every core on this particular machine, in this case). This can help identify whether a particular executor is struggling with its workload.

  

Spark also makes available a set of more detailed metrics, as shown in ???, which are probably not relevant to the large majority of users. To view those, click Show Additional Metrics, and then either choose (De)select All or select individual metrics, depending on what you want to see.

**Other Spark UI tabs**

The remaining Spark tabs are **Storage**, **Environment**, and **Executors.**The Storage tab shows information about the cached RDDs/DataFrames on the cluster. This can help you see if certain data has been evicted from the cache over time. The Environment tab shows you information about the Runtime Environment including information about Scala and Java as well as the various Spark Properties that you configured on your cluster.

**Configuring the Spark user interface**

There are a number of configurations that you can set regarding the Spark UI. Many of them are networking configurations such as enabling access control. Others let you configure how the Spark UI will behave, e.g., how many jobs, stages and tasks are stored.

Please see the relevant table on Spark UI Configurations in the Spark documentation.

[http://spark.apache.org/docs/latest/monitoring.html#spark-configuration-options](http://spark.apache.org/docs/latest/monitoring.html#spark-configuration-options)

  

**Spark REST API**

In addition to the Spark UI, you can also access Spark’s status and metrics via a REST API. This is is available at [http://localhost:4040/api/v1](http://localhost:4040/api/v1) and is a way of building visualizations and monitoring tools on top of Spark itself. For the most part this API exposes the same information presented in the web UI, except that it doesn’t include any of the SQL-related information. This can be a useful tool if you would like to build your own reporting solution based on the information available in the Spark UI. Please see the relevant table on REST API Endpoints in the Spark documentation. 

[http://spark.apache.org/docs/latest/monitoring.html#spark-configuration-options](http://spark.apache.org/docs/latest/monitoring.html#spark-configuration-options)

  

**Spark UI History Server**

Normally, the Spark UI is only available while a SparkContext is running. To get the history, Spark included a tool called the Spark History Server where users can run to reconstruct the Spark UI and REST API, provided that the application was configured to save an event log. You can find up to date information about how to use this tool in the Spark documentation.

[https://spark.apache.org/docs/latest/monitoring.html](https://spark.apache.org/docs/latest/monitoring.html)

  

_To use the history server, you first need to configure your application to store event logs to a certain location. You can do this by by enabling spark.eventLog.enabled and the event log location with the configuration spark.eventLog.dir. Then, once you have stored the events, you can run the history server as a standalone application, and it will automatically reconstruct the web UI based on these logs. Some cluster __managers and cloud services also configure logging automatically and run a history __server by default. Other configurations for the history server;_

[http://spark.apache.org/docs/latest/monitoring.html#spark-configuration-options](http://spark.apache.org/docs/latest/monitoring.html#spark-configuration-options)

  

  

**Debugging and Spark First Aid**

By Spark Debugging, we mean that we’re going to go through some signs and symptoms (S/S) of problems in your Spark jobs, including signs that you might observe (e.g., slow tasks) as well as symptoms from Spark itself (e.g., OutOfMemoryError). In addition to the signs and symptoms, we also cover some potential treatments (Tx) for these issues.

Debugging and Spark First Aid

Note

This issue can come up frequently, especially when you’re just getting started with a fresh deployment or environment.

S/S

• Spark jobs don’t start.

• The Spark UI doesn’t show any nodes on the cluster besides the driver.

• The Spark UI seems to be reporting incorrect information.

  

Spark Jobs Not Starting

This mostly occurs when your cluster or your application’s resource demands are not configured properly. Spark, in a distributed setting, does make some assumptions about networks, filesystems, and other resources. During the process of setting up the cluster, you likely configured something incorrectly, and now the node that runs the driver cannot talk to the executors. This might be because you didn’t specify what IP and port is open or didn’t open the correct one, which is most likely a cluster-level, machine issue, or configuration issue.

  

Another option is that your application requested more resources per executor than your cluster manager currently has free, in which case the driver will be waiting forever for executors to be launched.

  

**Solution:**

• Ensure that machines can communicate with one another on the ports that you expect. Ideally, you should open up all ports between the worker nodes.

• Ensure that your Spark resource configurations are correct and that your cluster manager is properly set up for Spark (e.g., with a simpler application). One common issue may be that you requested more memory per executor than the cluster manager has free to allocate, so check how much it is reporting free (in its UI) and your spark-submit memory configuration.

**Tx**

This can happen when you’re developing a new application and have previously run code on this cluster, but now some new code won’t work.

  

*   Commands don’t run at all and output large error messages.
    
*   You check the Spark UI and no jobs, stages, or tasks seem to run.
    

  

**Tx**

After checking and confirming that the Spark UI environment tab shows the correct information for your application, it’s worth double-checking your code. Many times,

there might be a simple typo or incorrect column name that is preventing the Spark job from compiling into its underlying Spark plan (when using the DataFrame API).

  

• It’s worth moving through the error returned by Spark to confirm that there isn’t an issue in your code, such as providing the wrong input file path or field name.

• Double-check to verify that the cluster has the network connectivity that you expect between your driver, your workers, and the storage system you are using.

• There might be issues with libraries or class paths that are causing the wrong version of a library to be loaded for accessing storage. Try simplifying your application until you get a smaller version that reproduces the issue (e.g. just reading one dataset).

  

  

  

**Errors Before Execution**

**S/S**

This kind of issue occurs when you already are working on a cluster or parts of your Spark Application run before you encounter an error. This can be a part of a scheduled job that runs at some interval or a part of some interactive exploration that seems to fail after some time.

  

**S/S**

• One Spark job runs successfully on the entire cluster but the next one fails.

• A step in a multistep query fails.

• A scheduled job that ran yesterday is failing today.

• Difficult to parse error message.

  

**Tx**

• Check to see if your data exists or is in the format that you expect.

• If an error appears quickly when you’re running a query, before tasks are launched, it is most likely an analysis error while planning the query. This means that you likely misspelled a column name referenced in the query or that a column, view, or table you referenced does not exist.

• Read through the stack trace to try to find clues about what components are involved (e.g. what operator and stage it was running in).

• Try to isolate the issue by progressively double-checking input data and ensuring the data conforms to your expectations. Also try removing logic until you can isolate the problem in a smaller version of your application.

• If a job runs tasks for some time and then fails, it could be due to a problem with the input data itself, wherein the schema might be specified incorrectly or a particular row does not conform to the expected schema. For instance, sometimes your schema might specify that the data contains no nulls but your data does actually contain nulls, which can cause certain transformations to fail.

• It’s also possible that your own code for processing the data is crashing, in which case Spark will show you the exception thrown by your code. In this case, you will see a task marked as “failed” on the Spark UI, and you can also view the logs on that machine to understand what it was doing when it failed. Try adding more logs inside your code to figure out which data record was being processed.

**Errors During Execution**

This issue is quite common when optimizing applications, and can occur either due to work not being evenly distributed across your machines (“skew”), or due to one of your machines being slower than the others (e.g., due to a hardware problem).

  

  

**S/S**

Any of the following are appropriate symptoms of the issue:

• Spark stages seem to execute until there are only a handful of tasks left. Those

tasks then take a long time.

• These slow tasks show up in the Spark UI and occur consistently on the same

dataset or datasets.

• These occur in stages, one after the other.

• Scaling up the number of machines given to the Spark Application doesn’t really

help — some tasks still take much longer than others.

• In the Spark metrics, certain executors are reading and writing much more data

than others.

  

**Tx**

Slow tasks are often called “stragglers.” There are many reasons they may occur, but most often the source of this issue is that your data is partitioned unevenly into DataFrame or RDD partitions. When this happens, some executors might need to work on much much larger amounts of work than others. One particularly common case is that you use a group-by-key operation and one of the keys just has more data than others. In this case, when you look at the Spark UI, you might see that the shuffle data for some nodes is much larger than for others.

  

• Try increasing the number of partitions to have less data per partition.

• Try repartitioning by another combination of columns. For example, stragglers can come up when you partition by a skewed ID column, or a column where many values are null. In the latter case, it might make sense to first filter out the null values.

• Try increasing the memory allocated to your executors if possible.

• Monitor the executor that is having trouble and see if it is the same machine across jobs; you might also have unhealthy executor or machine in your cluster — for example, one whose disk is nearly full.

• If this issue is associated with a join or an aggregation, see “Slow Joins” on page 307 and “Slow Aggregations” on page 306.

• Check whether your user-defined functions (UDFs) are wasteful in their object allocation or business logic. Try to convert them to DataFrame code if possible.

• Ensure that your UDFs or User-Defined Aggregate Functions (UDAFs) are running on small enough data. Often times an aggregation can pull a lot of data into memory for a common key, leading to that executor having to do a lot more work than others.

• Turning on speculation, which we discuss later in this chapter under slow reads and writes, will have Spark run a second copy of tasks that are extremely slow. This can be helpful if the issue is due to a faulty node because the task will get to run on a faster one. Speculation does come at a cost, however, because it consumes additional resources. In addition, for some storage systems that use eventual consistency, might end up with duplicate output data if your writes are not idempotent. 

• Another common issue can come up when you’re working with Datasets. Because Datasets perform a lot of object instantiation to convert records to Java objects for UDFs, they can cause a lot of garbage collection. If you’re using Datasets, look at the garbage collection metrics in the Spark UI to see if they’re consistent with the slow tasks.

**Slow Tasks or Stragglers**

If you have a slow aggregation, start by reviewing the issues in the “Slow Tasks” section before proceeding. Having tried those, you might continue to see the same problem.

  

**S/S**

• Slow tasks during a groupBy call.

• Jobs after the aggregation are slow, as well.

**Tx**

Unfortunately, this issue can’t always be solved. Sometimes, the data in your job just has some skewed keys, and the operation you want to run on them needs to be slow.

• Increasing the number of partitions, prior to an aggregation, might help by reducing the number of different keys processed in each task.

• Increasing executor memory can help alleviate this issue, as well. If a single key has lots of data, this will allow its executor to spill to disk less often and finish faster, although it may still be much slower than executors processing other keys. If you find that tasks after the aggregation are also slow, this means that your dataset might have remained unbalanced after the aggregation. Try inserting a repartition call to partition it randomly.

• Ensuring that all filters and select statements that can be are above the aggregation can help to ensure that you’re working only on the data that you need to be working on and nothing else. Spark’s query optimizer will automatically do this for the structured APIs.

• Ensure null values are represented correctly (using Spark’s concept of null) and not as some default value like " " or “EMPTY”. Spark often optimizes for skipping nulls early in the job when possible, but it can’t do so for your own placeholder values.

• Some aggregation functions are also just inherently slower than others. For instance, collect\_list and collect\_set are very slow aggregation functions because they must return all the matching objects to the driver, and should be avoided in performance-critical code.

**Slow Aggregations**

Joins and aggregations are both shuffles, so they share some of the same general symptoms as well as treatments.

  

**S/S**

• A join stage seems to be taking a long time. This can be one task or many tasks.

• Stages before and after the join seem to be operating normally.

**Tx**

• Many joins can be optimized (manually or automatically) to other types of joins.

• Experimenting with different join orderings can really help speed up jobs, especially if some of those joins filter out a large amount of data; do those first.

• Partitioning a dataset prior to joining can be very helpful to try to reduce data movement across the cluster, especially if the same dataset will be used in multiple join operations. It’s worth experimenting with different prejoin partitioning. Keep in mind, again, that this isn’t “free” and does come at the cost of a shuffle.

• Slow joins can also be caused by data skew. There’s not always a lot you can do here, but sizing up the Spark application and/or increasing the size of executors can help, as described in earlier sections. Ensuring that all filters and select statements that can be are above the join can help to ensure that you’re working only on the data that you need for the join.

• Ensure that null values are handled correctly (that you’re using null) and not some default value like " " or "EMPTY", as with aggregations.

• Sometimes Spark can’t properly plan for a broadcast join if it doesn’t know any statistics about the input DataFrame or table.

**Slow Joins**

Slow I/O can be difficult to diagnose, especially with networked filesystems.  

  

**S/S**

• Slow reading of data from a distributed filesystem or external system.

• Slow writes from network filesystems or blob storage.

**Tx**

• One of the things that can help with slow reads and writes can be to turn on speculation (set spark.speculation to true). This will launch additional tasks with the same operation in an attempt to see whether it’s just some transient issue in the first task. This is a powerful tool and works well with consistent filesystems. However, speculation can cause duplicate data writes with some eventually consistent cloud services, such as Amazon S3, so check whether it is supported by the storage system connector you are using.

• Ensuring sufficient network connectivity can be important — your Spark cluster may simply not have enough total network bandwidth to get to your storage system.

• For distributed filesystems such as HDFS running on the same nodes as Spark, make sure Spark sees the same hostnames for nodes as the filesystem. This will enable Spark to do locality-aware scheduling, which you will be able to see in the “locality” column in the Spark UI. 

**Slow Reads and Writes**

This is usually a pretty serious issue because it will crash your Spark Application. It often happens due to collecting too much data back to the driver, making it run out of memory.

  

**S/S**

• Spark Application is unresponsive or crashed.

• OutOfMemoryErrors or garbage collection messages in the driver logs.

• Commands take a very long time to run or don’t run at all.

• Interactivity is very low or non-existent.

• Memory usage is high for the driver JVM.

  

**Tx**

There are a variety of potential reasons for this happening, and diagnosis is not always straightforward.

• Your code might have tried to collect too a large dataset to the driver node using operations such as collect.

• You might be using a broadcast join where the data to be broadcasted is too big. Use Spark’s maximum broadcast join configuration to better control the size it will broadcast.

• A long-running application generated a large number of objects on the driver and is unable to release them. Java’s jmap tool can be useful to see what objects are filling most of the memory of your driver JVM by printing a histogram of the heap. However, take note that jmap will pause that JVM while running.

• Increase the driver’s memory allocation if possible to let it work with more data.

• Sometimes, issues with JVMs running out of memory can happen if you are using another language binding, such as Python, due to data conversion between the two requiring too much memory in the JVM. Try to see whether your issue is specific to your chosen language and bring back less data to the driver node, or write it to a file instead of bringing it back as in-memory objects.

• If you are sharing a SparkContext with other users (e.g. through the SQL JDBC server and some notebook environments), ensure that people aren’t trying to do something that might be causing large amounts of memory allocation in the driver (like working overly large arrays in their code or collecting large datasets).

**Driver OutOfMemoryError or Driver Unresponsive**

Spark applications can sometimes recover from this automatically, depending on the true underlying issue.

  

**S/S**

• OutOfMemoryErrors or garbage collection messages in the executor logs. You can

find these in the Spark UI.

• Executors that crash or become unresponsive.

• Slow tasks on certain nodes that never seem to recover.

  

**Tx**

• Try increasing the memory available to executors and the number of executors.

• Try increasing PySpark worker size via the relevant Python configurations.

• Look for garbage collection error messages in the executor logs. Some of the tasks that are running, especially if you’re using UDFs, can be creating lots of objects that need to be garbage collected. Repartition your data to increase parallelism, reduce the amount of records per task, and ensure that all executors are getting the same amount of work.

• Ensure that null values are handled correctly (that you’re using null) and not some default value like " " or "EMPTY", as we discussed earlier.

• This is more likely to happen with RDDs or with Datasets because of object instantiations. Try using fewer UDFs and more of Spark’s structured operations when possible.

• Use Java monitoring tools such as jmap to get a histogram of heap memory usage on your executors, and see which classes are taking up the most space.

• If executors are being placed on nodes that also have other workloads running on them, such as a key-value store, try to isolate your Spark jobs from other jobs.

**Executor OutOfMemoryError or Executor Unresponsive**

**S/S**

• Unexpected null values after transformations.

• Scheduled production jobs that used to work no longer work, or no longer pro‐

duce the right results.

  

**Tx**

• It’s possible that your data format has changed without adjusting your business logic. This means that code that worked before is no longer valid.

• Use an accumulator to try to count records or certain types, as well as parsing or processing errors where you skip a record. This can be helpful because you might think that you’re parsing data of a certain format, but some of the data doesn’t. Most often, users will place the accumulator in a UDF when they are parsing their raw data into a more controlled format and perform the counts there. This allows you to count “valid” and invalid records and then operate accordingly after the fact.

• Ensure that your transformations actually result in valid query plans. Spark SQL sometimes does implicit type coercions that can cause confusing results. For instance, the SQL expression SELECT 5\*"23" results in 115 because the string “25” converts to an the value 25 as an integer, but the expression SELECT 5 \* " " results in null because casting the empty string to an integer gives null. Make sure that your intermediate datasets have the schema you expect them to (try using printSchema on them), and look for any CAST operations in the final query plan.

**Unexpected Nulls in Results**

**S/S**

• You see “no space left on disk” errors and your jobs fail.

  

**Tx**

• The easiest way to alleviate this, of course, is to add more disk space. You can do this by sizing up the nodes that you’re working on or attaching external storage in a cloud environment.

• If you have a cluster with limited storage space, some nodes may run out first due to skew. Repartitioning the data as described earlier may help here.

• There are also a number of storage configurations with which you can experi‐ ment. Some of these determine how long logs should be kept on the machine before being removed.

• Try manually removing some old log files or old shuffle files from the machine(s) in question. This can help alleviate some of the issue although obviously is not a permanent fix.

**No Space Left on Disk Errors**

**S/S**  

• You see Serialization errors and your jobs fail.

**Tx**

• This is very uncommon when working with the Structured APIs, but you might be trying to perform some custom logic on executors with UDFs or RDDs and either the task that you’re trying to serialize to these executors or the data you are trying to share cannot be serialized. This often happens when you’re working with either some code or data that cannot be serialized into a UDF or function, or if you’re working with strange data types that cannot be serialized. If you are using (or intend to be using Kryo Serialization), verify that you’re actually registering your classes so that they are indeed serialized.

• Try not to refer to any fields of the enclosing object in your UDFs when creating UDFs inside a Java or Scala class. This can cause Spark to try to serialize the whole enclosing object, which may not be possible. Instead, copy the relevant fields to local variables in the same scope as closure and use those.

**Serialization Errors**

  

**Performance Tuning**

Performance choices that that are available to make your jobs run faster.

*   extremely fast network - make Spark jobs faster because shuffles are so often one of the costlier steps in a Spark job
    

  

**Spark job optimization options:**

• Code-level design choices (e.g., RDDs versus DataFrames)

• Data at rest

• Joins

• Aggregations

• Data in flight

• Individual application properties

• Inside of the Java Virtual Machine (JVM) of an executor

• Worker nodes

• Cluster and deployment properties

  

There are two ways of trying to achieve the execution characteristics that we would like out of Spark jobs:

*   **indirectly** by setting configuration values or changing the runtime environment.
    
*   **directly** change execution characteristic or design choices at the individual Spark job, stage, or task level
    

  

**Indirect Performance Enhancements**

5.  Improve your hardware
    
6.  When designing your applications, making good design choices is a very important step because it can help you to not just write better Spark applications, but also have them run in a more stable and consistent manner over time and in the face of external changes or variations. 
    
    **Scala Versus Java Versus Python Versus R: **Spark’s Structured APIs are consistent across languages in terms of speed and stability. That means that you should code with whatever language you are most comfortable using or is best suited for your use case. For UDFs, Python and R are not the best choice. (functions jump across languages)
    
    **DataFrames Versus SQL Versus Datasets Versus RDDs: **Across all languages, DataFrames, Datasets and SQL are equivalent in speed. Here, again, UDFs are not well-suited for Python and R. For RDDs - Scala or Java!
    
    **Object Serialization in RDDs:** Serialize with Kyro [https://github.com/EsotericSoftware/kryo](https://github.com/EsotericSoftware/kryo)
    
    You can use Kryo serialization by setting spark.serializer to org.apache.spark.serializer.KryoSerializer. You will also need to explicitly register the classes that you would like to register with the Kryo serializer via the spark.kryo.classesToRegister configuration. Documentation: [https://github.com/EsotericSoftware/kryo](https://github.com/EsotericSoftware/kryo) . To register your classes, use the SparkConf that you just created and pass in the names of your classes:
    
    conf.registerKryoClasses(Array(classOf\[MyClass1\], classOf\[MyClass2\]))
    
7.  **Cluster Configurations: **monitoring how the machines themselves are performing will be the most valuable approach toward optimizing your cluster configurations, especially when it comes to running multiple applications.
    

1.  **Cluster/application sizing and sharing**
    
2.  **Dynamic allocation: **Spark provides a mechanism to dynamically adjust the resources your application occupies based on the workload. This means that your application can give resources back to the cluster if they are no longer used, and request them again later when there is demand. This feature is particularly useful if multiple applications share resources in your Spark cluster. This feature is disabled by default and available on all coarse-grained cluster managers; that is, standalone mode, YARN mode, and Mesos coarse-grained mode. You can set this configuration by changing spark.dynamicAllocation.enabled to true. Individual parameters to tune: [https://spark.apache.org/docs/latest/configuration.html](https://spark.apache.org/docs/latest/configuration.html)
    
3.  **Scheduling: **setting --max-executor-cores, \-> specifies the maximum number of executor cores that your application will need. Specifying this value can ensure that your application does not take up all the resources on the cluster. You can also change the default, depending on your cluster manager, by setting the configuration spark.cores.max to a default of your choice.
    
4.  **Data at Rest: **Making sure that you’re storing your data for effective reads later on is absolutely essential to successful big data projects. This involves choosing your storage system, choosing your data format, and taking advantage of features such as data partitioning in some storage formats.
    

1.  **File-based long-term data storage:** You should always favor structured, binary types to store your data. “CSV” seem well-structured, but they’re very slow to parse, and often also full of edge cases and pain points.
    

1.  **Splittable file types and compression: **Make sure your file format “splittable”, meaning different tasks can read different parts of the file in parallel. Files compressed using gzip, **bzip2 or lz4** are generally **splittable** if they were written by a parallel processing framework like Hadoop or Spark. For your own input data, the simplest way to make it splittable is to upload it as separate files, ideally each no larger than a few hundred megabytes.
    

1.  **Table partitioning: **Table partitioning refers to storing files in separate directories based on a key, such as the date field in the data. Storage managers like Apache Hive support this concept, as do many of Spark’s built in data sources. Partitioning your data correctly allows Spark to skip many irrelevant files when it only requires data with a specific range of keys. For instance, if users frequently filter by “date” or “customerId” in their queries, partition your data by those columns. This will greatly reduce the amount of data that end users must read by most queries, and therefore dramatically increase speed. 
    
    Downside of partitioning, however, is that if you partition at too fine a granularity, it can result in many small files, and a great deal of overhead trying to list all the files in the storage system. Make sure your partitions each have at least several hundred megabytes of data.
    

1.  **Bucketing: **Bucketing your data allows Spark to “pre-partition” data according to how joins or aggregations are likely to be performed by readers.For instance, if joins are frequently performed on a column immediately after a read, you can use bucketing to ensure that the data is well partitioned according to those values. This can help prevent a shuffle before a join and therefore help speed up data access. Bucketing generally works hand-in-hand with partitioning as a second way of physically splitting up data.
    

1.  **The number of files: **If there are lots of small files, you’re going to pay a price listing and fetching each of those individual files.
    
    Having lots of small files is going to make the scheduler work much harder to locate the data and launch all of the read tasks. This can increase the network and scheduling overhead of the job. Having fewer large files is going to ease the pain off the scheduler but it is also going to make tasks run longer. In this case, though, you can always launch more tasks than there are input files if you want more parallelism — Spark will split each file across multiple tasks assuming you are using a splittable format. In general, we recommend sizing your files so that they each contain at least a few tens of megatbytes of data. One way of controlling data partitioning when you write your data is through a write option introduced in Spark 2.2. To control how many records go into each file, you can specify the maxRecordsPerFile option to the write operation.
    

1.  **Data locality: **Data locality basically specifies a preference for certain nodes that hold certain data, rather than having to exchange these blocks of data over the network. If you run your storage system on the same nodes as Spark, and the system supports locality hints, Spark will try to schedule tasks close to each input block of data. For example HDFS storage provides this option. There are several configurations that affect locality, but it will generally be used by default if Spark detects that it is using a local storage system. You will also see data-reading tasks marked as “local” in the Spark web UI.
    

1.  **Statistics collection**
    
    Spark includes a cost-based query optimizer that plans queries based on the properties of the input data when using the structured APIs. However, to allow the cost-based optimizer to make these sorts of decisions, you need to collect (and maintain) statistics about your tables that it can use. There are two kinds of statistics: **table-level a****nd column-level statistics**. Statistics collection is available only on named tables, not on arbitrary DataFrames or RDDs.
    
    **To collect table-level statistics**, you can run the following command: ANALYZE TABLE table\_name COMPUTE STATISTICS
    
    **To collect column-level statistics**, you can name the specific columns: ANALYZE TABLE table\_name COMPUTE STATISTICS FOR COLUMNS column\_name1, column\_name2, ...
    
    Column-level statistics are slower to collect, but provide more information for the cost-based optimizer to use about those data columns. Both types of statistics can help with joins, aggregations, filters, and a number of other potential things (e.g. automatically choosing when to do a broadcast join). This is a fast growing part of Spark, so different optimizations based on statistics likely be added in the future.
    

15.  **Shuffle Configurations: **Configuring Spark’s external shuffle service can often increase performance because it allows nodes to read shuffle data from remote machines even when the executors on those machines are busy, e.g. with garbage collection. If you have too few partitions, then too few nodes will be doing work and there may be skew, but if you have too many partitions, there is an overhead to launching each one that may start to dominate. Try to aim for at least afew tens of megabytes of data per output partition in your shuffle.
    
16.  **Memory Pressure and Garbage Collection: **One issue that can come up when you’re running Spark jobs is that the executors and driver have a lot of memory pressure. This might be where you use too much memory on a driver or some executors or it might be where garbage collection becomes extremely costly and slow as large numbers of objects are created in the JVM and subsequently garbage collected as they are no longer used. One strategy for easing this issue is to ensure that you’re using the Structured APIs as much as possible. These will not only increase the efficiency with which your Spark jobs will execute, but it will also greatly reduce memory pressure because JVM objects are never realized and Spark SQL simply performs the computation on its internal format. **The Spark documentation includes some great pointers on tuning garbage collection for RDD and UDF based applications, and an excerpt is paraphrased below.**
    
    **Measuring the impact of garbage collection**
    
    The first step in garbage collection tuning is to collect statistics on how frequentlygarbage collection occurs and the amount of time spent collecting garbage. You can do this by adding \-verbose:gc -XX:+PrintGCDetails -XX:+PrintGCTimeStamps to Spark’s JVM options using the spark.executor.extraJavaOptions configuration parameter. The next time you run your Spark job, you will see messages printed in the worker’s logs each time a garbage collection occurs. These logs will be on your cluster’s worker nodes (in the stdout files in their work directories), not in the driver.
    
    **Garbage collection tuning**
    
    **To further tune garbage collection, you first need to understand some basic informa**tion about memory management in the JVM:
    
    • Java heap space is divided in to two regions Young and Old. The Young generation is meant to hold short-lived objects whereas the Old generation is intended for objects with longer lifetimes.
    
    • The Young generation is further divided into three regions: Eden, Survivor1 and Survivor2.
    
    The goal of garbage collection tuning in Spark is to ensure that only long-lived cached datasets are stored in the Old generation and that the Young generation is sufficiently sized to store all short-lived objects. This will help avoid full garbage collec‐ tions to collect temporary objects created during task execution. Here are some steps than might be useful:
    

*   Check whether there are too many garbage collections by collecting garbage collection statistics. If a full garbage collection is invoked multiple times before a task completes, it means that there isn’t enough memory available for executing tasks, so you should decrease the amount of memory Spark uses for caching (spark.memory.fraction).  
    

*   If there are too many minor collections but not many major garbage collections, allocating more memory for Eden would help. You can set the size of the Eden to be an over-estimate of how much memory each task will need. If the size of Eden is determined to be E, you can set the size of the Young generation using the option -Xmn=4/3\*E. (The scaling up by 4/3 is to account for space used by survivor regions, as well.)
    
*   Try the G1GC garbage collector with -XX:+UseG1GC. It can improve performance in some situations in which garbage collection is a bottleneck and you don’t have a way to reduce it further by sizing the generations. Note that with large executor heap sizes, it can be important to increase the G1 region size with -XX:G1HeapRegionSize.
    
*   Monitor how the frequency and time taken by garbage collection changes with the new settings.
    

You can specify garbage collection tuning flags for executors by setting spark.executor.extraJavaOptions in a job’s configuration.

  

**Direct Performance Enhancements**

  

*   **Parallelism**
    

The first thing you should do whenever trying to speed up a specific stage is to increase the the degree of parallelism. In general, we recommend having at least two or three tasks per CPU core in your cluster if the stage processes a large amount of data. You can set this via the spark.default.parallelism property as well as tuning the spark.sql.shuffle.partitions according to the number of cores in your cluster.

  

*   **Improved Filtering**
    

Another frequent source of performance enhancements is moving filters to the earliest part of your Spark job that you can. Sometimes, these filters can be pushed into the data sources themselves and this means that you can avoid reading and working with data that is irrelevant to your end result. Enabling partitioning and bucketing also helps achieve this. Always look to be filtering as much data as you can early on, and you’ll find that your Spark jobs will almost always run faster.

  

*   **Repartitioning and Coalescing**
    

Repartition calls can incur a shuffle. However, doing some can optimize the overall execution of a job by balancing data across the cluster, so they can be worth it. In general, you should try to shuffle the least amount of data possible. For this reason, if you’re reducing the number of overall partitions in a DataFrame or RDD, first try coalesce method, which will not perform a shuffle but rather merge partitions on the same node into one partition. The slower repartition method will also shuffle data across the network to achieve even load balancing. Repartitions can be particularly helpful when performing joins or prior to a cache call. Remember that repartitioning is not free, but it can improve overall application performance and parallelism of your jobs.  
**Custom Partitioning**  

If your jobs are still slow or unstable, you might want to explore performing custom partitioning at the RDD level. This allows you to define a custom partition function that will organize the data across the cluster to a finer level of precision than is available at the DataFrame level.

  

*   **User-Dened Functions (UDFs)**
    

In general, avoiding UDFs is an good optimization opportunity. UDFs are expensive because they force representing data as objects in the JVM and sometimes do this multiple times per record in a query. You should try to use the Structured APIs as

much as possible to perform your manipulations simply because they are going to perform the transformations in a much more efficient manner than you can do in a high-level language. There is also ongoing work to make data available to UDFs in

batches, such as the Vectorized UDF extension for Python that gives your code multiple records at once using a Pandas data frame. In general, if you’re going to write a UDF, you should prefer to write it in Scala or Java because it’s going to be more efficient. However, if you must perform your UDFs in Python, be sure to scope the UDF to the smallest amount of manipulation in Python as possible. This will help you keep your Spark jobs fast and efficient. Always, always

try to look up the function you want in the Spark SQL documentation or compose one of SQL/DataFrame expressions before resorting to a UDF. It’s quite possible that the operation you’re looking to use is already in place.

*   **Temporary Data Storage (Caching)**
    

Caching will place a DataFrame, table or RDD into temporary storage (either memory or disk) across the executors in your cluster, and make subsequent reads faster. Although caching might sound like something we should do all the time, it’s not always a good thing to do. That’s because caching data incurs a serialization, deserialization and storage cost. For example, if you are only going to process a dataset once (in a later transformation), caching it will only slow you down.

The use case for caching is simple: as you work with data in Spark, either within an interactive session or a standalone application, you will often want to reuse a certain dataset (e.g., a DataFrame or RDD). For example, in an interactive data science session, you might load and clean your data and then reuse it to try multiple statistical models. Or in a standalone application, you might run an iterative algorithm that reuses the same dataset. You can tell Spark to cache a dataset using the cache method on DataFrames or RDDs.

Caching is a lazy operation, meaning that things will be cached only as they are accessed. The RDD API and the Structured API differ in how they actually perform caching, so let’s review the gory details before going over the storage levels. When we cache an RDD, we cache the actual, physical data. The bits. When this data is accessed again, Spark returns the proper data. This is done through the RDD reference. However, in the Structured API, caching is done based on the physical plan. This means that we effectively store the physical plan as our key (as opposed to the object reference) and perform a lookup prior to the execution of a Structured job. This can cause  

confusion because sometimes you might be expecting to access raw data but because someone else already cached the data, you’re actually accessing their cached version.

  

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-10%20at%2012.23.59%20AM.png)  

**Illustrations of the process.** We load an initial DataFrame from a CSV file and then derive some new DataFrames from it using transformations. We can avoid having to recompute the original DataFrame (i.e., load and parse the CSV file) many times by adding a line to cache it along the way.

![](Production%20Applications.html.resources/Screen%20Shot%202019-06-10%20at%2012.24.16%20AM.png)

  

**Code:**

_\# in Python_

_\# Original loading code that does \*not\* cache DataFrame_

DF1 = spark.read.format("csv")\\

.option("inferSchema", "true")\\

.option("header", "true")\\

.load("/data/flight-data/csv/2015-summary.csv")

DF2 = DF1.groupBy("DEST\_COUNTRY\_NAME").count().collect()

DF3 = DF1.groupBy("ORIGIN\_COUNTRY\_NAME").count().collect()

DF4 = DF1.groupBy("count").count().collect()

  

You’ll see here that we have our “lazily” created DataFrame (DF1), along with three other DataFrames that access data in DF1. All of our downstream DataFrames share that common parent (DF1) and will repeat the same work when we perform the preceding code. In this case, it’s just reading and parsing the raw CSV data, but that can be a fairly intensive process, especially for large datasets. On my machine, those commands take a second or two to run. Luckily caching can help speed things up. When we ask for a DataFrame to be cached, Spark will save the data in memory or on disk the first time it computes it. Then, when any other queries come along, they’ll just refer to the one stored in memory as opposed to the original file. You do this using the DataFrame’s cache method.

  

DF1.cache()  

DF1.count()

  

We used the count above to eagerly cache the data (basically perform an action to force Spark to store it in memory), because caching itself is lazy—the data is cached only on the first time you run an action on the DataFrame. Now that the data is cached, the previous commands will be faster, as we can see by running the following code:

  

_\# in Python_

DF2 = DF1.groupBy("DEST\_COUNTRY\_NAME").count().collect()

DF3 = DF1.groupBy("ORIGIN\_COUNTRY\_NAME").count().collect()

DF4 = DF1.groupBy("count").count().collect()

  

  

When we ran this code, it cut the time by more than half! This might not seem that wild, but picture a large dataset or one that requires a lot of computation to create (not just reading in a file). The savings can be immense. It’s also great for iterative machine learning workloads because they’ll often need to access the same data a number of times, which we’ll see shortly. The cache command in Spark always places data in memory by default, caching only part of the dataset if the cluster’s total memory is full. For more control, there is also a persist method that takes a StorageLevel object to specify where to cache the data: in memory, on disk, or both. We discuss these choices more in Part IV, when we cover optimizations and tuning.

  

  

  

**Joins**

Joins are a common area for optimization. The biggest weapon you have when it comes to optimizing joins is simply educating yourself about what each join does and how it’s performed. This will help you the most. Additionally, equi-joins are the most easy for Spark to optimize at this point and therefore should be preferred wherever possible. Beyond that, simple things like trying to use the filtering ability of inner

joins by changing join ordering can yield large speedups. Additionally, using broadcast join hints can help Spark make intelligent planning decisions when it comes to creating query plans, as described in Chapter 8. Avoiding Cartesian joins or even full outer joins is often low-hanging fruit for stability and optimizations because these can often be optimized into different filtering style joins when you look at the entire data flow instead of just that one particular job area. Lastly, following some of the other sections in this chapter can have a significant effect on joins. For example, collecting statistics on tables prior to a join will help Spark make intelligent join deci‐ sions. Additionally, bucketing your data appropriately can also help Spark avoid large shuffles when joins are performed. These tips are some of the more obvious that can apply well to almost all workloads.

  

**Aggregations**

For the most part, there are not too many ways that you can optimize specific aggregations beyond filtering data before the aggregation having a sufficiently high number of partitions. However, if you’re using RDDs, controlling exactly how these aggregations are performed (e.g., using reduceByKey when possible over groupByKey) can be very helpful and improve speed and stability of your code.

  

  

**Broadcast Variables**

We touched on broadcast joins and variables in previous chapters, and these are a good option for optimization. The basic premise is that if some large piece of data will be used across multiple UDF calls in your program, you can broadcast it to save just a single read-only copy on each node and avoid re-sending this data with each job. For example, broadcast variables may be useful to save a lookup table or a machine learning model. You can also broadcast arbitrary objects by creating broadcast variables using your SparkContext, and then simply refer to those variables in your tasks.
