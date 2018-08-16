from Cards import *
import abc


class AbstractUpdateTurnOperation:
    __metaclass__ = abc.ABCMeta

    def __init__(self, player_name):
        pass

    @abc.abstractmethod
    def card_result(self, card):
        pass


class NumberUpdateTurnOperation(AbstractUpdateTurnOperation):
    def __init__(self, number):
        self.number = number

    def card_result(self, card):
        return card.get_number() == self.number


class ColorUpdateTurnOperation(AbstractUpdateTurnOperation):
    def __init__(self, color):
        if color == Colors.RAINBOW:
            raise Exception('Can\'t update about rainbows!')
        self.color = color

    def card_result(self, card):
        return card.get_color() == self.color or card.get_color() is Colors.RAINBOW
