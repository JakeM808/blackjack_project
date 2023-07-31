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
import blackjack as b

class Game:
    def __init__(self):
        name = input('What is your name? ')
        self.player = b.Player(name)
        self.dealer = b.Player()


        print('Welcome to the J&J Blackjack table! For all questions asked please respond with a \'y\' for yes or a \'n\' for no.')
        while True:
            start = input('Would you like to start a game? ')
            if self.check_input(start) == 'y': self.deal()
            else: 
                print('Sorry to see you go. Come play again soon!')
                break

    def deal(self):
        self.deck = b.Deck()
        self.player.hand.clear_hand()
        self.dealer.hand.clear_hand()

        for i in range(2):
            self.player.hand.add_card(self.deck)
            self.dealer.hand.add_card(self.deck)

        self.show()
        self.evaluate()
        self.play()

    def show(self, end=False):
        if end == True:
            self.convert_aces()
            print(f"Player hand - {', '.join(str(x) for x in self.player.hand.cards)} - total: {self.player.hand.value()}")
            print(f"Dealer hand - {', '.join(str(x) for x in self.dealer.hand.cards)} - total: {self.dealer.hand.value()}")
        else:
            self.convert_aces()
            print(f"Player hand - {', '.join(str(x) for x in self.player.hand.cards)} - total: {self.player.hand.value()}")
            print(f'Dealer hand - {self.dealer.hand.cards[0]} - total: unknown')

    def play(self):
        while True:
            action = input('Would you like to hit? ')
            if self.check_input(action) == 'y': 
                self.hit()
                if self.evaluate() == 'bust':
                    break
                if self.evaluate() == 'blackjack' or self.evaluate() == 'dual_blackjacks':
                    break
            else: 
                self.stand()
                break

    def hit(self):
        self.player.hand.add_card(self.deck)
        self.show()

    def stand(self):
        while self.dealer.hand.value() < 17:
            self.dealer.hand.add_card(self.deck)
            self.convert_aces()
        self.show(True)
        self.evaluate(True)

    def evaluate(self, display = False):
        player_bj = False
        dealer_bj = False

        self.convert_aces()

        if self.player.hand.value() == 21 and len(self.player.hand.cards) == 2: player_bj = True
        if self.dealer.hand.value() == 21 and len(self.dealer.hand.cards) == 2: dealer_bj = True
        
        if player_bj == True and dealer_bj == True:
            print(f'Both the dealer and the player have blackjack. The game is a tie.')
            return 'dual_blackjacks'
        elif player_bj == True:
            print(f'You have blackjack.\nYou Win!')
            return 'blackjack'
        elif dealer_bj == True:
            print(f'The dealer has blackjack.\nYou Lose.')
            return 'blackjack'

        if self.player.hand.value() > 21:
            print(f"You are bust!")
            return 'bust'
        elif self.dealer.hand.value() > 21:
            print(f"The dealer is bust!")
        elif self.player.hand.value() > self.dealer.hand.value() and display == True:
            print(f"Highest hand is {', '.join(str(x) for x in self.player.hand.cards)} - total: {self.player.hand.value()}\nYou Win!")
        elif display == True:
            print(f"Highest hand is {', '.join(str(x) for x in self.dealer.hand.cards)} - total: {self.dealer.hand.value()}\nYou Lose.")

        #add win tracker



    def convert_aces(self):
        for hand in [self.dealer.hand.cards, self.player.hand.cards]:
            aces = []
            for i, num in enumerate(hand):
                if num == 'a' or num == 1 or num == 11:
                    aces.append(hand.pop(i))
            if len(aces) > 0:
                for ace in aces:
                    if sum(hand) <= 10:
                        hand.append(11)
                    else:
                        hand.append(1)
                #need contingency for 2 aces + 10 or 3 + 9 or 4 + 8 
    def check_input(self, val):
        while True:
            if val.lower() != 'y' and val.lower() != 'n':
                val = input('That is not a valid response. Please type either \'y\' for yes or a \'n\' for no. ')
            else:
                break
        return val

game_1 = Game()