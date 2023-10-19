[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/DIu74VZ7)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11548191&assignment_repo_type=AssignmentRepo)
# Bonus:  Build a DNS Server

Implement a basic DNS server that can perform both **iterative** and **recursive** resolution.

# Requirements:

* Must support simple DNS requests to UDP port 53.
* Create DNS cache structure and return any answers from cache if found. Update cache according to requests.
* If client requests recursive resolution, pass on request to "real" DNS server and respond back with answer. You must cache the result.
* If client requests iterative resolution, perform basic requests to root server, TLD server, and authoritative servers as required. (Note that you may simplify this by using your cache.)

The goal will be to maintain the DNS structure for queries in a static file such that you can examine what has been cached and requested from clients.  Your code will be tested as a stand-alone DNS server (meaning that it will just be turned on with any configuration you require (which will be documented) and used in place of the default DNS server.  

# Difficulty

This difficulty of this depends on your approach but is more involved than the IMCP/Scapy challenges.  The DNS server does not have to be complete or robust, but should answer and cache basic queries and responses (meaning that it could be used/functional for most basic operations). This can be easily written in Python as there are numerous libraries that can help with this.   The challenge is dealing with caching and forwarding requests of records.  You will need to review the details of the requirements for DNS but will give you a strong understanding of how this works.  You are also welcome to build in Java (more difficult).  

# Submission

Your solution must be pushed back upstream before the due date in addition to submitting the link to your repo to Canvas.  In your README.md file, you **must** include information on how to run your code. 

# Value

This bonus (base activity) is worth 1 lab units and will be tested on an all or nothing level (it must work).

# Caution

The challenge here is gaining an understanding of how to use the DNS libraries.  Be mindful of the fact that there are numerous resources available on the internet and if you use resources, ensure you document your code.   



