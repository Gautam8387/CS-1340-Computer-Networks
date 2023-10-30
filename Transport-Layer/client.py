# Gautam Ahuja
# CS-1340: Computer Networks
# Assignment 4: Transport Layer - Transmission Control Protocol (TCP)
# client.py
# This file contains the client-side code for the TCP implementation of the CS Course Advisor.
# The client is responsible for receiving the question list from the server and sending the question number to the server.
# The client then waits for the answer from the server and prints it.
# The client closes the connection with the server when the user sends 'q'.


# ============================= IMPORTS ============================= #
import socket
import json
import sys
import os

# ============================= CLIENT SETUP ============================= #
# Create a TCP/IP socket
# AF_INET = IPv4, SOCK_STREAM = TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set up IP and Port to connect to that of the server
IP = '127.0.0.1'
PORT = 5000
# Connect to the server
client_socket.connect((IP, PORT))

# ============================= WELCOMING SOCKET ============================= #
# Print Welcoming Message and Question List from Server (init() function)
print(client_socket.recv(1024).decode())

# ============================= CLIENT TCP COMMUNICATION SETUP ============================= #
## Continuously listen for user input
while True:
    question_number = input()
    # Check if the input is a valid integer or 'q'
    if question_number.isdigit():
        question_number = int(question_number)
    else:
        # If not a valid integer, check if it's 'q' to quit
        if question_number.lower() == 'q':
            client_socket.send(question_number.encode())
            print(client_socket.recv(2048).decode())
            break
        else:
            print("Invalid input. Please enter a valid integer or 'q'.")
            continue
    # Send the question number to the server
    client_socket.send(str(question_number).encode())
    # check if question sent is 9
    if question_number == 9:
        # Receive a question from the server
        print(client_socket.recv(1024).decode())
        # send user input to the server
        course_name = input()
        client_socket.send(course_name.encode())
    
    # Print the response from the server
    response = client_socket.recv(2048).decode()
    print(response)

# Close connection with the server
client_socket.close()
# ============================= END OF CODE ============================= #
