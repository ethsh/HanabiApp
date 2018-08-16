class Player:
    def __init__(self):
        self.cards = []
        self.game = None

    def enter_game(self, game):
        self.game = game
        self.cards = []

    def receive_card(self, card):
        self.cards.append(card)

    def perform_turn(self):
        if self.game is None:
            raise Exception('Can\'t perform turn - game is None')
        # TODO : fill this...

    def __str__(self):
        return 'Player name: {player}, Cards are: {cards}'.format(player=self.name, cards=','.join(map(str, self.cards)))
