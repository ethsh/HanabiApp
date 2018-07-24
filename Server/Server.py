import socket
import sys
from thread import *
import time
from Common.Player import Player
from Common.HanabiProtocol import HanabiProtocol, PacketType, PacketDirection
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


# Function for handling connections. This will be used to create threads
def clientthread(conn):
    # Sending message to connected client
    # conn.send('Welcome to the server. Type something and hit enter\n')  # send only takes string

    conn.setblocking(0)

    ready = select.select([conn], [], [], CLIENT_REGISTRATION_TIMEOUT)
    if not ready[0]:
        conn.close()
        return

    data = conn.recv(4096)

    # save the player
    # TODO : the name isnt data. need to parse the packet

    pkt_res = HanabiProtocol.parse_message(data)
    if not (pkt_res[0] == PacketType.Registration and pkt_res[1] == PacketDirection.Client2Server):
        conn.close()
        return

    name = pkt_res[2]
    player = Player(name, conn)
    players_list.append(player)

    print 'All players are: '
    print ' '.join(str(p) for p in players_list)

    while True:
        time.sleep(5)
    # came out of loop
    # conn.close()

