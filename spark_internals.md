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
## Overview

Let's answer the following questions:

**Q1: After a successful deployment, what are the running services in each node?**

**Q2: How is the Spark application created and executed?**

## Deployment Diagram
![deploy](../PNGfigures/deploy.png)

We can see from the deployment diagram (Standalone version):
  - A Spark cluster has a Master node and multiple Worker nodes, which are equivalent to Hadoop's Master and Slave nodes.
  - The Master node has a Master daemon process, which manages all the Worker nodes.
  - The Worker node has a Worker daemon process, responsible for communicating with the Master node and managing local Executors.
  - In the official document, the Driver is explained as "The process running the main() function of the application and creating the SparkContext". A driver program, such as WordCount.scala, is regarded as a Spark application. If the driver program is launched on the Master node as follows:

    ```scala
	./bin/run-example SparkPi 10
	```
	The SparkPi program will become the Driver (on the Master node). However, if the driver program is submitted to a YARN cluster, the Driver may be scheduled to a Worker node (e.g., Worker node 2 in the diagram). If the driver program is launched on a local PC, such as running the following program in IntelliJ IDEA:

	```scala
	val sc = new SparkContext("spark://master:7077", "AppName")
	...
	```
   The driver program will run atop the local PC. However, this approach is not recommended since the local PC may not be in the same network with the Worker nodes, which will slow down the communication between the driver and the executors.

  - Each Worker manages one or multiple ExecutorBackend processes. Each ExecutorBackend launches and manages an Executor instance. Each Executor maintains a thread pool, in which each task runs as a thread.
  - Each application has one Driver and multiple Executors. The tasks within the same Executor belong to the same application.
  - In Standalone deployment mode, ExecutorBackend is instantiated as CoarseGrainedExecutorBackend.

    > In my cluster there's only one CoarseGrainedExecutorBackend process on each worker node and I didn't manage to configure multiple CoarseGrainedExecutorBackend processes on each worker node (my guess is that there'll be multiple CoarseGrainedExecutorBackend process when multiple applications are running, which needs to be confirmed).

    > Check out this blog (in Chinese) [Summary on Spark Executor Driver Resource Scheduling](http://blog.csdn.net/oopsoom/article/details/38763985) by [@OopsOutOfMemory](http://weibo.com/oopsoom), if you want to know more about the relationship between Worker and Executor.

  - Worker manages each CoarseGrainedExecutorBackend process thourgh an ExecutorRunner instance (Object).

After studying the deployment diagram, we'll write a simple Spark application to see how the Spark application is created and executed.

## A simple Spark application
The example here is the `GroupByTest` application under the examples package in Spark. We assume that the application is launched on the Master node, with the following command:

```scala
/* Usage: GroupByTest [numMappers] [numKVPairs] [valSize] [numReducers] */

bin/run-example GroupByTest 100 10000 1000 36
```

The code of this application is as follows:

```scala
package org.apache.spark.examples

import java.util.Random

import org.apache.spark.{SparkConf, SparkContext}

/**
 * Usage: GroupByTest [numMappers] [numKVPairs] [KeySize] [numReducers]
 */
object GroupByTest {
  def main(args: Array[String]) {
    val sparkConf = new SparkConf().setAppName("GroupBy Test")
    var numMappers = if (args.length > 0) args(0).toInt else 2
    var numKVPairs = if (args.length > 1) args(1).toInt else 1000
    var valSize = if (args.length > 2) args(2).toInt else 1000
    var numReducers = if (args.length > 3) args(3).toInt else numMappers

    val sc = new SparkContext(sparkConf)

    val pairs1 = sc.parallelize(0 until numMappers, numMappers).flatMap { p =>
      val ranGen = new Random
      var arr1 = new Array[(Int, Array[Byte])](numKVPairs)
      for (i <- 0 until numKVPairs) {
        val byteArr = new Array[Byte](valSize)
        ranGen.nextBytes(byteArr)
        arr1(i) = (ranGen.nextInt(Int.MaxValue), byteArr)
      }
      arr1
    }.cache()
    // Enforce that everything has been calculated and in cache
    pairs1.count()

    println(pairs1.groupByKey(numReducers).count())

    sc.stop()
  }
}

```

The code runs like the following figure in our brains:
![deploy](../PNGfigures/UserView.png)

Since this is a simple application, let's estimate the runtime data size in each step:

  1. Initialize SparkConf.
  2. Initialize `numMappers=100`, `numKVPairs=10,000`, `valSize=1000`, `numReducers= 36`.
  3. Initialize SparkContext, which creates the necessary objects and actors for the driver.
  4. Each mapper creates an `arr1: Array[(Int, Byte[])]`, which has `numKVPairs` elements. Each  `Int` is a random integer, and each byte array's size is `valSize`. We can estimate `Size(arr1) = numKVPairs * (4 + valSize) = 10MB`, so that `Size(pairs1) = numMappers * Size(arr1) ＝1000MB`.
  5. Each mapper is instructed to cache its `arr1` array into the memory.
  6. The action count() is applied to sum the number of elements in  `arr1` in all mappers, the result is `numMappers * numKVPairs = 1,000,000`. This action triggers the caching of `arr1`s.
  7. `groupByKey` operation is performed on cached `pairs1`. The reducer number (a.k.a., partition number) is `numReducers`. Theoretically, if hash(key) is evenly distributed, each reducer will receive `numMappers * numKVPairs / numReducer ＝ 27,777` pairs of `(Int, Array[Byte])`, with a size of `Size(pairs1) / numReducer = 27MB`.
  8. Reducer aggregates the records with the same Int key, the result is `(Int, List(Byte[], Byte[], ..., Byte[]))`.
  9. Finally, a `count()` action sums up the record number in each reducer, the final result is actually the number of distinct integers in `pairs1`.

## Logical Plan

The actual execution procedure is more complicated than what we described above. Generally speaking, Spark firstly creates a logical plan (namely data dependency graph) for each application, then it transforms the logical plan into a physical plan (a DAG graph of map/reduce stages and map/reduce tasks). After that, concrete map/reduce tasks will be launched to process the input data. Let's detail the logical plan of this application:

The function call of `RDD.toDebugString` can return the logical plan:

```scala
  MapPartitionsRDD[3] at groupByKey at GroupByTest.scala:51 (36 partitions)
    ShuffledRDD[2] at groupByKey at GroupByTest.scala:51 (36 partitions)
      FlatMappedRDD[1] at flatMap at GroupByTest.scala:38 (100 partitions)
        ParallelCollectionRDD[0] at parallelize at GroupByTest.scala:38 (100 partitions)
```

We can draw a diagram to illustrate logical plan:
![deploy](../PNGfigures/JobRDD.png)

> Note that the **data in the partition** block only shows what data will be generated in this partition, but this does not mean that these data all reside in memory at the same time.

Let's detail the logical plan:
  - The user first initializes an array, which contains 100 integers (i.e., 0 to 99).
  - parallelize() generates the first RDD (ParallelCollectionRDD), in which each partititon contains an integer i.
  - FlatMappedRDD is generated by calling a transformation method (flatMap) on the ParallelCollectionRDD. Each partition of the FlatMappedRDD contains an `Array[(Int, Array[Byte])]`.
  - The first count() performs on FlatMappedRDD.
  - Since the FlatMappedRDD is cached in memory, its partitions are colored differently.
  - groupByKey() generates the following 2 RDDs (ShuffledRDD and MapPartitionsRDD), and we will see the reason in later chapters.
  - ShuffleRDD in the logical plan means that the job needs a shuffle. This shuffle is similar with the shuffle in Hadoop MapReduce.
  - MapPartitionRDD contains groupByKey()'s computing results.
  - Each value in MapPartitionRDD (`Array[Byte]`) is converted to `Iterable`.
  - The last count() action performs on MapPartitionRDD.

**The logical plan represents the application dataflow, including the data transformations , the intermediate RDDs, and the data dependency between these RDDs.**

## Physical Plan

The logical plan aims to model the dataflow, not the execution flow. The dataflow and execution flow are unified in Hadoop. In Hadoop, the dataflow is pre-defined and fixed, users just need to write map() and reduce() functions. The map/reduce tasks have fixed processing steps. However in Spark, the dataflow is very flexible and could be very complicated, so it's difficult to simply combine the dataflow and execution flow together. For this reason, Spark separates the dataflow from the actual task execution, and has algorithms to transform a logical plan into a physical plan. We'll discuss this transformation in later chapters.

For the example application, let's draw its physical DAG:
![deploy](../PNGfigures/PhysicalView.png)

We can see that the GroupByTest application generates 2 Spark jobs, the first job is triggered by the first action (i.e., `pairs1.count()`). Let's detail this first job:

  - This job contains only 1 stage, which has 100 ResultTasks. Here, the stage is similar with the map stage in Hadoop but not shown in this figure. The stage concept will be detailed in later chapters.
  - Each task performs flatMap, generates FlatMappedRDD, and then executes the action `count()` to count the record number in each partition. For example, partition 99 has  9 records, so the `result 99` is 9.
  - Since `pairs1` is specified to be cached, the tasks will cache the partitions of FlatMappedRDD inside the executor's memory space at runtime.
  - After the ResultTasks finish, the driver collects the tasks' results and sums them up.
  - Job 0 completes.

The second job is triggered by `pairs1.groupByKey(numReducers).count`:

  - This job has 2 stages.
  - Stage 0 contains 100 ShuffleMapTask, each task reads a partition of `paris1` from the cache, repartitions it, and then write the repartitioned results into local disk. This step is similar to partitioning map outputs in Hadoop.
  - Stage 1 contains 36 ResultTasks. Each task fetches and shuffles the data that it needs to process. It fetches the data, aggregates the data, and performes mapPartitions() operation in a pipeline style. Finally, count() is applied to get the result.
  - After the ResultTasks finish, the driver collects the tasks' results and sums them up.
  - Job 1 completes.

We can see that the physical plan is not simple. A Spark application can contain multiple jobs, each job could have multiple stages, and each stage has multiple tasks. **In later chapters, we'll detail how the jobs, stages and tasks are generated**

## Conclusion
Now, we have a basic knowledge of Spark job's creation and execution. We also discussed the cache feature of Spark.
In the following chapters, we'll discuss the key steps in job's creation and execution, including:
  1. Logical plan generation
  2. Physical plan generation
  3. Job submission and scheduling
  4. Task's creation, execution and result handling
  5. How shuffle is done in Spark
  6. Cache mechanism
  7. Broadcast mechanism
  
  
  * * *
  
  # Job Logical Plan

## An example of general logical plan
![deploy](../PNGfigures/GeneralLogicalPlan.png)

The above figure illustrates a general job logical plan, which takes 4 steps to get the final result:

1.	Create the initial `RDD` from any source (e.g., in-memory data structures, local file, HDFS, and HBase). Note that `createRDD()` is equivalent to `parallelize()` mentioned in the previous chapter.

2.	A series of *transformation operations* on `RDD`, denoted as `transformation()`. Each `transformation()` produces one or multiple serial `RDD[T]`s, where `T` can be any type in Scala.

	>	If T is (K, V), K cannot be set to be collection type, such as `Array` and `List`, since it is hard to define `partition()` function on collections.

3.	*Action operation*, denoted as `action()` is called on the final `RDD`. Then, each partition generates computing result.

4.	These results will be sent to the driver, then `f(List[Result])` will be performed to compute the final result. For example, `count()` takes two steps, `action()` and `sum()`.

> RDD can be cached in memory or persited on disk, by calling `cache()`, `persist()` or `checkpoint()`. The number of partitions is usually set by user. Partition mapping between two RDDs can be 1:1 or M:N. In the picture above, we can see not only 1:1 mapping, but also M:N mapping.

## Logical Plan

While writing Spark code, you might also have a logical plan (e.g.,  how many RDDs will be generated) in you mind (like the one above). However, in general, more RDDs will be generated at runtime.

In order to make this logical plan clear, we will answer the following questions from the view of Spark itself: Given a Spark program,

-	How to produce RDDs? What kinds of RDDs should be produced?
-	How to connect (i.e., build data dependency between) RDDs?

###	1. How to produce RDDs? What RDD should be produced?

A `transformation()` usually produces a new RDD, but some `transformation()`s can produce multiple RDDs because they have multiple processing steps or contain several sub-`transformation()`. That's why the number of RDDs is, in fact, more than we thought.

Logical plan is essentially a *computing chain*. Every RDD has a `compute()` method, which reads input records (e.g., key/value pairs) from the previous RDD or data source, performs `transformation()`, and then outputs new records.

What RDDs should be produced depends on the computing logic of the `transformation()`. Let's talk about some typical [transformation()](http://spark.apache.org/docs/latest/programming-guide.html#transformations) and their produced RDDs.

We can learn about the meaning of each `transformation()` on Spark site. More details are listed in the following table, where `iterator(split)` denotes *for each record in a partition*. There are some blanks in the table, because they are complex `transformation()` that produce multiple RDDs. They will be detailed soon after.

| Transformation |  Generated RDDs | Compute() |
|:-----|:-------|:---------|
| **map**(func) | MappedRDD | iterator(split).map(f) |
| **filter**(func) | FilteredRDD | iterator(split).filter(f) |
| **flatMap**(func) | FlatMappedRDD | iterator(split).flatMap(f) |
| **mapPartitions**(func) | MapPartitionsRDD | f(iterator(split)) | |
| **mapPartitionsWithIndex**(func) | MapPartitionsRDD |  f(split.index, iterator(split)) | |
| **sample**(withReplacement, fraction, seed) | PartitionwiseSampledRDD | PoissonSampler.sample(iterator(split))  BernoulliSampler.sample(iterator(split)) |
| **pipe**(command, [envVars]) | PipedRDD | |
| **union**(otherDataset) |  |  |
| **intersection**(otherDataset) | | |
| **distinct**([numTasks])) | | |
| **groupByKey**([numTasks]) | | |
| **reduceByKey**(func, [numTasks]) | | |
| **sortByKey**([ascending], [numTasks]) | | |
| **join**(otherDataset, [numTasks]) | | |
| **cogroup**(otherDataset, [numTasks]) | | |
| **cartesian**(otherDataset) | | |
| **coalesce**(numPartitions) | | |
| **repartition**(numPartitions) | | |

###	2. How to build data dependency between RDDs?

This question can be divided into three smaller questions:
-	A RDD (e.g., `RDD x`) depends on one parent RDD or several parent RDDs?
-	How many partitions are there in `RDD x`?
-	What's the relationship between the partitions of `RDD x` and those of its parent RDD(s)? One partition depends one or several partitions of the parent RDD?

The first question is trivial. `x = rdda.transformation(rddb)` means that RDD `x` depends on `rdda` and `rddb`. For example, `val x = a.join(b)` means that `RDD x` depends both `RDD a` and `RDD b`.

For the second question, as mentioned before, the number of partitions is defined by user, by default, it takes `max(partitionNum of parentRDD1, ..., partitionNum of parentRDDn)`.

The third question is a bit complex, we need to consider the semantics of `transformation()`. Different `transformation()`s have different data dependencies. For example, `map()` is 1:1. `groupByKey()` produces a `ShuffledRDD`, in which each partition depends on all partitions in its parent RDD. Some other `transformation()`s can be more complex.

In Spark, there are two  kinds of data partition dependencies between RDDs:
-	NarrowDependency (e.g., OneToOneDependency and RangeDependency)

	>	Each partition of the child RDD **fully** depends on a small number of partitions of its parent RDD. **Fully depends** (i.e., **FullDependency**) means that a child partition depends the **entire** parent partition.
-	ShuffleDependency (or Wide dependency mentioned in Matei's paper)

	>	Multiple child partitions **partially** depends on a parent partition. **Partially depends** (i.e., **PartialDependency**) means that each child partition depends **a part of** the parent partition.

For example, `map()` leads to a narrow dependency, while `join()` usually leads to to a wide
dependencies.

Moreover, a child partition can depend on one partition in a parent RDD and one partition in another parent RDD.

Note that:
-	For `NarrowDependency`, whether a child partition depends one or multiple parent partitions is determined by the `getParents(partition i)` function in child RDD. (More details later)
-	ShuffleDependency is like shuffle dependency  in MapReduce（the mapper partitions its outputs, then each reducer will fetch all the needed output partitions via http.fetch)

The two dependencies are illustrated in the following figure.

![Dependency](../PNGfigures/Dependency.png)

According to the definition, the first three cases are `NarrowDependency` and the last one is `ShuffleDependency`.

Need to mention that the left one on the second row is a rare case. It is a N:N `NarrowDependency`. Although it looks like ShuffleDependency, it is a full dependency. It can be created in some tricky `transformation()`s. We will not talk about this case, because `NarrowDependency` essentially means **each partition of the parent RDD is used by at most one partition of the child RDD** in Spark source code.

In summary, data partition dependencies are listed as below
- NarrowDependency (black arrow)
	- RangeDependency => only used for UnionRDD
	- OneToOneDependency (1:1) => e.g., map(), filter()
	- NarrowDependency (N:1) => e.g., co-partitioned join()
	- NarrowDependency (N:N) => a rare case
- ShuffleDependency (red arrow)

Note that, in the rest of this chapter, `NarrowDependency` will be drawn as black arrows and `ShuffleDependency` are red ones.

The classificaiton of `NarrowDependency` and `ShuffleDependency` is needed for generating physical plan, which will be detailed in the next chapter.

### 3. How to compute records in the RDD?

An `OneToOneDependency` case is shown in the following figure. Although the data partition relationship is 1:1, it doesn't mean that the records in each partition should be read, computed, and outputted one by one.

The difference between the two patterns on the right side is similar to the following code snippets.

![Dependency](../PNGfigures/OneToOneDependency.png)

Code of iter.f():
```java
int[] array = {1, 2, 3, 4, 5}
for(int i = 0; i < array.length; i++)
    output f(array[i])
```
Code of f(iter):
```java
int[] array = {1, 2, 3, 4, 5}
output f(array)
```

### 4. Illustration of typical data partition dependencies

**1) union(otherRDD)**

