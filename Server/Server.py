import socket
import sys
from thread import *
import time
from Common.Player import Player
from Common.HanabiProtocol import HanabiMessage, PacketType
import select


HOST = 'localhost'  # Symbolic name meaning all available interfaces
PORT = 8888         # Arbitrary non-privileged port

CLIENT_REGISTRATION_TIMEOUT = 5
SECONDS_IN_MINUTE = 60

players_list = []


class HanabiServer:
    def __init__(self):
        self.sock = HanabiServer.create_and_start_server_socket()
        start_new_thread(self.wait_for_clients, ())

    def wait_for_clients(self):
        while 1:
            # wait to accept a connection - blocking call
            conn, addr = self.sock.accept()
            print 'Connected with ' + addr[0] + ':' + str(addr[1])

            # start new thread takes 1st argument as a function name to be run,
            # second is the tuple of arguments to the function.
            start_new_thread(clientthread, (conn,))

        self.sock.close()

    @staticmethod
    def create_and_start_server_socket():
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

    def start_game(self):

        pass


class PlayerConnection:
    def __init__(self, name, conn):
        self.name = name
        self.conn = conn

    def __str__(self):
        return self.name

    def draw_card(self, card):
        self.conn.send(HanabiMessage(PacketType.RECEIVE_CARD, card=card).serialize_message())


# Function for handling connections. This will be used to create threads
def clientthread(conn):
    # Sending message to connected client
    # conn.send('Welcome to the server. Type something and hit enter\n')  # send only takes string

    conn.setblocking(0)

    ready = select.select([conn], [], [], CLIENT_REGISTRATION_TIMEOUT)
    if not ready[0]:
        conn.close()
        return

    name = rec_client_name(conn)
    if name is None:
        conn.close()
        return

    player = PlayerConnection(name, conn)
    players_list.append(player)

    print '\nAll players are: '
    print ' '.join(str(p) for p in players_list)
    print '\n'

    while True:
        ready = select.select([conn], [], [])
        if not ready[0]:
            continue
        data = conn.recv(4096)
        print '\n' + data + '\n'

    # came out of loop
    conn.close()


def rec_client_name(conn):
    data = conn.recv(4096)
    # save the player

    msg = HanabiMessage.deserialize_msg(data)
    if not (msg.msg_type == PacketType.REGISTRATION):
        return
    name = msg.kwargs['name']
    return name
