import socket
from time import sleep
from thread import *

HOST = 'localhost'  # Symbolic name meaning all available interfaces
PORT = 8888         # Arbitrary non-privileged port


class PlayerClient:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass

    def connect(self):
        self.client_socket.connect((HOST, PORT))
        print 'Socket connected and recv thread started'
        start_new_thread(self.recv_func, ())
        print 'Socket connected and recv thread started'

    def send_message(self, data):
        self.client_socket.send(data)

    def recv_func(self):
        while True:
            try:
                reply = self.client_socket.recv(131072)
                if not reply:
                    break
                print "recvd: ", reply
            except KeyboardInterrupt:
                print "bye"
                break
        self.client_socket.close()
        return



        pass

    def disconnect(self):
        self.client_socket.close()
        print 'Socket closed'
    pass