![union](../PNGfigures/union.png)

`union()` simply combines two RDDs together. It never changes the data of a partition. `RangeDependency`(1:1) retains the borders of original RDDs in order to make it easy to revisit the original partitions.

**2) groupByKey(numPartitions)** [changed in 1.3]

![groupByKey](../PNGfigures/groupByKey.png)

We have talked about `groupByKey`'s dependency before, now we make it more clear.

`groupByKey()` aggregates records with the same key by shuffle. The `compute()` function in `ShuffledRDD` fetches necessary data for its partitions, then performs `mapPartition()` operation in a `OneToOneDependency` style. Finally, `ArrayBuffer` type in the value is casted to `Iterable`.

>	`groupByKey()` has no map-side combine, because map-side combine does not reduce the amount of data shuffled and requires all map-side data be inserted into a hash table, leading to too many objects in the Old Gen.

>	`ArrayBuffer` is essentially `a CompactBuffer`, which is an append-only buffer similar to ArrayBuffer, but more memory-efficient for small buffers.

**2) reduceyByKey(func, numPartitions)** [changed in 1.3]

![reduceyByKey](../PNGfigures/reduceByKey.png)

`reduceByKey()` is similar to `reduce()` in MapReduce. The data flow is equivalent. `reduceByKey` enables map-side combine by default, which is carried out by `mapPartitions()` before shuffle and results in `MapPartitionsRDD`. After shuffle, `aggregate + mapPartitions()` is applied to `ShuffledRDD`. Again, we get a `MapPartitionsRDD`.

