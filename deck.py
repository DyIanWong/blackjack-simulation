import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()
    
    def build(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["Diamonds", "Clubs", "Hearts", "Spades"]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    
    def deal(self):
        return self.cards.pop()

