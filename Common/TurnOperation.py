from Cards import *
import abc


OperationType = Enum('OperationType', 'ColorUpdate NumberUpdate BurnCard PlaceCard')


class TurnOperation:
    __metaclass__ = abc.ABCMeta

    def __init__(self, op_type):
        self.op_type = op_type


class AbstractUpdateTurnOperation(TurnOperation):
    __metaclass__ = abc.ABCMeta

    def __init__(self, op_type, player_name):
        super(op_type)
        self.player_name = player_name

    @abc.abstractmethod
    def card_result(self, card):
        pass


class NumberUpdateTurnOperation(AbstractUpdateTurnOperation):
    def __init__(self, op_type, player_name, number):
        super(op_type, player_name)
        self.number = number

    def card_result(self, card):
        return card.get_number() == self.number


class ColorUpdateTurnOperation(AbstractUpdateTurnOperation):
    def __init__(self, op_type, player_name, color):
        super(op_type, player_name)
        if color == Colors.RAINBOW:
            raise Exception('Can\'t update about rainbows!')
        self.color = color

    def card_result(self, card):
        return card.get_color() == self.color or card.get_color() is Colors.RAINBOW


class BurnCardOperation(TurnOperation):
    def __init__(self, op_type, card):
        super(BurnCardOperation, self).__init__(op_type)
        # super.__init__(op_type)
        self.card_to_burn = card


class PlaceCardOperation(TurnOperation):
    # def __init__(self, op_type, card, pile_color):
    def __init__(self, op_type, card):
        super(PlaceCardOperation, self).__init__(op_type)
        self.card_to_place = card
        # self.pile_color = pile_color
