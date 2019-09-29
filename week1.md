---
layout: default
---
[Home](./README.md).
[Week 1](./week1.md).
[Week 2](./week2.md).
[Week 3](./week2.md).
[Week 4](./week1.md).
[Week 5](./week1.md).
[Week 6](./week1.md).
[Week 7](week1.md).

## Basics of Internet. TCP/IP, Servers, Ports, Firewalls

### Protocols
- A way of communicating - more specifically, a protocol is a set of rules or conventions that computers or computer programs use while communicating with each other
- Real World Example: We shake hands, a protocol that has plenty of rules regarding length of the handshake, and the politeness of responding or not
- Computers often use protocols when they intercommunicate, in order to get data from one place to another

* * *

### How the Internet Works?
- We go “on the Internet” and visit some webpage (Facebook, Google, Amazon)
- Somehow, that webpage understands how to interpret what we want and display an appropriate output
- We can imagine that somehow, our computer puts information into the Internet, which delivers that information to some computer or server owned by the company who owns the site we’re trying to visit
- Then, this server sends back the appropriate information to the Internet, which makes sure it gets delivered to our computer at home
- In essence, the Internet is a delivery mechanism for information…but how?

* * *

### Internet Protocol address (IP address)
- Every computer on the internet has an IP (Internet Protocol) address, of the form #.#.#.# -> Four numbers separated by dots of the values 0-255
- Other IP address formats exist today as well; Like postal addresses, they uniquely identify computers on the internet
- Any device connected to the internet has an IP address, allows other computers to talk to it
- ISPs assign a IP address to your computer (router)
- DHCP (Dynamic Host Configuration Protocol)
- Software that ISPs provides to allow your computer to request an IP address
- DHCP servers respond with a specific IP address for your Home
- Multiple devices can connect to your home network
- The home router supports DHCP and assigns IP addresses to your devices
- IP addresses are limited
- In the format #.#.#.#, each number is 8 bits, so 32 bits total
- This yields 232 or about 4 billion possible addresses
- We’re running out of addresses for all computers
- Current version of addresses is IPv4
- Moving towards IPv6
- Uses 128 bits, yielding 2128 possible addresses
- Question: How do you find your IP address?

| Mac       | Windows         | 
|:-------------|:------------------|
|![MacIP](assets/macip.png , width=300 )| ![WindowsIP](assets/windowsip.png , width=300 ) | 


* * *


Private addresses exist
10.#.#.#, 192.168.#.#, or 172.16.#.#
Only with special configuration can someone talk to your computer
Your personal device is not a server, so people should not need to access them directly
Your device needs to request data from servers
Even email is stored on a server such as Gmail and your device makes a request to that server to access that email
Looking at advanced settings…
Subnet mask is used to decide if another computer is on the same network
Router (aka Gateway) has its own address
Routs data in different directions

DNS
We access websites using domain names (Facebook.com, Google.com, etc.), but it turns out that these sites too have IP addresses
DNS (Domain Name System) servers convert domain names into IP addresses


Packets
Computers communicate by sending packets, which are like virtual envelopes sent between computers
Ultimately still 0s and 1s
As an analogy, suppose we want to find a ceu_logo image on the internet
So, we send a request to a server, say Google, like “get ceu_logo.jpg”
We place this request in an envelope
On the envelope, we list out IP as the return address
However, for the recipient of the request, we don’t know the IP address for Google
Have to rely on DNS
Send a request to our ISPs DNS server for Google’s IP address
If the ISP’s DNS server doesn’t know a website’s IP address, it has been configured to ask another DNS server
There exist root servers that know where to look to for an IP address if it exists
After sending the request off, we’ll get a response ms later



The ceu_logo will be sent back in one or more packets
If the ceu_logo image is too large for a single envelope, sending it in one packet could take up internet traffic
To solve this, Google will divide the ceu_logo image into smaller fragments
Put the fragments into different envelopes
Write information on the envelopes
Return address: Google’s IP address
Delivery address: Our IP address
List the number of packets on each envelope (1 of 4, 2 of 4, etc.)


TCP/IP
IP goes beyond addresses
Set of conventions computers and servers follow to allow intercommunication
Fragmentation like in the envelope example are supported by IP
If missing a packet, you can logically infer which packet you’re missing based on the ones received
However, IP doesn’t tell computers what to do in this case
TCP (Transmission Control Protocol) ensures packets can get to their destination
Commonly used with IP (TCP/IP)
Supports sequence numbers that help data get to its destination
When missing a packet, a computer can make a request for the missing packet
The computer will put packets together to get a whole file
Also includes conventions for requesting services (port identifiers)
To make sure Google knows we’re requesting a webpage and not an email or other service

Ports
Per TCP, the world has standardized numbers that represent different services
If 5.6.7.8 is Google’s IP address, 5.6.7.8;80 (port 80) lets use know that we want a webpage
80 means http (hypertext transfer protocol)
The language that web servers speak
Google will send the request to their web server via http
Many websites use secure connections with SSL or HTTPS, which uses the port 443
Email uses port 25
Other ports exist as well

