import socket
import sys
from thread import *

HOST = 'localhost'  # Symbolic name meaning all available interfaces
PORT = 8888         # Arbitrary non-privileged port

players_list = []


class HanabiServer:
    def __init__(self):
        self.s = HanabiServer.create_and_start_socket()
        start_new_thread(self.wait_for_clients, ())

    def wait_for_clients(self):
        while 1:
            # wait to accept a connection - blocking call
            conn, addr = self.s.accept()
            print 'Connected with ' + addr[0] + ':' + str(addr[1])

            # start new thread takes 1st argument as a function name to be run,
            # second is the tuple of arguments to the function.
            start_new_thread(clientthread, (conn,))

        self.s.close()

    @staticmethod
    def create_and_start_socket():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print 'Socket created'

        # Bnd socket to local host and port
        try:
            sock.bind((HOST, PORT))
        except socket.error as msg:
            print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()

        print 'Socket bind complete'

        # Start listening on socket
        sock.listen(0)
        print 'Socket now listening'
        return sock


# Function for handling connections. This will be used to create threads
def clientthread(conn):
    # Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string
     
    # infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data: 
            break
     
        conn.sendall(reply)
     
    # came out of loop
    conn.close()

