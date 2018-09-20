from Cards import *
from TurnOperation import *

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

    def end_game(self):
        for player in self.__players_list:
            player.leave_game()

    def perform_turn(self):
        current_player = self.__players_list[self.current_player_index]
        turn = current_player.perform_turn()
        self.handle_turn_operation(current_player, turn)
        self.current_player_index = (self.current_player_index + 1) % len(self.__players_list)

    def handle_turn_operation(self, current_player, turn):
        if turn.op_type == OperationType.BurnCard:
            self.handle_burn_card(current_player, turn)
        elif turn.op_type == OperationType.PlaceCard:
            self.handle_place_card(current_player, turn)
        else:
            raise Exception('Operation Not Implemented!')

    def handle_burn_card(self, current_player, turn):
        self.burnt_cards.burn_card(turn.card_to_burn)
        current_player.receive_card(self.deck.draw_card())

    def handle_place_card(self, current_player, turn):
        card_to_place = turn.card_to_place
        placing_options = self.board.can_place_card(card_to_place)
        if len(placing_options) == 0:
            # TODO - handle this
            pass
        else:
            if len(placing_options) > 1:
                # TODO - handle this as well
                pass
            else:
                # only one option to place card
                self.board.place_card(card_to_place, placing_options[0])
            current_player.receive_card(self.deck.draw_card())

    def handle_update_player(self, current_player, turn):
        return "March"



    def view_players(self, asking_player):
        temp_players_list = [player for player in self.__players_list if player.name != asking_player.name]
        return temp_players_list

    def print_game_state_for_player(self, asking_player):
        print 'NOT IN GAME STR!!!!!'
        players_str = '\n'.join(map(str, self.view_players(asking_player)))
        print 'Game Status\n'                               \
              'Players are:\n{players_str}\n'               \
              'The board status is:\n{board}\n'             \
              'And the burnt cards are:\n{burnt_cards}'.    \
            format(players_str=players_str, board=str(self.board), burnt_cards=str(self.burnt_cards))

    def __str__(self):
        print 'IN GAME STR!!!!!'
        players_str = '\n'.join(map(str, self.__players_list))
        return 'Game Status\n'                              \
               'Players are:\n{players_str}\n'              \
               'The board status is:\n{board}\n'            \
               'And the burnt cards are:\n{burnt_cards}'.   \
            format(players_str=players_str, board=str(self.board), burnt_cards=str(self.burnt_cards))
