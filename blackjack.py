from typing import Any


class Card:
    def __init__(self, value, suit, face):
        self.value = value
        self.suit = suit
        self.face = face
    def __str__(self):
        return f"{self.value} of {self.suit}"  

class Deck:
    def __init__(self):
        self.deck = [j for j in range(1,14) for i in range(1, 5)]  
        for n, num in enumerate(self.deck):
            if num == 11 or num == 12 or num == 13:
                self.deck[n] = 10
            if num == 1:
                self.deck[n] = 'a'

    def draw(self):
        return self.deck.pop()            


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):  
        self.cards.append(card) 

    def value(self):
        return sum(card.value for card in self.cards)

    def blackjack(self):
        return self.value == 21


class Player:
    def __init__(self, player_name='dealer'):
        self.name = player_name

    def hit(self):
            card = Deck.draw()
            self.hand.add_card(card) 

    def stand(self):
        pass 

    def blackjack(self):
        return self.hand.blackjack()   

dealer = Player()

player1 = Player('player1')      
                