**3) distinct(numPartitions)**

![distinct](../PNGfigures/distinct.png)

`distinct()` aims to deduplicate RDD records. Since duplicated records can be found in different partitions, shuffle + aggregation is needed to deduplicate the records. However, shuffle requires that the type of RDD is `RDD[(K,V)]`. If the original records have only keys (e.g., `RDD[Int]`), it should be completed as `<K,null>` through performing a `map()` (results in a `MappedRDD`). After that, `reduceByKey()` is used to do some shuffle (mapSideCombine => reduce => MapPartitionsRDD). Finally, only key is taken from `<K,null>` by `map()`(`MappedRDD`). The blue RDDs are exactly the RDDs in `reduceByKey()`.

**4) cogroup(otherRDD, numPartitions)**

![cogroup](../PNGfigures/cogroup.png)

Different from `groupByKey()`, `cogroup()` aggregates 2 or more RDDs. Here is a question: **Should the partition relationship between (RDD a, RDD b) and CoGroupedRDD be ShuffleDependency or OneToOneDependency?** This question is bit complex and related to the following two items.

-	Number of partition

	The # of partition in `CoGroupedRDD` is defined by user, and it has nothing to do with `RDD a` and `RDD b`. However, if #partition of `CoGroupedRDD` is different from that of `RDD a` or `RDD b`, the partition dependency cannot be an `OneToOneDependency`.

