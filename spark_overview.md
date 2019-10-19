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

<details><summary> Why Apache Spark? (<b>Optional</b>)</summary>

<p>
Spark is a cluster computing engine that generalizes the MapReduce programming model that Google introduced back in 2004. Basically, Spark tries to support more types of applications and make them easier to program than MapReduce does. The goal was to make Spark both easy and fast to process large data sets on a cluster of machines. The way Spark did it is (1) high level APIs in languages such as Java, Scala, Python and all that are easy to program in to try to make it as similar as possible to programming on a single machine when that's possible and (2) a unified engine that can capture many different workloads on the same engine. So you don't have to hook together many different systems to create a pipeline. You can actually express them all in the same programming model and that's very powerful to get both faster and and easier to use processing. Thus, in terms of the unified engine what that means is that on top of the Spark engine there's a wide variety of standard libraries that are built in and these are the four shipped with the project:<br>

<img src="Images/SparkOverview/sparkecosystem.png"> <br> <br>

<b>Spark SQL</b> lets you work with structured data and use languages like SQL or other API's as well to query this kind of data. <b>Spark Streaming</b> uses the engine to process and update results in real-time as new data comes in. <b>MLlib</b> is a library of distributed machine learning algorithms that project developers built and you can just call into. <b>GraphX</b> is a system for graph applications. <br>

The nice thing about these is that they're all just libraries you can combine together in one program and they all translate down to the same engine underneath. Let's discuss why Spark was designed to have a unified engine by introducing the history of large scale cluster computing. A lot of the recent wave in data intensive computing started back in 2004 with the MapReduce paper published by Google. 
<img src="Images/SparkOverview/googlemapreduce.png">

Google in this paper said: "Well we have this environment that's pretty unique which is a large number of commodity servers. It's data intensive computation as opposed to just compute intensive which is what scientific supercomputing was, it automatically deals with failures, it keeps going and it's easy for users to hide applications in. And that was the 'MapReduce paper' that was extremely influential." One thing you you may notice in the MapReduce paper though that was a very important part of it is they talked a lot about how general it was. They really liked the idea of having a general engine to do these different batch processing tasks they had. So they said: "We first wrote MapReduce in 2003 and since that time we have been pleasantly surprised at how badly applicable it was." MapReduce itself only handled batch processing which was fine for them because that's the main thing they did at the time. So what happened after that is MapReduce became very widely deployed especially through the Hadoop implementation, which was an open source MapReduce. But users quickly wanted to do more things on the same kind of hardware and at the same kind of scale that they were using MapReduce on. <br>

<b>They wanted to do three types of things:</b> (1) More complex multi pass algorithms. MapReduce is just a single pass computation you do a map through the data then you do a reduce and you can aggregate together some values but many real-world algorithms need to go through the data many times and basically they weren't that easy or efficient to build with MapReduce. (2) More interactive ad-hoc ways, so for example, you're collecting a large data set something about visits to a website or maybe a scientific data set or something like testing out pharmaceuticals and you can on a batch job over it and compute a result in like 30 minutes and aggregate together all the data. That's really great, but then if you have a new question about it - you want to ask that question and get back the results in a few seconds if possible - so that you can actually explore it interactively, well that's the thing that MapReduce wasn't able to do. (3) And finally users wanted to do more real-time stream processing as well so instead of for example building a web index having and updating that once per night in this way, why can't you update it in real-time as you browse, as you crawl the web and as you see new events happening, or news articles appear or stuff like that? So it's a very natural question in all of these environments.  <br>

Because of these different workloads, the result was that people proposed a wide variety of specialized cluster computing systems for these workloads that are sort of the equivalent of MapReduce for streaming. And that's kind of the direction that the software went into. So basically we started out with MapReduce that did batch processing but it was just a general engine. You could do many different types of batch processing, which was good. And then we got all these specialized systems including inside Google and also outside it. So in Google for example they developed Pregel and Dremel which were systems for graph processing and interactive queries respectively. In the open source Hadoop ecosystem, there are also a lot of open source projects with interesting names like Impala, Storm and so on that do different things. Some of them are graph processing some of them are streaming and so on. Today, you just see that there's a ton of these systems out there and people often use some kind of combination of them. With specialized systems, even though they solve the individual problems that they tackle, there are also some challenges with having them. <br>

Two challenges. (1) If you have a lot of specialized systems that you need to hook together to build an application, it's a lot of different pieces of software to manage to tune and configure to deploy to upgrade and so on. So it's a lot of operational overhead. You need to be an expert not just in one thing but in all of these different systems which have their own kind of stuff as to how they run. (2) You can't easily combine different types of processing and that's a problem because most big data applications actually need to do that. They need to combine many different processing steps to actually clean up the data and bring it into a form that you can do interesting analytics on, and then maybe serve the
results or apply it to something in real time. So as a really simple example, you might collect a bunch of data and then you may want to load a subset of the data with SQL and then on a machine learning algorithm on the result. <br>

And with the systems discussed above, there would be two different systems, and you'd need to figure out, okay well how do I run SQL in one of them, how do I export it into a format that the second one can read, how do I then query it? it's both difficult to use as a user and it's also inefficient because you need to move the data between these systems all the time. So in many cases actually if you measure what the computation is doing - the cost to transfer the data between these two engines is as expensive as the computation itself. And so basically this really slows down applications. The reason why big data is expensive to move around, it's expensive to copy it across the network, it's expensive divide it to disk or to change the file
format or any of that stuff. Often it's as expensive as actually running your algorithm on that. So this is a non-trivial cost. <br>

The question that led to Spark:  "Can we go out of this world of specialized systems and back to a single kind of general system that just captures these new workloads that motivated the previous ones?" <br>

That's what Spark tries to do. They designed a unified engine in a way that enabled different applications to be systematically captured. So how does it actually work? How did they do it? <br>




</p>
  
</details>




* * *

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

![driver_executor](Images/SparkOverview/driver_executor_spark.png)

- Driver is on the left, four executors on the right. It demonstrates how the cluster manager controls physical machines and allocates resources to Spark Applications. This can be one of three cluster managers ( YARN, Mesos, Spark's standalone cluster manager). This means that there can be multiple Spark Applications running on a cluster at the same time.

> Note: Spark, in addition to a cluster mode, also has a local mode. The driver and the executor are simply processes, this means they can live on the same machine or different machines. Local Mode - Driver and executor run as threads on your individual computer in stead of a cluster.

- Spark employs a cluster manager that keeps track of the resources available
- The driver process is responsible for executing the driver program's commands across the executor to complete a given task
- The executor only runs Spark code. However, the driver can be driven from a number of different languages through Spark's Language APIs

**Spark's Language APIs:** make it possible to run Spark code using programming languages. Spark presents 'core concepts' in every language; these concepts are then translated into Spark code that runs on the cluster of machines. 


