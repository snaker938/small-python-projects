suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

import random

class cards():
    

    def __init__(self):
        self.add_to_deck()
        

    def add_to_deck(self):
        # counter = 0
        for suit in suits:
            for value in values:
                card = f"{value} of {suit}"
                deck.cards.append(card)
            # counter += 1
    

class deck(cards):
    def __init__(self):
        self.number_of_cards = 52
        self.cards = []

        super(deck).__init__()

    def print_cards(self):
        for row in self.cards:
            print(row)

    def shuffle(self):

        def swapPositions(deck, pos1, pos2):
            deck[pos1], deck[pos2] = deck[pos2], deck[pos1]
            return deck

        random_pos1 = random.randint(0, self.number_of_cards -1)
        random_pos2 = random.randint(0, self.number_of_cards - 1)
        for i in range(0, random_pos1):
            for i in range(0, self.number_of_cards):
                random_pos1 = random.randint(1, self.number_of_cards - 1)
                random_pos2 = random.randint(1, self.number_of_cards - 1)
                for i in range(0, self.number_of_cards):
                    deck.cards = swapPositions(deck.cards, random_pos1 - 1, random_pos2 - 1)
                    random_pos1 = random.randint(0, self.number_of_cards)
                    random_pos2 = random.randint(0, self.number_of_cards)
        

    def new_deck(self):
        self.cards = []
        cards.add_to_deck()

        

        
                


        


deck = deck()
cards = cards()

deck.shuffle()

deck.print_cards()


