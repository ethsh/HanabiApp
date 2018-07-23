from Server.Server import *
from Client.PlayerClient import *
from time import sleep


def main():
    server = HanabiServer()
    player1 = PlayerClient()
    player2 = PlayerClient()
    print 'as'
    player1.connect()
    player2.connect()
    player1.send_message("Player1")
    player2.send_message("Player2")
    while True:
        sleep(5)
    pass

if __name__ == "__main__":
    main()
