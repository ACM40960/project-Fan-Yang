import random

# Define the suits and values of a deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Create the deck of cards
def create_deck():
    return [(value, suit) for value in values for suit in suits]

# Shuffle the deck function
def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

# Deal cards function
def deal_cards(deck, num=2):
    hand = deck[:num]
    del deck[:num]
    return hand
