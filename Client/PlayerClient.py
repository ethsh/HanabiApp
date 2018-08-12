import socket
import select
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
        try:
            while True:
                ready = select.select([self.client_socket], [], [])
                if not ready[0]:
                    continue
                data = self.client_socket.recv(4096)
                print '\n' + data + '\n'
        except KeyboardInterrupt:
            print "bye"

        self.client_socket.close()

        return

    def disconnect(self):
        self.client_socket.close()
        print 'Socket closed'

    def register(self):
        self.send_message(HanabiProtocol.create_registration_packet(PacketDirection.Client2Server, self.name))
