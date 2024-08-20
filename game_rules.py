from deck import deal_cards  # Import the deal_cards function

# Function to calculate the value of a hand
def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        if card[0] in ['J', 'Q', 'K']:
            value += 10
        elif card[0] == 'A':
            aces += 1
            value += 11
        else:
            value += int(card[0])

    # Handle the value of Aces
    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value

# Determine the winner
def check_winner(player_hand, dealer_hand):
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if player_value > 21:
        return "Dealer wins"
    elif dealer_value > 21 or player_value > dealer_value:
        return "Player wins"
    elif dealer_value > player_value:
        return "Dealer wins"
    else:
        return "Push"  # Tie

# Logic to decide whether to hit (draw a card)
def hit(deck, hand):
    card = deal_cards(deck, 1)[0]  # Draw one card
    hand.append(card)
    return hand

# Logic to stand (player stops drawing cards)
def stand():
    return "Player stands"
