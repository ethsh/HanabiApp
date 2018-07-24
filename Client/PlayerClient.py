import socket
from Common.HanabiProtocol import *
from thread import *

HOST = 'localhost'  # Symbolic name meaning all available interfaces
PORT = 8888         # Arbitrary non-privileged port


class PlayerClient:
    def __init__(self, name):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name = name

    def connect(self):
        self.client_socket.connect((HOST, PORT))
        start_new_thread(self.recv_func, ())
        self.register()

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

    def register(self):
        self.send_message(HanabiProtocol.create_registration_packet(PacketDirection.Client2Server, self.name))
