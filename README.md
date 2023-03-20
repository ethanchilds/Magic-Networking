# Overview

This networking software at its works like an extremely simple remote data storage and retrieval system for a collection of magic cards. To start this program from the client side, simply set your directory in command terminal to the file folder containing this client.py file and run the command "python client.py", this will start the script and give the user options to interact with server and retrieve or edit the data file local to the server. However, before starting the client, one must first start the server. To do this you can just run the python file in any IDE.

When choosing to write this program, I did not intend to write a data storage and retrieval client-server model, my only goal was to gain a better understanding of networking, its associated protocols, and how I could implement them in my own software. This resulted in me first learning about socket programming in python, implementing a very basic model that connected a server and a client, and finally developing out this basic model to offer more robust ways for the client to interact with the server.

[Software Demo Video](https://youtu.be/VbiEs14mn5M)

# Network Communication

As stated previously, the networking model used in this software is a client-server model.

This model is built using TCP protocol and both the server and client are using port 65432.

Messages are sent between the client and server using a utf-8

# Development Environment

Tools:
* Visual Studio Code

Language and Libraries
* Python
* socket
* threading
* json

# Useful Websites

* [youtube.com](https://www.youtube.com/watch?v=3QiPPX-KeSc)
* [realpython.com](https://realpython.com/python-sockets/)
* [geeksforgeeks.com](https://www.geeksforgeeks.org/append-to-json-file-using-python/)

# Future Work

* In the future I would like to improve upon this project by offering an even more expansive and robust number of ways that clients can interact with the server. At the moment, there is very few ways that the client can actually interact with the server and they are very fixed methods of interaction, so in the future I would like to create a more flexible client-server model.
* One issue about this software that I was very frustrated about was how rigid I had to make it in order to maintain the order of messaging sending and recieving. It may have been due to my lack of experience with networking software construction, but I found myself unhappy with the structure of the model. In the future I would definietly like to figure out a way to send and recieve messages in a much more flexible way.
* One thing I had to give up on with this project was trying to implement a user GUI for the server and client. The issue that I ran into with this project that prevented me from implementing the GUI was the fact that both GUI and networking softwares run until they are closed, and as a result when I tried to implement the GUI, I could not get the GUI and network to run in parallel. In the future I would like to try this out again as I would really like to figure out how to get these two processes to run in parallel.
