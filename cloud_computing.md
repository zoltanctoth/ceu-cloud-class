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

## Basics of Cloud Computing using Amazon Web Services (AWS): Storage and Virtual Machines

## Table of Contents
- [What is cloud computing?](#what-is-cloud-computing)
- [Origins](#origins)
- [Cloud Solutions](#cloud-solutions)
- [Caching](#caching)
- [SPOF - Single Point Of Failure](#spof---single-point-of-failure)
- [Costs](#costs)
- [IAaS - Infrastructure As a Service](#iaas---infrastructure-as-a-service)
- [Virtual Machines](#virtual-machines)
- [PAaS, SAaS - Platform and Software As a Service](#paas-saas---platform-and-software-as-a-service)
- [Databases](#databases)
- [Layering and Summary](#layering-and-summary)

### What is cloud computing?
- It may sound complicated and foreign
- But it’s really just many technologies coming together
- It allows for the outsourcing or borrowing of computers
- Computations and applications can be done on computers that are not physically ours or located near us

### Origins
- The Internet was often drawn as a “nebulous cloud”
- Its primary function was getting information from one location to another
- On the Internet, getting something up and running is relatively easy
- There are many languages and databases to choose from
- The problems arise when we’re successful
- With millions of customers, we have several logistical issues that come up
- Our computers only have so much RAM, so much storage, and so many CPUs
- With too many customers, or users, or requests, our technology can very quickly be overwhelmed

### Cloud Solutions
- Eventually we reach that upper limit, where too many users are trying to use our product
- These users maybe experience error messages, or no working product at all
- What if we added a second server, with the exact same technology?
- Now, we probably don’t want to arbitrarily change our URL, a la www1.example.com or www13.example.com
- What if we put a server in between our two new servers, and our URL brought users there
- Sometimes, this middleman gives users the IP address of our original server, and sometimes it gives those users the IP address of our second server
- We might call this middleman, which balances the traffic or load on our servers, a load-balancer
- Optional: look up Round Robin Approach via Google

### Caching
- IP addresses don’t change that often, though they can change
- If we remember, or cache an IP address for one of the servers behind our load-balancer, what happens if that server goes down or incurs downtime?
- Maybe we don’t give our two servers unique IP addresses
- Instead, our domain name leads users to the load-balancer
- And somehow, the load-balancer routes traffic
- If DNS returns the IP address of the load-balancer, then we don’t have this problem of having users unable to access a given server
- To make sure that the load-balancer is keeping track of which servers are online, we can use something called a heartbeat
- This just means having servers behind the load-balancer “check in” periodically with the load-balancer

### SPOF - Single Point Of Failure
- Now, our network can tolerate server one or two going down, but not the load-balancer
- We assume that our load-balancer can handle at least twice as much traffic as an individual one of our servers
- However, it can still be overwhelmed, and what happens if it is?
- Previously, we added hardware, maybe we could add another load-balancer
- Now, we have two load-balancers and two servers
- We could configure the load balancers to send heartbeats to each other
- If one of the load-balancers is down, then the other one takes on the responsibility of traffic

### Costs
- This hardware has both a financial and logistical cost
- There are now wires that need to be connected, and housing needs to be bought for the servers
- Maybe we don’t have enough physical space and cooling
- MBTF - Mean Time Between Failure can very quickly drop
- Maintaining this can quickly become quite difficult

### IAaS - Infrastructure As a Service
- This is one of the appeals of Cloud Computing - we can offload all of these logistical costs to the cloud
Amazon, Google, Microsoft, etc
- There is software that mimicks the behavior each of the things we’ve seen so far - load-balancers and servers - and more
- Now, we’re able to buy the infrastructure we need, but not worry about make and model of server, cooling, wiring, and other logistical costs
- Another added benefit is auto-scaling
- If our company is more successful than anticipated - maybe it’s the holiday season - we need more technology
- IAaS can provide for us the ability to scale up our hardware - maybe by turning on more servers
- This can happen passively, without us knowing
- The reverse is also true - the service automatically scales down when not being used
- Over the years, we’ve been able to pack more computability into the same space (a la Moore’s Law)
- Humans, however, have been checking their email at around the same speed
- This means, that we can put multiple simulated machines on the same hardware

### Virtual Machines
- Virtual machines are software that allow us to simulate running several computers on the same hardware
- This allows us to oversell to customers, where we only have so much memory on our servers, but we assume some customers will not have very successful businesses
- This means that those customers will not need as many computer or CPU cycles
- For the customer though, this means that your website can be hosted on the same machine as another customer whose business is hugely successful
- This translates to slower runtimes and services for reasons outside of your control
- Virtualization looks very much like splitting your computer into several smaller, virtual, computers
- Virtualization can be inefficient though - what if all customers are using the same guest OS or virtual operating system as the host OS, or operating system actually installed on the server?
- This is what has given rise to containerization, like in Docker
- Containerization allows us to use the host OS, sharing operating system resources, while still separating the other virtual computers
- While there is still some overhead - we need to have some enginer, Docker or Hypervisor, but there aren’t copies of the same operating system
- This provides the same separation, but with less watse of resources

### PAaS, SAaS - Platform and Software As a Service
- Even if you don’t know it, you’ve likely already used SAaS, as with Gmail, or Outlook.com
- We don’t need to worry about where our emails are, or how they get from place to place
- IAaS is where you still need to understand network topology, and how to put things together
- Between these two, is Platform As a Service, like Heroku
- Often, these services run on Amazon, Google, or Microsoft infrastructure, but provide a sort of middle ground
- This middle layer of abstraction makes it easier for us to run applications
- All we have to deal with is - host this as a server, without concerning me with how it communicates, scales, or load balancers
- The downside of course is not necessarily knowing how to solve a given problem, if that problem occurs within the platform provider

### Databases
- Beyond the application, we likely also need to store data somewhere
- Now, it’s very common for a web server to be very specialized - a server to send emails, a server to respond to HTTP requests, etc
- Our infrastructure likely has at least one database
- Databases are generally drawn as cylinders, and are connected to all of our servers
- All of our servers can then save and read all their data from the same place
- Vertical scaling - pay more money for bigger and better hardware
- Even the best database server can only handle so many connections, reads, and writes at any one time
- Maybe we can go back to the engineering solution - scaling horizontally
- If we add another database - we probably can’t just use a load balancer, because then some data will end up in one database and not in the other
- We could also shard the databases, where we put similar users in databases that only contain those users
- This doesn’t help us backup our data though
- We could go back to something like our first model, with one large masterdatabase
- In something called replication, we could add smaller or equivalent databases that can only read, from that main database
- In another step up, maybe we have two master databases, and even if data is only written to one of them, they communicate with each other to make sure the data gets replicated

* * * 

### Layering and Summary
- As difficult or foreign as these things can sometimes sound, we’re really just layering many layers on top of increaingly complicated ideas
- At each step, the differences are really on just abstracting away common problems to make our code as accessible and efficient as possible
- With all of this in mind, the idea is that we can use each of these layers and puzzle pieces to build better solutions to the challenges that arise in building our own site
