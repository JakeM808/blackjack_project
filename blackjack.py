from typing import Any
import random as r


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


class Hand:
    def __init__(self):
        self.cards = []

    def clear_hand(self):
        self.cards = []

    def add_card(self, deck):  
        self.cards.append(deck.deck.pop(r.randint(0,len(deck.deck))))
         
    def value(self):
        return sum(card for card in self.cards)


class Player:
    def __init__(self, player_name='dealer'):
        self.name = player_name
        self.hand = Hand()
        self.score = 0