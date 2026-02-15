class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        total = 0
        aces = 0

        for card in self.cards:
            total += card.value()
            if card.rank == "A":
                aces += 1
        
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total
    
    def is_bust(self):
        if self.get_value() > 21:
            return True
        else:
            return False