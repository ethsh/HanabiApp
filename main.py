from Common.Game import HanabiGame
from Server.Server import *
from Client.PlayerClient import *
from Common.Cards import *
from time import sleep
from Common.HanabiProtocol import *


def main():
    # player1 = Player("Player1")
    # player2 = Player("Player2")
    # player3 = Player("Player3")
    # players_list = [player1, player2, player3]
    # hanabi = HanabiGame(players_list, GameOptions.INCLUDING_RAINBOW_PILE)


    # deck = Deck()
    # new_card = deck.draw_card()
    # turn = NumberTurnOperation(Numbers.ONE)
    # turn = ColorTurnOperation(Colors.RED)

    # while new_card is not None:
    #     print str(new_card) + str(turn.card_result(new_card))
    #     new_card = deck.draw_card()
    try:
        server = HanabiServer()
        player1 = PlayerClient("Player1")
        player2 = PlayerClient("Player2")
        player1.connect()
        player2.connect()
        player1.send_message("Player1_message")
        player2.send_message("Player2_message")
        while True:
            sleep(5)
        pass
    except Exception:
        pass


if __name__ == "__main__":
    main()
