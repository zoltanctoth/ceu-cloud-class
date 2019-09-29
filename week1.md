<!DOCTYPE html>
<html>

<head>
     <meta charset="utf-8">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="exporter-version" content="Evernote Mac 7.10 (457750)" />
    <meta name="created" content="2019-09-29 11:41:33 +0000" />
    <meta name="updated" content="2019-09-29 14:21:21 +0000" />
    <title>Basics of Internet. TCP/IP, Servers, Ports, Firewalls</title>
</head>

<body>
    <div><br /></div>
    <div><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;"><span style="color: rgb(51, 51, 51);">Protocols</span></span></span></b></div>
    <ul>
        <li>
            <div><span style="font-size: 14px;"><span style="color: rgb(51, 51, 51);">A way of communicating - more specifically, a protocol is a set of rules or conventions that computers or computer programs use while communicating with each other</span></span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;"><span style="color: rgb(51, 51, 51);">Real World Example: We shake hands, a protocol that has plenty of rules regarding length of the handshake, and the politeness of responding or not</span></span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;"><span style="color: rgb(51, 51, 51);">Computers often use protocols when they intercommunicate, in order to get data from one place to another</span></span></div>
        </li>
    </ul>
    <hr />
    <div><br /></div>
    <div><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;"><span style="color: rgb(51, 51, 51);">How the Internet Works?</span></span></span></b></div>
    <ul>
        <li>
            <div><span style="font-size: 14px;">We go “on the Internet” and visit some webpage (Facebook, Google, Amazon)</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Somehow, that webpage understands how to interpret what we want and display an appropriate output</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">We can imagine that somehow, our computer puts information into the Internet, which delivers that information to some computer or <i>server</i> owned by the company who owns the site we’re trying to visit</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Then, this <i>server</i> sends back the appropriate information to the Internet, which makes sure it gets delivered to our computer at home</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">In essence, the Internet is a delivery mechanism for information…but how?</span></div>
        </li>
    </ul>
    <hr />
    <div><br /></div>
    <div><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;"><span style="color: rgb(34, 34, 34);">Internet Protocol address</span></span></span></b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;"><span style="color: rgb(34, 34, 34);"> (</span></span></span><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;"><span style="color: rgb(34, 34, 34);">IP address</span></span></span></b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;"><span style="color: rgb(34, 34, 34);">)</span></span></span></div>
    <ul>
        <li>
            <div><span style="font-size: 14px;">Every computer on the internet has an IP (Internet Protocol) address, of the form #.#.#.# -&gt; Four numbers separated by dots of the values 0-255</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Other IP address formats exist today as well; Like postal addresses, they uniquely identify computers on the internet</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Any device connected to the internet has an IP address, allows other computers to talk to it</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">ISPs assign a IP address to your computer (router)</span></div>
        </li>
        <ul>
            <li>
                <div><span style="font-size: 14px;">DHCP (Dynamic Host Configuration Protocol)</span></div>
            </li>
            <ul>
                <li>
                    <div><span style="font-size: 14px;">Software that ISPs provides to allow your computer to request an IP address</span></div>
                </li>
                <li>
                    <div><span style="font-size: 14px;">DHCP servers respond with a specific IP address for your Home</span></div>
                </li>
            </ul>
            <li>
                <div><span style="font-size: 14px;">Multiple devices can connect to your home network</span></div>
            </li>
            <ul>
                <li>
                    <div><span style="font-size: 14px;">The home router supports DHCP and assigns IP addresses to your devices</span></div>
                </li>
            </ul>
        </ul>
        <li>
            <div><span style="font-size: 14px;">IP addresses are limited</span></div>
        </li>
        <ul>
            <li>
                <div><span style="font-size: 14px;">In the format #.#.#.#, each number is 8 bits, so 32 bits total</span></div>
            </li>
            <ul>
                <li>
                    <div><span style="font-size: 14px;">This yields 2<sup>32</sup> or about 4 billion possible addresses</span></div>
                </li>
                <ul>
                    <li>
                        <div><span style="font-size: 14px;">We’re running out of addresses for all computers</span></div>
                    </li>
                </ul>
            </ul>
            <li>
                <div><span style="font-size: 14px;">Current version of addresses is IPv4</span></div>
            </li>
            <li>
                <div><span style="font-size: 14px;">Moving towards IPv6</span></div>
            </li>
            <ul>
                <li>
                    <div><span style="font-size: 14px;">Uses 128 bits, yielding 2<sup>128</sup> possible addresses</span></div>
                </li>
            </ul>
        </ul>
        <li>
            <div><span style="font-size: 14px;">How do you find your IP address?</span></div>
        </li>
    </ul>
    <table width="814px" style="width:814px;">
        <colgroup>
            <col style="width: 389px;" />
            <col style="width: 425px;" />
        </colgroup>
        <tbody>
            <tr>
                <td style="background-color:#d4d4d4;border-color:#AAAAAA;color:#333;">
                    <div style="text-align:center;"><span style="font-size: 14px;">Mac</span></div>
                </td>
                <td style="background-color:#d4d4d4;border-color:#AAAAAA;color:#333;">
                    <div style="text-align:center;"><span style="font-size: 14px;">Windows</span></div>
                </td>
            </tr>
            <tr>
                <td><img src="Basics%20of%20Internet.%20TCP_IP,%20Servers,%20Ports,%20Firewalls.html.resources/Screen%20Shot%202019-09-29%20at%203.30.54%20PM.png" height="922" width="1060" />
                    <div><br /></div>
                </td>
                <td><img src="Basics%20of%20Internet.%20TCP_IP,%20Servers,%20Ports,%20Firewalls.html.resources/Screen%20Shot%202019-09-29%20at%203.33.19%20PM.png" height="656" width="800" />
                    <div><br /></div>
                </td>
            </tr>
        </tbody>
    </table>
    <div><br /></div>
    <ul>
        <li>
            <div><span style="font-size: 14px;">Private addresses exist</span></div>
        </li>
        <ul>
            <li>
                <div><span style="font-size: 14px;">10.#.#.#, 192.168.#.#, or 172.16.#.#</span></div>
            </li>
            <li>
                <div><span style="font-size: 14px;">Only with special configuration can someone talk to your computer</span></div>
            </li>
            <li>
                <div><span style="font-size: 14px;">Your personal device is not a server, so people should not need to access them directly</span></div>
            </li>
            <ul>
                <li>
                    <div><span style="font-size: 14px;">Your device needs to request data from servers</span></div>
                </li>
            </ul>
            <li>
                <div><span style="font-size: 14px;">Even email is stored on a server such as Gmail and your device makes a request to that server to access that email</span></div>
            </li>
        </ul>
        <li>
            <div style="margin-bottom:16px;"><span style="font-size: 14px;">Looking at advanced settings…</span></div>
        </li>
        <ul>
            <li>
                <div><span style="font-size: 14px;">Subnet mask is used to decide if another computer is on the same network</span></div>
            </li>
            <li>
                <div><span style="font-size: 14px;">Router (aka Gateway) has its own address</span></div>
            </li>
            <ul>
                <li>
                    <div><span style="font-size: 14px;">Routs data in different directions</span></div>
                </li>
            </ul>
        </ul>
    </ul>
    <hr />
    <div><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;">DNS</span></span></b></div>
    <ul>
        <li>
            <div><span style="font-size: 14px;">We access websites using domain names (Facebook.com, Google.com, etc.), but it turns out that these sites too have IP addresses</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">DNS (Domain Name System) servers convert domain names into IP addresses</span></div>
        </li>
    </ul>
    <div><span style="font-size: 14px;"><span style="--en-markholder:true;"><br /></span></span></div>
    <hr />
    <div><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;">Packets</span></span></b></div>
    <ul>
        <li>
            <div><span style="font-size: 14px;">Computers communicate by sending packets, which are like virtual envelopes sent between computers</span></div>
        </li>
        <ul>
            <li>
                <div><span style="font-size: 14px;">Ultimately still 0s and 1s</span></div>
            </li>
        </ul>
        <li>
            <div><span style="font-size: 14px;">As an analogy, suppose we want to find a ceu_logo image on the internet</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">So, we send a request to a server, say Google, like “get ceu_logo.jpg”</span></div>
        </li>
        <ul>
            <li>
                <div><span style="font-size: 14px;">We place this request in an envelope</span></div>
            </li>
        </ul>
        <li>
            <div><span style="font-size: 14px;">On the envelope, we list out IP as the return address</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">However, for the recipient of the request, we don’t know the IP address for Google</span></div>
        </li>
        <ul>
            <li>
                <div><span style="font-size: 14px;">Have to rely on DNS</span></div>
            </li>
            <li>
                <div><span style="font-size: 14px;">Send a request to our ISPs DNS server for Google’s IP address</span></div>
            </li>
            <ul>
                <li>
                    <div><span style="font-size: 14px;">If the ISP’s DNS server doesn’t know a website’s IP address, it has been configured to ask another DNS server</span></div>
                </li>
                <li>
                    <div><span style="font-size: 14px;">There exist root servers that know where to look to for an IP address if it exists</span></div>
                </li>
            </ul>
        </ul>
        <li>
            <div style="margin-bottom:16px;"><span style="font-size: 14px;">After sending the request off, we’ll get a response ms later</span></div>
        </li>
    </ul>
    <div><br /></div><img src="Basics%20of%20Internet.%20TCP_IP,%20Servers,%20Ports,%20Firewalls.html.resources/ceulogo_0_1.jpg" height="239" width="480" />
    <div><br /></div>
    <div><span style="font-size: 14px;">The ceu_logo will be sent back in one or more packets</span></div>
    <ul>
        <li>
            <div><span style="font-size: 14px;">If the ceu_logo image is too large for a single envelope, sending it in one packet could take up internet traffic</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">To solve this, Google will divide the ceu_logo image into smaller fragments</span></div>
        </li>
        <ul>
            <li>
                <div><span style="font-size: 14px;">Put the fragments into different envelopes</span></div>
            </li>
            <li>
                <div><span style="font-size: 14px;">Write information on the envelopes</span></div>
            </li>
            <ul>
                <li>
                    <div><span style="font-size: 14px;">Return address: Google’s IP address</span></div>
                </li>
                <li>
                    <div><span style="font-size: 14px;">Delivery address: Our IP address</span></div>
                </li>
                <li>
                    <div><span style="font-size: 14px;">List the number of packets on each envelope (1 of 4, 2 of 4, etc.)</span></div>
                </li>
            </ul>
        </ul>
    </ul>
    <hr />
    <div><br /></div>
    <div><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;">TCP/IP</span></span></b></div>
    <ul>
        <li>
            <div><span style="font-size: 14px;">IP goes beyond addresses</span></div>
        </li>
        <ul>
            <li>
                <div><span style="font-size: 14px;">Set of conventions computers and servers follow to allow intercommunication</span></div>
            </li>
        </ul>
        <li>
            <div><span style="font-size: 14px;">Fragmentation like in the envelope example are supported by IP</span></div>
        </li>
        <ul>
            <li>
                <div><span style="font-size: 14px;">If missing a packet, you can logically infer which packet you’re missing based on the ones received</span></div>
            </li>
            <ul>
                <li>
                    <div><span style="font-size: 14px;">However, IP doesn’t tell computers what to do in this case</span></div>
                </li>
            </ul>
        </ul>
        <li>
            <div><span style="font-size: 14px;">TCP (Transmission Control Protocol) ensures packets can get to their destination</span></div>
        </li>
        <ul>
            <li>
                <div><span style="font-size: 14px;">Commonly used with IP (TCP/IP)</span></div>
            </li>
            <li>
                <div><span style="font-size: 14px;">Supports sequence numbers that help data get to its destination</span></div>
            </li>
            <ul>
                <li>
                    <div><span style="font-size: 14px;">When missing a packet, a computer can make a request for the missing packet</span></div>
                </li>
                <li>
                    <div><span style="font-size: 14px;">The computer will put packets together to get a whole file</span></div>
                </li>
            </ul>
            <li>
                <div><span style="font-size: 14px;">Also includes conventions for requesting services (port identifiers)</span></div>
            </li>
            <ul>
                <li>
                    <div><span style="font-size: 14px;">To make sure Google knows we’re requesting a webpage and not an email or other service</span></div>
                </li>
            </ul>
        </ul>
    </ul>
    <hr />
    <h2><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;">Ports</span></span></b></h2>
    <ul>
        <li>
            <div><span style="font-size: 14px;">Per TCP, the world has standardized numbers that represent different services</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">If 5.6.7.8 is Google’s IP address, 5.6.7.8;80 (port 80) lets use know that we want a webpage</span></div>
        </li>
        <ul>
            <li>
                <div><span style="font-size: 14px;">80 means http (hypertext transfer protocol)</span></div>
            </li>
            <ul>
                <li>
                    <div><span style="font-size: 14px;">The language that web servers speak</span></div>
                </li>
            </ul>
            <li>
                <div><span style="font-size: 14px;">Google will send the request to their web server via http</span></div>
            </li>
        </ul>
        <li>
            <div><span style="font-size: 14px;">Many websites use secure connections with SSL or HTTPS, which uses the port 443</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Email uses port 25</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Other ports exist as well</span></div>
        </li>
    </ul>
    <hr />
    <div><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;">Protocols</span></span></b></div>
    <ul>
        <li>
            <div><span style="font-size: 14px;">Protocols are just sets of rules</span></div>
        </li>
        <ul>
            <li>
                <div><span style="font-size: 14px;">Humans use these all the time, such as the protocol for meeting people: handshakes</span></div>
            </li>
        </ul>
        <li>
            <div><span style="font-size: 14px;">When a request is made to Google for an image, HTTP tells Google how to respond appropriately</span></div>
        </li>
    </ul>
    <hr />
    <div><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;">UDP</span></span></b></div>
    <ul>
        <li>
            <div><span style="font-size: 14px;">User Datagram Protocol</span></div>
        </li>
        <ul>
            <li>
                <div><span style="font-size: 14px;">Doesn’t guarantee delivery</span></div>
            </li>
            <li>
                <div><span style="font-size: 14px;">Used for video conferencing such as FaceTime</span></div>
            </li>
            <ul>
                <li>
                    <div><span style="font-size: 14px;">Packets can be dropped for the sake of keeping the conversation flowing</span></div>
                </li>
            </ul>
            <li>
                <div><span style="font-size: 14px;">Used anytime you want to keep data coming without waiting for a buffer to fill</span></div>
            </li>
        </ul>
    </ul>
    <hr />
    <div><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;">Routers</span></span></b></div>
    <ul>
        <li>
            <div><span style="font-size: 14px;">Routers have bunches if wires coming and going out of them</span></div>
        </li>
        <ul>
            <li>
                <div><span style="font-size: 14px;">They have a big table with IP addresses and where data should be routed to get to that destination</span></div>
            </li>
            <ul>
                <li>
                    <div><span style="font-size: 14px;">Often, the data is routed to some next router</span></div>
                </li>
            </ul>
        </ul>
        <li>
            <div><span style="font-size: 14px;">Routers purpose is to send data in the direction of a destination</span></div>
        </li>
        <ul>
            <li>
                <div><span style="font-size: 14px;">The next router will send it to another until it reaches a destination</span></div>
            </li>
        </ul>
    </ul><img src="Basics%20of%20Internet.%20TCP_IP,%20Servers,%20Ports,%20Firewalls.html.resources/Screen%20Shot%202019-09-29%20at%203.36.45%20PM.png" height="448" width="1634" />
    <div><span style="font-size: 14px;">The internet is a network of networks (with their own routers)</span></div>
    <ul>
        <li>
            <div><span style="font-size: 14px;">Often multiple ways to go from A to B</span></div>
        </li>
        <ul>
            <li>
                <div><span style="font-size: 14px;">Based in US Military logic to prevent downtime if a particular router goes down</span></div>
            </li>
            <li>
                <div><span style="font-size: 14px;">When multiple packets are sent, like ceu_logo.jpg from Google, they can each take a different path, still getting to their destination eventually</span></div>
            </li>
            <ul>
                <li>
                    <div><span style="font-size: 14px;">Sometimes the internet is busy and the quickest path changes</span></div>
                </li>
            </ul>
        </ul>
    </ul>
    <hr />
    <div><br /></div>
    <div><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;">DHCP - Dynamic Host Configuration Protocol</span></span></b></div>
    <ul>
        <li>
            <div><span style="font-size: 14px;">This protocol makes it so that when a computer you have - a phone, a laptop, etc - it can announce itself and ask for an address</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">The protocol says that these devices will be assigned a numeric address, much like our physical addresses, except unlike our physical addresses (like 123 Main St), this looks like #.#.#.#, where each # is between 0 and 255 (why?)</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Despite the large number of combinations here, there are actually a very large number of devices, to where we are increasingly using something called </span><b><span style="font-size: 14px;">IPv6</span></b><span style="font-size: 14px;"> (the previous was </span><b><span style="font-size: 14px;">IPv4</span></b><span style="font-size: 14px;">), which allows for far more combinations</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">When my computer sends out a request, it has to use this <i>IP address</i> to make sure our data goes to the proper place</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">However, we, as humans, don’t really read addresses like 8.8.8.8 or 192.168.0.1</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">There is a system to “translate” the human-readable </span><b><span style="font-size: 14px;"><i>domain names</i></span></b><span style="font-size: 14px;"> (google.com, facebook.com, cs50.io) to their </span><b><span style="font-size: 14px;">IP address</span></b><span style="font-size: 14px;"> counterparts</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">This service is called </span><b><span style="font-size: 14px;">DNS</span></b><span style="font-size: 14px;">, which allows us to use this translation to get from point A to B</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">We also have </span><b><span style="font-size: 14px;"><i>routers</i></span></b><span style="font-size: 14px;"> or </span><b><span style="font-size: 14px;"><i>gateways</i></span></b><span style="font-size: 14px;">, which know how to take in information, look at where it’s going, and send it to the proper router</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Data doesn’t have to follow the same path each time, but it will get to where it needs to go in around 30 <i>hops</i> or jumps from router to router or gateway to gateway</span></div>
        </li>
    </ul>
    <hr />
    <h2><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;">TCP - Transmission Control Protocol</span></span></b></h2>
    <ul>
        <li>
            <div><span style="font-size: 14px;">Guarantees <i>with high probability</i> that data gets to where it needs to go</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Sometimes, computers <i>drop</i> packets (data) - they get more data than they can, or they miss it entirely</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">TCP allows computers to know if they should resend data</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Port numbers, specifically TCP Port numbers, help identify which service should take which data</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">For example - Data headed to #.#.#.#:80 says that the data should be sent to #.#.#.# and put through port 80, which happens to be a human-defined standard port for HTTP or web requests.</span></div>
        </li>
    </ul>
    <hr />
    <h2><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;">UDP - User Datagram Protocol</span></span></b></h2>
    <ul>
        <li>
            <div><span style="font-size: 14px;">The feature here is </span><b><span style="font-size: 14px;">to <i>not</i> guarantee redelivery</span></b><span style="font-size: 14px;">….what?</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Still fairly common and appropriate</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">For example, video streaming, video conferencing, live communication - we don’t want a retransmission, we would rather stay up to date chronologically</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">In these cases, UDP is actually more optimal than is TCP, can you see why?</span></div>
        </li>
    </ul>
    <hr />
    <h2><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;">Traceroute</span></span></b></h2>
    <ul>
        <li>
            <div><span style="font-size: 14px;">Literally traces the route that information takes from our computer to some destination</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Allows us to see which routers are being used by data to get to where it needs to go</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">This route may change over time and according to web traffic patterns</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">How long does it take for this process of data transfer to take on the internet?</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Traceroute is a program that sends packets to each router on a path to a destination, reporting the time it takes to reach that router</span></div>
        </li>
    </ul>
    <div style="--en-codeblock:true;box-sizing: border-box; padding: 8px; font-family: Monaco, Menlo, Consolas, &quot;Courier New&quot;, monospace; font-size: 12px; color: rgb(51, 51, 51); border-top-left-radius: 4px; border-top-right-radius: 4px; border-bottom-right-radius: 4px; border-bottom-left-radius: 4px; background-color: rgb(251, 250, 248); border: 1px solid rgba(0, 0, 0, 0.14902); background-position: initial initial; background-repeat: initial initial;">
        <div>Mac (Terminal): traceroute domainname.com</div>
        <div>Windows: C:\&gt;tracert www.example.com</div>
    </div>
    <ul>
        <li>
            <div style="margin-bottom:16px;"><span style="font-size: 14px;"><span style="color: rgb(33, 37, 41);"><u>From Sanders Theatre to Berkeley.edu:</u></span></span></div>
        </li>
    </ul><img src="Basics%20of%20Internet.%20TCP_IP,%20Servers,%20Ports,%20Firewalls.html.resources/Screen%20Shot%202019-09-29%20at%203.41.28%20PM.png" height="532" width="948" />
    <ul>
        <li>
            <div><span style="font-size: 14px;">6: Northern Crossroads</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">7-14: A fast connection</span></div>
        </li>
        <ul>
            <li>
                <div><span style="font-size: 14px;">8-9: Chicago</span></div>
            </li>
            <li>
                <div><span style="font-size: 14px;">10-11: Denver</span></div>
            </li>
            <li>
                <div><span style="font-size: 14px;">12-13: Las Vegas</span></div>
            </li>
            <li>
                <div><span style="font-size: 14px;">4: Los Angeles</span></div>
            </li>
        </ul>
        <li>
            <div><span style="font-size: 14px;">19 is where it arrives at Berkeley in 80 ms!</span></div>
        </li>
    </ul>
    <div><br /></div>
    <div style="margin-bottom:16px;"><b><span style="font-size: 14px;"><span style="color: rgb(33, 37, 41);">From Sanders Theatre to CNN.jp</span></span></b></div><img src="Basics%20of%20Internet.%20TCP_IP,%20Servers,%20Ports,%20Firewalls.html.resources/Screen%20Shot%202019-09-29%20at%203.43.45%20PM.png" height="426" width="800" />
    <div><span style="font-size: 14px;"><span style="color: rgb(33, 37, 41);">9-10 jumps from Seattle to Osaka past an ocean!</span></span></div>
    <ul>
        <li>
            <div><b><span style="font-size: 14px;"><span style="color: rgb(33, 37, 41);">Using undersea cabling!</span></span></b></div>
        </li>
    </ul>
    <hr />
    <h2><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;">Undersea Cabling</span></span></b></h2>
    <ul>
        <li>
            <div><span style="font-size: 14px;">We can also traceroute to international destinations, especially those on different continents</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">There is a lot of cabling that connects locations across oceans, including the Pacific and Atlantic</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;"><a href="https://www.youtube.com/watch?v=IlAJJI-qG2k">Video</a></span></div>
        </li>
    </ul>
    <hr />
    <h2><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;">TCP/IP</span></span></b></h2>
    <ul>
        <li>
            <div><span style="font-size: 14px;">How do we make sure that data, even large amounts of data, gets to where it needs to go, and does so “fairly”, so that a single piece of data doesn’t take up more space than it should?</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">How do we send the data and make sure whoever gets it knows what to do with it?</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Maybe we could label the data in order, so that the recipient knowns that whichever data they get belongs in whichever order it’s supposed to</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">Additionally, if some data gets lost along the way, TCP allows us to ask for the missing data and complete it</span></div>
        </li>
    </ul>
    <hr />
    <h2><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;">HTTP - Hyper Text Transfer Protocol</span></span></b></h2>
    <ul>
        <li>
            <div><span style="font-size: 14px;">A very common protocol, which you’ve likely seen before - http://example.com</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;"><i>HTTP</i> is a sort of virtual envelope, which allows computers to communicate with one another, specifically in a webpage context (so between web browsers and servers)</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">We can use nslookup to check the IP address of a web domain - i.e. nslookup www.facebook.com</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">We can pretend to be a browser, and see the response that comes back when we visit a webpage</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">curl -I http://31.13.65.36/ - which tells us that Facebook would prefer we used their domain name (specifically which type of HTTP?)</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">This returns to us the response (if it worked) 200, which means to us, and our computers, that the response was ok</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">We’re likely more familiar with 404, which means things didn’t quite goes as planned</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">What we see here are called <i>headers</i>, which give us additional information about the data we’re given</span></div>
        </li>
    </ul>
    <hr />
    <h2><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;">HTML - Hyper Text Markup Language</span></span></b></h2>
    <ul>
        <li>
            <div><span style="font-size: 14px;">curl without the -I flag lets us see the HTML results, or the data</span></div>
        </li>
        <li>
            <div><span style="font-size: 14px;">This language tells the browser how to display everything from where pictures are located to how to format text on the page</span></div>
        </li>
    </ul>
    <hr />
    <div><br /></div>
    <div><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;">Q&amp;A</span></span></b></div>
    <ol>
        <li>
            <div><b><span style="font-size: 14px;"><span style="color: rgb(51, 51, 51);">Suppose that you turn on your computer and visit </span><a href="https://www.ceu.edu/" rev="en_rl_none">https://www.ceu.edu/</a><span style="color: rgb(51, 51, 51);"> in a browser. Using each of the terms below in a context that makes clear your understanding of each, explain in a paragraph the process by which CEU's home page appears on your screen: DHCP server, DNS server, IP address, packet, TCP port, web server.</span></span></b></div>
            <div><span style="font-size: 14px;"><span style="color: rgba(0, 0, 0, 0.87);">When I turn on my computer and connect to WiFi DHCP gives me a unique IP address and tells the IP address of the local DNS server. DNS converts domain names to IP addresses and vice versa so when I type www.ceu.edu, DNS translates it into a numeric address, the real address of the server where the website is located. Then an HTTP request is sent to the server, which sends a copy of the website (data) to me across TCP/IP. If the request gets approved then data packets will be sent to me. Then these small packets assemble and get displayed to me.</span></span></div>
            <div><span style="font-size: 14px;"><i><span style="color: rgba(0, 0, 0, 0.87);">DHCP server- assigns IP addresses</span></i></span></div>
            <div><span style="font-size: 14px;"><i><span style="color: rgba(0, 0, 0, 0.87);">DNS server - contains the IP addresses and host names (translation)</span></i></span></div>
            <div><span style="font-size: 14px;"><i><span style="color: rgba(0, 0, 0, 0.87);">IP address: #.#.#.#, where each # is between 0 and 255. (identification &amp; location)</span></i></span></div>
            <div><span style="font-size: 14px;"><i><span style="color: rgba(0, 0, 0, 0.87);">Packet: unit of data</span></i></span></div>
            <div><span style="font-size: 14px;"><i><span style="color: rgba(0, 0, 0, 0.87);">TCP port: used to identify the format that is requested. For example, port "80" requests web services, port "25" requests email, etc.</span></i></span></div>
            <div><span style="font-size: 14px;"><i><span style="color: rgba(0, 0, 0, 0.87);">Web Server: processes incoming network requests over HTTP and other protocols</span></i></span></div>
            <div><span style="font-size: 14px;"><i><span style="color: rgba(0, 0, 0, 0.87);"><span style="--en-markholder:true;"><br /></span></span></i></span></div>
        </li>
        <li>
            <div><b><span style="font-size: 14px;"><span style="color: rgb(51, 51, 51);">TCP (tries to) guarantee delivery by ensuring that any lost packets are resent. Why, though, might packets be lost between a sender and receiver?</span></span></b></div>
            <div><span style="font-size: 14px;"><span style="color: rgba(0, 0, 0, 0.87);">UDP: its feature is to not guarantee delivery. If some data gets lost, packets get dropped. It can be due to: malfunction, technical difficulties, overloaded routers. This protocol does not let data to be re-transmitted. Skype, streaming, video games are some examples where UDP is useful because it is better to wait a few seconds than watching something lagging all the time. Re-transmission is not as good as staying up to date chronologically. TCP: Packets can be lost here as well due to the routers being too busy or due to other reasons, but then TCP re-transmits.</span></span></div>
            <div><span style="font-size: 14px;"><span style="color: rgba(0, 0, 0, 0.87);"><span style="--en-markholder:true;"><br /></span></span></span></div>
        </li>
        <li>
            <div><b><span style="font-size: 14px;"><span style="color: rgb(51, 51, 51);">When a server receives a packet, how does it know whether that packet contains (part of) an email, a request for a website, an instant message, or something else altogether?</span></span></b></div>
            <div><span style="font-size: 14px;"><span style="color: rgba(0, 0, 0, 0.87);">SMTP (protocol for emails), on the 'envelope' there will be a port number specified. We need to specify what type of information is inside the envelope, which is represented by the port number.</span></span></div>
            <div><span style="font-size: 14px;"><span style="color: rgba(0, 0, 0, 0.87);"><span style="--en-markholder:true;"><br /></span></span></span></div>
        </li>
        <li>
            <div><b><span style="font-size: 14px;">In what sense are domain names similar to phone numbers like 1-800-COLLECT?</span></b></div>
            <div><span style="font-size: 14px;"><span style="color: rgba(0, 0, 0, 0.87);">Phone number: numeric reference, phone numbers were originally hard wired and the first few numbers told the geographic location of the exchange. Phone numbers are used to identify people. Everybody has a different one. Domain name is like an address as well and helps us locate web pages. There is no duplicate domain address. (IPv6 is needed so that we do not run out of them)</span></span></div>
            <div><span style="font-size: 14px;"><span style="color: rgba(0, 0, 0, 0.87);"><span style="--en-markholder:true;"><br /></span></span></span></div>
        </li>
        <li>
            <div><b><span style="font-size: 14px;">If not already familiar, read up on "bandwidth" and "latency" (as via Google) and then, in your own words, distinguish the two concepts as they relate to internet speed.</span></b></div>
            <div><span style="font-size: 14px;"><span style="color: rgba(0, 0, 0, 0.87);">Latency is basically the time it takes to send a packet from the source to the destination. Bandwidth is the maximum data transfer rate. So high latency is not good because it takes a lot of time to get a packet from the source to the destination, but with high bandwidth, we can reduce this time.</span></span></div>
            <div><span style="font-size: 14px;"><span style="color: rgba(0, 0, 0, 0.87);"><span style="--en-markholder:true;"><br /></span></span></span></div>
        </li>
        <li>
            <div><b><span style="font-size: 14px;"><span style="color: rgb(51, 51, 51);">How does every website that you visit know (and likely log!) your IP address?</span></span></b></div>
            <div><span style="font-size: 14px;"><span style="color: rgba(0, 0, 0, 0.87);">The web server needs an IP to be able to establish the connection and communicate, where to send the data requested etc. It is usually done in the NCSA format. Anonymization can be done via: Proxy, VPN, Tor, NAT, Gateway or Firewall. You'll know the following information if you know one’s IP address: approximate location based on IP/ISP, whether they have a static or dynamic IP, if they use traceroute (+ see the latency), with telnet or nmap open ports can be found as well. IP address is usually logged to show you relevant advertisements. The information is contained in the Packet Header.</span></span></div>
            <div><span style="font-size: 14px;"><span style="color: rgba(0, 0, 0, 0.87);"><span style="--en-markholder:true;"><br /></span></span></span></div>
        </li>
        <li>
            <div><b><span style="font-size: 14px;"><span style="color: rgb(51, 51, 51);">If not already familiar, read up on "DNS hijacking," and in your own words, explain what it means for an adversary to hijack a website via DNS.</span></span></b></div>
            <div><span style="font-size: 14px;"><span style="color: rgba(0, 0, 0, 0.87);">When we open a website, DNS translates the domain to an IP and then we can access the website. DNS hijacking means to redirect requests of a specific server to another and it is achieved by the translation of a domain to a fake IP address that takes the person to a malicious website and eventually people or companies may lose data (passwords, accounts etc.). One of the most popular DNS hijacking case is when hackers redirected traffic to all 36 of a Brazilian bank's domains.</span></span></div>
            <div><b><span style="font-size: 14px;"><i><a href="https://www.wired.com/story/what-is-dns-hijacking/">Optional Reading</a></i></span></b></div>
        </li>
    </ol>
    <div><b><span style="font-size: 14px;"><i><span style="--en-markholder:true;"><br /></span></i></span></b></div>
    <div><b><span style="font-size: 14px;"><span style="--en-highlight:yellow;background-color: #ffef9e;"><i>Practice Questions:</i></span></span></b></div>
    <ul>
        <li>
            <div><b><span style="font-size: 14px;"><i>What is the internet?</i></span></b></div>
        </li>
        <li>
            <div><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">What does it mean if a URL begins with https:// as opposed to http://?</span></span></b></div>
        </li>
        <li>
            <div><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">What does it mean for a computer to have a private IP address (e.g. one that begins with 10., 192.168., or 172.16.)?</span></span></b></div>
        </li>
        <li>
            <div><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">Why do TCP/IP packets from one computer to another not always take the same amount of time to arrive at their destination?</span></span></b></div>
        </li>
        <li>
            <div><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">Today's "home routers" are often much more than routers alone. They are also "access points" (aka APs) and "firewalls" too. What is an access point (AP)? And what is a firewall?</span></span></b></div>
        </li>
        <li>
            <div><b><span style="font-size: 14px;"><span style="color: rgb(0, 0, 0);">Whether or not you have internet service at home, Google around for an internet service provider (ISP) that provides internet service to your neighborhood (or somewhere nearby). What's the ISP you found? What speeds does the ISP you found offer? At what cost? And do they offer symmetric (i.e., identical) upload and download speeds, or do they differ?</span></span></b></div>
        </li>
    </ul>
    <div><b><span style="font-size: 14px;"><i><span style="--en-markholder:true;"><br /></span></i></span></b></div>
    <div><b><span style="font-size: 14px;"><i><span style="--en-markholder:true;"><br /></span></i></span></b></div>
    <div><b><span style="font-size: 14px;"><i><span style="--en-markholder:true;"><br /></span></i></span></b></div>
    <div><b><span style="font-size: 14px;"><i>Sources:</i></span></b></div>
    <div><a href="http://web.stanford.edu/class/cs101/lecture10.html#/4" rev="en_rl_none">http://web.stanford.edu/class/cs101/lecture10.html#/4</a></div>
    <div><a href="https://web.stanford.edu/class/cs101/network-2-internet.html" rev="en_rl_none">https://web.stanford.edu/class/cs101/network-2-internet.html</a></div>
    <div><a href="https://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm" rev="en_rl_none">https://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm</a></div>
    <div><a href="https://web.stanford.edu/class/cs101/network-1-introduction.html" rev="en_rl_none">https://web.stanford.edu/class/cs101/network-1-introduction.html</a></div>
</body>

</html>
