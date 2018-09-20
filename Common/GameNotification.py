import abc


class AbstractGameNotification:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass


class ChoosePileToPlaceCard(AbstractGameNotification):
    def __init__(self, color_options):
        self.color_options = color_options


class UpdateNotification(AbstractGameNotification):
    def __init__(self, update_turn_notification):
        self.update_turn_notification = update_turn_notification
