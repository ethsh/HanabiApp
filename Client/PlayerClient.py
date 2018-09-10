import socket
import select
from Common.HanabiProtocol import PacketType, HanabiMessage
from thread import *
from Common.Player import Player

HOST = 'localhost'  # Symbolic name meaning all available interfaces
PORT = 8888         # Arbitrary non-privileged port


class PlayerClient:
    def __init__(self, name):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name = name
        self.player = Player()

    def connect(self):
        self.client_socket.connect((HOST, PORT))
        start_new_thread(self.recv_func, ())
        self.register()

    def disconnect(self):
        self.client_socket.close()
        print 'Socket closed'

    def register(self):
        self.send_message(HanabiMessage(PacketType.REGISTRATION, name=self.name).serialize_message())

    def send_message(self, data):
        self.client_socket.send(data)

    def handle_message(self, msg):
        pass

    def recv_func(self):
        while True:
            ready = select.select([self.client_socket], [], [])
            if not ready[0]:
                continue
            data = self.client_socket.recv(4096)
            msg = HanabiMessage.deserialize_msg(data)
            print '\n' + msg.msg_type + '\n'
            self.handle_message(msg)

        self.client_socket.close()
        return

