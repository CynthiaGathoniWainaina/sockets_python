# P15/1712/2017-WAINAINA CYNTHIA GATHONI
# CSC 315: DISTRIBUTED SYSTEMS
# GROUP 1 : SOCKETS IPC CLIENT FILE

import socket
import sys


def client_program():
    client_socket = socket.socket()
    port = 2500
    client_socket.connect(('127.0.0.1', port))
    message = input(" -> ")  # take input

    client_socket.send(message.encode())  # send message
    data = client_socket.recv(1024).decode()  # receive response

    print('Received from server: Send me 2 numbers to subtract')  # show in terminal

    p = int(input("Enter a number: "))
    q = input("Enter another number: ")
    q = int(q)
    client_socket.send(str(p).encode())
    client_socket.send(str(q).encode())

    m = client_socket.recv(2048)
    m = m.decode()
    m = int(m) 
    print("The result is:" + str(m)) 
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
