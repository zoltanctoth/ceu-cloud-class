<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="exporter-version" content="Evernote Mac 7.10 (457750)" />
    <meta name="keywords" content="Actions, An End-to-End Example, DataFrames, DataFrames and SQL, Datasets: Type-Safe Structured APIs, Lazy Evaluation, Lower-Level APIs, Partitions, Running Production Applications, Spark Applications, Spark UI, Spark’s APIs, Spark’s Basic Architecture, Spark’s Ecosystem and Packages, Spark’s Language APIs, SparkR, Starting Spark, Structured-Streaming--Machine-Learning-and-Advanced-Analytics, The SparkSession, Transformations" />
    <meta name="created" content="2019-05-18 14:40:21 +0000" />
    <meta name="updated" content="2019-10-03 03:17:57 +0000" />
    ## Spark Overview
</head>

<body>
    <div style="text-align:center;"><br /></div>
    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><i>In our world collecting data is extremely inexpensive but processing it requires large, parallel computations, often on clusters of machines. That's what Apache Spark was built for.</i></span></span></div>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="--en-highlight:yellow;background-color: #ffef9e;">Apache Spark</span> </span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">is a </span></span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">unified</span> <span style="color: rgb(255, 0, 42);">computing</span></span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);"> </span></span></span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">engine</span></span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"> and a </span></span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">set of <span style="color: rgb(255, 0, 42);">libraries</span></span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"> for </span></span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">parallel data processing on computer clusters </span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">that </span></span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">supports programming languages</span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"> like R, Python, Java and Scala</span></span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"> and libraries</span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"> ranging from SQL to streaming and machine learning and runs everywhere from a laptop to a cluster of thousands of servers making it easy to scale up to big data processing or incredibly large scale.</span></span></div><img src="Spark%20Overview.html.resources/spark%20toollkit.png" height="599" width="882" />
    <div style="text-align:center;"><br /></div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);"><u>Unified:</u></span><span style="color: rgb(0, 0, 0);"> </span></span></b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Spark is designed to support a wide range of data analytics tasks over the same computing engine and with a consistent set of APIs. </span></span></div>
    <div><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">-&gt; Real world data analytics tasks tend to combine many different processing types and libraries. </span></span></div>
    <div><br /></div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);"><u>Consistent Composable APIs</u>: </span></span></b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">you can use to build an application out of smaller pieces or out of existing libraries. It also makes it easy for you to write your own analytics libraries on top. Spark's APIs are also designed to enable high performance by optimizing across the different libraries and functions composed together in a user program.</span></span></div>
    <div><span style="font-size: 12px;"><i><span style="color: rgb(0, 0, 0);">#Example_1: if you load data using SQL query and then evaluate a machine learning model over it using Spark's ML library, the engine can combine these steps into a one scan over the data. Thus, the combination of general APIs and high-performance execution, no matter how you combine them, makes Spark a powerful platform for interactive, and production applications.</span></i></span></div>
    <div><span style="font-size: 12px;"><i><span style="color: rgb(0, 0, 0);">#Example_2: Web developers benefit from unified frameworks such as Node.js or Django</span></i></span></div>
    <div><br /></div>
    <div><b><span style="font-size: 12px;"><i><span style="color: rgb(255, 0, 42);"><u>Computing Engine</u>:  </span></i></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Spark handles loading data from storage systems and performing computation on it, not being a permanent storage as the end itself. You can use Spark with a wide variety of storage systems such as Azure Storage and Amazon S3, distributed file systems such as Apache Hadoop, key-value stores such as Apache Cassandra and message buses such as Apache Kafka. However, Spark does not store data long-term itself.</span></span></span></div>
    <div><br /></div>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);"><u>Libraries:</u> </span></span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">builds on Spark's design as a unified engine to provide a unified API for common data analysis tasks. Spark supports standard libraries and external libraries. Spark includes libraries for SQL, and structured data SparkSQL, machine learning (MLlib), stream processing (Spark Streaming and the newer Structured Streaming), and graph analytics (GraphX). Beyond these libraries there are a hundreds of open source external libraries. (spark-packages.org)</span></span></span></div>
    <div><br /></div>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);"><u>Parallel Processing</u>: </span></span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">processing of program instructions by dividing them among multiple processors with the objective of running a program in less time. </span></span></span></div>
    <div><br /></div>
    <div><b><span style="font-size: 12px;">Running Spark -  </span></b><span style="font-size: 12px;">Spark runs on the JVM (Java Virtual Machine) so you need to install Java to run it. If you want to use the Python API, you will also need a Python interpreter. If you want to use R, you will need a version of R on your machine. </span></div>
    <div><br /></div>
    <div style="text-align:center;"><b><span style="font-size: 12px;">Launching Spark's Interactive Console</span></b></div>
    <div><br /></div>
    <table width="1427px" style="width:1427px;">
        <colgroup>
            <col style="width: 207px;" />
            <col style="width: 244px;" />
            <col style="width: 244px;" />
            <col style="width: 244px;" />
            <col style="width: 244px;" />
            <col style="width: 244px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;">Python</span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;">Scala</span></b></div>
                </td>
                <td rowspan="3" style="vertical-align:middle;"><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-18%20at%2010.14.35%20PM.png" height="300" width="1132" />
                    <div style="text-align:center;"><br /></div>
                </td>
                <td style="vertical-align:middle;">
                    <div style="text-align:center;"><b><span style="font-size: 12px;">SQL</span></b></div>
                </td>
                <td style="vertical-align:middle;">
                    <div style="text-align:center;"><span style="font-size: 12px;">|||||||||||</span></div>
                </td>
                <td style="vertical-align:middle;">
                    <div style="text-align:center;"><b><span style="font-size: 12px;">Cloud</span></b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;">./bin/pyspark</span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;">./bin/spark-shell</span></b></div>
                </td>
                <td style="vertical-align:middle;">
                    <div style="text-align:center;"><span style="font-size: 12px;">./bin/spark-sql</span></div>
                </td>
                <td style="vertical-align:middle;">
                    <div style="text-align:center;"><span style="font-size: 12px;">|||||||||||</span></div>
                </td>
                <td style="vertical-align:middle;">
                    <div style="text-align:center;"><span style="font-size: 12px;">Databrick's Community Edition</span></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div style="text-align:center;"><span style="font-size: 12px;">after you have done that type "spark" and press Enter. You will see the "SparkSession" object printed </span></div>
                </td>
                <td>
                    <div style="text-align:center;"><span style="font-size: 12px;">after you have done that type "spark" and press Enter. You will see the "SparkSession" object printed </span></div>
                </td>
                <td style="vertical-align:middle;">
                    <div><br /></div>
                </td>
                <td style="vertical-align:middle;">
                    <div style="text-align:center;"><span style="font-size: 12px;">|||||||||||</span></div>
                </td>
                <td style="vertical-align:middle;">
                    <div style="text-align:center;"><span style="font-size: 12px;">data used in this book: <a href="https://github.com/databricks/Spark-The-Definitive-Guide" rev="en_rl_none">https://github.com/databricks/Spark-The-Definitive-Guide</a></span></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">The SparkSession: </span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">You can control your Spark Application through a driver process called the SparkSession.</span></span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"> </span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">The SparkSession is the way Spark executes user-defined manipulations across the cluster. There is a one-to-one correspondance between a SparkSession and a SparkApplication.</span></span></div>
    <div style="text-align:center;"><br /></div>
    <div><b><span style="font-size: 12px;">Spark's Basic Architecture</span></b></div>
    <div><b><span style="font-size: 12px;"><i>Problem:</i></span></b><span style="font-size: 12px;"><i> one computer works well for watching movies or working with spreadsheet software. However, there are things a computer is not powerful enough to perform - e.g data processing. Single machines do not have the power and resources to perform computations on huge amounts of information or the user does not have time to wait for the computation to finish. </i></span></div>
    <div><span style="font-size: 12px;"><i>Solution -&gt;</i></span></div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);"><u>A cluster</u></span></span></b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);"> or group, of computers, pools the resources of many machines together, giving us the ability to use all the cumulative resources as if they were a single computer. A group of machines alone is not powerful, you need a framework to coordinate work across them - Spark does just that! - Coordinating and managing the execution of tasks on data across a cluster of computers.</span></span></div>
    <div><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">The cluster of machines that Spark uses to execute tasks is managed by a cluster manager. </span></span></div>
    <ul>
        <li>
            <div><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">YARN or Mesos or Spark's standalone cluster manager. We then submit Spark Applications to these cluster managers</span></span></div>
        </li>
    </ul>
    <div><br /></div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);"><u>Spark Application</u></span></span></b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);"> (</span></span><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><i>Architecture of a Spark Application)</i></span></span></div>
    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><i>Spark applications consist of a drives process and a set of executor processes.</i></span></span></div>
    <div><br /></div>
    <table width="1592px" style="width:1592px;">
        <colgroup>
            <col style="width: 724px;" />
            <col style="width: 868px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;"><span style="--en-highlight:yellow;background-color: #ffef9e;">Driver Process</span> </span></b><span style="font-size: 12px;"><i>(heart of a Spark Application, maintains all relevant information during the lifetime of the application.</i></span></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;"><span style="--en-highlight:yellow;background-color: #ffef9e;">Executor Processes</span></span></b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><span style="font-size: 12px;">Runs of your </span><b><span style="font-size: 12px;">main() function, </span></b><span style="font-size: 12px;">sits on a </span><b><span style="font-size: 12px;">node in the cluster,</span></b><span style="font-size: 12px;"> and is responsible for:</span></div>
                    <ol>
                        <li>
                            <div><span style="font-size: 12px;">maintaining information about the Spark Application</span></div>
                        </li>
                        <li>
                            <div><span style="font-size: 12px;">Responding to a user's program or input</span></div>
                        </li>
                        <li>
                            <div><span style="font-size: 12px;">analyzing, distributing and scheduling work across the executors</span></div>
                        </li>
                    </ol>
                </td>
                <td>
                    <div><span style="font-size: 12px;">Responsible for actually carrying out the work that the (&lt;-) </span><b><span style="font-size: 12px;">driver</span></b><span style="font-size: 12px;"> assigns them. Each executor is responsible for:</span></div>
                    <ol>
                        <li>
                            <div><span style="font-size: 12px;">Executing code assigned to it by the driver </span></div>
                        </li>
                        <li>
                            <div><span style="font-size: 12px;">Reporting the state of the computation on that executor BACK to the driver node.</span></div>
                        </li>
                    </ol>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <table width="1595px" style="width:1595px;">
        <colgroup>
            <col style="width: 723px;" />
            <col style="width: 872px;" />
        </colgroup>
        <tbody>
            <tr>
                <td><img src="Spark%20Overview.html.resources/arch.png" height="539" width="789" />
                    <div><br /></div>
                </td>
                <td>
                    <div><span style="font-size: 12px;">Driver is on the left, four executors on the right.  It demonstrates how the cluster manager controls physical machines and allocates resources to Spark Applications. This can be one of three cluster managers ( YARN, Mesos, Spark's standalone cluster manager).<i> </i></span><b><span style="font-size: 12px;"><i>This means that there can be multiple Spark Applications running on a cluster at the same time.</i></span></b></div>
                    <div><br /></div>
                    <div><b><span style="font-size: 12px;"><i>Note: </i></span></b><span style="font-size: 12px;"><i>Spark, in addition to a </i></span><b><span style="font-size: 12px;"><i>cluster mode</i></span></b><span style="font-size: 12px;"><i>, also has a </i></span><b><span style="font-size: 12px;"><i><u>local mode</u></i></span></b><span style="font-size: 12px;"><i>. The driver and the executor are simply processes, this means they can live on the same machine or different machines. </i></span></div>
                    <div><b><span style="font-size: 12px;"><i>Local Mode</i></span></b><span style="font-size: 12px;"><i> - Driver and executor run as threads </i>on your individual computer in stead of a cluster.</span></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div style="text-align:center;"><br /></div>
    <div style="text-align:center;"><span style="font-size: 12px;"><span style="color: rgb(184, 22, 215);"><input type="checkbox" />Spark employs a cluster manager that keeps track of the resources available</span></span></div>
    <div style="text-align:center;"><span style="font-size: 12px;"><span style="color: rgb(184, 22, 215);"><input checked="true" type="checkbox" />The driver process is responsible for executing the driver program's commands across the executor to complete a given task.</span></span></div>
    <div style="text-align:center;"><br /></div>
    <div><span style="font-size: 12px;">The </span><b><span style="font-size: 12px;">executor </span></b><span style="font-size: 12px;">only runs Spark code. However, the driver can be driven from a number of different languages through Spark's Language APIs.</span></div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Spark's Language APIs: </span></span></b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">make it possible to run Spark code using programming languages. Spark presents 'core concepts' in every language; these concepts are then translated into Spark code that runs on the cluster of machines. </span></span></div>
    <div><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">// If you use the Structured APIs, you can expect all languages to have similar performance characteristics.</span></span></div>
    <div><b><span style="font-size: 12px;">-&gt; Scala, </span><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">Java, Python, SQL, R</span></span></b></div>
    <div><br /></div>
    <table width="1138px" style="width:1138px;">
        <colgroup>
            <col style="width: 530px;" />
            <col style="width: 608px;" />
        </colgroup>
        <tbody>
            <tr>
                <td><img src="Spark%20Overview.html.resources/langhuage.png" height="334" width="1046" />
                    <div style="text-align:center;"><br /></div>
                </td>
                <td>
                    <div style="text-align:center;"><span style="font-size: 12px;">Represents the relationship between SparkSession and Spark's Language APIs.</span></div>
                    <div style="text-align:center;"><br /></div>
                    <div style="text-align:center;"><span style="font-size: 12px;"><i>When using Spark or Python, you don't write explicit JVM instructions; instead you write Python and R code that Spark translates into code that it then can run on the executor JVMs.</i></span></div>
                    <div style="text-align:center;"><br /></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Spark's APIs: </span></span></b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Spark has two fundamental sets of APIs: (1)</span></span><b><span style="font-size: 12px;"><i><span style="color: rgb(0, 0, 0);"> low-level UNSTRUCTURED API</span></i></span></b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);"> (2) </span></span><b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">higher-level STRUCTURED API</span></span></b></div>
    <div><br /></div>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="--en-highlight:yellow;background-color: #ffef9e;"><span style="color: rgb(0, 0, 0);">DataFrames</span></span></span></span></b></div>
    <div><span style="font-size: 12px;">Create a DataFrame with one column containing 1,000 rows with values from 0 to 999. </span></div>
    <div><b><span style="font-size: 12px;"><i>This range of numbers represents a distributed collection. When run on a cluster, each part of this range of numbers exists on a different executor. This is Spark DataFrame</i></span></b></div>
    <table width="1559px" style="width:1559px;">
        <colgroup>
            <col style="width: 501px;" />
            <col style="width: 492px;" />
            <col style="width: 566px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Python</span></span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Scala</span></span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b>Databricks/Excel - display()</b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">myRange = spark.range(1000).toDF("number")</span></span></b></div>
                    <div style="text-align:center;"><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-18%20at%2011.28.15%20PM.png" height="72" width="774" />
                    <div style="text-align:center;"><br /></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">val myRange = spark.range(1000).toDF("number")</span></span></b></div>
                    <div style="text-align:center;"><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-18%20at%2011.27.44%20PM.png" height="104" width="1014" />
                    <div style="text-align:center;"><br /></div>
                </td>
                <td>
                    <div style="text-align:center;"><b>click to zoom!</b></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-19%20at%2012.02.36%20AM.png" height="1016" width="1502" />
                    <div style="text-align:center;"><br /></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b><span style="font-size: 12px;">DataFrame </span></b><span style="font-size: 12px;">(<i>core abstraction</i>) is the most common Structured API and simply represents a table of data with rows and columns. The list the defines the columns and types within those columns is called a </span><b><span style="font-size: 12px;"><i>schema. </i></span></b><span style="font-size: 12px;">DataFrame is like a spreadsheet with named columns, but a spreadsheet sits on a computer in a specific location whereas Spark DataFrame can span thousands of computers. </span></div><img src="Spark%20Overview.html.resources/distributed-excel-vs-single-machine.png" height="399" width="1097" />
    <div><br /></div>
    <div><span style="font-size: 12px;"># Pandas (Python) DataFrames and R DataFrames are converted to Spark DataFrames because originally they exist on one machine rather than multiple machines thanks to Spark's language interfaces.</span></div>
    <div><br /></div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Partitions</span></span></b></div>
    <div><span style="font-size: 12px;">To allow every executor to perform work in parallel, Spark breaks up the data into chunks called </span><b><span style="font-size: 12px;">partitions</span></b><span style="font-size: 12px;">. </span></div>
    <div><span style="font-size: 12px;">A </span><b><span style="font-size: 12px;">Partition </span></b><span style="font-size: 12px;">is a </span><b><span style="font-size: 12px;">collection of rows</span></b><span style="font-size: 12px;"> tha</span><b><span style="font-size: 12px;">t sit on one physical machine</span></b><span style="font-size: 12px;"> </span><b><span style="font-size: 12px;">in your cluster</span></b><span style="font-size: 12px;">. It represents how the data is physically distributed across the cluster of machine during execution. </span></div>
    <div><span style="font-size: 12px;"><i>#If you have ONE partition Spark will have a parallelism of ONE even if you have thousands of executors. If you have MANY partitions but only ONE executor you will still have a parallelism of ONE because there is only ONE computation resource. You don't manipulate partitions manually, Spark decides how this will actually execute on the cluster. Low-level APIs do exist via RDDs though.</i></span></div>
    <div><br /></div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Transformations - </span></span></b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">ways of specifying different series of data manipulation</span></span></div>
    <div><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">In Spark, the</span></span><b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);"> core data structures</span></span></b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);"> are </span></span><b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">immutable</span></span></b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">, meaning they </span></span><b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">cannot be changed after they are created. </span></span></b></div>
    <div><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">You use </span></span><b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">transformations</span></span></b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);"> to instruct Spark how you would like to modify what you want.</span></span></div>
    <div><br /></div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">DAG</span></span></b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);"> = Execution Plan is a  (Directed Acyclic Graph) DAG of transformations. each resulting in a new immutable DataFrame.</span></span></div>
    <div><br /></div>
    <div><b><span style="font-size: 12px;"><i><span style="color: rgb(0, 0, 0);">Task: find all even numbers in current DataFrame:</span></i></span></b></div>
    <div><b><span style="font-size: 12px;"><i><span style="color: rgb(0, 0, 0);">No output!  -&gt;</span></i></span></b><span style="font-size: 12px;"><i><span style="color: rgb(0, 0, 0);"> we specified only an abstract transformation and Spark does not act on transformations until we call an action.</span></i></span></div>
    <div><br /></div>
    <table width="1620px" style="width:1620px;">
        <colgroup>
            <col style="width: 441px;" />
            <col style="width: 555px;" />
            <col style="width: 624px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;">Python</span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Scala</span></span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;">Databricks/Excel </span></b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">divisBy2 = myRange.where("number % 2 = 0")</span></span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-19%20at%2012.30.58%20AM.png" height="78" width="786" />
                    <div><br /></div>
                </td>
                <td>
                    <div><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">val divisBy2 = myRange.where("number % 2 = 0")</span></span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-19%20at%2012.31.46%20AM.png" height="182" width="1140" />
                    <div><br /></div>
                </td>
                <td><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-19%20at%2012.30.46%20AM.png" height="260" width="2030" />
                    <div><br /></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><span style="font-size: 12px;">There are<span style="color: rgb(0, 0, 0);"> two types of transformations:</span>  </span><b><span style="font-size: 12px;">Narrow dependencies </span></b><span style="font-size: 12px;">and </span><b><span style="font-size: 12px;"> Wide dependencies.</span></b></div>
    <div><br /></div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Narrow dependencies</span></span></b><span style="font-size: 12px;">: each input partition will contribute to only one output partition. In the above code the "where" statement specifies a narrow dependency, where only one partition contributes to at most one output partition. (see the map, filter part of the picture).</span></div>
    <div><span style="font-size: 12px;">Automatically performs an operation called pipelining, meaning that if we specify multiple filters on DataFrames, they will all be performed in-memory.</span></div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Wide dependencies:</span></span></b><span style="font-size: 12px;"> input partitions contributing to many output partitions. Also referred to as "<i>Shuffle</i>" whereby Spark will exchange partitions across the cluster. When we perform a shuffle, Spark writes the results to disk. </span></div>
    <div><br /></div><img src="Spark%20Overview.html.resources/narrowwide.png" height="386" width="633" />
    <div><br /></div>
    <div><br /></div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Lazy Evaluation</span></span></b></div>
    <div><span style="font-size: 12px;">Spark waits until the very last moment to execute the graph of computation instructions. Spark will not modify data immediately when you express some operation, you build up a plan of transformations that you would like to apply to your source data.</span></div>
    <div><span style="font-size: 12px;">Spark optimizes the entire data flow from end to end.  </span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><i>Predicate Pushdown - </i></span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">Spark will attempt to move filtering of data as close to the source as possible to avoid loading unnecessary data into memory.</span></span></div>
    <div><span style="font-size: 12px;">DataFrames have a set of columns with an unspecified number of rows -&gt; reading data is a transformation and is a lazy operation. Spark only peeks at a couple of rows to try guess what type each column should be. </span></div>
    <div><br /></div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Actions</span></span></b></div>
    <div><span style="font-size: 12px;">Transformations allow us to build up our logical transformation plan. To trigger the computation we run an action. Action instructs Spark to compute a result from a series of transformations. </span></div>
    <div><span style="font-size: 12px;">The </span><b><span style="font-size: 12px;">simplest</span></b><span style="font-size: 12px;"> </span><b><span style="font-size: 12px;">action</span></b><span style="font-size: 12px;"> is </span><b><span style="font-size: 12px;">count</span></b><span style="font-size: 12px;">, which gives us the total number of records in the DataFrame. </span></div>
    <div><span style="font-size: 12px;">There are three kinds of actions</span></div>
    <ol>
        <li>
            <div><span style="font-size: 12px;">Actions to view data in the console</span></div>
        </li>
        <li>
            <div><span style="font-size: 12px;">Actions to collect data to native objects in the respective language</span></div>
        </li>
        <li>
            <div><span style="font-size: 12px;">Actions to write to output data sources</span></div>
        </li>
    </ol>
    <div><br /></div>
    <table width="1406px" style="width:1406px;">
        <colgroup>
            <col style="width: 556px;" />
            <col style="width: 524px;" />
            <col style="width: 326px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;">Python</span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;">Scala</span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;">DataBricks</span></b></div>
                </td>
            </tr>
            <tr>
                <td><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-19%20at%2012.59.52%20AM.png" height="132" width="774" />
                    <div><br /></div>
                </td>
                <td><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-19%20at%201.00.01%20AM.png" height="286" width="1170" />
                    <div><br /></div>
                </td>
                <td><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-19%20at%201.00.12%20AM.png" height="296" width="474" />
                    <div><br /></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><span style="font-size: 12px;">In specifying this action, we </span><b><span style="font-size: 12px;">started a Spark job</span></b><span style="font-size: 12px;"> that </span><b><span style="font-size: 12px;">runs our </span></b><span style="font-size: 12px;">filter transformation </span><b><span style="font-size: 12px;">(narrow transformatio</span></b><span style="font-size: 12px;">n) then an </span><b><span style="font-size: 12px;">aggregation</span></b><span style="font-size: 12px;"> (</span><b><span style="font-size: 12px;">wide transformation</span></b><span style="font-size: 12px;">) that</span><b><span style="font-size: 12px;"> performs the counts on a per partition basis, </span></b><span style="font-size: 12px;">and then</span><b><span style="font-size: 12px;"> collect, </span></b><span style="font-size: 12px;">which </span><b><span style="font-size: 12px;">brings</span></b><span style="font-size: 12px;"> our result </span><b><span style="font-size: 12px;">to</span></b><span style="font-size: 12px;"> </span><b><span style="font-size: 12px;">a native object</span></b><span style="font-size: 12px;"> in the respective language. </span></div>
    <div><b><span style="font-size: 12px;">Spark UI: (for monitoring the progress of a job) </span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">Local mode: available on port 4040 of the driver node. <a href="http://localhost:4040/" rev="en_rl_none">http://localhost:4040</a></span></span></div>
    <div><b><span style="font-size: 12px;">Spark job:</span></b><span style="font-size: 12px;"> represents a set of transformations triggered by an individual action, and you can monitor that job from Spark UI</span></div>
    <div><br /></div>
    <div style="text-align:center;"><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-19%20at%201.18.16%20AM.png" height="560" width="3288" />
    <div style="text-align:center;"><br /></div>
    <div><br /></div>
    <div style="text-align:center;"><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">*** EXAMPLE ****</span></span></b></div>
    <div><span style="font-size: 12px;"><i>data from github - flight data csv 2015 databricks </i></span></div>
    <div><b><span style="font-size: 12px;"><i>schema inference - we want Spark to take a best guess at what the schema of our DataFrame should be. (CSV files are not completely structur</i></span></b><span style="font-size: 12px;"><i>ed)</i></span></div>
    <div><span style="font-size: 12px;"><i>we will specify that the first row is the header</i></span></div>
    <div><br /></div>
    <div><b>STEP 1: Load data</b></div>
    <ul>
        <li>
            <div><i>inferschema</i></div>
        </li>
        <li>
            <div><span style="font-size: 14px;"><i>header</i></span></div>
        </li>
    </ul>
    <div><br /></div>
    <table width="1562px" style="width:1562px;">
        <colgroup>
            <col style="width: 455px;" />
            <col style="width: 476px;" />
            <col style="width: 631px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b>Python</b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;"><i>Scala</i></span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b>Databricks</b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><i>flightData2015 = spark\</i></div>
                    <div><i>.read\</i></div>
                    <div><i>.option("inferSchema" , "true")\</i></div>
                    <div><i>.option("header", "true")\</i></div>
                    <div><i>.csv("/Users......csc")</i></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-19%20at%201.49.37%20AM.png" height="184" width="908" />
                    <div><br /></div>
                </td>
                <td>
                    <div><i>val flightData2015 = spark</i></div>
                    <div><i>.read</i></div>
                    <div><i>.option("inferSchema" , "true")</i></div>
                    <div><i>.option("header", "true")</i></div>
                    <div><i>.csv("/Users......csc")</i></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-19%20at%201.51.50%20AM.png" height="542" width="1568" />
                    <div><br /></div>
                </td>
                <td><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-19%20at%201.52.17%20AM.png" height="684" width="2832" />
                    <div><br /></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b><span style="font-size: 14px;">STEP 2: Perform a take action:</span></b></div>
    <table width="1548px" style="width:1548px;">
        <colgroup>
            <col style="width: 516px;" />
            <col style="width: 516px;" />
            <col style="width: 516px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Python</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Scala</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Databricks</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>flightData2015.take(3)</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-19%20at%203.03.35%20PM.png" height="126" width="1964" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);"><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-19%20at%203.32.50%20PM.png" height="410" width="1504" />
                    <div><br /></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><b>STEP 3:</b> Nothing happens when we call a <b><i>sort </i></b>beacuse it's just a transformation. But we can see the explain plan to see how Spark will execute it across the cluster . </div>
    <div>We can call an <b><i>explain</i></b> on any DataFrame object to see the DataFrame's lineage. Explain plans are read top to bottom, top being the end result  and bottom being the source of data.</div>
    <table width="1564px" style="width:1564px;">
        <colgroup>
            <col style="width: 532px;" />
            <col style="width: 516px;" />
            <col style="width: 516px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Python</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Scala</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>DataBricks</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>flightData2015.sort("count").explain()</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-19%20at%203.12.38%20PM.png" height="226" width="3358" />
                    <div><br /></div>
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);"><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-19%20at%203.36.33%20PM.png" height="420" width="3114" />
                    <div><br /></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b>STEP4: Set a configuration. </b>By default when we perform a shuffle Spark outputs two hundred shuffle partitions. Let's see this value to five to reduce the number of output partitions from the shuffle. <span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"> </span></div>
    <table width="1564px" style="width:1564px;">
        <colgroup>
            <col style="width: 532px;" />
            <col style="width: 516px;" />
            <col style="width: 516px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Python</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Scala</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>DataBricks</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">spark.conf.set("spark.sql.shuffle.partitions", "5")</span></div>
                    <div><span style="font-size: 14px;">flightData2015.sort("count").take(2)</span></div>
                    <div> </div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-19%20at%203.47.16%20PM.png" height="154" width="1982" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">spark.conf.set("spark.sql.shuffle.partitions", "5")</span></div>
                    <div><span style="font-size: 14px;">flightData2015.sort("count").take(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">spark.conf.set("spark.sql.shuffle.partitions", "5")</span></div>
                    <div><span style="font-size: 14px;">flightData20</span><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">15.sort("count").take(2)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-19%20at%203.47.28%20PM.png" height="402" width="1530" />
                    <div><br /></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><b>This picture illustrates the above operation --&gt;</b></div>
    <div><br /></div><img src="Spark%20Overview.html.resources/1_jEiAlKrVXPhZJKHDoQarUw.png" height="704" width="1600" />
    <div><br /></div>
    <div>The logical plan of transformations that we build up defines a lineage for the DataFrame so that at any given point in time Spark knows how to <b>recompute any partition </b>by performing all of the operations it had before on the same input data.</div>
    <div><b>Functional Programming:</b> where the same inputs always result in the same outputs when the transformations on that data stay constant.</div>
    <div><br /></div>
    <div><b><span style="color: rgb(255, 0, 42);">DataFrames and SQL:</span></b></div>
    <div><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Spark can run the same transformations regardless of the language, in the exact same way. With SparkSQL, you can register any DataFrame as a table and query it using pure SQL. </span></span></div>
    <div><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">There is no performance difference between writing SQL queries and DataFrame code.</span></span></div>
    <ul>
        <li>
            <div><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">You can make any DataFrame into a table or view with one simple method call</span></span></div>
        </li>
    </ul>
    <div><br /></div>
    <table width="1612px" style="width:1612px;">
        <colgroup>
            <col style="width: 313px;" />
            <col style="width: 411px;" />
            <col style="width: 444px;" />
            <col style="width: 444px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Python</span></span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Scala</span></span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b>Databricks</b></div>
                </td>
                <td>
                    <div><br /></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">flightData2015</span></span><b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">.createOrReplaceTempView("</span></span></b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">flight_data_2015</span></span><b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">")</span></span></b></div>
                </td>
                <td>
                    <div><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">flightData2015.createOrReplaceTempView("flight_data_2015")</span></span></div>
                </td>
                <td><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%206.49.40%20PM.png" height="234" width="1528" />
                    <div><br /></div>
                </td>
                <td>
                    <div style="text-align:center;"><b>createOrReplaceTempView</b></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><span style="font-size: 12px;">...Now we can query the data into SQL.</span></div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Function: spark.sql </span></span></b></div>
    <div><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">(hint: spark is the SparkSession variable that returns a new DataFrame)</span></span></div>
    <div><br /></div>
    <table width="1516px" style="width:1516px;">
        <colgroup>
            <col style="width: 440px;" />
            <col style="width: 286px;" />
            <col style="width: 426px;" />
            <col style="width: 364px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Python</span></span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Scala</span></span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b>Databricks (py)</b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b>Note</b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><br /></div>
                    <div><b><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">sqlWay</span></span></span></b><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);"> = spark.sql("""</span></span></span></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">SELECT DEST_COUNTRY_NAME, count(1)</span></span></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">FROM flight_data_2015</span></span></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">GROUP BY DEST_COUNTRY_NAME</span></span></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">""")</span></span></div>
                    <div><br /></div>
                    <div style="background-color:rgb(255, 255, 255);"><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;">&lt;br&gt;</span></span></div>
                    <div><b><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">dataFrameWay</span></span></b><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">= flightData2015\</span></span></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">.groupBy("DEST_COUNTRY_NAME")\</span></span></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">.count()</span></span></div>
                    <div><br /></div>
                    <div style="background-color:rgb(255, 255, 255);"><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;">&lt;br&gt;</span></span></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">sqlWay.explain()</span></span></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">dataFrameWay.explain()</span></span></div>
                    <div><br /></div>
                </td>
                <td>
                    <div><br /></div>
                    <div style="background-color:rgb(255, 255, 255);"><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">val </span></span></span><b><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">sqlWay</span></span></span></b><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);"> = spark.sql("""</span></span></span></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">SELECT DEST_COUNTRY_NAME, count(1)</span></span></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">FROM flight_data_2015</span></span></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">GROUP BY DEST_COUNTRY_NAME</span></span></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">""")</span></span></div>
                    <div><br /></div>
                    <div style="background-color:rgb(255, 255, 255);"><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;">&lt;br&gt;</span></span></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">val </span></span><b><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">dataFrameWay</span></span></b><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);"> = flightData2015</span></span></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">.groupBy('DEST_COUNTRY_NAME)</span></span></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">.count()</span></span></div>
                    <div><br /></div>
                    <div style="background-color:rgb(255, 255, 255);"><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;">&lt;br&gt;</span></span></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">sqlWay.explain</span></span></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">dataFrameWay.explain</span></span></div>
                    <div><br /></div>
                </td>
                <td><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%207.04.19%20PM.png" height="1192" width="1694" />
                    <div><br /></div>
                </td>
                <td>
                    <div>Notice that these plans compile to the exact same underlying plan</div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div style="text-align:center;"><br /></div>
    <div style="text-align:center;"><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">DataFrames and SQL in Spark have a huge number of manipulations available, there are hundreds of functions you can use and import to help resolve big data problems faster!</span></span></b></div>
    <table width="1612px" style="width:1612px;">
        <colgroup>
            <col style="width: 313px;" />
            <col style="width: 411px;" />
            <col style="width: 444px;" />
            <col style="width: 444px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Python</span></span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Scala</span></span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Databricks</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>from pyspark.sql.functions import max</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>import org.apache.spark.sql.functions.max</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);"><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%207.07.52%20PM.png" height="210" width="1492" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>IMPORT</b></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div style="text-align:center;"><b>Task/Example: Establish the maximum number of flights to and from any given location.</b></div>
    <table width="1297px" style="width:1297px;">
        <colgroup>
            <col style="width: 339px;" />
            <col style="width: 411px;" />
            <col style="width: 444px;" />
            <col style="width: 103px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Python</span></span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Scala</span></span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Databricks</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>flightdata2015.select(max("count")).take(1)</div>
                    <div><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%207.18.04%20PM.png" height="158" width="942" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>import org.apache.spark.sql.functions.max</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);"><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%207.18.12%20PM.png" height="264" width="1560" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>MAX</b></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div style="text-align:center;"><b>Task/Example 2: Find the top five destination countries in the data.</b></div>
    <div><br /></div>
    <table width="1561px" style="width:1561px;">
        <colgroup>
            <col style="width: 759px;" />
            <col style="width: 802px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">SQL W</span><span style="font-size: 14px;">ay</span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;">DataFrame Way </span></b></div>
                </td>
            </tr>
            <tr>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div><span style="color: rgb(0, 0, 0);">#</span><b><span style="color: rgb(0, 0, 0);">Python</span></b></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">maxSql = spark.sql("""</span></span></span></div>
                    <div style="background-color:rgb(255, 255, 255);"><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">SELECT DEST_COUNTRY_NAME, sum(count) as destination_total</span></span></span></div>
                    <div style="background-color:rgb(255, 255, 255);"><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">FROM flight_data_2015</span></span></span></div>
                    <div style="background-color:rgb(255, 255, 255);"><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">GROUP BY DEST_COUNTRY_NAME</span></span></span></div>
                    <div style="background-color:rgb(255, 255, 255);"><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">ORDER BY sum(count) DESC</span></span></span></div>
                    <div style="background-color:rgb(255, 255, 255);"><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">LIMIT 5</span></span></span></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">""")</span></span></span></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">maxSql.show()</span></span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%207.31.26%20PM.png" height="986" width="1024" />
                    <div><br /></div>
                    <div><br /></div>
                    <div><span style="color: rgb(0, 0, 0);">//Scala</span></div>
                    <div><span style="color: rgb(0, 0, 0);">val maxSql = spark.sql("""</span></div>
                    <div style="background-color:rgb(255, 255, 255);"><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">SELECT DEST_COUNTRY_NAME, sum(count) as destination_total</span></span></span></div>
                    <div style="background-color:rgb(255, 255, 255);"><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">FROM flight_data_2015</span></span></span></div>
                    <div style="background-color:rgb(255, 255, 255);"><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">GROUP BY DEST_COUNTRY_NAME</span></span></span></div>
                    <div style="background-color:rgb(255, 255, 255);"><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">ORDER BY sum(count) DESC</span></span></span></div>
                    <div style="background-color:rgb(255, 255, 255);"><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">LIMIT 5</span></span></span></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">""")</span></span></span></div>
                    <div><span style="font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;;"><span style="color: rgb(0, 0, 0);">maxSql.show()</span></span></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">Python DataFrame Way</span></span></b></div>
                    <div><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">Step 1: </span></span></b></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">from pyspark.sql.functions import desc</span></span></div>
                    <div><br /></div>
                    <div><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">Step</span></span></b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);"> </span></span><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">2</span></span></b></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">flightData2015\</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">.groupBy("DEST_COUNTRY_NAME")\</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">.sum("count")\</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">.withColumnRenamed("sum(count)", "destination_total")\</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">.limit(5)\</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">.show()</span></span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%207.37.42%20PM.png" height="820" width="962" />
                    <div><br /></div>
                    <div><br /></div>
                    <div><span style="color: rgb(0, 0, 0);">---</span></div>
                    <div><b><span style="color: rgb(0, 0, 0);">Scala  DataFrame syntax:</span></b></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">flightData2015</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">.groupBy("DEST_COUNTRY_NAME")</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">.sum("count")</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">.withColumnRenamed("sum(count)", "destination_total")</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">.limit(5)</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">.show()</span></span></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div><img src="Spark%20Overview.html.resources/spark-04.png" height="665" width="1255" />
    <div style="text-align:center;"><br /></div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(0, 170, 59);">Explanation of the above code (steps)</span></span></b></div>
    <ol>
        <li>
            <div><b><span style="font-size: 12px;">Read in the data</span></b><span style="font-size: 12px;"> (Spark does not actually read it until an action is called)</span></div>
        </li>
        <li>
            <div><b><span style="font-size: 12px;">Grouping</span></b><span style="font-size: 12px;"> - RelationalGroupedDataset, which is a fancy name fro DataFrame that has grouping specified but needs the user to specify an aggregation before it can be queried further. We just specified that we are going to be grouping by a key.</span></div>
        </li>
        <li>
            <div><b><span style="font-size: 12px;">Specify the aggregation</span></b><span style="font-size: 12px;"> - used the 'sum' aggregation. This takes an input as a column name, the result of the sum method call is a new DataFrame. No computation has been performed still. This is simply another transformation. You can check the schema, but it won't know the type of each column</span></div>
        </li>
        <li>
            <div><b><span style="font-size: 12px;">WithColumnRenaimed</span></b><span style="font-size: 12px;">() - takes two arguments: the original column name, and the new column name -this is just another transformation</span></div>
        </li>
        <li>
            <div><b><span style="font-size: 12px;">Sorts</span></b><span style="font-size: 12px;"> the data </span></div>
        </li>
        <li>
            <div><span style="font-size: 12px;">Then we specified a </span><b><span style="font-size: 12px;">limit</span></b><span style="font-size: 12px;"> to not return the entire DataFrame</span></div>
        </li>
        <li>
            <div><span style="font-size: 12px;">The last step is the </span><b><span style="font-size: 12px;">action</span></b><span style="font-size: 12px;"> - the process of collecting the results begin</span></div>
        </li>
    </ol>
    <div><b><span style="font-size: 12px;">-&gt; Now let's look at the explain plan:</span></b></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%207.54.02%20PM.png" height="684" width="2178" />
    <div><br /></div>
    <div><br /></div><img src="Spark%20Overview.html.resources/spark%20toollkit.png" height="599" width="882" />
    <div style="text-align:center;"><br /></div>
    <div>Spark is composed of primitives - the lower-level APIs and the Structured APIs - and then a series of standard libraries for additional functionality.</div>
    <div>Spark's libraries support graph analysis to machine learning to streaming and integrations with a host of computing and storage systems.</div>
    <div><br /></div>
    <div>Objectives: </div>
    <ol>
        <li>
            <div>Running production applications with spark-submit</div>
        </li>
        <li>
            <div>Dataset: type safe APIs for structured data</div>
        </li>
        <li>
            <div>Structured Streaming</div>
        </li>
        <li>
            <div>Machine Learning and advanced analytics</div>
        </li>
        <li>
            <div>Spark's lower level RDD API</div>
        </li>
        <li>
            <div>SparkR</div>
        </li>
        <li>
            <div>The third-party package ecosystem</div>
        </li>
    </ol>
    <div><br /></div>
    <div><b>Running <span style="color: rgb(255, 0, 42);">Production</span> Applications</b></div>
    <div><b><i>spark submit - </i></b>does one thing: it lets you send your application code to a cluster and launch it to execute there. Upon submission, the application will run until it exits or encounters an error. You can do this with Spark Standalone, Mesos and YARN.</div>
    <div>spark-submit offers several controls to specify the resources your application needs</div>
    <div><br /></div>
    <table width="1228px" style="width:1228px;">
        <colgroup>
            <col style="width: 555px;" />
            <col style="width: 673px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b>Python</b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Scala</span></b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><span style="font-size: 14px;">./bin/spark-submit \</span></div>
                    <div><span style="font-size: 14px;">--master local \</span></div>
                    <div><span style="font-size: 14px;">./examples/src/main/python/pi.py 10</span></div>
                </td>
                <td>
                    <div><span style="font-size: 14px;">./bin/spark-submit \</span></div>
                    <div><span style="font-size: 14px;">--class org.apache.spark.examples.SparkPi \ </span></div>
                    <div><span style="font-size: 14px;">--master local \</span></div>
                    <div><span style="font-size: 14px;">./examples/jars/spark-example_2.11-2.2.0.jar 10</span></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="color: rgb(255, 0, 42);">Datasets: Type-Safe Structured APIs</span></span></b></div>
    <div><span style="font-size: 12px;">Dataset = type-safe version of Spark's structured API for writing statically typed code in Java and Scala. - not available in Python and R because these languages are dyynamically typed.</span></div>
    <div><span style="font-size: 12px;">Dataset API gives users the ability to assign a Java class too the records within a DataFrame and manipulate it as collection of typed objects. The APIs available on Datasets are type-safe meaning that you cannot accidentally view the objects in a Dataset as being of another class than the class you put in initially. This makes Datasets attractive for writing large applications.</span></div>
    <div><span style="font-size: 12px;">The Dataset class is parametrized with the type of object contained inside: Dataset &lt;T&gt; in Java and Dataset[T]  in Scala. </span></div>
    <div><span style="font-size: 12px;">For Example: Dataset [Person] will be guaranteed to contain objects of class Person. </span></div>
    <div><span style="font-size: 12px;">Benefit: you can use Datasets only when you need or want to.</span></div>
    <div><span style="font-family: Arial, &quot;Helvetica Neue&quot;, Helvetica, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(36, 39, 41);">Dataset API is an extension to DataFrames that provides a type-safe, object-oriented programming interface. It is a strongly-typed, immutable collection of objects that are mapped to a relational schema.</span></span></span></div>
    <div><br /></div>
    <div><span style="font-family: Arial, &quot;Helvetica Neue&quot;, Helvetica, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(36, 39, 41);">At the core of the Dataset, API is a new concept called an encoder, which is responsible for converting between JVM objects and tabular representation. The tabular representation is stored using Spark internal Tungsten binary format, allowing for operations on serialized data and improved memory utilization. Spark 1.6 comes with support for automatically generating encoders for a wide variety of types, including primitive types (e.g. String, Integer, Long), Scala case classes, and Java Beans.</span></span></span></div>
    <h2><span style="font-family: Arial, &quot;Helvetica Neue&quot;, Helvetica, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(36, 39, 41);">Dataset Features:-</span></span></span></h2>
    <ul>
        <li>
            <div><b><span style="font-family: Arial, &quot;Helvetica Neue&quot;, Helvetica, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(36, 39, 41);">Provides best of both RDD and Dataframe:</span></span></span></b><span style="font-family: Arial, &quot;Helvetica Neue&quot;, Helvetica, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(36, 39, 41);"> RDD(functional programming, type safe), DataFrame (relational model, Query optimazation , Tungsten execution, sorting and shuffling)</span></span></span></div>
        </li>
        <li>
            <div><b><span style="font-family: Arial, &quot;Helvetica Neue&quot;, Helvetica, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(36, 39, 41);">Encoders:</span></span></span></b><span style="font-family: Arial, &quot;Helvetica Neue&quot;, Helvetica, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(36, 39, 41);"> With the use of Encoders, it is easy to convert any JVM object into a Dataset, allowing users to work with both structured and unstructured data unlike Dataframe.</span></span></span></div>
        </li>
        <li>
            <div><b><span style="font-family: Arial, &quot;Helvetica Neue&quot;, Helvetica, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(36, 39, 41);">Programming Languages supported:</span></span></span></b><span style="font-family: Arial, &quot;Helvetica Neue&quot;, Helvetica, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(36, 39, 41);"> Datasets API is currently only available in Scala and Java. Python and R are currently not supported in version 1.6. Python support is slated for version 2.0.</span></span></span></div>
        </li>
        <li>
            <div><b><span style="font-family: Arial, &quot;Helvetica Neue&quot;, Helvetica, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(36, 39, 41);">Type Safety:</span></span></span></b><span style="font-family: Arial, &quot;Helvetica Neue&quot;, Helvetica, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(36, 39, 41);"> Datasets API provides compile time safety which was not available in Dataframes. In the example below, we can see how Dataset can operate on domain objects with compile lambda functions.</span></span></span></div>
        </li>
    </ul>
    <div><br /></div>
    <div><b><span style="font-size: 12px;">Example/Task: Drop down to lower level, perform type-safe coding and move higher up to SQL for more rapid analysis.</span></b></div>
    <div><br /></div>
    <table width="1283px" style="width:1283px;">
        <colgroup>
            <col style="width: 1283px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;">Scala</span></b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><span style="font-size: 12px;">case class Flight(DEST_COUNTRY_NAME: String,</span></div>
                    <div><span style="font-size: 12px;">ORIGIN_COUNTRY_NAME: String,</span></div>
                    <div><span style="font-size: 12px;">count: BigInt)</span></div>
                    <div><span style="font-size: 12px;">val flightsDF = spark.read</span></div>
                    <div><span style="font-size: 12px;">.parquet("/data/flights-data/parquet/2010-summary.parquet/")</span></div>
                    <div><span style="font-size: 12px;">val flights = flightsDF.as[Flight]</span></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div>The advantage is that when you call collect or take on the Dataset, we are going to collect to objects of the proper type in the DataSet, not DataFrame Rows. </div>
    <div><span style="font-size: 14px;">This makes it easy to get type safety and safely perform manipulation in distributed and a local manner without code changes. </span></div>
    <table width="1283px" style="width:1283px;">
        <colgroup>
            <col style="width: 1283px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 12px;">Scala</span></b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 12px;">flights</span></div>
                    <div><span style="font-size: 12px;">.filter(flight_row =&gt; flight_row.ORIGIN_COUNTRY_NAME != "Canada")</span></div>
                    <div><span style="font-size: 12px;">.map(flight_row =&gt; flight_row)</span></div>
                    <div><span style="font-size: 12px;">.take(5)</span></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b>Structured Streaming</b></div>
    <div><span style="font-size: 12px;">Structured Streaming is a high level API for stream processing. With Structured Streaming you can teake the same operations that you perform in batch mode (computer processing in which commands are input from a batch file, not interactively) using Spark's structured APIs and run them in a streaming fashion. This reduces latency and allows for incremental processing.  It allows you to rapidly and quickly extract value out of streaming systems with virtually no code changes. You can write your batch jobs as a way to prototype and then you can convert it to streaming job by incrementally processing data.</span></div>
    <div><br /></div>
    <div><span style="font-size: 12px;">Sample of the data:  (retail-data/def-guide)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%209.08.39%20PM.png" height="344" width="1430" />
    <div><br /></div>
    <div><br /></div>
    <div><b><span style="font-size: 12px;">Step 1: analyze the data as a static dataset and create a DataFrame to do so. We'll also create a schema from this static dataset.</span></b></div>
    <div><br /></div>
    <table width="1237px" style="width:1237px;">
        <colgroup>
            <col style="width: 594px;" />
            <col style="width: 449px;" />
            <col style="width: 194px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Python</span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Scala</span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Notes</span></b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div>staticDataFrame = spark.read.format("csv")\</div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">.option("header", "true")\</span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">.option("inferSchema", "true")\</span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">.load("/Users/mikepetridisz/Desktop/retail-data/by-day/*.csv")</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%207.18.04%20PM.png" height="158" width="942" />
                    <div><br /></div>
                </td>
                <td>
                    <div>val staticDataFrame = spark.read.format("csv")</div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">.option("header", "true")</span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">.option("inferSchema", "true")</span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">.load("/Users/mikepetridisz/Desktop/retail-data/by-day/*.csv")</span></div>
                </td>
                <td>
                    <div>Load the data</div>
                    <div>Retail</div>
                    <div>By day</div>
                    <div>Def Guide</div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><span style="font-size: 12px;">Step 2: Add a total cost column and see on what days a customer spend the most. </span></div>
    <div><span style="font-size: 12px;"><a href="https://knockdata.github.io/spark-window-function/" rev="en_rl_none">window()</a> - will include all data from each day in the aggregation. It's simply a window over the time-series column in our data. This is a helpful tool for manipulating date and timestamps because we can specify our requirements in a more human form via intervals, and Spark will group all of them together for us. </span></div>
    <div><br /></div>
    <table width="1271px" style="width:1271px;">
        <colgroup>
            <col style="width: 628px;" />
            <col style="width: 449px;" />
            <col style="width: 194px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 12px;">Python</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 12px;">Scala</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 12px;">Notes</span></b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="margin-top:16px;"><span style="font-size: 12px;"> </span></div>
                    <div><br /></div>
                    <div><span style="font-size: 12px;">staticDataFrame.createOrReplaceTempView("retail_data")</span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">staticSchema = staticDataFrame.schema</span></span></div>
                    <div><br /></div>
                    <div><span style="font-size: 12px;">from pyspark.sql.functions import </span><b><span style="font-size: 12px;"><i>window</i></span></b><span style="font-size: 12px;">,</span><b><span style="font-size: 12px;"><i> column, desc, col</i></span></b></div>
                    <div><br /></div>
                    <div><b><span style="font-size: 12px;"><i>staticDataFrame\ </i></span></b></div>
                    <div><b><span style="font-size: 12px;"><i>.</i></span><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><i>selectExpr( "CustomerId", "(UnitPrice * Quantity) as total_cost", "InvoiceDate")\</i></span></span></b></div>
                    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><i> .groupBy( </i></span></span></b></div>
                    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><i>col("CustomerId"), window(col("InvoiceDate"), "1 day"))\</i></span></span></b></div>
                    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><i>.sum("total_cost")\</i></span></span></b></div>
                    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><i>.show(5)</i></span></span></b></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%209.39.54%20PM.png" height="562" width="930" />
                    <div><br /></div>
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 12px;">import org.apache.spark.sql.functions.{window, column, desc, coll}</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 12px;">Null values represent the fact that we don't have a customer Id for some transactions. </span></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b><span style="font-size: 12px;">Step 3: take a look at the streaming code:</span></b></div>
    <div><br /></div>
    <table width="746px" style="width:746px;">
        <colgroup>
            <col style="width: 486px;" />
            <col style="width: 130px;" />
            <col style="width: 130px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;">Python</span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;">Scala</span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 12px;">Notes</span></b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><span style="font-size: 12px;">streamingDataFrame = spark.readStream\</span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">.schema(staticSchema)\</span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">.option("maxFilesPerTrigger", 1)\</span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">.format("csv")\</span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">.option("header", "true")\</span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">.load("/data/retail-data/by-day/*.csv")</span></span></div>
                    <div><br /></div>
                    <div><span style="font-size: 12px;">streamingDataFrame.isStreaming</span></div>
                    <div><br /></div>
                    <div><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%209.42.37%20PM.png" height="258" width="780" />
                    <div><br /></div>
                    <div><br /></div>
                    <div>Let's perform a summation now:</div>
                    <div><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%2010.21.43%20PM.png" height="1294" width="1516" />
                    <div><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%2010.22.02%20PM.png" height="1554" width="1630" />
                    <div><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%2010.22.08%20PM.png" height="1444" width="3106" />
                    <div><br /></div>
                </td>
                <td>
                    <div><br /></div>
                </td>
                <td>
                    <div><br /></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><b><span style="font-size: 12px;">Machine Learning and Advanced Analytics</span></b></div>
    <div><span style="font-size: 12px;">MLlib allows for preprocessing, munging, training of models and making predictions at scale on data.</span></div>
    <div><span style="font-size: 12px;">You can use models trained in MLlib to make predictions in Structured Streaming. </span></div>
    <div><b><span style="font-size: 12px;">Standark Algorithm:<a href="https://www.youtube.com/watch?v=3vHqmPF4VBA" rev="en_rl_none"> K-means</a></span></b></div>
    <div><b><span style="font-size: 12px;"><a href="https://www.youtube.com/watch?v=4b5d3muPQmA" rev="en_rl_none">K-means clustering algorithm</a>:</span></b><span style="font-size: 12px;"> clustering algorithm in which 'K' centers are randomly assigned within the data. The point closest to that point are then assigned to a class and the center of the assigned points is computed.</span></div>
    <div><span style="font-size: 12px;">This center point is called centroid. We then label the points closest to that centroid, to the centroid's class, and shift the centroid to the new center of that cluster of points. We repeat this process for a finite set of iterations or until convergence (our center points stop changing.)</span></div>
    <div><br /></div>
    <table width="1302px" style="width:1302px;">
        <colgroup>
            <col style="width: 455px;" />
            <col style="width: 488px;" />
            <col style="width: 359px;" />
        </colgroup>
        <tbody>
            <tr>
                <td><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%2011.04.05%20PM.png" height="1178" width="2112" />
                    <div><br /></div>
                </td>
                <td><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%2011.04.18%20PM.png" height="1170" width="2118" />
                    <div><br /></div>
                </td>
                <td><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%2011.04.35%20PM.png" height="1192" width="2140" />
                    <div><br /></div>
                </td>
            </tr>
            <tr>
                <td><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%2011.04.45%20PM.png" height="1154" width="2100" />
                    <div><br /></div>
                </td>
                <td><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%2011.04.58%20PM.png" height="1168" width="2104" />
                    <div><br /></div>
                </td>
                <td><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%2011.05.10%20PM.png" height="1180" width="2094" />
                    <div><br /></div>
                </td>
            </tr>
            <tr>
                <td><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%2011.05.26%20PM.png" height="980" width="1376" />
                    <div><br /></div>
                </td>
                <td><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%2011.05.46%20PM.png" height="960" width="1124" />
                    <div><br /></div>
                </td>
                <td><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%2011.06.05%20PM.png" height="1114" width="2104" />
                    <div><br /></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">K-means clustering does not work well if the data is noisy or there are overlapping data. Unsupervised.</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-20%20at%2011.11.45%20PM.png" height="984" width="2014" />
    <div><br /></div>
    <div><br /></div>
    <div><b><span style="font-size: 12px;">Applications of K-means clustering:</span></b></div>
    <ol>
        <li>
            <div><span style="font-size: 12px;">Telephone companies use K-means clustering algorithm to place towers so that all its users receive optimum signal strenght</span></div>
        </li>
        <li>
            <div><span style="font-size: 12px;">Police stations use K means clustering so that patrol vehicles are stationed across the area so that the areas of high crime rates are in the vicinity of the patrol van</span></div>
        </li>
        <li>
            <div><span style="font-size: 12px;">Hospital care chains open a series of emergency care wards while considering accident prone areas in the region </span></div>
        </li>
        <li>
            <div><span style="font-size: 12px;">Can also be used for market segmentation, price spend behaviors and customer need segmentation and also used in computer vision</span></div>
        </li>
    </ol>
    <div><br /></div>
    <div><b><span style="font-size: 12px;">Advantages of K-means clustering</span></b></div>
    <div><span style="font-size: 12px;">K-means speed&gt;hierarchical clustering speed if K is small</span></div>
    <div><span style="font-size: 12px;">K-means will produce tighter clusters than hierarchical clustering</span></div>
    <div><br /></div>
    <div><b><span style="font-size: 12px;">Disadvantages of K-means clustering</span></b></div>
    <div><span style="font-size: 12px;">Difficulty in comparing quality of the clusters produced </span></div>
    <div><span style="font-size: 12px;">Fixed number of clusters can make it difficult to predict what K should be </span></div>
    <div><span style="font-size: 12px;">Strong sensitivity to outliers and noise </span></div>
    <div><span style="font-size: 12px;">Does not work well in non-circular cluster shape </span></div>
    <div><span style="font-size: 12px;">Low capability to pass the local optimum</span></div>
    <div><br /></div>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Machine learning algorithms in MLlib require that data is represented as numerical values. Our current data is represented by a variety of different types including time stamps, integers and strings. Therefore, we need to transform this data into some numerical representation. So we will use several DataFrame transformations to manipulate out date data.</span></span></span></b></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <hr />
    <div><b><span style="font-size: 12px;">Key concepts:</span></b></div>
    <div><b><span style="font-size: 12px;">Spark is a distributed programming model in which the user specifies transformations. These transformations build up a directed acyclic graph of transformations and action. An action begins the process of execution that graph of instructions, as a single job, by breaking it down into stages and tasks to execute across the cluster. The logical structures that we manipulate with transformations and actions are DataFrames and Datasets. To create a new DataFrame or Dataset, you call a transformation. To start computation or convert to native language types, you call an action.</span></b></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><b><span style="font-size: 12px;"><i><span style="color: rgb(255, 0, 42);">Fundamental concepts:</span></i></span></b></div>
    <div><b><span style="font-size: 12px;"><i>Spark is a distributed programming model in which the user specifies transformations. These transformations build up a directed acyclic graph of transformations and action. An action begins the process of execution that graph of instructions, as a single job, by breaking it down into stages and tasks to execute across the cluster. The logical structures that we manipulate with transformations and actions are DataFrames and Datasets. To create a new DataFrame or Dataset, you call a transformation. To start computation or convert to native language types, you call an action.</i></span></b></div>
    <div> </div>
    <div><b><span style="font-size: 12px;">Structured API Overview</span></b></div>
    <div><span style="font-size: 12px;">Structured APIs are a tool for manipulating all sorts of data, from unstructured log files to semi-structured CSV files and highly structured Parquet <i>(Apache Parquet is a columnar storage format available to any project in the Hadoop ecosystem, regardless of the choice of data processing framework, data model or programming language)</i> files. These APIs refer to three core types of distributed collection APIs:</span></div>
    <ol>
        <li>
            <div><span style="font-size: 12px;">Datasets</span></div>
        </li>
        <li>
            <div><span style="font-size: 12px;">DataFrames</span></div>
        </li>
        <li>
            <div><span style="font-size: 12px;">SQL Tables and Views</span></div>
        </li>
    </ol>
    <div><span style="font-size: 12px;">Majority of the Structured APIs apply to both </span><b><span style="font-size: 12px;"><i>batch</i></span></b><span style="font-size: 12px;"> and </span><b><span style="font-size: 12px;"><i>streaming</i></span></b><span style="font-size: 12px;"> computation. This means that when you work with the Structured APIs, it should be simple to migrate from batch to streaming or vice versa with little to no effort.  </span><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">Structured APIs are the fundamental abstraction used to write the majority of data flows. </span></span></div>
    <div> </div>
    <div><b><span style="font-size: 12px;">DataFrames and Datasets</span></b></div>
    <div><span style="font-size: 12px;">DataFrames and Datasets are </span><b><span style="font-size: 12px;">distributed</span></b><span style="font-size: 12px;"> table-like collection with well-defined rows and columns. Each column must have the same number of rows as all the other columns although you can use null to specify the absence of a value and </span><b><span style="font-size: 12px;">each column has type information</span></b><span style="font-size: 12px;"> that must be consistent for every row in the collection. To Spark, DataFrames and Datasets represent </span><b><span style="font-size: 12px;">immutable</span></b><span style="font-size: 12px;">, </span><b><span style="font-size: 12px;">lazily evaluated plans(</span></b><span style="font-size: 12px;">transformations</span><b><span style="font-size: 12px;">) </span></b><span style="font-size: 12px;">that specify what operations to apply to data residing at a location to generate some output. When we perform an action on a DataFrame, we instruct Spark to perform the actual transformations and return the results. These represent plans of how to manipulate rows and columns to compute the user's desired result. </span></div>
    <div> </div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Tables and views</span> </span></b><span style="font-size: 12px;">- like a DataFrame, but we execute SQL against them instead of DataFrame code. </span></div>
    <div> </div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Schema</span></span></b><span style="font-size: 12px;"> - defines the column names and types of a DataFrame. You can define schemas manually or read a schema from a data source. Schemas consist of types meaning that you need a way of specifying what lies where.</span></div>
    <div> </div>
    <div><b><span style="font-size: 12px;">Overview of Structured Spark Types</span></b></div>
    <div><span style="font-size: 12px;">Spark is effectively a programming language of its own. </span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">Spark</span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"> uses an </span></span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">engine</span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"> called </span></span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">Catalyst</span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">.</span></span></div>
    <div> </div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Catalyst - </span></span></b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">maintains its own type information through the planning and processing of work. This opens up execution optimizations.</span></span></div>
    <div><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Even if we use Spark's Structured APIs from Python or R, the majority of our manipulations will operate strictly on Spark types not Python types. </span></span></div>
    <div> </div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2012.36.16%20AM.png" height="90" width="568" />
    <div><br /></div>
    <div> </div>
    <div><span style="font-size: 12px;">This addition operation happens because Spark will convert an expression written in an input language to Spark's internal Catalyst representation of that same type information. It then will operate on that internal representation. </span></div>
    <div> </div>
    <div><b><span style="font-size: 12px;">DataFrames VS Datasets</span></b></div>
    <table width="937px" style="width:937px;">
        <colgroup>
            <col style="width: 471px;" />
            <col style="width: 466px;" />
        </colgroup>
        <tbody>
            <tr>
                <td colspan="2" style="background-color:rgb(254, 222, 193);border-color:rgb(253, 175, 105);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">STRUCTURED APIs</span></span></b></div>
                </td>
            </tr>
            <tr>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">DataFrames</span></span></b></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">Datasets</span></span></b></div>
                </td>
            </tr>
            <tr>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="color: rgb(0, 0, 0);">untyped</span></b></div>
                    <div style="text-align:center;"><span style="color: rgb(0, 0, 0);">(Spark maintains them completely)</span></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="color: rgb(0, 0, 0);">typed</span></b></div>
                    <div style="text-align:center;"><span style="color: rgb(0, 0, 0);">(checks whether types conform to the specification at compile time.)</span></div>
                    <div style="text-align:center;"><span style="color: rgb(0, 0, 0);">Only available to JVM based languages Scala and Java.</span></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">DataFrames are Datasets of Type </span><i><span style="color: rgb(255, 0, 42);">Row</span></i><span style="color: rgb(255, 0, 42);">. </span></span></b></div>
    <div><span style="font-size: 12px;">The "Row" type is Spark's internal representation of its optimized in-memory format for computation. </span></div>
    <div><span style="font-size: 12px;">To Spark in Python and R there is no such thing as a Dataset, everything is a DataFrame and therefore we always operate on that optimized format.</span></div>
    <div> </div>
    <div><b><span style="font-size: 12px;"><i>//WATCH! - Spark Catalyst Engine talks by Josh Rosen and Herman van Hovell</i></span></b></div>
    <div><br /></div>
    <div>KEY Takeaway: When you use DataFrames, you are taking advantage of Spark's optimized internal format.</div>
    <div><br /></div>
    <div><b>Columns: </b>represent a simple type like an integer or string or complex type like an array or map or null values. </div>
    <div><b>Rows</b>: record of data.</div>
    <div> </div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2012.53.06%20AM.png" height="94" width="448" />
    <div><br /></div>
    <div><br /></div>
    <div><b>Spark Types</b></div>
    <div>(Spark documentation - get updated time to time)</div>
    <div><br /></div>
    <div><b>Overview of Structured API Execution</b></div>
    <ol>
        <li>
            <div>Write DataFrame/Dataset/SQL Code</div>
        </li>
        <li>
            <div><span style="font-size: 14px;">If valid code, converts this to a Logical Plan</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Spark . transforms this Logical Plan, checking for optimizations along the way</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Spark then executes this Physical Plan (RDD Manipulations) on the cluster</span></div>
        </li>
    </ol>
    <div><br /></div>
    <div>The code we write gets submitted to Spark either through console or via a submitted job. This <b>code passes through the Catalyst Optimize</b>r, which decides how the code should be executed and lays out a plan for doing so before, finally, the code is run and the result is returned to the user.</div><img src="Spark%20Overview.html.resources/spdg_0401.png" height="523" width="1014" />
    <div><br /></div>
    <table width="1600px" style="width:1600px;">
        <colgroup>
            <col style="width: 803px;" />
            <col style="width: 797px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Logical Planning</span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Physical Planning</span></b></div>
                    <div style="text-align:center;"> </div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><span style="font-size: 14px;">The first phase takes user code and converts it into a logical plan (optimized version of the user's set of expressions)</span></div>
                    <div><span style="font-size: 14px;">It does this by converting user code into an </span><b><span style="font-size: 14px;"><i>unresolved logical plan. </i></span></b><span style="font-size: 14px;">The plan is unresolved because although your code might be valid, the tables and columns that it refers to might or might not exist. Spark uses the catalog, a repository of all table and DataFrame information to </span><b><span style="font-size: 14px;"><i>resolve</i></span></b><span style="font-size: 14px;"> columns and tables in the </span><b><span style="font-size: 14px;"><i>analyzer. </i></span></b><span style="font-size: 14px;">The analyzer might reject the unresolved logical plan if the required column name does not exist in the catalog. If the analyzer can resolve it, the result is passed through the Catalyst Optimizer, a collection of rules that attempt to optimize the logical plan by pushing down predicates or selections. Packages can extend the Catalyst to include their own rules for domain-specific optimizations.</span></div><img src="Spark%20Overview.html.resources/spdg_0402.png" height="343" width="1250" />
                    <div><br /></div>
                </td>
                <td>
                    <div>After creating the optimized logical plan, Spark begins the physical planning process. The physical plan - often called SPark plan - specifies how the logical plan will execute on the cluster by generating different physical execution strategies and comparing them through a cost model. Upon selecting a physical plan Spark runs all of this code over RDDs.</div><img src="Spark%20Overview.html.resources/spdg_0403.png" height="449" width="1367" />
                    <div><br /></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><b><span style="font-size: 12px;">Basic Structured Operations</span></b></div>
    <div><span style="font-size: 12px;">DataFrame consists of a series of records that are of type <i>Row</i> and a number of columns that represent a computation expression that can perform on each individual record in the Dataset. </span><b><span style="font-size: 12px;"><i>Schemas</i></span></b><span style="font-size: 12px;"> define the name as well as the type of data in each column. </span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><i>Partitioning</i></span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><i> </i>of the DataFrame defines the layout of the DataFrame or Dataset's physical distribution across the cluster. The </span></span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><i>partitioning scheme</i></span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"> defines how that is allocated.</span></span></div>
    <div><br /></div>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Creating a DataFrame:</span></span></span></b></div>
    <table width="913px" style="width:913px;">
        <colgroup>
            <col style="width: 446px;" />
            <col style="width: 467px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">Python</span></span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">Scala</span></span></b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">df = spark.read.format("json").load("/Users/mikepetridisz/Desktop/json/2015-summary.json")</span></span></b></div>
                </td>
                <td>
                    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">val df = spark.read.format("json").load("/Users/mikepetridisz/Desktop/json/2015-summary.json")</span></span></b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">printSchema</span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">df.printSchema()</span></span></div>
                    <div> </div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"># A schema is a StructType made up of a number of fields, StructFields, that have a name, type, a boolean flag (null values/missing values), metadata (metadata used in Machine Learning)</span></span></div>
                </td>
                <td>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">printSchema</span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">df.printSchema()</span></span></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;</span></div>
                    <div><br /></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"> </span></span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">myManualScheme</span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"> = StructType([</span></span></div>
                    <div><br /></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">... StructField("DEST_COUNTRY_NAME", StringType(), True),</span></span></div>
                    <div><br /></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">... StructField("ORIGIN_COUNTRY_NAME", StringType(), True),</span></span></div>
                    <div><br /></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">... StructField("count", LongType(), False, metadata={"hello":"world"})</span></span></div>
                    <div><br /></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">... ])</span></span></div>
                    <div><br /></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">&gt;&gt;&gt; df = spark.read.format("json").schema(myManualScheme)\</span></span></div>
                    <div><br /></div>
                    <div style="margin-bottom:16px;"><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">... .load("/Users/mikepetridisz/Desktop/json/2015-summary.json")</span></span></div>
                </td>
                <td>
                    <div> </div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">Columns and Expressions</span></span></b></div>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><i>Expressions</i></span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"> - when you select, remove manipulate columns from DataFrames</span></span></div>
    <div><br /></div>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Creating a Column</span></span></span></b></div>
    <table width="1588px" style="width:1588px;">
        <colgroup>
            <col style="width: 769px;" />
            <col style="width: 620px;" />
            <col style="width: 199px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Python</span></span></span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Scala</span></span></span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">NOTE</span></b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">from pyspark.sql.functions import cal, column</span></span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">col("someColumnName")</span></span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">column("someColumnName")</span></span></span></div>
                </td>
                <td>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">import org.apache.spark.sql.functions.{col, column}</span></span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">col("someColumnName")</span></span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">column("someColumnName")</span></span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">--</span></span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">other way:</span></span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">scala&gt; $"myColumn"</span></span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">scala&gt;'myColumn</span></span></span></div>
                </td>
                <td>
                    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><i><span style="color: rgb(0, 0, 0);">col()  or column function</span></i></span></span></b></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><b><span style="font-size: 12px;">Explicit Column References </span></b></div>
    <div><span style="font-size: 12px;">if you need to refer to a specific DataFrame's column, you can use the col method on the specific DataFrame. This can be useful when performing a join and need to refer to a specific column in one DataFrame that might share the same name with another column in the joined DataFrame.</span></div>
    <div> </div>
    <div><b><span style="font-size: 12px;">Expressions</span></b></div>
    <div><span style="font-size: 12px;">Columns are expressions. An expression is a set of transformations on one or more values in a record in a DataFrame. </span></div>
    <div><span style="font-size: 12px;">An expression created via the expr function is just a DataFrame column reference.</span></div>
    <div><span style="font-size: 12px;"><i>expr("someCol") is equivalent to </i></span><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><i>col("someCol")</i></span></span></div>
    <div> </div>
    <div><b><span style="font-size: 12px;">Columns as Expressions</span></b></div>
    <div><span style="font-size: 12px;">When using an expression, the expr function can actually parse transformations and column references from a string and can subsequently be passed into further transformations.</span></div>
    <div><span style="font-size: 12px;"><i>Key takeaways:</i></span></div>
    <ul>
        <li>
            <div><span style="font-size: 12px;">Columns are just expressions</span></div>
        </li>
        <li>
            <div><span style="font-size: 12px;">Columns and transformations of those columns compile to the same logical plan as parsed expressions.</span></div>
        </li>
    </ul>
    <div><span style="font-size: 12px;"><i>Example:</i></span></div>
    <div><span style="font-size: 12px;"><i>DataFrame Code</i></span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%202.55.57%20AM.png" height="96" width="818" />
    <div><br /></div>
    <div><span style="font-size: 12px;"><i>SQL code</i></span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%202.59.18%20AM.png" height="96" width="836" />
    <div><br /></div>
    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">#You can write expressions as DataFrame code or SQL code and get the exact same performance characteristics.</span></span></div>
    <div><br /></div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Accessing a DataFrame's Columns</span></span></b></div>
    <div>printSchema or:</div>
    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">spark.read.format("json").load("/Users/mikepetridisz/Desktop/json/2015-summary.json")</span></span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">.columns</span></span></span></b></div>
    <div> </div>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Records and Rows</span></span></span></b></div>
    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Each row in a DataFrame is a single </span></span></span></div>
    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">record as an object type Row. </span></span></span></div>
    <div><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Spark manipulates Row objects using column expressions in order to produce usable values. </span></span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%203.04.44%20AM.png" height="72" width="1310" />
    <div><br /></div>
    <div><br /></div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Creating Rows</span></span></b></div>
    <table width="1834px" style="width:1834px;">
        <colgroup>
            <col style="width: 544px;" />
            <col style="width: 645px;" />
            <col style="width: 645px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Python</span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Scala</span></b></div>
                </td>
                <td>
                    <div>Note</div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><span style="font-size: 14px;">from pyspark.sql import Row</span></div>
                    <div><span style="font-size: 14px;">myRow = Row("Hello", None, 1, False)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%203.07.45%20AM.png" height="178" width="646" />
                    <div><br /></div>
                </td>
                <td>
                    <div><span style="font-size: 14px;">import org.apache.spark.sql.Row</span></div>
                    <div><span style="font-size: 14px;">val myRow = Row("Hello", null, 1, false)</span></div>
                </td>
                <td>
                    <div>Creating Rows</div>
                    <div>Importing Rows</div>
                    <div><span style="font-size: 14px;">Accessing data in rows </span></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">DataFrame Transformations</span></span></span></b></div>
    <ol>
        <li>
            <div><span style="font-size: 12px;">We can add rows or columns</span></div>
        </li>
        <li>
            <div><span style="font-size: 12px;">We can remove rows and columns</span></div>
        </li>
        <li>
            <div><span style="font-size: 12px;">We can transform a row into a column or vice versa</span></div>
        </li>
        <li>
            <div><span style="font-size: 12px;">We can change the order of rows based on the values in columns</span></div>
        </li>
    </ol>
    <div> </div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Creating DataFrames on the fly</span></span></b></div>
    <table width="1152px" style="width:1152px;">
        <colgroup>
            <col style="width: 530px;" />
            <col style="width: 622px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Python</span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Scala</span></b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><span style="font-size: 14px;">from pyspark.sql import Row</span></div>
                    <div><span style="font-size: 14px;">from pyspark.sql.types import StructField, StructType, StringType, LongType</span></div>
                    <div> </div>
                    <div><span style="font-size: 14px;">myManualSchema = StructType([</span></div>
                    <div><span style="font-size: 14px;">StructField("some", StringType(), True),</span></div>
                    <div><span style="font-size: 14px;">StructField("col", StringType(), True),</span></div>
                    <div><span style="font-size: 14px;">StructField("names", LongType(), False)</span></div>
                    <div><span style="font-size: 14px;">])</span></div>
                    <div><span style="font-size: 14px;">myRow = ("hello", None, 1)</span></div>
                    <div><span style="font-size: 14px;">myDf = spark.createDataFrame([myRow], myManualSchema)</span></div>
                    <div><span style="font-size: 14px;">myDf.show()</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%203.17.57%20AM.png" height="544" width="1174" />
                    <div><br /></div>
                    <div> </div>
                    <div> </div>
                </td>
                <td>
                    <div><span style="font-size: 14px;">import org.apache.spark.sql.Row</span></div>
                    <div><span style="font-size: 14px;">import org.apache.spark.sql.types.{ StructField, StructType, StringType, LongType}</span></div>
                    <div> </div>
                    <div><span style="font-size: 14px;">val myManualSchema = new StructType(Array(</span></div>
                    <div><span style="font-size: 14px;">new StructField("some", StringType, true),</span></div>
                    <div><span style="font-size: 14px;">new StructField("col", StringType, true),</span></div>
                    <div><span style="font-size: 14px;">new StructField("names", LongType, false)))</span></div>
                    <div><span style="font-size: 14px;">val myRow = Seq(Row("hello", None, 1L))</span></div>
                    <div><span style="font-size: 14px;">val myRDD = spark.sparkContext.parallelize(myRows)</span></div>
                    <div><span style="font-size: 14px;">val myDf = spark.createDataFrame(myRDD, myManualSchema)</span></div>
                    <div><span style="font-size: 14px;">myDf.show()</span></div>
                    <div><span style="font-size: 14px;">val myDf = Seq(("Hello", 2, 1L)).toDF("col1","col2", "col3")</span></div>
                    <div><span style="font-size: 14px;">myDf.show()</span></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Select and SelectExpr</span></span></b></div>
    <ul>
        <li>
            <div>allows you to do the DataFrame equivalent of SQL queries on a table of data</div>
        </li>
    </ul>
    <table width="1596px" style="width:1596px;">
        <colgroup>
            <col style="width: 433px;" />
            <col style="width: 486px;" />
            <col style="width: 450px;" />
            <col style="width: 227px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;">SQL</span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Python</span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b>Scala</b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b>Note</b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><b>SELECT</b> DEST_COUNTRY_NAME <b>FROM</b> dfTable <b>LIMIT</b> 2</div>
                </td>
                <td>
                    <div><span style="font-size: 14px;">df.select("DEST_COUNTRY_NAME").show(2)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%203.42.56%20AM.png" height="244" width="692" />
                    <div><br /></div>
                </td>
                <td>
                    <div><span style="font-size: 14px;">df.select("DEST_COUNTRY_NAME").show(2)</span></div>
                </td>
                <td>
                    <div>Use the select method and pass in <span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">the column names as strings with  which you would like to work</span></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><b>SELECT</b> DEST_COUNTRY_NAME, ORIGIN_COUNTRY_NAME <b>FROM</b> dfTable <b>LIMIT</b> 2</div>
                </td>
                <td>
                    <div><span style="font-size: 14px;">df.select("DEST_COUNTRY_NAME", "ORIGIN_COUNTRY_NAME").show(2)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%203.46.05%20AM.png" height="254" width="946" />
                    <div><br /></div>
                </td>
                <td>
                    <div><span style="font-size: 14px;">df.select("DEST_COUNTRY_NAME", "ORIGIN_COUNTRY_NAME").show(2)</span></div>
                </td>
                <td>
                    <div>you can select multiple columns</div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><br /></div>
                </td>
                <td>
                    <div><b>you can refer to columns in a number of different ways</b></div>
                    <div>df.select(</div>
                    <div><b>expr</b>(<span style="font-size: 14px;">"DEST_COUNTRY_NAME"),</span></div>
                    <div><b><span style="font-size: 14px;">col</span></b>(<span style="font-size: 14px;">"DEST_COUNTRY_NAME"),</span></div>
                    <div><b><span style="font-size: 14px;">column</span></b>(<span style="font-size: 14px;">"DEST_COUNTRY_NAME"))\</span></div>
                    <div><span style="font-size: 14px;">.show(2)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%203.49.52%20AM.png" height="348" width="790" />
                    <div><br /></div>
                </td>
                <td>
                    <div><br /></div>
                </td>
                <td>
                    <div><br /></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b><span style="color: rgb(255, 0, 42);">AS and alias - </span><span style="color: rgb(0, 0, 0);">change the name using the AS and alias keywords</span></b></div>
    <table width="1626px" style="width:1626px;">
        <colgroup>
            <col style="width: 433px;" />
            <col style="width: 516px;" />
            <col style="width: 450px;" />
            <col style="width: 227px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">SQL</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Python</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Scala</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Note</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>SELECT</b> DEST_COUNTRY_NAME as destination <b>FROM</b> dfTable <b>LIMIT</b> 2</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.select(expr("DEST_COUNTRY_NAME AS destination").alias("DEST_COUNTRY_NAME")).show(2)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%204.01.30%20AM.png" height="232" width="898" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.select("DEST_COUNTRY_NAME").show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>change the name of the column</div>
                    <div><b>AS</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.select(expr("DEST_COUNTRY_NAME AS destination").alias("DEST_COUNTRY_NAME")).show(2)<span style="font-size: 14px;">)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%204.03.20%20AM.png" height="280" width="1348" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="margin-top:16px;margin-bottom:16px;">df.select(expr("DEST_COUNTRY_NAME AS destination").alias("DEST_COUNTRY_NAME")).show(2)</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>alias</b></div>
                    <div>change the column name back to its original name</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT *, (DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as withinCountry</div>
                    <div>FROM dfTable</div>
                    <div>LIMIT 2</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.<b>selectExpr</b>(</div>
                    <div>"*",</div>
                    <div><span style="font-size: 14px;">"(DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as withinCountry")\</span></div>
                    <div><span style="font-size: 14px;">.show(2)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%204.10.38%20AM.png" height="320" width="966" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.<b>selectExpr</b>(</div>
                    <div>"*",</div>
                    <div><span style="font-size: 14px;">"(DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as withinCountry")</span></div>
                    <div><span style="font-size: 14px;">.show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>add a new column withinCountry to DataFrame that specifies whether the destination and origin are the same</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT act(count), count(distinct(DEST_COUNTRY_NAME)) FROM dfTable LIMIT 2</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.selectExpr("avg(count)", "count(distinct(DEST_COUNTRY_NAME))").show(2)</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%204.25.59%20AM.png" height="170" width="1110" />
                    <div><br /></div>
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.selectExpr("avg(count)", "count(distinct(DEST_COUNTRY_NAME))").show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Aggregations</div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><br /></div>
    <div><b><span style="font-size: 14px;"><span style="color: rgb(255, 0, 42);">Converting to Spark Types</span></span></b></div>
    <div><span style="font-size: 14px;">Sometimes we need to pass explicit values into Spark that aren't a new column but are just a value.</span></div>
    <div><span style="font-size: 14px;">The was we do this is through </span><b><span style="font-size: 14px;"><i>literals</i></span></b><span style="font-size: 14px;">. This is a translation from a given programming language's literal value to one that Spark understands. Literals are expressions.</span></div>
    <table width="1626px" style="width:1626px;">
        <colgroup>
            <col style="width: 433px;" />
            <col style="width: 516px;" />
            <col style="width: 450px;" />
            <col style="width: 227px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">SQL</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Python</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Scala</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Note</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT *, 1 as One FROM dfTable LIMIT2</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>from pyspark.sql.functions import lit</div>
                    <div>df.select(expr("*"),lit(1).alias("One")).show(2)</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%204.31.21%20AM.png" height="268" width="760" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>import org.apache.spark.sql.functions.lit</div>
                    <div><span style="font-size: 14px;">df.select(expr("*"),lit(1).as("One")).show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><b><span style="color: rgb(255, 0, 42);">Adding Columns</span></b></div>
    <table width="1528px" style="width:1528px;">
        <colgroup>
            <col style="width: 433px;" />
            <col style="width: 516px;" />
            <col style="width: 315px;" />
            <col style="width: 264px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">SQL</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Python</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Scala</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Note</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT *, 1 as numberOne FROM dfTable LIMIT2</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.withColumn("numberOne", lit(1)).show(2)</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%204.34.11%20AM.png" height="248" width="806" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.withColumn("numberOne", lit(1)).show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>formal way of<b> adding a column</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.withColumn("withinCountry", expr("ORIGIN_COUNTRY_NAME == DEST_COUNTRY_NAME"))\</span></div>
                    <div><span style="font-size: 14px;">.show(2)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%204.36.44%20AM.png" height="286" width="1226" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.withColumn("withinCOuntry", expr("ORIGIN_COUNTRY_NAME == DEST_COUNTRY_NAME"))\</span></div>
                    <div><span style="font-size: 14px;">.show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Boolean</b> expression for when the original country is the same as the Destination Country</div>
                    <div><br /></div>
                    <div> </div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.withColumn("Destination", expr("DEST_COUNTRY_NAME").columns</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">NOTICE that withColumn function takes two arguments; the column name and the expression that will create the value for that given row in the DataFrame. We can also rename a column this way. (SQL syntax is the same as previously so it is not here now.</span></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b><span style="color: rgb(255, 0, 42);">Renaming Columns</span></b></div>
    <div><b><i>withColumnRenamed</i></b> method</div>
    <table width="1528px" style="width:1528px;">
        <colgroup>
            <col style="width: 433px;" />
            <col style="width: 516px;" />
            <col style="width: 315px;" />
            <col style="width: 264px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">SQL</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Python</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Scala</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Note</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.withColumnRenamed("DEST_COUNTRY_NAME", "dest").columns</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%204.44.22%20AM.png" height="90" width="900" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.withColumnRenamed("DEST_COUNTRY_NAME", "dest").columns</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>rename columns</b></div>
                    <div>name of the string = first argument</div>
                    <div>string = second argument</div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="color: rgb(255, 0, 42);">Reserved Characters and Keywords</span></span></b></div>
    <div><span style="font-size: 12px;">like spaces or dashes in column names. Handling these means escaping column names appropriately. </span></div>
    <div><span style="font-size: 12px;">We do this by using </span><b><span style="font-size: 12px;">backtick</span></b><span style="font-size: 12px;"> ("`")</span></div>
    <table width="1559px" style="width:1559px;">
        <colgroup>
            <col style="width: 464px;" />
            <col style="width: 516px;" />
            <col style="width: 315px;" />
            <col style="width: 264px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">SQL</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Python</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Scala</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Note</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="background-color:rgb(252, 83, 86);border-color:rgb(251, 17, 21);">
                    <div><span style="color: rgb(255, 255, 255);">dfWithLongColName = df.withColumn(</span></div>
                    <div><span style="color: rgb(255, 255, 255);">"This Long Column-Name",</span></div>
                    <div><span style="color: rgb(255, 255, 255);">expr("ORIGIN)COUNTRY_NAME")</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>import org.apache.spark.sql.functions.expr</div>
                    <div><span style="font-size: 14px;">val dfWithLongColName = df.withColumn(</span></div>
                    <div><span style="font-size: 14px;">"this Long Column-Name",</span></div>
                    <div><span style="font-size: 14px;">expr("ORIGIN_COUNTRY_NAME"))</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Could not run this nor understand this part! - Need to come back &amp; Check!</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="background-color:rgb(252, 83, 86);border-color:rgb(251, 17, 21);">
                    <div><span style="font-size: 14px;"><span style="color: rgb(255, 255, 255);">dfWithLongColName.selectExpr(</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(255, 255, 255);">" This Long Column-Name ",</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(255, 255, 255);">" This Long Column-Name as `new col`")\</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(255, 255, 255);">.show(2)</span></span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>set spark.sql.caseSensitive true</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Case Sensitivity </b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.drop("ORIGIN_COUNTRY_NAME").columns</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Removing Columns</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>dfWithLongColName.drop("ORIGIN_COUNTRY_NAME", "DEST_COUNTRY_NAME")</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Removing multiple columns</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>SELECT</b> *, <b>cast</b>(<b>count as</b> long) <b>AS</b> count2 <b>FROM</b> dfTable</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="margin-top:16px;">df.withColumn("count2", col("count").cast("long"))</div>
                    <div><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%208.20.25%20PM.png" height="80" width="1386" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Change Column's Type (cast)</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT * FROM dfTable WHERE count &lt; 2 LIMIT 2</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="margin-top:16px;">df.filter(col("count") &lt; 2).show(2)</div>
                    <div><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%208.24.05%20PM.png" height="240" width="654" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Filtering Rows </b>- evaluates to true or false. You can use <b>where</b> or <b>filter </b>an they both will perform the same operation.</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>SELECT</b> * <b>FROM</b> dfTable <b>WHERE</b> <b>count</b> &lt; 2 <b>AND</b> ORIGIN_COUNTRY_NAME != "Croatia <b>LIMIT</b> 2</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.where(col("count") &lt; 2).where(col("ORIGIN_COUNTRY_NAME") != "Croatia")\</div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">.show(2)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%208.29.04%20PM.png" height="264" width="1138" />
                    <div><br /></div>
                    <div style="margin-bottom:16px;"><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.where(col("count") &lt; 2).where(col("ORIGIN_COUNTRY_NAME") != "Croatia")</div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">.show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Multiple filters </b></div>
                    <div><span style="font-size: 14px;">you can put multiple filters into the same expression. It's not always useful because Spark automatically performs all filtering operations at the same time regardless of the filter ordering. This optimization is called </span><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;"><span style="color: rgb(184, 22, 215);">PIPELINING</span></span></span></b><span style="font-size: 14px;">. This means that if you want to specify multiple AND filters, just chain them sequentially and let Spark handle the rest.</span></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT COUNT(DISTINCT(<span style="font-size: 14px;">ORIGIN_COUNTRY_NAME,  DEST_COUNTRY_NAME) FROM dfTable</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="margin-top:16px;">df.select("ORIGIN_COUNTRY_NAME", "DEST_COUNTRY_NAME").distinct().count()</div>
                    <div><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%208.33.16%20PM.png" height="66" width="1188" />
                    <div><br /></div>
                    <div style="margin-bottom:16px;"><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.select("ORIGIN_COUNTRY_NAME", "DEST_COUNTRY_NAME").distinct().count()</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Getting unique Rows</div>
                    <div>extract unique or distinct values. These values van be in one or more columns. <b>distinct </b>method allws us to duplicate any rows that are in the DataFrame. </div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="background-color:rgb(255, 230, 151);border-color:rgb(255, 211, 70);">
                    <div><span style="color: rgb(0, 0, 0);">seed = 5</span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="color: rgb(0, 0, 0);">withReplacement = False</span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="color: rgb(0, 0, 0);">fraction = 0.5</span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="color: rgb(0, 0, 0);">df.sample(withReplacement, fraction, seed).count()</span></span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%208.35.54%20PM.png" height="172" width="780" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>val seed = 5</div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">val withReplacement = False</span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">val fraction = 0.5</span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">df.sample(withReplacement, fraction, seed).count()</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>sample </b>method - sample some random records from your DataFrame.</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>dataFrames = df.randomSplit([0.25, 0.75], seed)</div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">dataFrames[0].count() &gt; dataFrames[1].count()</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%208.48.03%20PM.png" height="92" width="734" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>val dataFrames = df.randomSplit(Array(0.25, 0.75), seed)</div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">dataFrames(0).count() &gt; dataFrames(1).count()</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Random Splits </b>can be useful when you need to break up your DataFrame.  It cannot guarantee that all records are in one of the DataFrames from which you are sampling. This is often used with machine learning.</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>from pyspark.sql import Row</div>
                    <div>schema = df.schema</div>
                    <div>newRows = [</div>
                    <div>Row("New Country", "Other Country", 5),</div>
                    <div><span style="font-size: 14px;">Row("New Country 2", "Other Country 3", 1),</span></div>
                    <div><span style="font-size: 14px;">]</span></div>
                    <div><span style="font-size: 14px;">parallelizeRows = spark.sparkContext.parallelize(newRows)</span></div>
                    <div><span style="font-size: 14px;">newDF = spark.createDataFrame(parallelizeRows, schema)</span></div>
                    <div> </div>
                    <div><span style="font-size: 14px;">df.union(newDF)\</span></div>
                    <div><span style="font-size: 14px;">.where("count =1")\</span></div>
                    <div><span style="font-size: 14px;">.where(col("ORIGIN_COUNTRY_NAME") != "United States")\</span></div>
                    <div><span style="font-size: 14px;">.show()</span></div>
                    <div> </div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%209.04.25%20PM.png" height="812" width="888" />
                    <div><br /></div>
                    <div> </div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Concentrating and Appending Rows (Union)</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.sort("count").show(5)</div>
                    <div>df.orderBy("count", "DEST_COUNTRY_NAME").show(5)</div>
                    <div>df.orderBy(col("count"), col("DEST_COUNTRY_NAME")).show(5)</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%209.08.10%20PM.png" height="1006" width="900" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.sort("count").show(5)</span></div>
                    <div><span style="font-size: 14px;">df.orderBy("count", "DEST_COUNTRY_NAME").show(5)</span></div>
                    <div><span style="font-size: 14px;">df.orderBy(col("count"), col("DEST_COUNTRY_NAME")).show(5)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Sorting Rows</b></div>
                    <div> </div>
                    <div><b>sort </b>and<b> orderBy </b>do the same</div>
                    <div>the default is sort in ascending order</div>
                    <div><br /></div>
                    <div><br /></div>
                    <div>to more explicitly specify sort direction, you need to use <b>asc </b>and <b>desc</b> functions if operating on a column. </div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>from pyspark.sql.functions import asc, desc</div>
                    <div>df.orderBy(expr("count desc")).show(2)</div>
                    <div>df.orderBy(col("count").desc(),  col("DEST_COUNTRY_NAME").asc()).show(2)</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%209.11.58%20PM.png" height="518" width="1086" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>(sort)</div>
                    <div>to more explicitly specify sort direction, you need to use <b>asc </b>and <b>desc</b> functions if operating on a column. </div>
                    <div><br /></div>
                    <div>Advanced tip is to use asc_nulls_first, desc_nulls_first, asc_nulls_last, or _desc_nulls_last</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT * FROM dfTable LIMIT 6</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.limit(5).show()</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.limit(5).show()</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Limit</b></div>
                    <div>Restrict what you extract from the dataframe</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b><span style="font-size: 14px;">SELECT</span></b><span style="font-size: 14px;"> * </span><b><span style="font-size: 14px;">FROM</span></b><span style="font-size: 14px;"> dfTable </span><b><span style="font-size: 14px;">ORDER BY count</span></b><span style="font-size: 14px;"> </span><b><span style="font-size: 14px;">desc</span></b><span style="font-size: 14px;"> </span><b><span style="font-size: 14px;">LIMIT</span></b><span style="font-size: 14px;"> 6</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.orderBy(expr("count")).asc().limit(6).show()</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.orderBy(expr("count")).asc().limit(6).show()</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.rdd.getNumPartitions()</div>
                    <div>df.repartition(5)</div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><b>Repartition based on a columns name </b></div>
                    <div><b><span style="font-size: 14px;">df.repartition(5, col("DEST_COUNTRY_NAME"))</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.rdd.getNumPartitions()</span></div>
                    <div><span style="font-size: 14px;">df.repartition(5)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Repartition </b></div>
                    <div>partition the data according to some frequently filtered columns, which control the physical layout of data across the cluster including the partitioning scheme and the number of partitions. </div>
                    <div><br /></div>
                    <div>Repartition will incur a full shuffle of the data, regardless of whether one is necessary. This means that you should typically only repartition when the future number of partitions os greater than your current number of partitions or when you are looking to partition by a set of columns. </div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.repartition(5, col("DEST_COUNTRY_NAME")).coalesce(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.repartition(5, col("DEST_COUNTRY_NAME")).coalesce(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Coalesce</b></div>
                    <div><span style="font-size: 14px;">will not incur a full shuffle and will try to combine partitions. This operation will shuffle your data into five partitions based on the destination country name and then coalesce them without a full shuffle.</span></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>collectDF=df.limit(10)</div>
                    <div><span style="font-size: 14px;">collectDF.take(5) #works with an integer count</span></div>
                    <div><span style="font-size: 14px;">collectDF.show() #this prints it out nicely</span></div>
                    <div><span style="font-size: 14px;">collectDF.show(5, False)</span></div>
                    <div><span style="font-size: 14px;">collectDF.collect()</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%209.31.14%20PM.png" height="1068" width="1068" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>val collectDF=df.limit(10)</div>
                    <div><span style="font-size: 14px;">collectDF.take(5)</span></div>
                    <div><span style="font-size: 14px;">collectDF.show()</span></div>
                    <div><span style="font-size: 14px;">collectDF.show(5, False)</span></div>
                    <div><span style="font-size: 14px;">collectDF.collect()</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Collecting Rows to the Driver</b></div>
                    <div>Spark maintains the state of the cluster in the driver. There are times when you want to collect some of the data to the driver in order to manipulate it on your local machine.</div>
                    <div><br /></div>
                    <div><b>collect </b>gets all the data from the entire Dataframe</div>
                    <div><b>take </b>selects the first N rows </div>
                    <div><b>show </b>prints out a number of rows nicely.</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>collectDF.toLocalIterator()</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Iterate over the entire dataset. The method is called <b>toLocalIterator </b>that collects partitions to the driver as an iterator. Iterates over the entire dataset partition by partition in a serial manner</div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><br /></div>
    <div style="text-align:center;"><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;"><span style="color: rgb(255, 0, 42);">Working with Different Types of Data</span></span></span></b></div>
    <div><b><span style="font-size: 14px;">Objectives</span></b></div>
    <ul>
        <li>
            <div>Booleans</div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Numbers</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Strings</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Dates and Timestamps</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Handling Null</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Complex Types</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">User Defined Functions</span></div>
        </li>
    </ul>
    <div> </div>
    <div><b><span style="font-size: 14px;">Where to look for APIs?</span></b></div>
    <div><span style="font-size: 14px;">DataFrame (Dataset) Methods: DataFrame is just a Dataset of Row types, so you will look at the Dataset methods available at: <a href="http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Dataset" rev="en_rl_none">http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Dataset</a></span></div>
    <div>DataFrameStatFunctions: <span style="font-size: 14px;"><a href="http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.DataFrameStatFunctions" rev="en_rl_none">http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.DataFrameStatFunctions</a></span></div>
    <div>DataFrameNaFunctions <span style="font-size: 14px;"><a href="http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.DataFrameNaFunctions" rev="en_rl_none">http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.DataFrameNaFunctions</a></span></div>
    <div>Column methods: <span style="font-size: 14px;"><a href="http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Column" rev="en_rl_none">http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Column</a></span></div>
    <div><span style="font-size: 14px;">Functions: <a href="http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.functions$" rev="en_rl_none">http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.functions$</a></span></div>
    <div>Dataset: <span style="font-size: 14px;"><a href="http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Dataset" rev="en_rl_none">http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Dataset</a></span></div>
    <div><br /></div>
    <div><b><span style="font-size: 14px;">DataFrame used here =&gt; by-day/2010.12.01.csv</span></b></div>
    <table width="1582px" style="width:1582px;">
        <colgroup>
            <col style="width: 335px;" />
            <col style="width: 512px;" />
            <col style="width: 394px;" />
            <col style="width: 341px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">SQL</span></span></b></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">Python</span></span></b></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="color: rgb(0, 0, 0);">Scala</span></b></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="color: rgb(0, 0, 0);">Notes</span></b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div> </div>
                </td>
                <td>
                    <div style="margin-top:16px;">&gt;&gt;&gt; df = spark.read.format("csv")\</div>
                    <div><br /></div>
                    <div>... .option("header", "true")\</div>
                    <div><br /></div>
                    <div>... .option("inferSchema", "true")\</div>
                    <div><br /></div>
                    <div>... .load("/Users/mikepetridisz/Desktop/retail-data/by-day/2010-12-01.csv")</div>
                    <div><br /></div>
                    <div>&gt;&gt;&gt; df.printSchema()</div>
                    <div><br /></div>
                    <div>&gt;&gt;&gt; df.createOrReplaceTempView("dfTable")</div>
                    <div><br /></div>
                    <div> </div>
                    <div><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2010.05.39%20PM.png" height="502" width="1118" />
                    <div><br /></div>
                    <div style="margin-bottom:16px;"><br /></div>
                </td>
                <td>
                    <div><br /></div>
                </td>
                <td>
                    <div><b>Load data</b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div>no equivalent function necessary in SQL</div>
                </td>
                <td>
                    <div>from pyspark.sql.functions import lit</div>
                    <div>df.select(lit(5), lit("five"), lit(5.0))</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2010.11.53%20PM.png" height="128" width="650" />
                    <div><br /></div>
                </td>
                <td>
                    <div><span style="font-size: 14px;">import org.apache.spark.sql.functions.lit</span></div>
                    <div><span style="font-size: 14px;">df.select(lit(5), lit("five"), lit(5.0))</span></div>
                </td>
                <td>
                    <div>convert to spart types</div>
                    <div>convert native types to spark types.</div>
                    <div><br /></div>
                    <div>We do this by using the <b>lit</b> function</div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><br /></div>
                </td>
                <td>
                    <div>from pyspark.sql.functions import col</div>
                    <div>df.where(col("InvoiceNo") != 536365)\</div>
                    <div>.select("InvoiceNo", "Description")\</div>
                    <div>.show(5, False)</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2010.16.53%20PM.png" height="400" width="610" />
                    <div><br /></div>
                    <div> </div>
                    <div> </div>
                    <div><span style="font-size: 14px;">OR</span></div>
                    <div><span style="font-size: 14px;">df.where("InvoiceNo == 536365")\</span></div>
                    <div><span style="font-size: 14px;">.show(5, false)</span></div>
                </td>
                <td>
                    <div><span style="font-size: 14px;">df.where(col("InvoiceNo") === 536365)</span></div>
                    <div><span style="font-size: 14px;">.select("InvoiceNo", "Description")</span></div>
                    <div><span style="font-size: 14px;">.show(5, False)</span></div>
                </td>
                <td>
                    <div><b>Working with Booleans</b></div>
                    <div><span style="font-size: 14px;">Boolean statements consist of four elements: and, or, true, false</span></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><b>SELECT</b> * <b>FROM</b> dfTable <b>WHERE</b> StockCode <b>in</b> ("DOT") <b>AND</b> (UnitPrice &gt;600 <b>OR</b> <b>instr</b>(Description, "POSTAGE") &gt;= 1</div>
                </td>
                <td>
                    <div>from pyspark.sql.functions import instr</div>
                    <div>priceFilter = col("UnitPrice") &gt; 600</div>
                    <div>descripFilter = instr(df.Description, "POSTAGE") &gt;= 1</div>
                    <div>df.where(df.StockCode.isin("DOT")).where(priceFilter | descripFilter).show()</div>
                    <div><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2010.49.26%20PM.png" height="288" width="1422" />
                    <div><br /></div>
                </td>
                <td>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">val priceFilter = col("UnitPrice") &gt; 600</span></div>
                    <div><span style="font-size: 14px;">val descripFilter = col("Description").contains( "POSTAGE")</span></div>
                    <div><span style="font-size: 14px;">df.where(df.StockCode.isin("DOT")).where(priceFilter | descripFilter).show()</span></div>
                    <div> </div>
                </td>
                <td>
                    <div><br /></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div>SELECT UnitPrice, (StockCode = 'DOT' AND</div>
                    <div>(UnitPrice &gt; 600 OR instr(Description, "POSTAGE") &gt;= 1)) as isExpensive</div>
                    <div>FROM dfTable</div>
                    <div>WHERE (StockCode = 'DOT' AND</div>
                    <div>(UnitPrice &gt; 600 OR instr(Description, "POSTAGE") &gt;= 1))</div>
                </td>
                <td style="background-color:rgb(254, 222, 193);border-color:rgb(253, 175, 105);">
                    <div><span style="color: rgb(0, 0, 0);">from pyspark.sql.functions import instr</span></div>
                    <div><span style="color: rgb(0, 0, 0);">DOTCodeFilter = col("StockCode") == "DOT"</span></div>
                    <div><span style="color: rgb(0, 0, 0);">priceFilter = col("UnitPrice") &gt; 600</span></div>
                    <div><span style="color: rgb(0, 0, 0);">descripFilter = instr(col("Description"), "POSTAGE") &gt;= 1</span></div>
                    <div><span style="color: rgb(0, 0, 0);">df.withColumn("isExpensive", DOTCodeFilter &amp; (priceFilter | descripFilter))\</span></div>
                    <div><span style="color: rgb(0, 0, 0);">.where("isExpensive")\</span></div>
                    <div><span style="color: rgb(0, 0, 0);">.select("unitPrice", "isExpensive").show(5)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2010.56.23%20PM.png" height="432" width="1156" />
                    <div><br /></div>
                </td>
                <td>
                    <div><br /></div>
                </td>
                <td>
                    <div>To specify a DataFrame, you can also just specify a <b>Boolean column</b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.where(col("Description").eqNullSafe("hello")).show()</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.02.05%20PM.png" height="198" width="1206" />
                    <div><br /></div>
                </td>
                <td>
                    <div><span style="font-size: 14px;">df.where(col("Description").eqNullSafe("hello")).show()</span></div>
                </td>
                <td>
                    <div><b>Null safe equivalence test:</b></div>
                    <div>df.where(col("Description").eqNullSafe("hello")).show()</div>
                    <div><br /></div>
                    <div>if there is a null in the data, we need to treat things differently. the above example shows how we can tackle it.</div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><b><span style="font-size: 14px;">Working with Numbers</span></b></div>
    <div><span style="font-size: 14px;">after filtering the most common thing in big data is counting things. </span></div>
    <table width="1559px" style="width:1559px;">
        <colgroup>
            <col style="width: 464px;" />
            <col style="width: 516px;" />
            <col style="width: 315px;" />
            <col style="width: 264px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">SQL</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Python</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Scala</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Note</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT customerId, (POWER((Quantity * UnitPrice), 2.0) +5) as realQuantity FROM dfTable</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>from pyspark.sql.functions import pow, expr</div>
                    <div>fabricatedQuantity = pow(col("Quantity") * col("UnitPrice"), 2) +5</div>
                    <div>df.select(expr("CustomerId"), fabricatedQuantity.alias("realQuantity")).show(2)</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.09.26%20PM.png" height="300" width="1206" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>val <span style="font-size: 14px;">fabricatedQuantity = pow(col("Quantity") * col("UnitPrice"), 2) +5</span></div>
                    <div><span style="font-size: 14px;">df.select(expr("CustomerId"), fabricatedQuantity.alias("realQuantity")).show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Let's imagine that we found out that we misrecorded the quantity in our retail dataset and the true quantity is equal to the <b>((current quantity * the unit price)^2 +5)</b></div>
                    <div> </div>
                    <div><b>pow function (</b>raises a column to the expressed power</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT round (2.5), bround(2.5)</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">from pyspark.sql.functions import lit, round, bround</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">df.select(round(lit("2.5")), bround(lit("2.5"))).show(2)</span></span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.18.07%20PM.png" height="234" width="848" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>import org.apache.spark.functions.lit</div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">df.select(round(lit("2.5")), bround(lit("2.5"))).show(2)</span></span></div>
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Rounding</b></div>
                    <div>example round to 1 decimal places</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT corr(Quantity, UnitPrice) FROM dfTable</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import corr</span></div>
                    <div><span style="font-size: 14px;">df.stat.corr("Quantity", "UnitPrice")</span></div>
                    <div><span style="font-size: 14px;">df.select(corr("Quantity", "UnitPrice")).show()</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.24.40%20PM.png" height="256" width="738" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">import org.apache.spark.functions.{corr}</span></div>
                    <div><span style="font-size: 14px;">df.stat.corr("Quantity", "UnitPrice")</span></div>
                    <div><span style="font-size: 14px;">df.select(corr("Quantity", "UnitPrice")).show()</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Compute the <b>correlation</b> of two columns. e.g to see if cheaper things are typically bought in greater quantities. </div>
                    <div><br /></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.describe().show()</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.27.27%20PM.png" height="302" width="1974" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.describe().show()</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Summary Statistics for a column or a set of columns. </div>
                    <div><br /></div>
                    <div><b>describe </b>method. This takes all numeric columns and calculate the count, mean, standard deviation, min, max.</div>
                    <div>You should use this for viewing the console because the schema might change in the future.</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>from pyspark.sql.functions import <b>count, mean, stddev_pop, min, max</b></div>
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>if you need exact numbers you can also perform this aggregation yourself by importing the functions and applying them to the columns that you need.</div>
                    <div><br /></div>
                    <div>These are the statistical functions available in the StatFunctions Package. </div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="background-color:rgb(254, 222, 193);border-color:rgb(253, 175, 105);">
                    <div><span style="color: rgb(0, 0, 0);">colName = "UnitPrice"</span></div>
                    <div><span style="color: rgb(0, 0, 0);">quantileProbs = [0.5]</span></div>
                    <div><span style="color: rgb(0, 0, 0);">relError = 0.05</span></div>
                    <div><span style="color: rgb(0, 0, 0);">df.stat.approxQuantile("UnitPrice", quantileProbs, relError)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.32.04%20PM.png" height="152" width="926" />
                    <div><br /></div>
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">val colName = "UnitPrice"</span></div>
                    <div><span style="font-size: 14px;">val quantileProbs = [0.5]</span></div>
                    <div><span style="font-size: 14px;">val relError = 0.05</span></div>
                    <div><span style="font-size: 14px;">df.stat.approxQuantile("UnitPrice", quantileProbs, relError)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>You can calculate exact or approximate quantiles of your data using the <b>approxQuantile</b> method.</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.stat.crosstab("StockCode", "Quantity").show()</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.33.58%20PM.png" height="1330" width="1912" />
                    <div><br /></div>
                    <div> </div>
                    <div><span style="font-size: 14px;">df.stat.freqItems(["StockCode", "Quantity"]).show()</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.35.47%20PM.png" height="244" width="802" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.stat.crosstab("StockCode", "Quantity").show()</div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div> </div>
                    <div><span style="font-size: 14px;">df.stat.freqItems(["StockCode", "Quantity"]).show()</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>cross-tabulation or frequent item pairs </div>
                    <div>this output will be large!!!!!</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>from pyspark.sql.functions import monotonically_increasing_id </div>
                    <div><span style="font-size: 14px;">df.select(monotonically_increasing_id()).show(2)</span></div>
                    <div> </div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.38.21%20PM.png" height="264" width="936" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.select(monotonically_increasing_id()).show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Add unique ID to reach Row by using</div>
                    <div><b>monotonically_increasing_id </b>function</div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><br /></div>
    <div><b><span style="font-size: 14px;">Working with Strings</span></b></div>
    <table width="1582px" style="width:1582px;">
        <colgroup>
            <col style="width: 335px;" />
            <col style="width: 512px;" />
            <col style="width: 394px;" />
            <col style="width: 341px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">SQL</span></span></b></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">Python</span></span></b></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="color: rgb(0, 0, 0);">Scala</span></b></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="color: rgb(0, 0, 0);">Notes</span></b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div> SELECT initcap(Description) FROM dfTable</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import initcap</span></div>
                    <div><br /></div>
                    <div><span style="font-size: 14px;">df.select(initcap(col("Description"))).show()</span></div>
                    <div><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.50.33%20PM.png" height="770" width="720" />
                    <div><br /></div>
                    <div style="margin-bottom:16px;"><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.select(initcap(col("Description"))).show(2, false)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>initcap - </b>capitalize every word in a given string when that word is separated from another by a space</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT Description, lower(Description), Ipper(lower(Description)) FROM dfTable</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import lower, upper</span></div>
                    <div><span style="font-size: 14px;">df.select(col("Description"),</span></div>
                    <div><span style="font-size: 14px;">lower(col("Description")),</span></div>
                    <div><span style="font-size: 14px;">upper(lower(col("Description")))).show(2)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.55.15%20PM.png" height="328" width="986" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>cast string in <b>uppercase / lowercase</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">SELECT</span></div>
                    <div><span style="font-size: 14px;">ltrim(lit('     HELLOOOOO     '),</span></div>
                    <div><span style="font-size: 14px;">rtrim(lit('     HELLOOOOO     '), </span></div>
                    <div><span style="font-size: 14px;">lpad(lit(' HELLOOOOO     '),2, ' ')</span></div>
                    <div><span style="font-size: 14px;">FROM dfTable</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import lit, trim, ltrim, rtrim, lpad, rpad</span></div>
                    <div><span style="font-size: 14px;">df.select(</span></div>
                    <div><span style="font-size: 14px;">ltrim(lit("     HELLOOOOO     ")).alias("ltrim"),</span></div>
                    <div><span style="font-size: 14px;">rtrim(lit("     HELLOOOOO     ")).alias("rtrim"),</span></div>
                    <div><span style="font-size: 14px;">trim(lit("     HELLOOOOO     ")).alias("trim"),</span></div>
                    <div><span style="font-size: 14px;">lpad(lit("HELLOOOOO     "),2, " ").alias("lpad"),</span></div>
                    <div><span style="font-size: 14px;">rpad(lit("HELLOOOOO"), 10, "").alias("rpad")).show(2)</span></div>
                    <div> </div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%2012.02.30%20AM.png" height="404" width="1052" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">import....</span></div>
                    <div> </div>
                    <div><span style="font-size: 14px;">df.select(</span></div>
                    <div><span style="font-size: 14px;">ltrim(lit("     HELLOOOOO     ")).alias("ltrim"),</span></div>
                    <div><span style="font-size: 14px;">rtrim(lit("     HELLOOOOO     ")).alias("rtrim"),</span></div>
                    <div><span style="font-size: 14px;">trim(lit("     HELLOOOOO     ")).alias("trim"),</span></div>
                    <div><span style="font-size: 14px;">lpad(lit("HELLOOOOO     "),2, " ").alias("lpad"),</span></div>
                    <div><span style="font-size: 14px;">rpad(lit("HELLOOOOO"), 10, "").alias("rpad")).show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Adding/removing spaces around a string</div>
                    <div><b>lpad</b></div>
                    <div><b>ltrim</b></div>
                    <div><b>rpad</b></div>
                    <div><b>rtrim</b></div>
                    <div><b>trim</b></div>
                    <div> </div>
                    <div>If lpad and rpad takes a number less than the length of the string it will always remove values from the right side of the string</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>regex_replace(Description, 'BLACK|WHITE|RED|BLUE', 'COLOR') as color)clean, Description</div>
                    <div>FROM dfTable</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import regexp_replace</span></div>
                    <div> </div>
                    <div><span style="font-size: 14px;">regex_string = "BLACK|WHITE|RED|BLUE"</span></div>
                    <div><span style="font-size: 14px;">df.select(</span></div>
                    <div><span style="font-size: 14px;">regexp_replace(col("Description"), regex_string, "COLOR").alias("color_clean"),</span></div>
                    <div><span style="font-size: 14px;"> col("Description")).show(2)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%2012.27.46%20AM.png" height="358" width="1154" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Regular Expressions</b></div>
                    <div>-replacing all mentions of a string with another value</div>
                    <div>-searching for the existence of one string</div>
                    <div>This is done with a tool called <i>regular expressions (</i><b><i>regexes)</i></b></div>
                    <div>used to extract values from a string or replace them with some other values</div>
                    <div><b>regexo_extract</b></div>
                    <div><b>regexp_replace</b></div>
                    <div> </div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT translate(Description, 'LEET', '1337'), Description FROM dfTable</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import translate</span></div>
                    <div><span style="font-size: 14px;">df.select(translate(col("Description"), "LEET", "1337"), col("Description")).show(2)</span></div>
                    <div> </div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%2012.32.17%20AM.png" height="310" width="1190" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import translate</span></div>
                    <div><span style="font-size: 14px;">df.select(translate(col("Description"), "LEET", "1337"), col("Description")).show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Replacing given characters with other characters</div>
                    <div><b><span style="font-size: 14px;">translate</span></b><span style="font-size: 14px;"> function</span></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT regexp_extract(Description, 'BLACK|WHITE|RED|BLUE)', 1),</div>
                    <div>Description FROM dfTable</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import regexp_extract</span></div>
                    <div><span style="font-size: 14px;">extract_str ="(BLACK|WHITE|RED|BLUE)"</span></div>
                    <div><span style="font-size: 14px;">df.select(</span></div>
                    <div><span style="font-size: 14px;">regexp_extract(col("Description"), extract_str, 1).alias("color_clean"),</span></div>
                    <div><span style="font-size: 14px;">  col("Description")).show(2)</span></div>
                    <div> </div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%2012.36.48%20AM.png" height="364" width="1086" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>pull out the <b>first mentioned </b>color</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT  Description FROM dfTable</div>
                    <div>WHERE instr(Description, 'BLACK') &gt;= OR instr(Description, 'WHITE') &gt;= 1</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import instr</span></div>
                    <div><span style="font-size: 14px;">containsBlack = instr(col("Description"), "BLACK") &gt;=1</span></div>
                    <div><span style="font-size: 14px;">containsWhite = instr(col("Description"), "WHITE") &gt;=1</span></div>
                    <div><span style="font-size: 14px;">df.withColumn("hasSimpleColor", containsBlack | containsWhite)\</span></div>
                    <div><span style="font-size: 14px;">.where("hasSimpleColor")\</span></div>
                    <div><span style="font-size: 14px;">.select("Description").show(3, False)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%2012.42.05%20AM.png" height="414" width="968" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>contains method</b></div>
                    <div>check for values existence - this will return a Boolean</div>
                    <div><b>instr</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="background-color:rgb(254, 222, 193);border-color:rgb(253, 175, 105);">
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">from pyspark.sql.functions import expr, locate</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">simpleColors = ["black", "white", "red", "green", "blue"]</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">def color_locator(column, color_string):</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">  return locate(color_string.upper(), column)\</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">.cast("boolean")\</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">.alias("is_" + c)</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">selectedColumns = [color_locator(df.Description, c) for c in simpleColors]</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">selectedColumns.append(expr("*"))</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">df.select(*selectedColumns).where(expr("is_white OR is_red"))\</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">.select("Description").show(3, False)</span></span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>problem</div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><br /></div>
    <div><b><span style="font-size: 14px;">Working with Dates and Timestamps</span></b></div>
    <div><span style="font-size: 14px;">Dates - focus exclusively on calendar dates</span></div>
    <div><span style="font-size: 14px;">timestamps - both date and time information included</span></div>
    <div> </div>
    <div><span style="font-size: 14px;">TimeStampType class supports only second-level precision, which means that if you are going to be working with milliseconds or microseconds you will need to work around this problem by potentially operating on them as </span><b><span style="font-size: 14px;">longs,</span></b></div>
    <div><span style="font-size: 14px;">Important to be explicit when parsing or converting to ensure that there are no issues in doing so.</span></div>
    <div><span style="font-size: 14px;">Conforms to java standards when working with dates and timestamps.</span></div>
    <table width="1547px" style="width:1547px;">
        <colgroup>
            <col style="width: 386px;" />
            <col style="width: 512px;" />
            <col style="width: 281px;" />
            <col style="width: 368px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">SQL</span></span></b></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">Python</span></span></b></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="color: rgb(0, 0, 0);">Scala</span></b></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="color: rgb(0, 0, 0);">Notes</span></b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import current_date, current_timestamp</span></div>
                    <div><span style="font-size: 14px;">dateDF = spark.range(10)\</span></div>
                    <div><span style="font-size: 14px;">.withColumn("today", current_date())\</span></div>
                    <div><span style="font-size: 14px;">.withColumn("now", current_timestamp())</span></div>
                    <div><span style="font-size: 14px;">dateDF.createOrReplaceTempView("dataTable")</span></div>
                    <div><span style="font-size: 14px;">dateDF.printSchema()</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%201.08.00%20AM.png" height="502" width="1152" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT date_sub(today, 5), date_add(today_5) FROM dateTable</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import date_add, date_sub</span></div>
                    <div><span style="font-size: 14px;">dateDF.select(date_sub(col("today"),5), date_add(col("today"), 5)).show(1)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%201.11.03%20AM.png" height="450" width="1322" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Now <b>subtract five days from today</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT to_date('2016-01-01'), months_between('2016-01-01', '2017-01-01'),</div>
                    <div>datediff('2016-01-01', '2017-01-01')</div>
                    <div>FROM dateTable</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import datediff, months_between, to_date</span></div>
                    <div><span style="font-size: 14px;">dateDF.withColumn("week_ago", date_sub(col("today"),7))\</span></div>
                    <div><span style="font-size: 14px;">.select(datediff(col("week_ago"), col("today"))).show(1)</span></div>
                    <div><span style="font-size: 14px;">dateDF.select(</span></div>
                    <div><span style="font-size: 14px;">to_date(lit("2016-01-01")).alias("start"),</span></div>
                    <div><span style="font-size: 14px;"> to_date(lit("2017-05-22")).alias("end"))\</span></div>
                    <div><span style="font-size: 14px;">.select(months_between(col("start"), col("end"))).show(1)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%201.18.24%20AM.png" height="928" width="1174" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Difference between two dates</b></div>
                    <div><b>datediff </b>function</div>
                    <div>it will return the number of days in between two dates</div>
                    <div><br /></div>
                    <div><b>to_date </b>function - allows you to convert a string to a date, optionally with a specified format. </div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import to_date, lit</span></div>
                    <div><span style="font-size: 14px;">spark.range(5).withColumn("date", lit("2017-01-01"))\</span></div>
                    <div><span style="font-size: 14px;">.select(to_date(col("date"))).show(1)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%201.22.22%20AM.png" height="540" width="970" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>if Spark cannot parse the date it will return <b>null</b></div>
                    <div><span style="font-size: 14px;">tricky situation for bugs because some data might match the correct format. </span></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">dateDF.select(to_date(lit("2016-20-12")), to_date(lit("2017-12-11"))).show(1)</span></div>
                    <div> </div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%201.24.58%20AM.png" height="468" width="1360" />
                    <div><br /></div>
                    <div> </div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Notice that this date appears as Dec 11 instead of the correct day Nov 12. Spark doesn't throw an error because it cannot know whether the days are mixed up or that specific row is incorrect.</div>
                    <div><br /></div>
                    <div><b>Let's fix this pipeline! </b></div>
                    <div><b>---&gt;</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT to_date(date, 'yyyy-dd-MM'), to_date(date2, 'yyyy-dd-MM'), to_date(date) FROM dataTable2</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import to_date</span></div>
                    <div><span style="font-size: 14px;">dateFormat = "yyyy-dd-MM"</span></div>
                    <div><span style="font-size: 14px;">cleanDateDF = spark.range(1).select(</span></div>
                    <div><span style="font-size: 14px;">to_date(lit("2017-12-11"), dateFormat).alias("date"),</span></div>
                    <div><span style="font-size: 14px;">  to_date(lit("2017-20-12"), dateFormat).alias("date2"))</span></div>
                    <div><span style="font-size: 14px;">cleanDateDF.createOrReplaceTempView("dateTable2")</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>---&gt;</div>
                    <div>The first step is to remember that we need to specify our date format according to the Java SimpleDateFormat standard.</div>
                    <div>We use two functions:</div>
                    <div>to_date</div>
                    <div>to_timestamp</div>
                    <div>the former optionally expects a format whereas the latter requires one.</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT to)timestamp(date, 'yyyy-dd-MM'), to_timestamp(date2, 'yyyy-dd-MM') FROM dateTable2</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import to_timestamp</span></div>
                    <div><span style="font-size: 14px;">cleanDateDF.select(to_timestamp(col("date"), dateFormat)).show()</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%201.35.06%20AM.png" height="408" width="1136" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>to_timestamp</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">cleanDateDF.filter(col("date2") &gt; "'2017-12-12'").show()</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%201.38.47%20AM.png" height="358" width="982" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>after we have our date or timestamp into the correct format and type comparing between them is easy. We just need to make sure that either use a date/timestamp type or specify our string according to the right format of yyyy-MM-dd if we are comparing a date</div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><br /></div>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">Working with Nulls in Data</span></b></div>
    <div><span style="font-size: 14px;">you should always use null to represent missing or empty data in your DataFrames. Spark can optimize working with null values more than it can if you use empty strings or other values.</span></div>
    <div><span style="font-size: 14px;">use the </span><b><span style="font-size: 14px;">.nasubpackage</span></b><span style="font-size: 14px;"> on a DataFrame</span></div>
    <div> </div>
    <div> </div>
    <div><b><span style="font-size: 12px;"><i><span style="color: rgb(255, 0, 42);">Fundamental concepts:</span></i></span></b></div>
    <div><b><span style="font-size: 12px;"><i>Spark is a distributed programming model in which the user specifies transformations. These transformations build up a directed acyclic graph of transformations and action. An action begins the process of execution that graph of instructions, as a single job, by breaking it down into stages and tasks to execute across the cluster. The logical structures that we manipulate with transformations and actions are DataFrames and Datasets. To create a new DataFrame or Dataset, you call a transformation. To start computation or convert to native language types, you call an action.</i></span></b></div>
    <div> </div>
    <div><b><span style="font-size: 12px;">Structured API Overview</span></b></div>
    <div><span style="font-size: 12px;">Structured APIs are a tool for manipulating all sorts of data, from unstructured log files to semi-structured CSV files and highly structured Parquet <i>(Apache Parquet is a columnar storage format available to any project in the Hadoop ecosystem, regardless of the choice of data processing framework, data model or programming language)</i> files. These APIs refer to three core types of distributed collection APIs:</span></div>
    <ol>
        <li>
            <div><span style="font-size: 12px;">Datasets</span></div>
        </li>
        <li>
            <div><span style="font-size: 12px;">DataFrames</span></div>
        </li>
        <li>
            <div><span style="font-size: 12px;">SQL Tables and Views</span></div>
        </li>
    </ol>
    <div><span style="font-size: 12px;">Majority of the Structured APIs apply to both </span><b><span style="font-size: 12px;"><i>batch</i></span></b><span style="font-size: 12px;"> and </span><b><span style="font-size: 12px;"><i>streaming</i></span></b><span style="font-size: 12px;"> computation. This means that when you work with the Structured APIs, it should be simple to migrate from batch to streaming or vice versa with little to no effort.  </span><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">Structured APIs are the fundamental abstraction used to write the majority of data flows. </span></span></div>
    <div> </div>
    <div><b><span style="font-size: 12px;">DataFrames and Datasets</span></b></div>
    <div><span style="font-size: 12px;">DataFrames and Datasets are </span><b><span style="font-size: 12px;">distributed</span></b><span style="font-size: 12px;"> table-like collection with well-defined rows and columns. Each column must have the same number of rows as all the other columns although you can use null to specify the absence of a value and </span><b><span style="font-size: 12px;">each column has type information</span></b><span style="font-size: 12px;"> that must be consistent for every row in the collection. To Spark, DataFrames and Datasets represent </span><b><span style="font-size: 12px;">immutable</span></b><span style="font-size: 12px;">, </span><b><span style="font-size: 12px;">lazily evaluated plans(</span></b><span style="font-size: 12px;">transformations</span><b><span style="font-size: 12px;">) </span></b><span style="font-size: 12px;">that specify what operations to apply to data residing at a location to generate some output. When we perform an action on a DataFrame, we instruct Spark to perform the actual transformations and return the results. These represent plans of how to manipulate rows and columns to compute the user's desired result. </span></div>
    <div> </div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Tables and views</span> </span></b><span style="font-size: 12px;">- like a DataFrame, but we execute SQL against them instead of DataFrame code. </span></div>
    <div> </div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Schema</span></span></b><span style="font-size: 12px;"> - defines the column names and types of a DataFrame. You can define schemas manually or read a schema from a data source. Schemas consist of types meaning that you need a way of specifying what lies where.</span></div>
    <div> </div>
    <div><b><span style="font-size: 12px;">Overview of Structured Spark Types</span></b></div>
    <div><span style="font-size: 12px;">Spark is effectively a programming language of its own. </span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">Spark</span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"> uses an </span></span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">engine</span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"> called </span></span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">Catalyst</span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">.</span></span></div>
    <div> </div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Catalyst - </span></span></b><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">maintains its own type information through the planning and processing of work. This opens up execution optimizations.</span></span></div>
    <div><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Even if we use Spark's Structured APIs from Python or R, the majority of our manipulations will operate strictly on Spark types not Python types. </span></span></div>
    <div> </div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2012.36.16%20AM.png" height="90" width="568" />
    <div><br /></div>
    <div> </div>
    <div><span style="font-size: 12px;">This addition operation happens because Spark will convert an expression written in an input language to Spark's internal Catalyst representation of that same type information. It then will operate on that internal representation. </span></div>
    <div> </div>
    <div><b><span style="font-size: 12px;">DataFrames VS Datasets</span></b></div>
    <table width="937px" style="width:937px;">
        <colgroup>
            <col style="width: 471px;" />
            <col style="width: 466px;" />
        </colgroup>
        <tbody>
            <tr>
                <td colspan="2" style="background-color:rgb(254, 222, 193);border-color:rgb(253, 175, 105);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">STRUCTURED APIs</span></span></b></div>
                </td>
            </tr>
            <tr>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">DataFrames</span></span></b></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">Datasets</span></span></b></div>
                </td>
            </tr>
            <tr>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="color: rgb(0, 0, 0);">untyped</span></b></div>
                    <div style="text-align:center;"><span style="color: rgb(0, 0, 0);">(Spark maintains them completely)</span></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="color: rgb(0, 0, 0);">typed</span></b></div>
                    <div style="text-align:center;"><span style="color: rgb(0, 0, 0);">(checks whether types conform to the specification at compile time.)</span></div>
                    <div style="text-align:center;"><span style="color: rgb(0, 0, 0);">Only available to JVM based languages Scala and Java.</span></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">DataFrames are Datasets of Type </span><i><span style="color: rgb(255, 0, 42);">Row</span></i><span style="color: rgb(255, 0, 42);">. </span></span></b></div>
    <div><span style="font-size: 12px;">The "Row" type is Spark's internal representation of its optimized in-memory format for computation. </span></div>
    <div><span style="font-size: 12px;">To Spark in Python and R there is no such thing as a Dataset, everything is a DataFrame and therefore we always operate on that optimized format.</span></div>
    <div> </div>
    <div><b><span style="font-size: 12px;"><i>//WATCH! - Spark Catalyst Engine talks by Josh Rosen and Herman van Hovell</i></span></b></div>
    <div><br /></div>
    <div>KEY Takeaway: When you use DataFrames, you are taking advantage of Spark's optimized internal format.</div>
    <div><br /></div>
    <div><b>Columns: </b>represent a simple type like an integer or string or complex type like an array or map or null values. </div>
    <div><b>Rows</b>: record of data.</div>
    <div> </div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2012.53.06%20AM.png" height="94" width="448" />
    <div><br /></div>
    <div><br /></div>
    <div><b>Spark Types</b></div>
    <div>(Spark documentation - get updated time to time)</div>
    <div><br /></div>
    <div><b>Overview of Structured API Execution</b></div>
    <ol>
        <li>
            <div>Write DataFrame/Dataset/SQL Code</div>
        </li>
        <li>
            <div><span style="font-size: 14px;">If valid code, converts this to a Logical Plan</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Spark . transforms this Logical Plan, checking for optimizations along the way</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Spark then executes this Physical Plan (RDD Manipulations) on the cluster</span></div>
        </li>
    </ol>
    <div><br /></div>
    <div>The code we write gets submitted to Spark either through console or via a submitted job. This <b>code passes through the Catalyst Optimize</b>r, which decides how the code should be executed and lays out a plan for doing so before, finally, the code is run and the result is returned to the user.</div><img src="Spark%20Overview.html.resources/spdg_0401.png" height="523" width="1014" />
    <div><br /></div>
    <table width="1600px" style="width:1600px;">
        <colgroup>
            <col style="width: 803px;" />
            <col style="width: 797px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Logical Planning</span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Physical Planning</span></b></div>
                    <div style="text-align:center;"> </div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><span style="font-size: 14px;">The first phase takes user code and converts it into a logical plan (optimized version of the user's set of expressions)</span></div>
                    <div><span style="font-size: 14px;">It does this by converting user code into an </span><b><span style="font-size: 14px;"><i>unresolved logical plan. </i></span></b><span style="font-size: 14px;">The plan is unresolved because although your code might be valid, the tables and columns that it refers to might or might not exist. Spark uses the catalog, a repository of all table and DataFrame information to </span><b><span style="font-size: 14px;"><i>resolve</i></span></b><span style="font-size: 14px;"> columns and tables in the </span><b><span style="font-size: 14px;"><i>analyzer. </i></span></b><span style="font-size: 14px;">The analyzer might reject the unresolved logical plan if the required column name does not exist in the catalog. If the analyzer can resolve it, the result is passed through the Catalyst Optimizer, a collection of rules that attempt to optimize the logical plan by pushing down predicates or selections. Packages can extend the Catalyst to include their own rules for domain-specific optimizations.</span></div><img src="Spark%20Overview.html.resources/spdg_0402.png" height="343" width="1250" />
                    <div><br /></div>
                </td>
                <td>
                    <div>After creating the optimized logical plan, Spark begins the physical planning process. The physical plan - often called SPark plan - specifies how the logical plan will execute on the cluster by generating different physical execution strategies and comparing them through a cost model. Upon selecting a physical plan Spark runs all of this code over RDDs.</div><img src="Spark%20Overview.html.resources/spdg_0403.png" height="449" width="1367" />
                    <div><br /></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><b><span style="font-size: 12px;">Basic Structured Operations</span></b></div>
    <div><span style="font-size: 12px;">DataFrame consists of a series of records that are of type <i>Row</i> and a number of columns that represent a computation expression that can perform on each individual record in the Dataset. </span><b><span style="font-size: 12px;"><i>Schemas</i></span></b><span style="font-size: 12px;"> define the name as well as the type of data in each column. </span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><i>Partitioning</i></span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><i> </i>of the DataFrame defines the layout of the DataFrame or Dataset's physical distribution across the cluster. The </span></span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><i>partitioning scheme</i></span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"> defines how that is allocated.</span></span></div>
    <div><br /></div>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Creating a DataFrame:</span></span></span></b></div>
    <table width="913px" style="width:913px;">
        <colgroup>
            <col style="width: 446px;" />
            <col style="width: 467px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">Python</span></span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">Scala</span></span></b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">df = spark.read.format("json").load("/Users/mikepetridisz/Desktop/json/2015-summary.json")</span></span></b></div>
                </td>
                <td>
                    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">val df = spark.read.format("json").load("/Users/mikepetridisz/Desktop/json/2015-summary.json")</span></span></b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">printSchema</span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">df.printSchema()</span></span></div>
                    <div> </div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"># A schema is a StructType made up of a number of fields, StructFields, that have a name, type, a boolean flag (null values/missing values), metadata (metadata used in Machine Learning)</span></span></div>
                </td>
                <td>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">printSchema</span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">df.printSchema()</span></span></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;&lt;br&gt;</span></div>
                    <div><br /></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"> </span></span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">myManualScheme</span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"> = StructType([</span></span></div>
                    <div><br /></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">... StructField("DEST_COUNTRY_NAME", StringType(), True),</span></span></div>
                    <div><br /></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">... StructField("ORIGIN_COUNTRY_NAME", StringType(), True),</span></span></div>
                    <div><br /></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">... StructField("count", LongType(), False, metadata={"hello":"world"})</span></span></div>
                    <div><br /></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">... ])</span></span></div>
                    <div><br /></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">&gt;&gt;&gt; df = spark.read.format("json").schema(myManualScheme)\</span></span></div>
                    <div><br /></div>
                    <div style="margin-bottom:16px;"><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">... .load("/Users/mikepetridisz/Desktop/json/2015-summary.json")</span></span></div>
                </td>
                <td>
                    <div> </div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">Columns and Expressions</span></span></b></div>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><i>Expressions</i></span></span></b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"> - when you select, remove manipulate columns from DataFrames</span></span></div>
    <div><br /></div>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Creating a Column</span></span></span></b></div>
    <table width="1588px" style="width:1588px;">
        <colgroup>
            <col style="width: 769px;" />
            <col style="width: 620px;" />
            <col style="width: 199px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Python</span></span></span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Scala</span></span></span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">NOTE</span></b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">from pyspark.sql.functions import cal, column</span></span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">col("someColumnName")</span></span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">column("someColumnName")</span></span></span></div>
                </td>
                <td>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">import org.apache.spark.sql.functions.{col, column}</span></span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">col("someColumnName")</span></span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">column("someColumnName")</span></span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">--</span></span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">other way:</span></span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">scala&gt; $"myColumn"</span></span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">scala&gt;'myColumn</span></span></span></div>
                </td>
                <td>
                    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><i><span style="color: rgb(0, 0, 0);">col()  or column function</span></i></span></span></b></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><b><span style="font-size: 12px;">Explicit Column References </span></b></div>
    <div><span style="font-size: 12px;">if you need to refer to a specific DataFrame's column, you can use the col method on the specific DataFrame. This can be useful when performing a join and need to refer to a specific column in one DataFrame that might share the same name with another column in the joined DataFrame.</span></div>
    <div> </div>
    <div><b><span style="font-size: 12px;">Expressions</span></b></div>
    <div><span style="font-size: 12px;">Columns are expressions. An expression is a set of transformations on one or more values in a record in a DataFrame. </span></div>
    <div><span style="font-size: 12px;">An expression created via the expr function is just a DataFrame column reference.</span></div>
    <div><span style="font-size: 12px;"><i>expr("someCol") is equivalent to </i></span><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><i>col("someCol")</i></span></span></div>
    <div> </div>
    <div><b><span style="font-size: 12px;">Columns as Expressions</span></b></div>
    <div><span style="font-size: 12px;">When using an expression, the expr function can actually parse transformations and column references from a string and can subsequently be passed into further transformations.</span></div>
    <div><span style="font-size: 12px;"><i>Key takeaways:</i></span></div>
    <ul>
        <li>
            <div><span style="font-size: 12px;">Columns are just expressions</span></div>
        </li>
        <li>
            <div><span style="font-size: 12px;">Columns and transformations of those columns compile to the same logical plan as parsed expressions.</span></div>
        </li>
    </ul>
    <div><span style="font-size: 12px;"><i>Example:</i></span></div>
    <div><span style="font-size: 12px;"><i>DataFrame Code</i></span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%202.55.57%20AM.png" height="96" width="818" />
    <div><br /></div>
    <div><span style="font-size: 12px;"><i>SQL code</i></span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%202.59.18%20AM.png" height="96" width="836" />
    <div><br /></div>
    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">#You can write expressions as DataFrame code or SQL code and get the exact same performance characteristics.</span></span></div>
    <div><br /></div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Accessing a DataFrame's Columns</span></span></b></div>
    <div>printSchema or:</div>
    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;">spark.read.format("json").load("/Users/mikepetridisz/Desktop/json/2015-summary.json")</span></span><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">.columns</span></span></span></b></div>
    <div> </div>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Records and Rows</span></span></span></b></div>
    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Each row in a DataFrame is a single </span></span></span></div>
    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">record as an object type Row. </span></span></span></div>
    <div><span style="font-size: 12px;"><span style="color: rgb(0, 0, 0);">Spark manipulates Row objects using column expressions in order to produce usable values. </span></span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%203.04.44%20AM.png" height="72" width="1310" />
    <div><br /></div>
    <div><br /></div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Creating Rows</span></span></b></div>
    <table width="1834px" style="width:1834px;">
        <colgroup>
            <col style="width: 544px;" />
            <col style="width: 645px;" />
            <col style="width: 645px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Python</span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Scala</span></b></div>
                </td>
                <td>
                    <div>Note</div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><span style="font-size: 14px;">from pyspark.sql import Row</span></div>
                    <div><span style="font-size: 14px;">myRow = Row("Hello", None, 1, False)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%203.07.45%20AM.png" height="178" width="646" />
                    <div><br /></div>
                </td>
                <td>
                    <div><span style="font-size: 14px;">import org.apache.spark.sql.Row</span></div>
                    <div><span style="font-size: 14px;">val myRow = Row("Hello", null, 1, false)</span></div>
                </td>
                <td>
                    <div>Creating Rows</div>
                    <div>Importing Rows</div>
                    <div><span style="font-size: 14px;">Accessing data in rows </span></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">DataFrame Transformations</span></span></span></b></div>
    <ol>
        <li>
            <div><span style="font-size: 12px;">We can add rows or columns</span></div>
        </li>
        <li>
            <div><span style="font-size: 12px;">We can remove rows and columns</span></div>
        </li>
        <li>
            <div><span style="font-size: 12px;">We can transform a row into a column or vice versa</span></div>
        </li>
        <li>
            <div><span style="font-size: 12px;">We can change the order of rows based on the values in columns</span></div>
        </li>
    </ol>
    <div> </div>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Creating DataFrames on the fly</span></span></b></div>
    <table width="1152px" style="width:1152px;">
        <colgroup>
            <col style="width: 530px;" />
            <col style="width: 622px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Python</span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Scala</span></b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><span style="font-size: 14px;">from pyspark.sql import Row</span></div>
                    <div><span style="font-size: 14px;">from pyspark.sql.types import StructField, StructType, StringType, LongType</span></div>
                    <div> </div>
                    <div><span style="font-size: 14px;">myManualSchema = StructType([</span></div>
                    <div><span style="font-size: 14px;">StructField("some", StringType(), True),</span></div>
                    <div><span style="font-size: 14px;">StructField("col", StringType(), True),</span></div>
                    <div><span style="font-size: 14px;">StructField("names", LongType(), False)</span></div>
                    <div><span style="font-size: 14px;">])</span></div>
                    <div><span style="font-size: 14px;">myRow = ("hello", None, 1)</span></div>
                    <div><span style="font-size: 14px;">myDf = spark.createDataFrame([myRow], myManualSchema)</span></div>
                    <div><span style="font-size: 14px;">myDf.show()</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%203.17.57%20AM.png" height="544" width="1174" />
                    <div><br /></div>
                    <div> </div>
                    <div> </div>
                </td>
                <td>
                    <div><span style="font-size: 14px;">import org.apache.spark.sql.Row</span></div>
                    <div><span style="font-size: 14px;">import org.apache.spark.sql.types.{ StructField, StructType, StringType, LongType}</span></div>
                    <div> </div>
                    <div><span style="font-size: 14px;">val myManualSchema = new StructType(Array(</span></div>
                    <div><span style="font-size: 14px;">new StructField("some", StringType, true),</span></div>
                    <div><span style="font-size: 14px;">new StructField("col", StringType, true),</span></div>
                    <div><span style="font-size: 14px;">new StructField("names", LongType, false)))</span></div>
                    <div><span style="font-size: 14px;">val myRow = Seq(Row("hello", None, 1L))</span></div>
                    <div><span style="font-size: 14px;">val myRDD = spark.sparkContext.parallelize(myRows)</span></div>
                    <div><span style="font-size: 14px;">val myDf = spark.createDataFrame(myRDD, myManualSchema)</span></div>
                    <div><span style="font-size: 14px;">myDf.show()</span></div>
                    <div><span style="font-size: 14px;">val myDf = Seq(("Hello", 2, 1L)).toDF("col1","col2", "col3")</span></div>
                    <div><span style="font-size: 14px;">myDf.show()</span></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b><span style="font-size: 12px;"><span style="color: rgb(255, 0, 42);">Select and SelectExpr</span></span></b></div>
    <ul>
        <li>
            <div>allows you to do the DataFrame equivalent of SQL queries on a table of data</div>
        </li>
    </ul>
    <table width="1596px" style="width:1596px;">
        <colgroup>
            <col style="width: 433px;" />
            <col style="width: 486px;" />
            <col style="width: 450px;" />
            <col style="width: 227px;" />
        </colgroup>
        <tbody>
            <tr>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;">SQL</span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Python</span></b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b>Scala</b></div>
                </td>
                <td>
                    <div style="text-align:center;"><b>Note</b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><b>SELECT</b> DEST_COUNTRY_NAME <b>FROM</b> dfTable <b>LIMIT</b> 2</div>
                </td>
                <td>
                    <div><span style="font-size: 14px;">df.select("DEST_COUNTRY_NAME").show(2)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%203.42.56%20AM.png" height="244" width="692" />
                    <div><br /></div>
                </td>
                <td>
                    <div><span style="font-size: 14px;">df.select("DEST_COUNTRY_NAME").show(2)</span></div>
                </td>
                <td>
                    <div>Use the select method and pass in <span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">the column names as strings with  which you would like to work</span></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><b>SELECT</b> DEST_COUNTRY_NAME, ORIGIN_COUNTRY_NAME <b>FROM</b> dfTable <b>LIMIT</b> 2</div>
                </td>
                <td>
                    <div><span style="font-size: 14px;">df.select("DEST_COUNTRY_NAME", "ORIGIN_COUNTRY_NAME").show(2)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%203.46.05%20AM.png" height="254" width="946" />
                    <div><br /></div>
                </td>
                <td>
                    <div><span style="font-size: 14px;">df.select("DEST_COUNTRY_NAME", "ORIGIN_COUNTRY_NAME").show(2)</span></div>
                </td>
                <td>
                    <div>you can select multiple columns</div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><br /></div>
                </td>
                <td>
                    <div><b>you can refer to columns in a number of different ways</b></div>
                    <div>df.select(</div>
                    <div><b>expr</b>(<span style="font-size: 14px;">"DEST_COUNTRY_NAME"),</span></div>
                    <div><b><span style="font-size: 14px;">col</span></b>(<span style="font-size: 14px;">"DEST_COUNTRY_NAME"),</span></div>
                    <div><b><span style="font-size: 14px;">column</span></b>(<span style="font-size: 14px;">"DEST_COUNTRY_NAME"))\</span></div>
                    <div><span style="font-size: 14px;">.show(2)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%203.49.52%20AM.png" height="348" width="790" />
                    <div><br /></div>
                </td>
                <td>
                    <div><br /></div>
                </td>
                <td>
                    <div><br /></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b><span style="color: rgb(255, 0, 42);">AS and alias - </span><span style="color: rgb(0, 0, 0);">change the name using the AS and alias keywords</span></b></div>
    <table width="1626px" style="width:1626px;">
        <colgroup>
            <col style="width: 433px;" />
            <col style="width: 516px;" />
            <col style="width: 450px;" />
            <col style="width: 227px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">SQL</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Python</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Scala</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Note</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>SELECT</b> DEST_COUNTRY_NAME as destination <b>FROM</b> dfTable <b>LIMIT</b> 2</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.select(expr("DEST_COUNTRY_NAME AS destination").alias("DEST_COUNTRY_NAME")).show(2)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%204.01.30%20AM.png" height="232" width="898" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.select("DEST_COUNTRY_NAME").show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>change the name of the column</div>
                    <div><b>AS</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.select(expr("DEST_COUNTRY_NAME AS destination").alias("DEST_COUNTRY_NAME")).show(2)<span style="font-size: 14px;">)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%204.03.20%20AM.png" height="280" width="1348" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="margin-top:16px;margin-bottom:16px;">df.select(expr("DEST_COUNTRY_NAME AS destination").alias("DEST_COUNTRY_NAME")).show(2)</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>alias</b></div>
                    <div>change the column name back to its original name</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT *, (DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as withinCountry</div>
                    <div>FROM dfTable</div>
                    <div>LIMIT 2</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.<b>selectExpr</b>(</div>
                    <div>"*",</div>
                    <div><span style="font-size: 14px;">"(DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as withinCountry")\</span></div>
                    <div><span style="font-size: 14px;">.show(2)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%204.10.38%20AM.png" height="320" width="966" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.<b>selectExpr</b>(</div>
                    <div>"*",</div>
                    <div><span style="font-size: 14px;">"(DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as withinCountry")</span></div>
                    <div><span style="font-size: 14px;">.show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>add a new column withinCountry to DataFrame that specifies whether the destination and origin are the same</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT act(count), count(distinct(DEST_COUNTRY_NAME)) FROM dfTable LIMIT 2</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.selectExpr("avg(count)", "count(distinct(DEST_COUNTRY_NAME))").show(2)</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%204.25.59%20AM.png" height="170" width="1110" />
                    <div><br /></div>
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.selectExpr("avg(count)", "count(distinct(DEST_COUNTRY_NAME))").show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Aggregations</div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><br /></div>
    <div><b><span style="font-size: 14px;"><span style="color: rgb(255, 0, 42);">Converting to Spark Types</span></span></b></div>
    <div><span style="font-size: 14px;">Sometimes we need to pass explicit values into Spark that aren't a new column but are just a value.</span></div>
    <div><span style="font-size: 14px;">The was we do this is through </span><b><span style="font-size: 14px;"><i>literals</i></span></b><span style="font-size: 14px;">. This is a translation from a given programming language's literal value to one that Spark understands. Literals are expressions.</span></div>
    <table width="1626px" style="width:1626px;">
        <colgroup>
            <col style="width: 433px;" />
            <col style="width: 516px;" />
            <col style="width: 450px;" />
            <col style="width: 227px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">SQL</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Python</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Scala</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Note</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT *, 1 as One FROM dfTable LIMIT2</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>from pyspark.sql.functions import lit</div>
                    <div>df.select(expr("*"),lit(1).alias("One")).show(2)</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%204.31.21%20AM.png" height="268" width="760" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>import org.apache.spark.sql.functions.lit</div>
                    <div><span style="font-size: 14px;">df.select(expr("*"),lit(1).as("One")).show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><b><span style="color: rgb(255, 0, 42);">Adding Columns</span></b></div>
    <table width="1528px" style="width:1528px;">
        <colgroup>
            <col style="width: 433px;" />
            <col style="width: 516px;" />
            <col style="width: 315px;" />
            <col style="width: 264px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">SQL</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Python</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Scala</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Note</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT *, 1 as numberOne FROM dfTable LIMIT2</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.withColumn("numberOne", lit(1)).show(2)</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%204.34.11%20AM.png" height="248" width="806" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.withColumn("numberOne", lit(1)).show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>formal way of<b> adding a column</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.withColumn("withinCountry", expr("ORIGIN_COUNTRY_NAME == DEST_COUNTRY_NAME"))\</span></div>
                    <div><span style="font-size: 14px;">.show(2)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%204.36.44%20AM.png" height="286" width="1226" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.withColumn("withinCOuntry", expr("ORIGIN_COUNTRY_NAME == DEST_COUNTRY_NAME"))\</span></div>
                    <div><span style="font-size: 14px;">.show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Boolean</b> expression for when the original country is the same as the Destination Country</div>
                    <div><br /></div>
                    <div> </div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.withColumn("Destination", expr("DEST_COUNTRY_NAME").columns</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">NOTICE that withColumn function takes two arguments; the column name and the expression that will create the value for that given row in the DataFrame. We can also rename a column this way. (SQL syntax is the same as previously so it is not here now.</span></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b><span style="color: rgb(255, 0, 42);">Renaming Columns</span></b></div>
    <div><b><i>withColumnRenamed</i></b> method</div>
    <table width="1528px" style="width:1528px;">
        <colgroup>
            <col style="width: 433px;" />
            <col style="width: 516px;" />
            <col style="width: 315px;" />
            <col style="width: 264px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">SQL</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Python</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Scala</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Note</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.withColumnRenamed("DEST_COUNTRY_NAME", "dest").columns</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%204.44.22%20AM.png" height="90" width="900" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.withColumnRenamed("DEST_COUNTRY_NAME", "dest").columns</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>rename columns</b></div>
                    <div>name of the string = first argument</div>
                    <div>string = second argument</div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="color: rgb(255, 0, 42);">Reserved Characters and Keywords</span></span></b></div>
    <div><span style="font-size: 12px;">like spaces or dashes in column names. Handling these means escaping column names appropriately. </span></div>
    <div><span style="font-size: 12px;">We do this by using </span><b><span style="font-size: 12px;">backtick</span></b><span style="font-size: 12px;"> ("`")</span></div>
    <table width="1559px" style="width:1559px;">
        <colgroup>
            <col style="width: 464px;" />
            <col style="width: 516px;" />
            <col style="width: 315px;" />
            <col style="width: 264px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">SQL</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Python</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Scala</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Note</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="background-color:rgb(252, 83, 86);border-color:rgb(251, 17, 21);">
                    <div><span style="color: rgb(255, 255, 255);">dfWithLongColName = df.withColumn(</span></div>
                    <div><span style="color: rgb(255, 255, 255);">"This Long Column-Name",</span></div>
                    <div><span style="color: rgb(255, 255, 255);">expr("ORIGIN)COUNTRY_NAME")</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>import org.apache.spark.sql.functions.expr</div>
                    <div><span style="font-size: 14px;">val dfWithLongColName = df.withColumn(</span></div>
                    <div><span style="font-size: 14px;">"this Long Column-Name",</span></div>
                    <div><span style="font-size: 14px;">expr("ORIGIN_COUNTRY_NAME"))</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Could not run this nor understand this part! - Need to come back &amp; Check!</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="background-color:rgb(252, 83, 86);border-color:rgb(251, 17, 21);">
                    <div><span style="font-size: 14px;"><span style="color: rgb(255, 255, 255);">dfWithLongColName.selectExpr(</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(255, 255, 255);">" This Long Column-Name ",</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(255, 255, 255);">" This Long Column-Name as `new col`")\</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(255, 255, 255);">.show(2)</span></span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>set spark.sql.caseSensitive true</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Case Sensitivity </b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.drop("ORIGIN_COUNTRY_NAME").columns</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Removing Columns</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>dfWithLongColName.drop("ORIGIN_COUNTRY_NAME", "DEST_COUNTRY_NAME")</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Removing multiple columns</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>SELECT</b> *, <b>cast</b>(<b>count as</b> long) <b>AS</b> count2 <b>FROM</b> dfTable</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="margin-top:16px;">df.withColumn("count2", col("count").cast("long"))</div>
                    <div><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%208.20.25%20PM.png" height="80" width="1386" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Change Column's Type (cast)</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT * FROM dfTable WHERE count &lt; 2 LIMIT 2</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="margin-top:16px;">df.filter(col("count") &lt; 2).show(2)</div>
                    <div><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%208.24.05%20PM.png" height="240" width="654" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Filtering Rows </b>- evaluates to true or false. You can use <b>where</b> or <b>filter </b>an they both will perform the same operation.</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>SELECT</b> * <b>FROM</b> dfTable <b>WHERE</b> <b>count</b> &lt; 2 <b>AND</b> ORIGIN_COUNTRY_NAME != "Croatia <b>LIMIT</b> 2</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.where(col("count") &lt; 2).where(col("ORIGIN_COUNTRY_NAME") != "Croatia")\</div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">.show(2)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%208.29.04%20PM.png" height="264" width="1138" />
                    <div><br /></div>
                    <div style="margin-bottom:16px;"><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.where(col("count") &lt; 2).where(col("ORIGIN_COUNTRY_NAME") != "Croatia")</div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">.show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Multiple filters </b></div>
                    <div><span style="font-size: 14px;">you can put multiple filters into the same expression. It's not always useful because Spark automatically performs all filtering operations at the same time regardless of the filter ordering. This optimization is called </span><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;"><span style="color: rgb(184, 22, 215);">PIPELINING</span></span></span></b><span style="font-size: 14px;">. This means that if you want to specify multiple AND filters, just chain them sequentially and let Spark handle the rest.</span></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT COUNT(DISTINCT(<span style="font-size: 14px;">ORIGIN_COUNTRY_NAME,  DEST_COUNTRY_NAME) FROM dfTable</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="margin-top:16px;">df.select("ORIGIN_COUNTRY_NAME", "DEST_COUNTRY_NAME").distinct().count()</div>
                    <div><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%208.33.16%20PM.png" height="66" width="1188" />
                    <div><br /></div>
                    <div style="margin-bottom:16px;"><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.select("ORIGIN_COUNTRY_NAME", "DEST_COUNTRY_NAME").distinct().count()</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Getting unique Rows</div>
                    <div>extract unique or distinct values. These values van be in one or more columns. <b>distinct </b>method allws us to duplicate any rows that are in the DataFrame. </div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="background-color:rgb(255, 230, 151);border-color:rgb(255, 211, 70);">
                    <div><span style="color: rgb(0, 0, 0);">seed = 5</span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="color: rgb(0, 0, 0);">withReplacement = False</span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="color: rgb(0, 0, 0);">fraction = 0.5</span></span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;"><span style="color: rgb(0, 0, 0);">df.sample(withReplacement, fraction, seed).count()</span></span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%208.35.54%20PM.png" height="172" width="780" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>val seed = 5</div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">val withReplacement = False</span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">val fraction = 0.5</span></div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">df.sample(withReplacement, fraction, seed).count()</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>sample </b>method - sample some random records from your DataFrame.</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>dataFrames = df.randomSplit([0.25, 0.75], seed)</div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">dataFrames[0].count() &gt; dataFrames[1].count()</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%208.48.03%20PM.png" height="92" width="734" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>val dataFrames = df.randomSplit(Array(0.25, 0.75), seed)</div>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">dataFrames(0).count() &gt; dataFrames(1).count()</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Random Splits </b>can be useful when you need to break up your DataFrame.  It cannot guarantee that all records are in one of the DataFrames from which you are sampling. This is often used with machine learning.</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>from pyspark.sql import Row</div>
                    <div>schema = df.schema</div>
                    <div>newRows = [</div>
                    <div>Row("New Country", "Other Country", 5),</div>
                    <div><span style="font-size: 14px;">Row("New Country 2", "Other Country 3", 1),</span></div>
                    <div><span style="font-size: 14px;">]</span></div>
                    <div><span style="font-size: 14px;">parallelizeRows = spark.sparkContext.parallelize(newRows)</span></div>
                    <div><span style="font-size: 14px;">newDF = spark.createDataFrame(parallelizeRows, schema)</span></div>
                    <div> </div>
                    <div><span style="font-size: 14px;">df.union(newDF)\</span></div>
                    <div><span style="font-size: 14px;">.where("count =1")\</span></div>
                    <div><span style="font-size: 14px;">.where(col("ORIGIN_COUNTRY_NAME") != "United States")\</span></div>
                    <div><span style="font-size: 14px;">.show()</span></div>
                    <div> </div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%209.04.25%20PM.png" height="812" width="888" />
                    <div><br /></div>
                    <div> </div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Concentrating and Appending Rows (Union)</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.sort("count").show(5)</div>
                    <div>df.orderBy("count", "DEST_COUNTRY_NAME").show(5)</div>
                    <div>df.orderBy(col("count"), col("DEST_COUNTRY_NAME")).show(5)</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%209.08.10%20PM.png" height="1006" width="900" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.sort("count").show(5)</span></div>
                    <div><span style="font-size: 14px;">df.orderBy("count", "DEST_COUNTRY_NAME").show(5)</span></div>
                    <div><span style="font-size: 14px;">df.orderBy(col("count"), col("DEST_COUNTRY_NAME")).show(5)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Sorting Rows</b></div>
                    <div> </div>
                    <div><b>sort </b>and<b> orderBy </b>do the same</div>
                    <div>the default is sort in ascending order</div>
                    <div><br /></div>
                    <div><br /></div>
                    <div>to more explicitly specify sort direction, you need to use <b>asc </b>and <b>desc</b> functions if operating on a column. </div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>from pyspark.sql.functions import asc, desc</div>
                    <div>df.orderBy(expr("count desc")).show(2)</div>
                    <div>df.orderBy(col("count").desc(),  col("DEST_COUNTRY_NAME").asc()).show(2)</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%209.11.58%20PM.png" height="518" width="1086" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>(sort)</div>
                    <div>to more explicitly specify sort direction, you need to use <b>asc </b>and <b>desc</b> functions if operating on a column. </div>
                    <div><br /></div>
                    <div>Advanced tip is to use asc_nulls_first, desc_nulls_first, asc_nulls_last, or _desc_nulls_last</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT * FROM dfTable LIMIT 6</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.limit(5).show()</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.limit(5).show()</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Limit</b></div>
                    <div>Restrict what you extract from the dataframe</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b><span style="font-size: 14px;">SELECT</span></b><span style="font-size: 14px;"> * </span><b><span style="font-size: 14px;">FROM</span></b><span style="font-size: 14px;"> dfTable </span><b><span style="font-size: 14px;">ORDER BY count</span></b><span style="font-size: 14px;"> </span><b><span style="font-size: 14px;">desc</span></b><span style="font-size: 14px;"> </span><b><span style="font-size: 14px;">LIMIT</span></b><span style="font-size: 14px;"> 6</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.orderBy(expr("count")).asc().limit(6).show()</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.orderBy(expr("count")).asc().limit(6).show()</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.rdd.getNumPartitions()</div>
                    <div>df.repartition(5)</div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><b>Repartition based on a columns name </b></div>
                    <div><b><span style="font-size: 14px;">df.repartition(5, col("DEST_COUNTRY_NAME"))</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.rdd.getNumPartitions()</span></div>
                    <div><span style="font-size: 14px;">df.repartition(5)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Repartition </b></div>
                    <div>partition the data according to some frequently filtered columns, which control the physical layout of data across the cluster including the partitioning scheme and the number of partitions. </div>
                    <div><br /></div>
                    <div>Repartition will incur a full shuffle of the data, regardless of whether one is necessary. This means that you should typically only repartition when the future number of partitions os greater than your current number of partitions or when you are looking to partition by a set of columns. </div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.repartition(5, col("DEST_COUNTRY_NAME")).coalesce(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.repartition(5, col("DEST_COUNTRY_NAME")).coalesce(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Coalesce</b></div>
                    <div><span style="font-size: 14px;">will not incur a full shuffle and will try to combine partitions. This operation will shuffle your data into five partitions based on the destination country name and then coalesce them without a full shuffle.</span></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>collectDF=df.limit(10)</div>
                    <div><span style="font-size: 14px;">collectDF.take(5) #works with an integer count</span></div>
                    <div><span style="font-size: 14px;">collectDF.show() #this prints it out nicely</span></div>
                    <div><span style="font-size: 14px;">collectDF.show(5, False)</span></div>
                    <div><span style="font-size: 14px;">collectDF.collect()</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%209.31.14%20PM.png" height="1068" width="1068" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>val collectDF=df.limit(10)</div>
                    <div><span style="font-size: 14px;">collectDF.take(5)</span></div>
                    <div><span style="font-size: 14px;">collectDF.show()</span></div>
                    <div><span style="font-size: 14px;">collectDF.show(5, False)</span></div>
                    <div><span style="font-size: 14px;">collectDF.collect()</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Collecting Rows to the Driver</b></div>
                    <div>Spark maintains the state of the cluster in the driver. There are times when you want to collect some of the data to the driver in order to manipulate it on your local machine.</div>
                    <div><br /></div>
                    <div><b>collect </b>gets all the data from the entire Dataframe</div>
                    <div><b>take </b>selects the first N rows </div>
                    <div><b>show </b>prints out a number of rows nicely.</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>collectDF.toLocalIterator()</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Iterate over the entire dataset. The method is called <b>toLocalIterator </b>that collects partitions to the driver as an iterator. Iterates over the entire dataset partition by partition in a serial manner</div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><br /></div>
    <div style="text-align:center;"><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;"><span style="color: rgb(255, 0, 42);">Working with Different Types of Data</span></span></span></b></div>
    <div><b><span style="font-size: 14px;">Objectives</span></b></div>
    <ul>
        <li>
            <div>Booleans</div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Numbers</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Strings</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Dates and Timestamps</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Handling Null</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Complex Types</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">User Defined Functions</span></div>
        </li>
    </ul>
    <div> </div>
    <div><b><span style="font-size: 14px;">Where to look for APIs?</span></b></div>
    <div><span style="font-size: 14px;">DataFrame (Dataset) Methods: DataFrame is just a Dataset of Row types, so you will look at the Dataset methods available at: <a href="http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Dataset" rev="en_rl_none">http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Dataset</a></span></div>
    <div>DataFrameStatFunctions: <span style="font-size: 14px;"><a href="http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.DataFrameStatFunctions" rev="en_rl_none">http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.DataFrameStatFunctions</a></span></div>
    <div>DataFrameNaFunctions <span style="font-size: 14px;"><a href="http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.DataFrameNaFunctions" rev="en_rl_none">http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.DataFrameNaFunctions</a></span></div>
    <div>Column methods: <span style="font-size: 14px;"><a href="http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Column" rev="en_rl_none">http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Column</a></span></div>
    <div><span style="font-size: 14px;">Functions: <a href="http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.functions$" rev="en_rl_none">http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.functions$</a></span></div>
    <div>Dataset: <span style="font-size: 14px;"><a href="http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Dataset" rev="en_rl_none">http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Dataset</a></span></div>
    <div><br /></div>
    <div><b><span style="font-size: 14px;">DataFrame used here =&gt; by-day/2010.12.01.csv</span></b></div>
    <table width="1582px" style="width:1582px;">
        <colgroup>
            <col style="width: 335px;" />
            <col style="width: 512px;" />
            <col style="width: 394px;" />
            <col style="width: 341px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">SQL</span></span></b></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">Python</span></span></b></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="color: rgb(0, 0, 0);">Scala</span></b></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="color: rgb(0, 0, 0);">Notes</span></b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div> </div>
                </td>
                <td>
                    <div style="margin-top:16px;">&gt;&gt;&gt; df = spark.read.format("csv")\</div>
                    <div><br /></div>
                    <div>... .option("header", "true")\</div>
                    <div><br /></div>
                    <div>... .option("inferSchema", "true")\</div>
                    <div><br /></div>
                    <div>... .load("/Users/mikepetridisz/Desktop/retail-data/by-day/2010-12-01.csv")</div>
                    <div><br /></div>
                    <div>&gt;&gt;&gt; df.printSchema()</div>
                    <div><br /></div>
                    <div>&gt;&gt;&gt; df.createOrReplaceTempView("dfTable")</div>
                    <div><br /></div>
                    <div> </div>
                    <div><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2010.05.39%20PM.png" height="502" width="1118" />
                    <div><br /></div>
                    <div style="margin-bottom:16px;"><br /></div>
                </td>
                <td>
                    <div><br /></div>
                </td>
                <td>
                    <div><b>Load data</b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div>no equivalent function necessary in SQL</div>
                </td>
                <td>
                    <div>from pyspark.sql.functions import lit</div>
                    <div>df.select(lit(5), lit("five"), lit(5.0))</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2010.11.53%20PM.png" height="128" width="650" />
                    <div><br /></div>
                </td>
                <td>
                    <div><span style="font-size: 14px;">import org.apache.spark.sql.functions.lit</span></div>
                    <div><span style="font-size: 14px;">df.select(lit(5), lit("five"), lit(5.0))</span></div>
                </td>
                <td>
                    <div>convert to spart types</div>
                    <div>convert native types to spark types.</div>
                    <div><br /></div>
                    <div>We do this by using the <b>lit</b> function</div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><br /></div>
                </td>
                <td>
                    <div>from pyspark.sql.functions import col</div>
                    <div>df.where(col("InvoiceNo") != 536365)\</div>
                    <div>.select("InvoiceNo", "Description")\</div>
                    <div>.show(5, False)</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2010.16.53%20PM.png" height="400" width="610" />
                    <div><br /></div>
                    <div> </div>
                    <div> </div>
                    <div><span style="font-size: 14px;">OR</span></div>
                    <div><span style="font-size: 14px;">df.where("InvoiceNo == 536365")\</span></div>
                    <div><span style="font-size: 14px;">.show(5, false)</span></div>
                </td>
                <td>
                    <div><span style="font-size: 14px;">df.where(col("InvoiceNo") === 536365)</span></div>
                    <div><span style="font-size: 14px;">.select("InvoiceNo", "Description")</span></div>
                    <div><span style="font-size: 14px;">.show(5, False)</span></div>
                </td>
                <td>
                    <div><b>Working with Booleans</b></div>
                    <div><span style="font-size: 14px;">Boolean statements consist of four elements: and, or, true, false</span></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><b>SELECT</b> * <b>FROM</b> dfTable <b>WHERE</b> StockCode <b>in</b> ("DOT") <b>AND</b> (UnitPrice &gt;600 <b>OR</b> <b>instr</b>(Description, "POSTAGE") &gt;= 1</div>
                </td>
                <td>
                    <div>from pyspark.sql.functions import instr</div>
                    <div>priceFilter = col("UnitPrice") &gt; 600</div>
                    <div>descripFilter = instr(df.Description, "POSTAGE") &gt;= 1</div>
                    <div>df.where(df.StockCode.isin("DOT")).where(priceFilter | descripFilter).show()</div>
                    <div><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2010.49.26%20PM.png" height="288" width="1422" />
                    <div><br /></div>
                </td>
                <td>
                    <div><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">val priceFilter = col("UnitPrice") &gt; 600</span></div>
                    <div><span style="font-size: 14px;">val descripFilter = col("Description").contains( "POSTAGE")</span></div>
                    <div><span style="font-size: 14px;">df.where(df.StockCode.isin("DOT")).where(priceFilter | descripFilter).show()</span></div>
                    <div> </div>
                </td>
                <td>
                    <div><br /></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div>SELECT UnitPrice, (StockCode = 'DOT' AND</div>
                    <div>(UnitPrice &gt; 600 OR instr(Description, "POSTAGE") &gt;= 1)) as isExpensive</div>
                    <div>FROM dfTable</div>
                    <div>WHERE (StockCode = 'DOT' AND</div>
                    <div>(UnitPrice &gt; 600 OR instr(Description, "POSTAGE") &gt;= 1))</div>
                </td>
                <td style="background-color:rgb(254, 222, 193);border-color:rgb(253, 175, 105);">
                    <div><span style="color: rgb(0, 0, 0);">from pyspark.sql.functions import instr</span></div>
                    <div><span style="color: rgb(0, 0, 0);">DOTCodeFilter = col("StockCode") == "DOT"</span></div>
                    <div><span style="color: rgb(0, 0, 0);">priceFilter = col("UnitPrice") &gt; 600</span></div>
                    <div><span style="color: rgb(0, 0, 0);">descripFilter = instr(col("Description"), "POSTAGE") &gt;= 1</span></div>
                    <div><span style="color: rgb(0, 0, 0);">df.withColumn("isExpensive", DOTCodeFilter &amp; (priceFilter | descripFilter))\</span></div>
                    <div><span style="color: rgb(0, 0, 0);">.where("isExpensive")\</span></div>
                    <div><span style="color: rgb(0, 0, 0);">.select("unitPrice", "isExpensive").show(5)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2010.56.23%20PM.png" height="432" width="1156" />
                    <div><br /></div>
                </td>
                <td>
                    <div><br /></div>
                </td>
                <td>
                    <div>To specify a DataFrame, you can also just specify a <b>Boolean column</b></div>
                </td>
            </tr>
            <tr>
                <td>
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.where(col("Description").eqNullSafe("hello")).show()</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.02.05%20PM.png" height="198" width="1206" />
                    <div><br /></div>
                </td>
                <td>
                    <div><span style="font-size: 14px;">df.where(col("Description").eqNullSafe("hello")).show()</span></div>
                </td>
                <td>
                    <div><b>Null safe equivalence test:</b></div>
                    <div>df.where(col("Description").eqNullSafe("hello")).show()</div>
                    <div><br /></div>
                    <div>if there is a null in the data, we need to treat things differently. the above example shows how we can tackle it.</div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><b><span style="font-size: 14px;">Working with Numbers</span></b></div>
    <div><span style="font-size: 14px;">after filtering the most common thing in big data is counting things. </span></div>
    <table width="1559px" style="width:1559px;">
        <colgroup>
            <col style="width: 464px;" />
            <col style="width: 516px;" />
            <col style="width: 315px;" />
            <col style="width: 264px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">SQL</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;">Python</span></b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Scala</b></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div style="text-align:center;"><b>Note</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT customerId, (POWER((Quantity * UnitPrice), 2.0) +5) as realQuantity FROM dfTable</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>from pyspark.sql.functions import pow, expr</div>
                    <div>fabricatedQuantity = pow(col("Quantity") * col("UnitPrice"), 2) +5</div>
                    <div>df.select(expr("CustomerId"), fabricatedQuantity.alias("realQuantity")).show(2)</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.09.26%20PM.png" height="300" width="1206" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>val <span style="font-size: 14px;">fabricatedQuantity = pow(col("Quantity") * col("UnitPrice"), 2) +5</span></div>
                    <div><span style="font-size: 14px;">df.select(expr("CustomerId"), fabricatedQuantity.alias("realQuantity")).show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Let's imagine that we found out that we misrecorded the quantity in our retail dataset and the true quantity is equal to the <b>((current quantity * the unit price)^2 +5)</b></div>
                    <div> </div>
                    <div><b>pow function (</b>raises a column to the expressed power</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT round (2.5), bround(2.5)</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">from pyspark.sql.functions import lit, round, bround</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">df.select(round(lit("2.5")), bround(lit("2.5"))).show(2)</span></span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.18.07%20PM.png" height="234" width="848" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>import org.apache.spark.functions.lit</div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">df.select(round(lit("2.5")), bround(lit("2.5"))).show(2)</span></span></div>
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Rounding</b></div>
                    <div>example round to 1 decimal places</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT corr(Quantity, UnitPrice) FROM dfTable</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import corr</span></div>
                    <div><span style="font-size: 14px;">df.stat.corr("Quantity", "UnitPrice")</span></div>
                    <div><span style="font-size: 14px;">df.select(corr("Quantity", "UnitPrice")).show()</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.24.40%20PM.png" height="256" width="738" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">import org.apache.spark.functions.{corr}</span></div>
                    <div><span style="font-size: 14px;">df.stat.corr("Quantity", "UnitPrice")</span></div>
                    <div><span style="font-size: 14px;">df.select(corr("Quantity", "UnitPrice")).show()</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Compute the <b>correlation</b> of two columns. e.g to see if cheaper things are typically bought in greater quantities. </div>
                    <div><br /></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.describe().show()</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.27.27%20PM.png" height="302" width="1974" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.describe().show()</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Summary Statistics for a column or a set of columns. </div>
                    <div><br /></div>
                    <div><b>describe </b>method. This takes all numeric columns and calculate the count, mean, standard deviation, min, max.</div>
                    <div>You should use this for viewing the console because the schema might change in the future.</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>from pyspark.sql.functions import <b>count, mean, stddev_pop, min, max</b></div>
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>if you need exact numbers you can also perform this aggregation yourself by importing the functions and applying them to the columns that you need.</div>
                    <div><br /></div>
                    <div>These are the statistical functions available in the StatFunctions Package. </div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="background-color:rgb(254, 222, 193);border-color:rgb(253, 175, 105);">
                    <div><span style="color: rgb(0, 0, 0);">colName = "UnitPrice"</span></div>
                    <div><span style="color: rgb(0, 0, 0);">quantileProbs = [0.5]</span></div>
                    <div><span style="color: rgb(0, 0, 0);">relError = 0.05</span></div>
                    <div><span style="color: rgb(0, 0, 0);">df.stat.approxQuantile("UnitPrice", quantileProbs, relError)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.32.04%20PM.png" height="152" width="926" />
                    <div><br /></div>
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">val colName = "UnitPrice"</span></div>
                    <div><span style="font-size: 14px;">val quantileProbs = [0.5]</span></div>
                    <div><span style="font-size: 14px;">val relError = 0.05</span></div>
                    <div><span style="font-size: 14px;">df.stat.approxQuantile("UnitPrice", quantileProbs, relError)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>You can calculate exact or approximate quantiles of your data using the <b>approxQuantile</b> method.</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.stat.crosstab("StockCode", "Quantity").show()</div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.33.58%20PM.png" height="1330" width="1912" />
                    <div><br /></div>
                    <div> </div>
                    <div><span style="font-size: 14px;">df.stat.freqItems(["StockCode", "Quantity"]).show()</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.35.47%20PM.png" height="244" width="802" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>df.stat.crosstab("StockCode", "Quantity").show()</div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div><br /></div>
                    <div> </div>
                    <div><span style="font-size: 14px;">df.stat.freqItems(["StockCode", "Quantity"]).show()</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>cross-tabulation or frequent item pairs </div>
                    <div>this output will be large!!!!!</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>from pyspark.sql.functions import monotonically_increasing_id </div>
                    <div><span style="font-size: 14px;">df.select(monotonically_increasing_id()).show(2)</span></div>
                    <div> </div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.38.21%20PM.png" height="264" width="936" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.select(monotonically_increasing_id()).show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Add unique ID to reach Row by using</div>
                    <div><b>monotonically_increasing_id </b>function</div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><br /></div>
    <div><b><span style="font-size: 14px;">Working with Strings</span></b></div>
    <table width="1582px" style="width:1582px;">
        <colgroup>
            <col style="width: 335px;" />
            <col style="width: 512px;" />
            <col style="width: 394px;" />
            <col style="width: 341px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">SQL</span></span></b></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">Python</span></span></b></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="color: rgb(0, 0, 0);">Scala</span></b></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="color: rgb(0, 0, 0);">Notes</span></b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div> SELECT initcap(Description) FROM dfTable</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import initcap</span></div>
                    <div><br /></div>
                    <div><span style="font-size: 14px;">df.select(initcap(col("Description"))).show()</span></div>
                    <div><br /></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.50.33%20PM.png" height="770" width="720" />
                    <div><br /></div>
                    <div style="margin-bottom:16px;"><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">df.select(initcap(col("Description"))).show(2, false)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>initcap - </b>capitalize every word in a given string when that word is separated from another by a space</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT Description, lower(Description), Ipper(lower(Description)) FROM dfTable</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import lower, upper</span></div>
                    <div><span style="font-size: 14px;">df.select(col("Description"),</span></div>
                    <div><span style="font-size: 14px;">lower(col("Description")),</span></div>
                    <div><span style="font-size: 14px;">upper(lower(col("Description")))).show(2)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-21%20at%2011.55.15%20PM.png" height="328" width="986" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>cast string in <b>uppercase / lowercase</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">SELECT</span></div>
                    <div><span style="font-size: 14px;">ltrim(lit('     HELLOOOOO     '),</span></div>
                    <div><span style="font-size: 14px;">rtrim(lit('     HELLOOOOO     '), </span></div>
                    <div><span style="font-size: 14px;">lpad(lit(' HELLOOOOO     '),2, ' ')</span></div>
                    <div><span style="font-size: 14px;">FROM dfTable</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import lit, trim, ltrim, rtrim, lpad, rpad</span></div>
                    <div><span style="font-size: 14px;">df.select(</span></div>
                    <div><span style="font-size: 14px;">ltrim(lit("     HELLOOOOO     ")).alias("ltrim"),</span></div>
                    <div><span style="font-size: 14px;">rtrim(lit("     HELLOOOOO     ")).alias("rtrim"),</span></div>
                    <div><span style="font-size: 14px;">trim(lit("     HELLOOOOO     ")).alias("trim"),</span></div>
                    <div><span style="font-size: 14px;">lpad(lit("HELLOOOOO     "),2, " ").alias("lpad"),</span></div>
                    <div><span style="font-size: 14px;">rpad(lit("HELLOOOOO"), 10, "").alias("rpad")).show(2)</span></div>
                    <div> </div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%2012.02.30%20AM.png" height="404" width="1052" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">import....</span></div>
                    <div> </div>
                    <div><span style="font-size: 14px;">df.select(</span></div>
                    <div><span style="font-size: 14px;">ltrim(lit("     HELLOOOOO     ")).alias("ltrim"),</span></div>
                    <div><span style="font-size: 14px;">rtrim(lit("     HELLOOOOO     ")).alias("rtrim"),</span></div>
                    <div><span style="font-size: 14px;">trim(lit("     HELLOOOOO     ")).alias("trim"),</span></div>
                    <div><span style="font-size: 14px;">lpad(lit("HELLOOOOO     "),2, " ").alias("lpad"),</span></div>
                    <div><span style="font-size: 14px;">rpad(lit("HELLOOOOO"), 10, "").alias("rpad")).show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Adding/removing spaces around a string</div>
                    <div><b>lpad</b></div>
                    <div><b>ltrim</b></div>
                    <div><b>rpad</b></div>
                    <div><b>rtrim</b></div>
                    <div><b>trim</b></div>
                    <div> </div>
                    <div>If lpad and rpad takes a number less than the length of the string it will always remove values from the right side of the string</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>regex_replace(Description, 'BLACK|WHITE|RED|BLUE', 'COLOR') as color)clean, Description</div>
                    <div>FROM dfTable</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import regexp_replace</span></div>
                    <div> </div>
                    <div><span style="font-size: 14px;">regex_string = "BLACK|WHITE|RED|BLUE"</span></div>
                    <div><span style="font-size: 14px;">df.select(</span></div>
                    <div><span style="font-size: 14px;">regexp_replace(col("Description"), regex_string, "COLOR").alias("color_clean"),</span></div>
                    <div><span style="font-size: 14px;"> col("Description")).show(2)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%2012.27.46%20AM.png" height="358" width="1154" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Regular Expressions</b></div>
                    <div>-replacing all mentions of a string with another value</div>
                    <div>-searching for the existence of one string</div>
                    <div>This is done with a tool called <i>regular expressions (</i><b><i>regexes)</i></b></div>
                    <div>used to extract values from a string or replace them with some other values</div>
                    <div><b>regexo_extract</b></div>
                    <div><b>regexp_replace</b></div>
                    <div> </div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT translate(Description, 'LEET', '1337'), Description FROM dfTable</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import translate</span></div>
                    <div><span style="font-size: 14px;">df.select(translate(col("Description"), "LEET", "1337"), col("Description")).show(2)</span></div>
                    <div> </div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%2012.32.17%20AM.png" height="310" width="1190" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import translate</span></div>
                    <div><span style="font-size: 14px;">df.select(translate(col("Description"), "LEET", "1337"), col("Description")).show(2)</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Replacing given characters with other characters</div>
                    <div><b><span style="font-size: 14px;">translate</span></b><span style="font-size: 14px;"> function</span></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT regexp_extract(Description, 'BLACK|WHITE|RED|BLUE)', 1),</div>
                    <div>Description FROM dfTable</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import regexp_extract</span></div>
                    <div><span style="font-size: 14px;">extract_str ="(BLACK|WHITE|RED|BLUE)"</span></div>
                    <div><span style="font-size: 14px;">df.select(</span></div>
                    <div><span style="font-size: 14px;">regexp_extract(col("Description"), extract_str, 1).alias("color_clean"),</span></div>
                    <div><span style="font-size: 14px;">  col("Description")).show(2)</span></div>
                    <div> </div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%2012.36.48%20AM.png" height="364" width="1086" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>pull out the <b>first mentioned </b>color</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT  Description FROM dfTable</div>
                    <div>WHERE instr(Description, 'BLACK') &gt;= OR instr(Description, 'WHITE') &gt;= 1</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import instr</span></div>
                    <div><span style="font-size: 14px;">containsBlack = instr(col("Description"), "BLACK") &gt;=1</span></div>
                    <div><span style="font-size: 14px;">containsWhite = instr(col("Description"), "WHITE") &gt;=1</span></div>
                    <div><span style="font-size: 14px;">df.withColumn("hasSimpleColor", containsBlack | containsWhite)\</span></div>
                    <div><span style="font-size: 14px;">.where("hasSimpleColor")\</span></div>
                    <div><span style="font-size: 14px;">.select("Description").show(3, False)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%2012.42.05%20AM.png" height="414" width="968" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>contains method</b></div>
                    <div>check for values existence - this will return a Boolean</div>
                    <div><b>instr</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="background-color:rgb(254, 222, 193);border-color:rgb(253, 175, 105);">
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">from pyspark.sql.functions import expr, locate</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">simpleColors = ["black", "white", "red", "green", "blue"]</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">def color_locator(column, color_string):</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">  return locate(color_string.upper(), column)\</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">.cast("boolean")\</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">.alias("is_" + c)</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">selectedColumns = [color_locator(df.Description, c) for c in simpleColors]</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">selectedColumns.append(expr("*"))</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">df.select(*selectedColumns).where(expr("is_white OR is_red"))\</span></span></div>
                    <div><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">.select("Description").show(3, False)</span></span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>problem</div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><br /></div>
    <div><b><span style="font-size: 14px;">Working with Dates and Timestamps</span></b></div>
    <div><span style="font-size: 14px;">Dates - focus exclusively on calendar dates</span></div>
    <div><span style="font-size: 14px;">timestamps - both date and time information included</span></div>
    <div> </div>
    <div><span style="font-size: 14px;">TimeStampType class supports only second-level precision, which means that if you are going to be working with milliseconds or microseconds you will need to work around this problem by potentially operating on them as </span><b><span style="font-size: 14px;">longs,</span></b></div>
    <div><span style="font-size: 14px;">Important to be explicit when parsing or converting to ensure that there are no issues in doing so.</span></div>
    <div><span style="font-size: 14px;">Conforms to java standards when working with dates and timestamps.</span></div>
    <table width="1547px" style="width:1547px;">
        <colgroup>
            <col style="width: 386px;" />
            <col style="width: 512px;" />
            <col style="width: 281px;" />
            <col style="width: 368px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">SQL</span></span></b></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">Python</span></span></b></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="color: rgb(0, 0, 0);">Scala</span></b></div>
                </td>
                <td style="background-color:rgb(234, 234, 234);border-color:rgb(187, 187, 187);">
                    <div style="text-align:center;"><b><span style="color: rgb(0, 0, 0);">Notes</span></b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import current_date, current_timestamp</span></div>
                    <div><span style="font-size: 14px;">dateDF = spark.range(10)\</span></div>
                    <div><span style="font-size: 14px;">.withColumn("today", current_date())\</span></div>
                    <div><span style="font-size: 14px;">.withColumn("now", current_timestamp())</span></div>
                    <div><span style="font-size: 14px;">dateDF.createOrReplaceTempView("dataTable")</span></div>
                    <div><span style="font-size: 14px;">dateDF.printSchema()</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%201.08.00%20AM.png" height="502" width="1152" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT date_sub(today, 5), date_add(today_5) FROM dateTable</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import date_add, date_sub</span></div>
                    <div><span style="font-size: 14px;">dateDF.select(date_sub(col("today"),5), date_add(col("today"), 5)).show(1)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%201.11.03%20AM.png" height="450" width="1322" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Now <b>subtract five days from today</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT to_date('2016-01-01'), months_between('2016-01-01', '2017-01-01'),</div>
                    <div>datediff('2016-01-01', '2017-01-01')</div>
                    <div>FROM dateTable</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import datediff, months_between, to_date</span></div>
                    <div><span style="font-size: 14px;">dateDF.withColumn("week_ago", date_sub(col("today"),7))\</span></div>
                    <div><span style="font-size: 14px;">.select(datediff(col("week_ago"), col("today"))).show(1)</span></div>
                    <div><span style="font-size: 14px;">dateDF.select(</span></div>
                    <div><span style="font-size: 14px;">to_date(lit("2016-01-01")).alias("start"),</span></div>
                    <div><span style="font-size: 14px;"> to_date(lit("2017-05-22")).alias("end"))\</span></div>
                    <div><span style="font-size: 14px;">.select(months_between(col("start"), col("end"))).show(1)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%201.18.24%20AM.png" height="928" width="1174" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><b>Difference between two dates</b></div>
                    <div><b>datediff </b>function</div>
                    <div>it will return the number of days in between two dates</div>
                    <div><br /></div>
                    <div><b>to_date </b>function - allows you to convert a string to a date, optionally with a specified format. </div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import to_date, lit</span></div>
                    <div><span style="font-size: 14px;">spark.range(5).withColumn("date", lit("2017-01-01"))\</span></div>
                    <div><span style="font-size: 14px;">.select(to_date(col("date"))).show(1)</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%201.22.22%20AM.png" height="540" width="970" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>if Spark cannot parse the date it will return <b>null</b></div>
                    <div><span style="font-size: 14px;">tricky situation for bugs because some data might match the correct format. </span></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">dateDF.select(to_date(lit("2016-20-12")), to_date(lit("2017-12-11"))).show(1)</span></div>
                    <div> </div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%201.24.58%20AM.png" height="468" width="1360" />
                    <div><br /></div>
                    <div> </div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>Notice that this date appears as Dec 11 instead of the correct day Nov 12. Spark doesn't throw an error because it cannot know whether the days are mixed up or that specific row is incorrect.</div>
                    <div><br /></div>
                    <div><b>Let's fix this pipeline! </b></div>
                    <div><b>---&gt;</b></div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT to_date(date, 'yyyy-dd-MM'), to_date(date2, 'yyyy-dd-MM'), to_date(date) FROM dataTable2</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import to_date</span></div>
                    <div><span style="font-size: 14px;">dateFormat = "yyyy-dd-MM"</span></div>
                    <div><span style="font-size: 14px;">cleanDateDF = spark.range(1).select(</span></div>
                    <div><span style="font-size: 14px;">to_date(lit("2017-12-11"), dateFormat).alias("date"),</span></div>
                    <div><span style="font-size: 14px;">  to_date(lit("2017-20-12"), dateFormat).alias("date2"))</span></div>
                    <div><span style="font-size: 14px;">cleanDateDF.createOrReplaceTempView("dateTable2")</span></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>---&gt;</div>
                    <div>The first step is to remember that we need to specify our date format according to the Java SimpleDateFormat standard.</div>
                    <div>We use two functions:</div>
                    <div>to_date</div>
                    <div>to_timestamp</div>
                    <div>the former optionally expects a format whereas the latter requires one.</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>SELECT to)timestamp(date, 'yyyy-dd-MM'), to_timestamp(date2, 'yyyy-dd-MM') FROM dateTable2</div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">from pyspark.sql.functions import to_timestamp</span></div>
                    <div><span style="font-size: 14px;">cleanDateDF.select(to_timestamp(col("date"), dateFormat)).show()</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%201.35.06%20AM.png" height="408" width="1136" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>to_timestamp</div>
                </td>
            </tr>
            <tr>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><span style="font-size: 14px;">cleanDateDF.filter(col("date2") &gt; "'2017-12-12'").show()</span></div><img src="Spark%20Overview.html.resources/Screen%20Shot%202019-05-22%20at%201.38.47%20AM.png" height="358" width="982" />
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div><br /></div>
                </td>
                <td style="border-color:rgb(204, 204, 204);">
                    <div>after we have our date or timestamp into the correct format and type comparing between them is easy. We just need to make sure that either use a date/timestamp type or specify our string according to the right format of yyyy-MM-dd if we are comparing a date</div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <div><br /></div>
    <div><b><span style="font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Fira Sans&quot;, &quot;Droid Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif;">Working with Nulls in Data</span></b></div>
    <div><span style="font-size: 14px;">you should always use null to represent missing or empty data in your DataFrames. Spark can optimize working with null values more than it can if you use empty strings or other values.</span></div>
    <div><span style="font-size: 14px;">use the </span><b><span style="font-size: 14px;">.nasubpackage</span></b><span style="font-size: 14px;"> on a DataFrame</span></div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div> </div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div> </div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
    <div><br /></div>
</body>

</html>
