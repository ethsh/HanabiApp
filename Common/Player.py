from TurnOperation import *


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.game = None
        self.update_history = []

    def enter_game(self, game):
        self.game = game
        self.cards = []

    def leave_game(self):
        self.game = None

    def receive_card(self, card):
        if self.game is None:
            raise Exception('can\'t receive card while not in active game')
        self.cards.append(card)

    def perform_turn(self):
        if self.game is None:
            raise Exception('Can\'t perform turn while not in active game')
        self.game.print_game_state_for_player(self)
        choise = input('Perform Action: 1 - burn card, 2 - place card, 3 - update player\n')
        switcher = {
            1: self.burn_card,
            2: self.place_card,
            3: self.update_player,
        }
        # Get the function from switcher dictionary
        func = switcher.get(choise, lambda: "Invalid choise")
        # Execute the function
        return func()

    def burn_card(self):
        card_index = input('Choose card number to burn: ')
        card = self.cards.pop(card_index)
        return BurnCardOperation(OperationType.BurnCard, card)

    def place_card(self):
        card_index = input('Choose card number to place: ')
        card = self.cards.pop(card_index)
        return PlaceCardOperation(OperationType.PlaceCard, card)

    def update_player(self):
        return "March"

    def receive_game_notification(self, notification):
        pass

    def receive_update(self, update):
        self.update_history.append(update)

    def __str__(self):
        return 'Player name: {player}, Cards are: {cards}'.format(player=self.name, cards=','.join(map(str, self.cards)))
