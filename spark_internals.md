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

#### Introduction
Spark is a generalized framework for distributed data processing providing functional API for manipulating data at scale, in-memory data caching and reuse across computations. It applies set of coarse-grained transformations over partitioned data and relies on dataset's lineage to recompute tasks in case of failures. Worth mentioning is that Spark supports majority of data formats, has integrations with various storage systems and can be executed on Mesos or YARN. 

*Powerful and concise API in conjunction with rich library makes it easier to perform data operations at scale. E.g. performing backup and restore of Cassandra column families in Parquet format:*
```
def backup(path: String, config: Config) {  
  sc.cassandraTable(config.keyspace, config.table)
    .map(_.toEvent).toDF()
    .write.parquet(path)
}

def restore(path: String, config: Config) {  
  sqlContext.read.parquet(path)
  .map(_.toEvent)
  .saveToCassandra(config.keyspace, config.table)
}
```
*Or run discrepancies analysis comparing the data in different data stores:*
```
sqlContext.sql {  
  """
     SELECT count()
     FROM cassandra_event_rollups
     JOIN mongo_event_rollups
     ON cassandra_event_rollups.uuid = cassandra_event_rollups.uuid
     WHERE cassandra_event_rollups.value != cassandra_event_rollups.value
  """.stripMargin
}
```

Spark is built around the concepts of Resilient Distributed Datasets and Direct Acyclic Graph representing transformations and dependencies between them.

![internals2](Images/InternalsSpark/internal1.png)

Spark Application (often referred to as Driver Program or Application Master) at high level consists of SparkContext and user code which interacts with it creating RDDs and performing series of transformations to achieve final result. These transformations of RDDs are then translated into DAG and submitted to Scheduler to be executed on set of worker nodes.

#### RDD: Resilient Distributed Dataset
RDD could be thought as an immutable parallel data structure with failure recovery possibilities. It provides API for various transformations and materializations of data as well as for control over caching and partitioning of elements to optimize data placement. RDD can be created either from external storage or from another RDD and stores information about its parents to optimize execution (via pipelining of operations) and recompute partition in case of failure.

From a developer's point of view RDD represents distributed immutable data (partitioned data + iterator) and lazily evaluated operations (transformations). As an interface RDD defines five main properties:
```
//a list of partitions (e.g. splits in Hadoop)
def getPartitions: Array[Partition]

//a list of dependencies on other RDDs
def getDependencies: Seq[Dependency[_]]

//a function for computing each split
def compute(split: Partition, context: TaskContext): Iterator[T]

//(optional) a list of preferred locations to compute each split on
def getPreferredLocations(split: Partition): Seq[String] = Nil

//(optional) a partitioner for key-value RDDs
val partitioner: Option[Partitioner] = None  
```
Here's an example of RDDs created during a call of method sparkContext.textFile("hdfs://...") which first loads HDFS blocks in memory and then applies map() function to filter out keys creating two RDDs:

![internals2](Images/InternalsSpark/internal2.png)

- HadoopRDD:
  - getPartitions = HDFS blocks
  - getDependencies = None
  - compute = load block in memory
  - getPrefferedLocations = HDFS block locations
  - partitioner = None
- MapPartitionsRDD
  - getPartitions = same as parent
  - getDependencies = parent RDD
  - compute = compute parent and apply map()
  - getPrefferedLocations = same as parent
  - partitioner = None
  
  RDD Operations
Operations on RDDs are divided into several groups:

#### Transformations
- apply user function to every element in a partition (or to the whole partition) 
- apply aggregation function to the whole dataset (groupBy, sortBy)
- introduce dependencies between RDDs to form DAG
- provide functionality for repartitioning (repartition, partitionBy)

#### Actions
- trigger job execution
- used to materialize computation results

#### Extra: persistence
- explicitly store RDDs in memory, on disk or off-heap (cache, persist)
- checkpointing for truncating RDD lineage
- Here's a code sample of some job which aggregates data from Cassandra in lambda style combining previously rolled-up data with the data from raw storage and demonstrates some of the transformations and actions available on RDDs:
```
//aggregate events after specific date for given campaign
val events =  
    sc.cassandraTable("demo", "event")
      .map(_.toEvent)                                
      .filter { e =>
        e.campaignId == campaignId && e.time.isAfter(watermark)
      }
      .keyBy(_.eventType)
      .reduceByKey(_ + _)                                        
      .cache()                                            

//aggregate campaigns by type
val campaigns =  
    sc.cassandraTable("demo", "campaign")
      .map(_.toCampaign)
      .filter { c => 
         c.id == campaignId && c.time.isBefore(watermark)
      }
      .keyBy(_.eventType)
      .reduceByKey(_ + _)
      .cache()

//joined rollups and raw events
val joinedTotals = campaigns.join(events)  
           .map { case (key, (campaign, event)) => 
             CampaignTotals(campaign, event) 
            }
           .collect()

//count totals separately
val eventTotals =  
    events.map{ case (t, e) => s"$t -> ${e.value}" }
    .collect()

val campaignTotals =  
    campaigns.map{ case (t, e) => s"$t -> ${e.value}" }
    .collect()
```
![internals3](Images/InternalsSpark/internal3.png)

Here's a quick recap on the execution workflow before digging deeper into details: user code containing RDD transformations forms Direct Acyclic Graph which is then split into stages of tasks by DAGScheduler. Stages combine tasks which don’t require shuffling/repartitioning if the data. Tasks run on workers and results then return to client.

![internals4](Images/InternalsSpark/internal4.png)

Here's a DAG for the code sample above. So basically any data processing workflow could be defined as reading the data source, applying set of transformations and materializing the result in different ways. Transformations create dependencies between RDDs and here we can see different types of them.

The dependencies are usually classified as "narrow" and "wide":
![internals6](Images/InternalsSpark/internal6.png)

- Narrow (pipelineable)
  - each partition of the parent RDD is used by at most one partition of the child RDD
  - allow for pipelined execution on one cluster node
  - failure recovery is more efficient as only lost parent partitions need to be recomputed
- Wide (shuffle)
- multiple child partitions may depend on one parent partition
- require data from all parent partitions to be available and to be shuffled across the nodes
- if some partition is lost from all the ancestors a complete recomputation is needed

#### Splitting DAG into Stages
Spark stages are created by breaking the RDD graph at shuffle boundaries
![internals7](Images/InternalsSpark/internal7.png)
