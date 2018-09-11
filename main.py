from Common.Game import HanabiGame
from Common.Cards import *
from Common.Player import Player


def main():
    player1 = Player("Player1")
    player2 = Player("Player2")
    player3 = Player("Player3")
    players_list = [player1, player2, player3]
    hanabi = HanabiGame(players_list, GameOptions.INCLUDING_RAINBOW_PILE)
    while True:
        hanabi.perform_turn()


if __name__ == "__main__":
    main()
