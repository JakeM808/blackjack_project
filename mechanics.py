"""
Requirements:
1. start game
2. create deck (deck class)
3. initialize players (player class)
4. give players cards
    i. check for blackjack
5. display hands - 2 of player 1 of dealer
6. allow action
    i. hit - take one new card
    ii. stand - stop hitting --> dealers moves (hit till >= 17)
7. evaluate winner
8. restart

Notes:
- ace auto as whatever provides best score
- ties go to dealer
"""

import random as r

class Game:
    def __init__(self):
        self.deck = [j for j in range(1,14) for i in range(1, 5)] #to be replaced with Deck()
        for n, num in enumerate(self.deck):
            if num == 11 or num == 12 or num == 13:
                self.deck[n] = 10
            if num == 1:
                self.deck[n] = 'a'

        self.player_cards = []
        self.dealer_cards = []

        print('Welcome to the J&J Blackjack table! For all questions asked please respond with a \'y\' for yes or a \'n\' for no.')
        start = input('Would you like to start a game? ')
        if self.check_input(start) == 'y': self.deal()
        else: print('Sorry to see you go. Come play again soon!')

    def deal(self):
        for i in range (2):
            self.player_cards.append(self.deck.pop(r.randint(0,len(self.deck))))
            self.dealer_cards.append(self.deck.pop(r.randint(0,len(self.deck))))
        print(self.player_cards)
        print(self.dealer_cards)
        print(self.evaluate(self.player_cards, self.dealer_cards))

    def show(self):
        pass

    def play(self):
        def hit(self):
            pass

        def stand(self):
            pass

    def evaluate(self, *hands):
        greatest_hand = []
        blackjack_num = 0
        for hand in hands:
            aces = []
            for i, num in enumerate(hand):
                if num == 'a':
                    aces.append(hand.pop(i))
            if len(aces) > 0:
                for ace in aces:
                    if sum(hand) <= 10:
                        hand.append(11)
                    else:
                        hand.append(1)
                #need contingency for 2 aces + 10 or 3 + 9 or 4 + 8 
                    
            if len(hand) == 2 and len(aces) == 1 and 10 in hand:
                if blackjack_num == 0: 
                    greatest_hand = hand
                else:
                    greatest_hand.append(hand)
                blackjack_num += 1
            elif sum(hand) > sum(greatest_hand):
                greatest_hand = hand
            #need elif with dealer identification for ties

        if blackjack_num > 1:
            return 'multiple blackjacks'
        else:
            return greatest_hand
            

    def check_input(self, val):
        while True:
            if val.lower() != 'y' and val.lower() != 'n':
                val = input('That is not a valid response. Please type either \'y\' for yes or a \'n\' for no. ')
            else:
                break
        return val

game_1 = Game()



