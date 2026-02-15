from deck import Deck
from hand import Hand

class Game:
    def __init__(self):
        self.deck = Deck()

        self.player = Hand()
        self.dealer = Hand()

        self.playerwin = False
        self.push = False
        

    def play(self):
        #player
        self.player.add_card(self.deck.deal())
        self.player.add_card(self.deck.deal())

        #player strategy
        while self.player.get_value() < 17:
            self.player.add_card(self.deck.deal())


        #dealer
        self.dealer.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())

        while self.dealer.get_value() < 17 and self.player.is_bust() == False:
            self.dealer.add_card(self.deck.deal())


        #win
        if self.player.get_value() > self.dealer.get_value() and self.player.is_bust() == False:
            self.playerwin = True
        elif self.player.is_bust() == False and self.dealer.is_bust() ==  True:
            self.playerwin = True
        elif self.player.get_value() == self.dealer.get_value():
            self.push = True
        else:
            self.playerwin = False