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

        print('Welcome to the J&J Blackjack table! For all questions asked please respond with a \'y\' for yes or a \'n\' for no.')
        while True:
            start = input('Would you like to start a game? ')
            if self.check_input(start) == 'y': self.deal()
            else: 
                print('Sorry to see you go. Come play again soon!')
                break

    def deal(self):
        self.deck = [j for j in range(1,14) for i in range(1, 5)] #to be replaced with Deck()
        for n, num in enumerate(self.deck):
            if num == 11 or num == 12 or num == 13:
                self.deck[n] = 10
            if num == 1:
                self.deck[n] = 'a'

        self.player_cards = []
        self.dealer_cards = []

        for i in range(2):
            self.player_cards.append(self.deck.pop(r.randint(0,len(self.deck))))
            self.dealer_cards.append(self.deck.pop(r.randint(0,len(self.deck))))
        self.show()
        self.evaluate()
        self.play()

    def show(self, end=False):
        if end == True:
            self.convert_aces()
            print(f"Player hand - {', '.join(str(x) for x in self.player_cards)} - total: {sum(self.player_cards)}")
            print(f"Dealer hand - {', '.join(str(x) for x in self.dealer_cards)} - total: {sum(self.dealer_cards)}")
        else:
            self.convert_aces()
            print(f"Player hand - {', '.join(str(x) for x in self.player_cards)} - total: {sum(self.player_cards)}")
            print(f'Dealer hand - {self.dealer_cards[0]} - total: unknown')

    def play(self):
        while True:
            action = input('Would you like to hit? ')
            if self.check_input(action) == 'y': 
                self.hit()
                if self.evaluate() == 'bust':
                    break
            else: 
                self.stand()
                break

    def hit(self):
        self.player_cards.append(self.deck.pop(r.randint(0,len(self.deck))))
        self.show()

    def stand(self):
        while sum(self.dealer_cards) < 17:
            self.dealer_cards.append(self.deck.pop(r.randint(0,len(self.deck))))
            self.convert_aces()
        self.show(True)
        self.evaluate(True)

    def evaluate(self):
        greatest_hand = []
        blackjack_num = 0
        self.convert_aces()
        for hand in [self.dealer_cards,self.player_cards]:
            if sum(hand) > 21:
                return 'bust'      
            elif len(hand) == 2 and 11 in hand and 10 in hand:
                #blackjack message
                if blackjack_num == 0: 
                    greatest_hand = hand
                else:
                    greatest_hand.append(hand)
                blackjack_num += 1
            elif sum(hand) > sum(greatest_hand):
                greatest_hand = hand
            #need elif with dealer identification for ties <-- somewhere in the Hand class I need to get the name of the player associated with that hand

        if blackjack_num == 1:
            return 'blackjack'
        if blackjack_num > 1:
            return 'multiple blackjacks'
        else:
            return f"Highest hand is {', '.join(str(x) for x in self.player_cards)} - total: {sum(self.player_cards)}"

    def evaluate(self, display = False):

        player_bust = False
        player_bj = False
        dealer_bust = False
        dealer_bj = False

        self.convert_aces()


        if sum(self.player_cards) == 21 and len(self.player_cards) == 2: player_bj = True
        if sum(self.dealer_cards) == 21 and len(self.dealer_cards) == 2: dealer_bj = True
        
        if player_bj == True and dealer_bj == True:
            print(f'Both the dealer and the player have blackjack. The game is a tie.')
            return 'dual_blackjacks'
        elif player_bj == True:
            print(f'You have blackjack.\nYou Win!')
            return 'blackjack'
        elif dealer_bj == True:
            print(f'The dealer has blackjack.\nYou Lose.')
            return 'blackjack'

        if sum(self.player_cards) > 21:
            print(f"You are bust!")
            return 'bust'
        elif sum(self.dealer_cards) > 21:
            print(f"The dealer is bust!")
        elif sum(self.player_cards) > sum(self.dealer_cards) and display == True:
            print(f"Highest hand is {', '.join(str(x) for x in self.player_cards)} - total: {sum(self.player_cards)}\nYou Win!")
        elif display == True:
            print(f"Highest hand is {', '.join(str(x) for x in self.dealer_cards)} - total: {sum(self.dealer_cards)}\nYou Lose.")

        #add win tracker



    def convert_aces(self):
        for hand in [self.dealer_cards,self.player_cards]:
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