-	Type of the partitioner

	The `partitioner` defined by user (`HashPartitioner` by default) determines how to partition the data. If `RDD a`, `RDD b`, and `CoGroupedRDD` have the same # of partition but different partitioners, the partition dependency cannot be `OneToOneDependency`. Let's take the last case in the above figure as an example, `RDD a` is `RangePartitioner`, `RDD b` is `HashPartitioner`, and `CoGroupedRDD` is `RangePartitioner` with the same # partition as `RDD a`. Obviously, the records in each partition of `RDD a` can be directly sent to the corresponding partition in `CoGroupedRDD`, but those in `RDD b` need to be divided in order to be shuffled into the right partitions of `CoGroupedRDD`.

To conclude, `OneToOneDependency` occurs if the partitioner type and #partitions of the parent RDDs and `CoGroupedRDD` are the same. Otherwise, the dependency must be a `ShuffleDependency`. More details can be found in `CoGroupedRDD.getDependencies()`'s source code.

**How does Spark keep multiple partition dependencies for each partition in  `CoGroupedRDD`?**

Firstly, `CoGroupedRDD` put all the parent `RDD`s into `rdds: Array[RDD]`

Then,
```
Foreach rdd = rdds(i):
	if the dependency between CoGroupedRDD and rdd is OneToOneDependency
		Dependecy[i] = new OneToOneDependency(rdd)
	else
		Dependecy[i] = new ShuffleDependency(rdd)
```

Finally, it returns `deps: Array[Dependency]`, which is an array of `Dependency` corresponding to each parent RDD.

`Dependency.getParents(partition id)` returns `partitions: List[Int]`, which are the parent partitions of the partition (id) with respect to the given `Dependency`.

`getPartitions()` tells how many partitions exist in a `RDD` and how each partition is serialized.

**5) intersection(otherRDD)**

![intersection](../PNGfigures/intersection.png)

`intersection()` aims to extract all the common elements from  `RDD a` and `RDD b`. `RDD[T]` is mapped into `RDD[(T,null)]`, where `T` cannot be any collections. Then, `a.cogroup(b)` (colored in blue) is performed. Next, `filter()` only keeps the records where neither of `[iter(groupA()), iter(groupB())]` is empty (`FilteredRDD`). Finally, only keys of the reocrds are kept in `MappedRDD`.

6) **join(otherRDD, numPartitions)**

![join](../PNGfigures/join.png)

`join()` takes two `RDD[(K,V)]`, like `join` in SQL. Similar to `intersection()`, it does `cogroup()` first and results in a `MappedValuesRDD` whose type is `RDD[(K, (Iterable[V1],Iterable[V2]))]`. Then, it computes the Cartesian product between the two `Iterable`, and finally `flatMap()` is performed.

