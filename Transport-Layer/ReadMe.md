## Gautam Ahuja
## CS-1340: Computer Networks
## Assignment 3: Transport Layer - Transmission Control Protocol (TCP)
## Documentation

### Server (```server.py```)
- This file contains the server-side code for the TCP implementation of the CS Course Advisor.
- The server is responsible for sending the question list to the client and receiving the client's question number.
- The server then calls the appropriate function (from ```utils.py```) to answer the question and sends the answer to the client using the next() function.
- The server then waits for the next question number from the client.
- The server closes the connection with the client when the client sends ```q```.
- The server is multithreaded, i.e., it can handle multiple clients (10) at the same time.

### Client (```client.py```)
- This file contains the client-side code for the TCP implementation of the CS Course Advisor.
- This file contains the client-side code for the TCP implementation of the CS Course Advisor.
- The client is responsible for receiving the question list from the server and sending the question number to the server.
- The client then waits for the answer from the server and prints it.
- The client closes the connection with the server when the user sends 'q'.

### Utilities (```utils.py```)
The ```utils.py``` file enables the server to answer the questions asked by the client. It contains the following:
- ```question_list``` : A list of questions to be sent to the client.
- ```core_courses``` : A list of core courses and their credits.
- ```courses_prereq``` : A dictionary of courses and their pre-requisites.
- ```answer_list``` : A list of functions corresponding to the questions in ```question_list```.
- ```init()``` : A function that sends the question list to the client.
- ```next()``` : A function that sends the next question to the client.
- ```q1()``` : A function that returns the answer to question 1.
- ```q2()``` : A function that returns the answer to question 2.
- ```q3()``` : ... and so on.

### To Run:
Use the following commands to run the server and client:
- Set up the server Host IP and Port in ```server.py```. Execute the following command to run the server:
    - The Server can support multiple clients (10) at a time in a multithreaded manner.
```
python3 server.py
```
- Set up the IP and Port in ```client.py``` (same as server). Execute the following command to run the client:
```
python3 client.py
```
- The client will ask for the question number. Enter the question number and press enter.