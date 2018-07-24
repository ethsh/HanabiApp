from Server.Server import *
from Client.PlayerClient import *
from time import sleep
from Common.HanabiProtocol import *


def main():
    server = HanabiServer()
    player1 = PlayerClient("Player1")
    player2 = PlayerClient("Player2")
    player1.connect()
    player2.connect()
    while True:
        sleep(5)
    pass

if __name__ == "__main__":
    main()