Here are two examples, in the first one, `RDD 1` and `RDD 2` use `RangePartitioner`, while `CoGroupedRDD` uses `HashPartitioner`, so the partition dependency is `ShuffleDependency`. In the second one, `RDD 1` is previously partitioned on key by `HashPartitioner` and gets 3 partitions.  Since `CoGroupedRDD` also uses `HashPartitioner` and generates 3 partitions, their depedency is `OneToOneDependency`. Furthermore, if `RDD 2` is also previously divided by `HashPartitioner(3)`, all the dependencies will be `OneToOneDependency`. This kind of `join` is called `hashjoin()`.

**7) sortByKey(ascending, numPartitions)**

![sortByKey](../PNGfigures/sortByKey.png)

`sortByKey()` sorts records of `RDD[(K,V)]` by key. `ascending` is a self-explanatory boolean flag. It produces a `ShuffledRDD` which takes a `rangePartitioner`. The partitioner decides the border of each partition. For example, the first partition takes records with keys from `char A` to `char B`, and the second takes those from `char C` to `char D`. Inside each partition, records are sorted by key. Finally, the records in `MapPartitionsRDD` are in order.

> `sortByKey()` uses `Array` to store the records of each partition, then sorts them.

**8) cartesian(otherRDD)**

![cartesian](../PNGfigures/Cartesian.png)

`Cartesian()` returns a Cartesian product of two `RDD`s. The resulting `RDD` has `#partition(RDD a) * #partition(RDD b)` partitions.

Need to pay attention to the dependency, each partition in `CartesianRDD` depends 2 **entire** parent RDDs. They are all `NarrowDependency`.

> `CartesianRDD.getDependencies()` returns `rdds: Array(RDD a, RDD b)`. The i-th partition of `CartesianRDD` depends:
-	`a.partitions(i / #partitionA)`
-	`b.partitions(i % #partitionB)`

**9) coalesce(numPartitions, shuffle = false)**

![Coalesce](../PNGfigures/Coalesce.png)

`coalesce()` can reorganize partitions, e.g. decrease # of partitions from 5 to 3, or increase from 5 to 10. Need to notice that when `shuffle = false`, we cannot increase partitions, because that will force a shuffle.

To understand `coalesce()`, we need to know **the relationship between `CoalescedRDD`'s partitions and its parent partitions**

-	`coalesce(shuffle = false)`
	Since shuffle is disabled, what we can do is just to group certain parent partitions. In fact, to achieve a *good* group, there are many factors to take into consideration, e.g. # records in partition, locality, balance, etc. Spark has a rather complicated algorithm to do with that (we will not talk about that for the moment). For example, `a.coalesce(3, shuffle = false)` is essentially a `NarrowDependency` of N:1.

- 	`coalesce(shuffle = true)`
	When shuffle is enabled, `coalesce` simply divides all records of `RDD` into N partitions, which can be done by the following tricky method (like round-robin algorithm):
	-	for each partition, every record is assigned a key which is an increasing number.
	-	hash(key) leads to a uniform records distribution on all different partitions.

	In the second example, every record in `RDD a` is combined with a increasing key (on the left side of the pair). The key of the first record in each partition is equal to `(new Random(index)).nextInt(numPartitions)`, where `index` is the index of the partition and `numPartitions` is the # of partitions in `CoalescedRDD`. The following keys increase by 1. After shuffle, the records in `ShuffledRDD` are uniformly distributed. The relationship between `ShuffledRDD` and `CoalescedRDD` is defined a complicated algorithm. In the end, keys are removed (`MappedRDD`).

**10) repartition(numPartitions)**

Equivalent to coalesce(numPartitions, shuffle = true)

## The primitive transformation()
**combineByKey()**

**So far, we have analyzed a lot of logic plans. It's true that some of them are very similar. The reason is that they have the same shuffle+aggregate behavior:**

The RDD on left side of `ShuffleDependency` is `RDD[(K,V)]`, while, on the right side, all records with the same key are aggregated, then different operations will be applied on these aggregated records.

In fact, many `transformation()`, like `groupByKey()`, `reduceBykey()`, executes `aggregate()` while doing logical computation. So **the similarity is that `aggregate()` and `compute()` are executed in the same time.** Spark uses `combineByKey()` to implement `aggregate() + compute()` operation.

Here is the definition of `combineByKey()`
```scala
 def combineByKey[C](createCombiner: V => C,
      mergeValue: (C, V) => C,
      mergeCombiners: (C, C) => C,
      partitioner: Partitioner,
      mapSideCombine: Boolean = true,
      serializer: Serializer = null): RDD[(K, C)]
```

There are three important parameters:
 -	`createCombiner`, which turns a V into a C (e.g., creates an one-element list)
 -	`mergeValue`, to merge a V into a C (e.g., adds an element to the end of the list)
 -	`mergeCombiners`, to combine two C's into a single one (e.g., merge two lists into a new one).

Details:

-	When some (K, V) records are being pushed to `combineByKey()`, `createCombiner` takes the first record to initialize a combiner of type `C` (e.g., C = V).
-	From then on, `mergeValue` takes every incoming record, `mergeValue(combiner, record.value)`, to update the combiner. Let's take `sum` as an example, `combiner = combiner + recode.value`. In the end, all concerned records are merged into the combiner
-	If there is another set of records with the same key as the pairs above. `combineByKey()` will produce another `combiner'`. In the last step, the final result is equal to `mergeCombiners(combiner, combiner')`.

## Conclusion

So far, we have discussed how to produce job's logical plan as well as the complex partition dependency and computation behind Spark.

`tranformation()` decides what kind of RDDs will be produced. Some `transformation()` are reused by other operations (e.g., `cogroup`).

The dependency of a `RDD` depends on the semantics of `transformation()`. For example, `CoGroupdRDD` depends on all `RDD`s used for `cogroup()`.

The relationship of `RDD` partitions are `NarrowDependency` and `ShuffleDependency`. The former is **full dependency** and the latter is **partial dependency**. `NarrowDependency` can be represented in many cases. A dependency is a `NarrowDependency`, if the RDDs' #partition and partitioner type are the same.

In terms of dataflow, `MapReduce` is equivalent to `map() + reduceByKey()`. Technically, the `reduce()` of `MapReduce` would be more powerful than `reduceByKey()`. The design and implementation of shuffle will be detailed in chapter **Shuffle details**.

