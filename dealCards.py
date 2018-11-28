#dictionaries
import random

def main():
    #create a deck of cards
    times = int(input('How many rounds to deal cards?'))

    for i in range(times):
        deck = create_deck()

        #get the number of cards to deal
        num_cards - int(input('How many cards should I deal?'))

        #Deal the cards
        deal_cards(deck, num_cards)


deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
