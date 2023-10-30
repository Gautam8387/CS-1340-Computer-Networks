# Gautam Ahuja
# CS-1340: Computer Networks
# Assignment 4: Transport Layer - Transmission Control Protocol (TCP)
# server.py
# This file contains the server-side code for the TCP implementation of the CS Course Advisor.
# The server is responsible for sending the question list to the client and receiving the client's question number.
# The server then calls the appropriate function (from ```utils.py```) to answer the question and sends the answer to the client using the next() function.
# The server then waits for the next question number from the client.
# The server closes the connection with the client when the client sends 'q'.
# The server is multithreaded, i.e., it can handle multiple clients (10) at the same time.


# ============================= IMPORTS ============================= #
import socket
import json
import sys
import os
import time
from utils import *
import threading

# ============================= SERVER SETUP ============================= #
# Create a TCP/IP socket
# AF_INET = IPv4, SOCK_STREAM = TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Set up Server IP and Port
IP = '127.0.0.1'
PORT = 5000

# Bind the socket to the port
server.bind((IP, PORT))
server.listen(10)
print("Server UP and Running...")
print(f"Listening on {IP}:{PORT}\nWaiting for a Connection...\n\n")

# ============================= CLIENT TCP COMMUNICATION SETUP ============================= #

def client_handler(client_socket, client_address):
    # For each new client
    print(f"Client {client_address} Connected!")
    # Call the init() function from utils.py which sends the question list to the client
    init(client_socket)
    # Continuously listen for client's question number
    while True:
        question_number = client_socket.recv(1024).decode()
        # If client sends 'q', close connection with client
        if question_number == 'q':
            break
        # Check if the question_number can be converted to an integer
        if not question_number.isdigit():
            to_invalid = '''------------------------------\nInvalid input. Please enter a valid integer or 'q'.\n------------------------------'''
            next(client_socket, to_invalid)
            continue
        # Convert question_number to int
        question_number = int(question_number)
        # If question_number is invalid, send error message to client
        if question_number < 1 or question_number > len(question_list):
            to_invalid = '''------------------------------\nInvalid question number\n------------------------------'''
            next(client_socket, to_invalid)
            continue
        # Else, call the function corresponding to the question_number
        if (question_number == 9):
            client_socket.send("------------------------------\n(pre-req) Please enter the course name: ".encode())
            course_name = client_socket.recv(1024).decode()
            to_send = q9(course_name)
        else:
            to_send = answer_list[question_number-1]()

        to_send = "======================================================\n"+to_send+"\n======================================================"
        next(client_socket, to_send)

    # Close connection with client
    to_close = "======================================================\nThank you for using CS Course Advisor!" 
    client_socket.send(to_close.encode())
    print(f"\nDisconnecting from {client_address}...")
    client_socket.close()
    print(f"Connection with {client_address} Closed.\n")

# ============================= SERVER LOGIC ============================= #
if __name__ == "__main__":
    while True:
        (client_socket, client_address) = server.accept()
        print(f"Connection Established with {client_address}")
        # Assign a new thread to each client
        client_thread = threading.Thread(target=client_handler, args=(client_socket, client_address))
        client_thread.start()
        # client_handler(client_socket, client_address)
        # print(f"\nDisconnecting from {client_address}...")
        # client_socket.close()
        # print(f"Connection with {client_address} Closed.\n")

# ============================= SERVER OFF ============================= #
print("\nServer Shutting Down...")
server.close()
print("Server Shut Down.")
