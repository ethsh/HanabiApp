import abc
from enum import Enum
import itertools
from random import shuffle


Colors = Enum('Colors', 'RED GREEN BLUE WHITE YELLOW RAINBOW')
Numbers = Enum('Numbers', 'ONE TWO THREE FOUR FIVE')
Operations = Enum('Operations', 'COLOR NUMBER')

initial_cards_amounts = {Numbers.ONE : 3, Numbers.TWO : 2, Numbers.THREE : 2, Numbers.FOUR : 2, Numbers.FIVE : 1}


class Card:
    def __init__(self, number, color):
        self.color = color
        self.number = number

    def get_color(self):
        return self.color

    def get_number(self):
        return self.number


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
    def get_initial_amount_of_cards_in_deck(card_number, card_color):
        if card_color is Colors.RAINBOW:
            return 1
        return initial_cards_amounts[card_number]

    @staticmethod
    def create_card_deck():
        cards = []
        for (number, color) in itertools.product(Numbers, Colors):
            card_amount = Deck.get_initial_amount_of_cards_in_deck(number, color)
            cards.extend([Card(number, color)] * card_amount)
        return cards

    def __init__(self):
        self.deck = Deck.create_card_deck()
        self.shuffle_deck()

    def shuffle_deck(self):
        shuffle(self.deck)

    def draw_card(self):
        card = self.deck[0]
        self.deck = self.deck[1:]
        return card

    def get_num_pf_remaining_cards(self):
        return len(self.deck)




def CardsFactory(name, argnames, BaseClass=Card):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            # here, the argnames variable is the one passed to the
            # ClassFactory call
            if key not in argnames:
                raise TypeError("Argument %s not valid for %s"
                    % (key, self.__class__.__name__))
            setattr(self, key, value)
        BaseClass.__init__(self, name[:-len("Class")])
    newclass = type(name, (BaseClass,),{"__init__": __init__})
    return newclass
