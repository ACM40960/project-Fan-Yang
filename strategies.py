# Continuous strategy (based on the stand threshold)
def strategy_with_threshold(threshold):
    def strategy(hand_value):
        if hand_value >= threshold:
            return "stand"
        else:
            return "hit"
    return strategy

# Card count strategy (taking into account the number of cards the player holds)
def card_count_strategy(hand_value, hand_length):
    # Strategy based on card count: If the player holds more than 4 cards and the value is close to 21, favor standing
    if hand_length >= 4 and hand_value >= 13:
        return "stand"
    elif hand_value >= 14:
        return "stand"
    else:
        return "hit"

def small_card_strategy(hand_value, small_card_count, deck):
    # If many small cards have already appeared, assume higher odds of drawing big cards, allowing the player to be more aggressive
    if small_card_count >= 10 and hand_value <= 13:
        return "hit"  # Choose to hit more aggressively
    elif hand_value >= 14:
        return "stand"
    else:
        return "hit"
