from Deck import Deck
from Card import Card


class Dealer:

    def __init__(self, num_decks):
        self.deck = Deck(num_decks)
        self.plastic_card = Card('P', 0)