Protocols
Protocols are just sets of rules
Humans use these all the time, such as the protocol for meeting people: handshakes
When a request is made to Google for an image, HTTP tells Google how to respond appropriately

UDP
User Datagram Protocol
Doesn’t guarantee delivery
Used for video conferencing such as FaceTime
Packets can be dropped for the sake of keeping the conversation flowing
Used anytime you want to keep data coming without waiting for a buffer to fill

Routers
Routers have bunches if wires coming and going out of them
They have a big table with IP addresses and where data should be routed to get to that destination
Often, the data is routed to some next router
Routers purpose is to send data in the direction of a destination
The next router will send it to another until it reaches a destination

The internet is a network of networks (with their own routers)
Often multiple ways to go from A to B
Based in US Military logic to prevent downtime if a particular router goes down
When multiple packets are sent, like ceu_logo.jpg from Google, they can each take a different path, still getting to their destination eventually
Sometimes the internet is busy and the quickest path changes


DHCP - Dynamic Host Configuration Protocol
This protocol makes it so that when a computer you have - a phone, a laptop, etc - it can announce itself and ask for an address
The protocol says that these devices will be assigned a numeric address, much like our physical addresses, except unlike our physical addresses (like 123 Main St), this looks like #.#.#.#, where each # is between 0 and 255 (why?)
Despite the large number of combinations here, there are actually a very large number of devices, to where we are increasingly using something called IPv6 (the previous was IPv4), which allows for far more combinations
When my computer sends out a request, it has to use this IP address to make sure our data goes to the proper place
However, we, as humans, don’t really read addresses like 8.8.8.8 or 192.168.0.1
There is a system to “translate” the human-readable domain names (google.com, facebook.com, cs50.io) to their IP address counterparts
This service is called DNS, which allows us to use this translation to get from point A to B
We also have routers or gateways, which know how to take in information, look at where it’s going, and send it to the proper router
Data doesn’t have to follow the same path each time, but it will get to where it needs to go in around 30 hops or jumps from router to router or gateway to gateway

TCP - Transmission Control Protocol
Guarantees with high probability that data gets to where it needs to go
Sometimes, computers drop packets (data) - they get more data than they can, or they miss it entirely
TCP allows computers to know if they should resend data
Port numbers, specifically TCP Port numbers, help identify which service should take which data
For example - Data headed to #.#.#.#:80 says that the data should be sent to #.#.#.# and put through port 80, which happens to be a human-defined standard port for HTTP or web requests.

UDP - User Datagram Protocol
The feature here is to not guarantee redelivery….what?
Still fairly common and appropriate
For example, video streaming, video conferencing, live communication - we don’t want a retransmission, we would rather stay up to date chronologically
In these cases, UDP is actually more optimal than is TCP, can you see why?

Traceroute
Literally traces the route that information takes from our computer to some destination
Allows us to see which routers are being used by data to get to where it needs to go
This route may change over time and according to web traffic patterns
How long does it take for this process of data transfer to take on the internet?
Traceroute is a program that sends packets to each router on a path to a destination, reporting the time it takes to reach that router
Mac (Terminal): traceroute domainname.com
Windows: C:\>tracert www.example.com
From Sanders Theatre to Berkeley.edu:


6: Northern Crossroads
7-14: A fast connection
8-9: Chicago
10-11: Denver
12-13: Las Vegas
4: Los Angeles
19 is where it arrives at Berkeley in 80 ms!

From Sanders Theatre to CNN.jp



9-10 jumps from Seattle to Osaka past an ocean!
Using undersea cabling!

Undersea Cabling
We can also traceroute to international destinations, especially those on different continents
There is a lot of cabling that connects locations across oceans, including the Pacific and Atlantic
Video

TCP/IP
How do we make sure that data, even large amounts of data, gets to where it needs to go, and does so “fairly”, so that a single piece of data doesn’t take up more space than it should?
How do we send the data and make sure whoever gets it knows what to do with it?
Maybe we could label the data in order, so that the recipient knowns that whichever data they get belongs in whichever order it’s supposed to
Additionally, if some data gets lost along the way, TCP allows us to ask for the missing data and complete it

HTTP - Hyper Text Transfer Protocol
A very common protocol, which you’ve likely seen before - http://example.com
HTTP is a sort of virtual envelope, which allows computers to communicate with one another, specifically in a webpage context (so between web browsers and servers)
We can use nslookup to check the IP address of a web domain - i.e. nslookup www.facebook.com
We can pretend to be a browser, and see the response that comes back when we visit a webpage
curl -I http://31.13.65.36/ - which tells us that Facebook would prefer we used their domain name (specifically which type of HTTP?)
This returns to us the response (if it worked) 200, which means to us, and our computers, that the response was ok
We’re likely more familiar with 404, which means things didn’t quite goes as planned
What we see here are called headers, which give us additional information about the data we’re given

