class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.game = None
        self.update_history = []

    def enter_game(self, game):
        self.game = game
        self.cards = []

    def receive_card(self, card):
        if self.game is None:
            raise Exception('can\'t receive card while not in active game')
        self.cards.append(card)

    def perform_turn(self):
        if self.game is None:
            raise Exception('Can\'t perform turn while not in active game')
        self.game.print_game_state_for_player(self)
        print 'Perform Action: 1 - burn card, 2 - place card, 3 - update player'
        # TODO : fill this...

    def receive_update(self, update):
        self.update_history.append(update)

    def __str__(self):
        return 'Player name: {player}, Cards are: {cards}'.format(player=self.name, cards=','.join(map(str, self.cards)))
