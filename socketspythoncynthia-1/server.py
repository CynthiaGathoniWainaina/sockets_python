# P15/1712/2017-WAINAINA CYNTHIA GATHONI
# CSC 315: DISTRIBUTED SYSTEMS
# GROUP 1 : SOCKETS IPC SERVER FILE


import socket
import sys


def server_program():
    host = socket.gethostname()
    port = 2500
    s = socket.socket() 
    print
    "Socket was created successfully"
    s.bind(('', port))
    print
    "Socket binded to %s" % (port)
    s.listen(5)
    print
    "Socket is listening" 
    conn, address = s.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        conn.send(data.encode('utf-8'))   # send data to the client     
        p = int((conn.recv(2048)).decode())
        q = int((conn.recv(2048)).decode())
        m = str(p-q).encode()
        conn.send(m)
    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()

