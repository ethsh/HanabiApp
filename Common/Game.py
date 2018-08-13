from Cards import *

CARDS_PER_PLAYER = 4

class HanabiGame:
    def __init__(self, players_list, game_option):
        self.players_list = players_list
        self.game_option = game_option
        self.deck = Deck()
        self.board = BoardCards(self.game_option)
        self.burnt_cards = BurntCards()
        self.init_game()
        print self

    def init_game(self):
        for player in self.players_list:
            for i in xrange(CARDS_PER_PLAYER):
                player.receive_card(self.deck.draw_card())

    def __str__(self):
        players_str = '\n'.join(map(str, self.players_list))
        return 'Game Status\n' \
              'Players are: {players_str}\nThe board status is: {board}\nAnd the burnt cards are: {burnt_cards}'.\
            format(players_str=players_str, board=str(self.board), burnt_cards=str(self.burnt_cards))
