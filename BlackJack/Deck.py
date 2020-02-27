from Card import Card
import random


class Deck:

    def __init__(self, num_decks):
        self.suits = ['H', 'S', 'D', 'C']
        self.cards = []

        for deck in range(1, num_decks):
            for suit in self.suits:
                for num in range(1, 13):
                    self.cards.append(Card(suit, num))

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def draw_card(self):
        card = self.cards.pop()
        self.cards.append(card)

        return card