* * *

# Physical Plan

In the overview chapter, we briefly introduced the DAG-like physical plan, which contains stages and tasks. In this chapter, we'll look at **how the physical plan (e.g., the stages and tasks) is generated from a logical plan of a Spark application.**

## A Complex Logical Plan

![ComplexJob](../PNGfigures/ComplexJob.png)
The code of this application is attached at the end of this chapter.

**How to properly determine the stages and tasks within such a complex data dependency graph?**

An intuitive idea is to associate one RDD and its preceding RDD to form a stage. In this way, each arrow in the above figure will become a task. For the case of 2 RDDs aggregate into one, we may create a stage with these 3 RDDs. This strategy could be a working solution, but it's not efficient. It has a subtle, but severe problem: **lots of intermediate data needs to be stored**. For a physical task, its result will be stored either on local disk, or in the memory, or both. If a task is generated for each arrow in the data dependency graph, the system needs to store data of all the RDDs. It will cost a lot.

If we examine the logical plan more closely, we may find out that in each RDD, the partitions are independent from each other. That is to say, inside each RDD, the data within a partition will not interfere others. With this observation, an aggressive idea is to consider the whole diagram as a single stage and create one physical task for each partition of the final RDD (`FlatMappedValuesRDD`). The following diagram illustrates this idea:

![ComplexTask](../PNGfigures/ComplexTask.png)

All thick arrows in above diagram belong to task1, whose result is the first partition of the final RDD of the job. Note that in order to compute the first partition of the `CoGroupedRDD`, we need to compute all partitions of its preceding RDDs (e.g., all the partitions in UnionRDD) since it's a `ShuffleDependency`. After that, we can compute the `CoGroupedRDD`'s second and third partition using task2 (thin arrows) and task3 (dashed arrows), which are much simpler.

However, there's 2 problems within this idea:
  - The first task is too large. We have to compute all the partitions of the preceding RDDs (i.e., UnionRDD), because of the `ShuffleDependency`.
  - Need to design clever algorithms to determine which partitions (computed in the first task) need to be cached for the following tasks.

Although there are problems within this idea, there is still a good point in this idea, that is to **pipeline the data: the data is computed only if they are actually needed in a flow fashion**. For example in the first task, we check backwards from the final RDD (`FlatMappedValuesRDD`) to see which RDDs and partitions are actually needed to be computed. Moreover, between the RDDs with `NarrowDependency` relation, no intermediate data needs to be stored.

It will be clearer to understand the pipelining if we look at the partition relationship from a record-level point of view. The following diagram illustrates different  patterns of record processing for RDDs with `NarrowDependency`.

![Dependency](../PNGfigures/pipeline.png)

The first pattern (pipeline pattern) is equivalent to:

```scala
for (record <- records) {
  g(f(record))
}
```

Considering `records` as a stream, we can see that no intermediate results need to be stored. For example, once the result of `g(f(record1))` is generated, the original `record1` and result of `f(record1)` can be garbarge collected. Next, we can compute `g(f(record2))`. However, for other patterns (e.g., the third pattern as follows), this is not the case:

```scala
// The third pattern
def f(records) {
  var result
  for (record <- records)
    result.aggregate(process(record)) // need to store the intermediate result here
  result.iterator // return the iterator of newly-generated [record1, record2, record3]
}

val fResult = f(records) // newly-generated [record1, record2, record3]

for (record <- fResult) {
  g(record)
}
```

It's clear that `f`'s results need to be stored somewhere (e.g., in-memory data structures).

Let's go back to our problem with stages and tasks. The main issue of the above aggressive idea is that we can't pipeline the data flow if there's a `ShuffleDependency`. Since `NarrowDependency` can be pipelined, we can cut off the data flow at each `ShuffleDependency`, leaving chains of RDDs connected by `NarrowDependency`. For example, we can just divide the logical plan into stages like this:

![ComplextStage](../PNGfigures/ComplexJobStage.png)

The strategy for creating stages is to: **check backwards from the final RDD, add each `NarrowDependency` into the current stage, and break out for a new stage when there's a `ShuffleDependency`. In each stage, the task number is determined by the partition number of the last RDD in the stage.**

In above diagram, all thick arrows represent tasks. Since the stages are determined backwards, the last stage's id is 0, stage 1 and stage 2 are both parents of stage 0. **If a stage generates the final result, the tasks in this stage are of type `ResultTask`, otherwise they are `ShuffleMapTask`.** `ShuffleMapTask` gets its name because its results need to be shuffled to the next stage, which is similar to the mappers in Hadoop MapReduce. `ResultTask` can be regarded as reducer (when it gets shuffled data from its parent stages), or mapper (when the current stage has no parents).

**One problem remains:** `NarrowDependency` chain can be pipelined, but in our example application, we've showed only `OneToOneDependency` and `RangeDependency`, how about the `NarrowDependency (M:N)`?

Let's check back the cartesian operation in the previous chapter with complex `NarrowDependency` inside:

![cartesian](../PNGfigures/Cartesian.png)

This NarrowDependency only needs one stage as follows:

![cartesian](../PNGfigures/cartesianPipeline.png)

The thick arrows represent the first `ResultTask`. Since the stage directly outputs the final result, 6 `ResultTask` are generated. Different with `OneToOneDependency`, each `ResultTask` in this job needs to compute 3 RDDs (RDD a, b, and CartesianRDD) and read 2 data blocks, all executed in one single task. **We can see that regardless of the actual type of `NarrowDependency`, be it 1:1 or N:N, `NarrowDependency` chain can always be pipelined. The number of task  is the same as the partition number in the final RDD.**

## Execution of the Physical Plan
We have known how to generate stages and tasks, next problem is that: **how the tasks are executed?**

Let's go back to the physical plan of our example application. Recall that in Hadoop MapReduce, the tasks are executed in order, `map()` generates map outputs, which are partitioned and written to local disk. Then, `shuffle-sort-aggregate` process is applied to generate reduce inputs (i.e., \<k, list(v)\> records). Finally `reduce()` is performed to generate the final result. This process is illustrated in the following diagram:

