
# DNS Server

A basic DNS server that can perform both **iterative** and **recursive** resolution.
Can help cache dns requests in an enterprise network , therefore optimizing internet performance for frequently visited websites.


# Requirements:

* Must support simple DNS requests to UDP port 53.
* Create DNS cache structure and return any answers from cache if found. Update cache according to requests.
* If client requests recursive resolution, pass on request to "real" DNS server and respond back with answer. You must cache the result.
* If client requests iterative resolution, perform basic requests to root server, TLD server, and authoritative servers as required. (Note that you may simplify this by using your cache.)

The goal will be to maintain the DNS structure for queries in a static file such that you can examine what has been cached and requested from clients. Code will be tested as a stand-alone DNS server (meaning that it will just be turned on with any configuration you require (which will be documented) and used in place of the default DNS server.  