HTML - Hyper Text Markup Language
curl without the -I flag lets us see the HTML results, or the data
This language tells the browser how to display everything from where pictures are located to how to format text on the page


Q&A
Suppose that you turn on your computer and visit https://www.ceu.edu/ in a browser. Using each of the terms below in a context that makes clear your understanding of each, explain in a paragraph the process by which CEU's home page appears on your screen: DHCP server, DNS server, IP address, packet, TCP port, web server.
When I turn on my computer and connect to WiFi DHCP gives me a unique IP address and tells the IP address of the local DNS server. DNS converts domain names to IP addresses and vice versa so when I type www.ceu.edu, DNS translates it into a numeric address, the real address of the server where the website is located. Then an HTTP request is sent to the server, which sends a copy of the website (data) to me across TCP/IP. If the request gets approved then data packets will be sent to me. Then these small packets assemble and get displayed to me.
DHCP server- assigns IP addresses
DNS server - contains the IP addresses and host names (translation)
IP address: #.#.#.#, where each # is between 0 and 255. (identification & location)
Packet: unit of data
TCP port: used to identify the format that is requested. For example, port "80" requests web services, port "25" requests email, etc.
Web Server: processes incoming network requests over HTTP and other protocols

TCP (tries to) guarantee delivery by ensuring that any lost packets are resent. Why, though, might packets be lost between a sender and receiver?
UDP: its feature is to not guarantee delivery. If some data gets lost, packets get dropped. It can be due to: malfunction, technical difficulties, overloaded routers. This protocol does not let data to be re-transmitted. Skype, streaming, video games are some examples where UDP is useful because it is better to wait a few seconds than watching something lagging all the time. Re-transmission is not as good as staying up to date chronologically. TCP: Packets can be lost here as well due to the routers being too busy or due to other reasons, but then TCP re-transmits.

When a server receives a packet, how does it know whether that packet contains (part of) an email, a request for a website, an instant message, or something else altogether?
SMTP (protocol for emails), on the 'envelope' there will be a port number specified. We need to specify what type of information is inside the envelope, which is represented by the port number.

In what sense are domain names similar to phone numbers like 1-800-COLLECT?
Phone number: numeric reference, phone numbers were originally hard wired and the first few numbers told the geographic location of the exchange. Phone numbers are used to identify people. Everybody has a different one. Domain name is like an address as well and helps us locate web pages. There is no duplicate domain address. (IPv6 is needed so that we do not run out of them)

If not already familiar, read up on "bandwidth" and "latency" (as via Google) and then, in your own words, distinguish the two concepts as they relate to internet speed.
Latency is basically the time it takes to send a packet from the source to the destination. Bandwidth is the maximum data transfer rate. So high latency is not good because it takes a lot of time to get a packet from the source to the destination, but with high bandwidth, we can reduce this time.

How does every website that you visit know (and likely log!) your IP address?
The web server needs an IP to be able to establish the connection and communicate, where to send the data requested etc. It is usually done in the NCSA format. Anonymization can be done via: Proxy, VPN, Tor, NAT, Gateway or Firewall. You'll know the following information if you know one’s IP address: approximate location based on IP/ISP, whether they have a static or dynamic IP, if they use traceroute (+ see the latency), with telnet or nmap open ports can be found as well. IP address is usually logged to show you relevant advertisements. The information is contained in the Packet Header.

If not already familiar, read up on "DNS hijacking," and in your own words, explain what it means for an adversary to hijack a website via DNS.
When we open a website, DNS translates the domain to an IP and then we can access the website. DNS hijacking means to redirect requests of a specific server to another and it is achieved by the translation of a domain to a fake IP address that takes the person to a malicious website and eventually people or companies may lose data (passwords, accounts etc.). One of the most popular DNS hijacking case is when hackers redirected traffic to all 36 of a Brazilian bank's domains.
Optional Reading

Practice Questions:
What is the internet?
What does it mean if a URL begins with https:// as opposed to http://?
What does it mean for a computer to have a private IP address (e.g. one that begins with 10., 192.168., or 172.16.)?
Why do TCP/IP packets from one computer to another not always take the same amount of time to arrive at their destination?
Today's "home routers" are often much more than routers alone. They are also "access points" (aka APs) and "firewalls" too. What is an access point (AP)? And what is a firewall?
Whether or not you have internet service at home, Google around for an internet service provider (ISP) that provides internet service to your neighborhood (or somewhere nearby). What's the ISP you found? What speeds does the ISP you found offer? At what cost? And do they offer symmetric (i.e., identical) upload and download speeds, or do they differ?



Sources:
http://web.stanford.edu/class/cs101/lecture10.html#/4
https://web.stanford.edu/class/cs101/network-2-internet.html
https://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm
https://web.stanford.edu/class/cs101/network-1-introduction.html














```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/mikepetridisz/CEU_Data_Engineering/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