![MapReduce](../PNGfigures/MapReduce.png)

This execution process cannot be used directly on Spark's physical plan since Hadoop MapReduce's physical plan is simple and fixed, and without pipelining.

The main idea of pipelining is that **the data is computed when they are actually needed in a flow fashion.** We start from the final result and check backwards the RDD chain to find what RDDs and partitions are needed for computing the final result. In most cases, we trace back to some partitions in the leftmost RDD and they are the first to be computed.

**For a stage without parent stages, its leftmost RDD can be evaluate directly (it has no dependency), and each record evaluated can be streamed into the subsequent computations (pipelining).** The computation chain is deduced backwards from the final step, but the actual execution streams the records forwards. One record goes through the whole computation chain before the computation of the next record starts.

For stages with parent stages, we need to execute its parent stages and then fetch the data through shuffle. Once it's done, it becomes the same case as a stage without parent stages.

> In the code, each RDD's `getDependency()` method declares its data dependency. `compute()` method is in charge of receiving upstream records (from parent RDD or data source) and applying computation logic. We often see code like this in RDDs: `firstParent[T].iterator(split, context).map(f)`. Here, `firstParent` is the first dependent RDD, `iterator()` shows that the records are consumed one by one, and `map(f)` applies the computation logic `f` on each record. The `compute()` method returns an iterator of the computed records in this RDD for next computation.

Summary so far: **The whole computation chain is created by checking backwards the data depency from the last RDD. Each `ShuffleDependency` separates stages. In each stage, each RDD's `compute()` method calls `parentRDD.iterator()` to receive the upstream record stream.**

Note that `compute()` method is declared only for computation logic. The actual dependent RDDs are declared in `getDependency()` method, and the dependent partitions are declared in `dependency.getParents()` method.

Let's check the `CartesianRDD` as an example:

```scala
 // RDD x is the cartesian product of RDD a and RDD b
 // RDD x = (RDD a).cartesian(RDD b)
 // Defines how many partitions RDD x should have, and the type of each partition
 override def getPartitions: Array[Partition] = {
    // Create the cross product split
    val array = new Array[Partition](rdd1.partitions.size * rdd2.partitions.size)
    for (s1 <- rdd1.partitions; s2 <- rdd2.partitions) {
      val idx = s1.index * numPartitionsInRdd2 + s2.index
      array(idx) = new CartesianPartition(idx, rdd1, rdd2, s1.index, s2.index)
    }
    array
  }

  // Defines the computation logic for each partition of RDD x (the result RDD)
  override def compute(split: Partition, context: TaskContext) = {
    val currSplit = split.asInstanceOf[CartesianPartition]
    // s1 shows that a partition in RDD x depends on one partition in RDD a
    // s2 shows that a partition in RDD x depends on one partition in RDD b
    for (x <- rdd1.iterator(currSplit.s1, context);
         y <- rdd2.iterator(currSplit.s2, context)) yield (x, y)
  }

  // Defines which are the dependent partitions and RDDs for partition i in RDD x
  //
  // RDD x depends on RDD a and RDD b, both are `NarrowDependency`
  // For the first dependency, partition i in RDD x depends on the partition with
  //     index "i / numPartitionsInRDD2" in RDD a
  // For the second dependency, partition i in RDD x depends on the partition with
  //     index "i % numPartitionsInRDD2" in RDD b
  override def getDependencies: Seq[Dependency[_]] = List(
    new NarrowDependency(rdd1) {
      def getParents(id: Int): Seq[Int] = List(id / numPartitionsInRdd2)
    },
    new NarrowDependency(rdd2) {
      def getParents(id: Int): Seq[Int] = List(id % numPartitionsInRdd2)
    }
  )
```

## Job Creation

Now we've introduced the logical plan and physical plan, then **how and when a Spark job is created? What exactly is a job?**

