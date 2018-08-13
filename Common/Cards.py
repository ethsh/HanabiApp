import abc
from enum import Enum
import itertools
from random import shuffle


Colors = Enum('Colors', 'RED GREEN BLUE WHITE YELLOW RAINBOW')
Numbers = Enum('Numbers', 'ONE TWO THREE FOUR FIVE')
Operations = Enum('Operations', 'COLOR NUMBER')

GameOptions = Enum('GameOptions', 'ONLY_COLORS_PILES INCLUDING_RAINBOW_PILE')

initial_cards_amounts = {Numbers.ONE : 3, Numbers.TWO : 2, Numbers.THREE : 2, Numbers.FOUR : 2, Numbers.FIVE : 1}


class Card:
    def __init__(self, number, color):
        self.color = color
        self.number = number

    def get_color(self):
        return self.color

    def get_number(self):
        return self.number

    def __str__(self):
        return '{number}-{color}'.format(number=self.get_number(), color=self.get_color())


class AbstractTurnOperation:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def card_result(self, card):
        pass


class NumberTurnOperation(AbstractTurnOperation):
    def __init__(self, number):
        self.number = number

    def card_result(self, card):
        return card.get_number() == self.number


class ColorTurnOperation(AbstractTurnOperation):
    def __init__(self, color):
        self.color = color

    def card_result(self, card):
        return card.get_color() == self.color or card.get_color() is Colors.RAINBOW


class Deck:
    @staticmethod
    def __get_initial_amount_of_cards_in_deck(card_number, card_color):
        if card_color is Colors.RAINBOW:
            return 1
        return initial_cards_amounts[card_number]

    @staticmethod
    def __create_card_deck():
        cards = []
        for (number, color) in itertools.product(Numbers, Colors):
            card_amount = Deck.__get_initial_amount_of_cards_in_deck(number, color)
            cards.extend([Card(number, color)] * card_amount)
        return cards

    def __init__(self):
        self.deck = Deck.__create_card_deck()
        self.shuffle_deck()

    def shuffle_deck(self):
        shuffle(self.deck)

    def draw_card(self):
        if self.get_num_of_remaining_cards() is 0:
            return None
        card = self.deck[0]
        self.deck = self.deck[1:]
        return card

    def get_num_of_remaining_cards(self):
        return len(self.deck)


class BurntCards:
    def __init__(self):
        self.cards = []

    def burn_card(self, card):
        self.cards.extend(card)

    def __str__(self):
        return ','.join(map(str, self.cards))


class BoardCards:
    def __init__(self, game_option):
        self.game_option = game_option
        self.card_piles = {}
        for color in Colors:
            self.card_piles[color] = []
        if self.game_option is GameOptions.ONLY_COLORS_PILES:
            self.card_piles.pop(Colors.RAINBOW, None)

    def can_place_card(self, card):
        placing_options = []
        for color in Colors:
            color_match = False
            if color == card.get_color() or \
                    (self.game_option == GameOptions.ONLY_COLORS_PILES and card.get_color() == Colors.RAINBOW):
                color_match = True

            if color_match and \
                    (len(self.card_piles[color]) == 0 and card.get_number() == 1) or \
                    (self.card_piles[color][-1].get_number() == card.get_number() - 1):
                placing_options.extend(color)

        return placing_options

    def place_card(self, card, color):
        if color not in self.can_place_card(card):
            raise Exception('Tried to place card in invalid pile!')
        self.card_piles[color].extend(card)

    def __str__(self):
        ret_str = ''
        for color_pile in self.card_piles:
            ret_str += 'The {color} pile: {cards}'.\
                format(color=color_pile, cards=','.join(map(str, self.card_piles[color_pile])))
        return ret_str
