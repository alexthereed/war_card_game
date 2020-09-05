"""WAR CARD GAME"""
#random module used for shuffling deck
import random

#lists for card suits, ranks and values

suit = ('HEARTS','CLUBS','SPADES','DIAMONDS')
rank = ('TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','JACK','QUEEN','KING','ACE')
values = {'TWO':2,'THREE':3,'FOUR':4,'FIVE':5,'SIX':6,'SEVEN':7,'EIGHT':8,'NINE':9,'TEN':10,'JACK':11,'QUEEN':12,'KING':13,'ACE':14}

#card class
class Card:

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

#deck class to initiate the deck of 52 cards and handle methods such as shuffling and dealing cards

class Deck:

    def __init__(self):
        self.deck = []
        for r in rank:
            for s in suit:
                self.deck.append(Card(r,s))

    def __str__(self):
        currentDeck = ''
        for card in self.deck:
            currentDeck += '\n' + card.__str__()
        return 'The Deck consists of: ' + currentDeck

    def shuffle(self):
        random.shuffle(self.deck)

    def dealOne(self):
        singleCard = self.deck.pop()
        return singleCard

#player class to handle different players and their hands

class Player:

    def __init__(self,name):
        self.name = name
        self.hand = []

    def __str__(self):
        return f'{self.name} has {len(self.hand)} cards'

    def remove_card(self):
        return self.hand.pop(0)

    def add_cards(self,newCards):
        if type(newCards) == type([]):
            self.hand.extend(newCards)
        else:
            self.hand.append(newCards)


"""GAME LOGIC"""
#create deck and players

gameDeck = Deck()
p1 = Player('ONE')
p2 = Player('TWO')

#shuffle deck and deal cards evenly to both players

gameDeck.shuffle()

for num in range(26):
    p1.add_cards(gameDeck.dealOne())
    p2.add_cards(gameDeck.dealOne())


game_on = True
count = 0

while game_on:

    count += 1

    print(f'ROUND {count}')

    #check for a winner

    if len(p1.hand) == 0:
        print('Player one is out of cards. Player Two Wins!')
        game_on = False
        break

    elif len(p2.hand) == 0:
        print('Player two is out of cards. Player One Wins!')
        game_on = False
        break

    p1_working_cards = []
    p2_working_cards = []

    p1_working_cards.append(p1.remove_card())
    p2_working_cards.append(p2.remove_card())

    at_war = True
    while at_war:

        if p1_working_cards[-1].value > p2_working_cards[-1].value:
            p1.add_cards(p1_working_cards)
            p1.add_cards(p2_working_cards)
            at_war = False

        elif p1_working_cards[-1].value < p2_working_cards[-1].value:
            p2.add_cards(p1_working_cards)
            p2.add_cards(p2_working_cards)
            at_war = False

        else:
            print('WAR!!!')

            if len(p1.hand) < 5:
                print('Player one does not have enough cards to declare war')
                print('PLAYER TWO WINS!')
                game_on = False
                break

            elif len(p2.hand) < 5:
                print('Player two does not have enough cards to declare war')
                print('PLAYER ONE WINS!')
                game_on = False
                break

            else:
                for num in range(5):
                    p1_working_cards.append(p1.remove_card())
                    p2_working_cards.append((p2.remove_card()))


