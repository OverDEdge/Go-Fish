class Player:

    def __init__(self, number):
        self.hand = {}
        self.sets = []
        self.number = number

    def player_has_set(self, card):
        if self.hand[card] == 4:
            self.sets.append(card)
        else:
            pass
