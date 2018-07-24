class Player:
    def __init__(self, name, sock):
        self.name = name
        self.sock = sock

    def __str__(self):
        return self.name