The following table shows the typical [action()](http://spark.apache.org/docs/latest/programming-guide.html#actions). The second column is `processPartition()` method, it defines how to process the records in each partition and generate the result of finalRDD (we call it partial results). The third column is `resultHandler()` method, it defines how to process the partial results from each partition to form the final results.

| Action | finalRDD(records) => result | compute(results) |
|:---------| :-------|:-------|
| reduce(func) | (record1, record2) => result, (result, record i) => result | (result1, result 2) => result, (result, result i) => result
| collect() |Array[records] => result | Array[result] |
| count() | count(records) => result | sum(result) |
| foreach(f) | f(records) => result | Array[result] |
| take(n) | record (i<=n) => result | Array[result] |
| first() | record 1 => result | Array[result] |
| takeSample() | selected records => result | Array[result] |
| takeOrdered(n, [ordering]) | TopN(records) => result | TopN(results) |
| saveAsHadoopFile(path) | records => write(records) | null |
| countByKey() | (K, V) => Map(K, count(K)) | (Map, Map) => Map(K, count(K)) |

Each time there is an `action()` in user's driver program, a job will be created. For example, `foreach()` action will call `sc.runJob(this, (iter: Iterator[T]) => iter.foreach(f)))` to submit a job to the `DAGScheduler`. If there are other `action()`s in the driver program, there will be other jobs submitted. So, we will have as many jobs as the `action()` operations in a driver program. This is why a driver program is called as an application rather than a job.

The last stage of a job generates the job's results. For example in the `GroupByTest` in the first chapter, there're 2 jobs with 2 sets of results. When a job is submitted, the `DAGScheduler` applies the Application-LogicalPlan-PhysicalPlan strategy to figure out the stages, and submits firstly the **stages without parents** for execution. In this process, the number and type of tasks are also determined. A stage is executed after its parent stages' finish.

## Details in Job Submission

Let's briefly analyze the code for job creation and submission. We'll come back to this part in the Architecture chapter.

1. `rdd.action()` calls `DAGScheduler.runJob(rdd, processPartition, resultHandler)` to create a job.
2. `runJob()` gets the partition number and type of the final RDD by calling `rdd.getPartitions()`. Then it allocates `Array[Result](partitions.size)` for holding the results based on the partition number.
3. Finally, `runJob(rdd, cleanedFunc, partitions, allowLocal, resultHandler)` in `DAGScheduler` is called to submit the job. `cleanedFunc` is the closure-cleaned version of `processPartition`. In this way this function can be serialized and sent to the different worker nodes.
4. `DAGScheduler`'s `runJob()` calls `submitJob(rdd, func, partitions, allowLocal, resultHandler)` to submit a job.
5. `submitJob()` gets a `jobId`, then wrap the function once again and send a `JobSubmitted` message to `DAGSchedulerEventProcessActor`. Upon receiving this message, the actor calls `dagScheduler.handleJobSubmitted()` to handle the submitted job. This is an example of event-driven programming model.
6. `handleJobSubmitted()` firstly calls `finalStage = newStage()` to create stages, then it `submitStage(finalStage)`. If `finalStage` has parents, the parent stages will be submitted first. In this case, `finalStage` is actually submitted by `submitWaitingStages()`.

How `newStage()` divide an RDD chain in stages?
- This method calls `getParentStages()` of the final RDD when instantiating a new stage (`new Stage(...)`)
- `getParentStages()` starts from the final RDD, check backwards the logical plan. It adds the RDD into the current stage if it's a `NarrowDependency`. When it meets a `ShuffleDependency` between RDDs, it takes in the right-side RDD (the RDD after the shuffle) and then concludes the current stage. Then the same logic is applied on the left hand side RDD of the shuffle to form another stage.
- Once a `ShuffleMapStage` is created, its last RDD will be registered `MapOutputTrackerMaster.registerShuffle(shuffleDep.shuffleId, rdd.partitions.size)`. This is important since the shuffle process needs to know the data output location from `MapOuputTrackerMaster`.

Now let's see how `submitStage(stage)` submits stages and tasks:

1. `getMissingParentStages(stage)` is called to determine the `missingParentStages` of the current stage. If the parent stages are all executed, `missingParentStages` will be empty.
2. If `missingParentStages` is not empty, then recursively submit these missing stages, and the current stage is inserted into `waitingStages`. Once the parent stages are done, stages inside `waitingStages` will be run.
3. if `missingParentStages` is empty, then we know the stage can be executed right now. Then `submitMissingTasks(stage, jobId)` is called to generate and submit the actual tasks. If the stage is a `ShuffleMapStage`, then we'll allocate as many `ShuffleMapTask` as the partition number in the final RDD. In the case of `ResultStage`, `ResultTask` instances are allocated instead. The tasks in a stage form a `TaskSet`. Finally `taskScheduler.submitTasks(taskSet)` is called to submit the whole task set.
4. The type of `taskScheduler` is `TaskSchedulerImpl`. In `submitTasks()`, each `taskSet` gets wrapped in a `manager` variable of type `TaskSetManager`, then we pass it to `schedulableBuilder.addTaskSetManager(manager)`. `schedulableBuilder` could be `FIFOSchedulableBuilder` or `FairSchedulableBuilder`, depending on the configuration. The last step of `submitTasks()` is to inform `backend.reviveOffers()` to run the task. The type of backend is `SchedulerBackend`. If the application is run on a cluster, its type will be `SparkDeploySchedulerBackend`.
5. `SparkDeploySchedulerBackend` is a subclass of `CoarseGrainedSchedulerBackend`, `backend.reviveOffers()` actually sends `ReviveOffers` message to `DriverActor`. `SparkDeploySchedulerBackend` launches a `DriverActor` when it starts. Once `DriverActor` receives the `ReviveOffers` message, it will call `launchTasks(scheduler.resourceOffers(Seq(new WorkerOffer(executorId, executorHost(executorId), freeCores(executorId)))))` to launch the tasks. `scheduler.resourceOffers()` obtains the sorted `TaskSetManager` from the FIFO or Fair scheduler and gethers other information about the tasks from `TaskSchedulerImpl.resourceOffer()`. These information are stored in a `TaskDescription`. In this step the data locality information is also considered.
6. `launchTasks()` in the `DriverActor` serialize each task. If the serialized size does not exceed the `akkaFrameSize` limit of Akka, then the task is finally sent to the executor for execution: `executorActor(task.executorId) ! LaunchTask(new SerializableBuffer(serializedTask))`.

## Discussion
Up till now, we've discussed:
- How the driver program triggers jobs
- How to generate a physical plan from a logical plan
- What is pipelining in Spark and how it is used and implemented
- The code analysis of job creation and submission

However, there are subjects left for furhter discussion:
- The shuffle process
- Task execution procedure and execution location

In the next chapter, we'll discuss the shuffle process in Spark.

In my personal opinion, the transformation from logical plan to physical plan is really a masterpiece. The abstractions, such as dependencies, stages, and tasks are all well defined and the logic of the implementation algorithms are very clear.

## Source Code of the Example Job

```scala
package internals

import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.HashPartitioner


object complexJob {
  def main(args: Array[String]) {

    val sc = new SparkContext("local", "ComplexJob test")

    val data1 = Array[(Int, Char)](
      (1, 'a'), (2, 'b'),
      (3, 'c'), (4, 'd'),
      (5, 'e'), (3, 'f'),
      (2, 'g'), (1, 'h'))
    val rangePairs1 = sc.parallelize(data1, 3)

    val hashPairs1 = rangePairs1.partitionBy(new HashPartitioner(3))


    val data2 = Array[(Int, String)]((1, "A"), (2, "B"),
      (3, "C"), (4, "D"))

    val pairs2 = sc.parallelize(data2, 2)
    val rangePairs2 = pairs2.map(x => (x._1, x._2.charAt(0)))


    val data3 = Array[(Int, Char)]((1, 'X'), (2, 'Y'))
    val rangePairs3 = sc.parallelize(data3, 2)


    val rangePairs = rangePairs2.union(rangePairs3)


    val result = hashPairs1.join(rangePairs)

    result.foreachWith(i => i)((x, i) => println("[result " + i + "] " + x))

    println(result.toDebugString)
  }
}
```

