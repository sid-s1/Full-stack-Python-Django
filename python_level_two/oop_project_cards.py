import random
from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
DECK=[]
player_one=[]
player_two=[]

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        for house in SUITE:
            for numb in RANKS:
                DECK.append(house+numb)

    def cut(self):
        length=int(len(DECK)/2)
        for item in range(0,length-1):
            player_one.append(DECK[item])
        for item in range(length,len(DECK)-1):
            player_two.append(DECK[item])

    def shuff(self):
        shuffle(DECK)

    #def __str__(self):
        #return "Player one's deck: {} \nPlayer two's deck: {}".format(player_one,player_two)


class Hand:
    """
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    """

    def __init__(self,d):
        self.d=d

    def add(self,h):
        self.d.extend(h)

    def remove(self):
        return self.d.pop()

    def __str__(self):
        return "Contains {} cards".format(len(self.d))

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """

    def __init__(self,name,hand):
        self.name=name
        self.hand=hand

    def play_card(self):
        drawn_card=self.hand.remove()
        print("{} has placed {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards=[]
        if len(self.hand.d) < 3:
            return war_cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove())
            return war_cards

    def still_has_cards(self):
        """Returns true if player still has cards left"""
        return len(self.hand.d) != 0


#### GAME PLAY #######
print("Welcome to War, let's begin...")
ob=Deck()
ob.shuff()
ob.cut()
comp=Player("Computer",Hand(player_two))
name=input("What is your name, sire/madame?")
user=Player(name,Hand(player_one))
total_rounds=0
war_count=0
while user.still_has_cards() and comp.still_has_cards():
    total_rounds+=1
    print("Time for a new round!")
    print("Here are the current standings")
    print(user.name,"has the count: ",str(len(user.hand.d)))
    print(comp.name,"has the count: ",str(len(comp.hand.d)))
    print("Play a card!\n")

    table_cards=[]
    c_card=comp.play_card()
    p_card=user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1:] == p_card[1:]:
        war_count+=1
        print("War!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1:]) < RANKS.index(p_card[1:]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

    else:
        if RANKS.index(c_card[1:]) < RANKS.index(p_card[1:]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print("Game over! Number of rounds: ",str(total_rounds))
print("A war happened ",str(war_count)," times")
print("Does the computer still have cards?")
print(str(comp.still_has_cards()))
print("Does the user still have cards?")
print(str(user.still_has_cards()))
