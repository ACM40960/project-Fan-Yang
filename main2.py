import random
from deck import create_deck, shuffle_deck, deal_cards
from game_rules import calculate_hand_value, check_winner, hit
from strategies import strategy_with_threshold, card_count_strategy, small_card_strategy

# Simulate 100,000 games
def simulate_games(strategy, num_games=100000, use_hand=False, use_deck=False):
    results = {"Player wins": 0, "Dealer wins": 0, "Tie": 0}
    for _ in range(num_games):
        deck = shuffle_deck(create_deck())
        player_hand = deal_cards(deck)
        dealer_hand = deal_cards(deck)

        # Player's turn
        while True:
            player_hand_value = calculate_hand_value(player_hand)
            if use_hand and use_deck:
                action = strategy(player_hand_value, player_hand, deck)
            elif use_hand:
                action = strategy(player_hand_value, player_hand)
            else:
                action = strategy(player_hand_value)

            if action == 'hit':
                player_hand = hit(deck, player_hand)
                if calculate_hand_value(player_hand) > 21:
                    results["Dealer wins"] += 1
                    break
            elif action == 'stand':
                break

        # Dealer's turn
        if calculate_hand_value(player_hand) <= 21:
            while calculate_hand_value(dealer_hand) < 17:
                dealer_hand = hit(deck, dealer_hand)

            result = check_winner(player_hand, dealer_hand)
            if result == "Push":
                result = "Tie"
            results[result] += 1

    return results

# Calculate win, tie, and loss rates
def calculate_rates(results, num_games):
    player_win_rate = results["Player wins"] / num_games * 100
    dealer_win_rate = results["Dealer wins"] / num_games * 100
    tie_rate = results["Tie"] / num_games * 100
    return player_win_rate, dealer_win_rate, tie_rate

if __name__ == "__main__":
    num_games = 100000

    # Store the results of different policies
    strategies = []
    strategy_names = []

    # 1. Continuity strategy (based on 12-20 stop points)
    for threshold in range(12, 21):
        strategy = strategy_with_threshold(threshold)
        results = simulate_games(strategy, num_games)
        player_win_rate, dealer_win_rate, tie_rate = calculate_rates(results, num_games)

        # Store results
        strategy_names.append(f"Threshold: {threshold}")
        strategies.append((player_win_rate, dealer_win_rate, tie_rate))

    # Card count strategy
    def card_count_wrapped_strategy(hand_value, player_hand):
        return card_count_strategy(hand_value, len(player_hand))

    results = simulate_games(card_count_wrapped_strategy, num_games, use_hand=True)
    player_win_rate, dealer_win_rate, tie_rate = calculate_rates(results, num_games)
    strategy_names.append("Card Count Strategy")
    strategies.append((player_win_rate, dealer_win_rate, tie_rate))

    # Small card strategy
    def small_card_wrapped_strategy(hand_value, player_hand, deck):
        small_card_count = sum(1 for card in deck if card[0] in ['2', '3', '4', '5', '6'])
        return small_card_strategy(hand_value, small_card_count, deck)

    results = simulate_games(small_card_wrapped_strategy, num_games, use_hand=True, use_deck=True)
    player_win_rate, dealer_win_rate, tie_rate = calculate_rates(results, num_games)
    strategy_names.append("Small Card Strategy")
    strategies.append((player_win_rate, dealer_win_rate, tie_rate))

    # Print the results
    print(f"{'Strategy':<25}{'Player Win Rate (%)':<20}{'Dealer Win Rate (%)':<20}{'Tie Rate (%)'}")
    print("-" * 65)
    for name, (player_win, dealer_win, tie) in zip(strategy_names, strategies):
        print(f"{name:<25}{player_win:<20.2f}{dealer_win:<20.2f}{tie:.2f}")
