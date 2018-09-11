from Cards import *
import copy

CARDS_PER_PLAYER = 4


class HanabiGame:
    def __init__(self, players_list, game_option):
        if len(players_list) < 2:
            raise Exception('can\'t play a game with less than 2 players!')
        self.__players_list = players_list
        for player in self.__players_list:
            player.enter_game(self)
        self.current_player_index = 0
        self.game_option = game_option
        self.deck = Deck()
        self.board = BoardCards(self.game_option)
        self.burnt_cards = BurntCards()
        self.init_game()

    def init_game(self):
        for player in self.__players_list:
            for i in xrange(CARDS_PER_PLAYER):
                player.receive_card(self.deck.draw_card())

    def perform_turn(self):
        current_player = self.__players_list[self.current_player_index]
        current_player.perform_turn()
        self.current_player_index = (self.current_player_index + 1) % len(self.__players_list)

    def view_players(self, asking_player):
        temp_players_list = [player for player in self.__players_list if player.name != asking_player.name]
        return temp_players_list

    def print_game_state_for_player(self, asking_player):
        print 'NOT IN GAME STR!!!!!'
        players_str = '\n'.join(map(str, self.view_players(asking_player)))
        print 'Game Status\n' \
               'Players are:\n {players_str}\nThe board status is: {board}\nAnd the burnt cards are: {burnt_cards}'. \
            format(players_str=players_str, board=str(self.board), burnt_cards=str(self.burnt_cards))

    def __str__(self):
        print 'IN GAME STR!!!!!'
        players_str = '\n'.join(map(str, self.__players_list))
        return 'Game Status\n' \
              'Players are:\n {players_str}\nThe board status is: {board}\nAnd the burnt cards are: {burnt_cards}'.\
            format(players_str=players_str, board=str(self.board), burnt_cards=str(self.burnt_cards))
