import random
import matplotlib.pyplot as plt
from deck import create_deck, shuffle_deck, deal_cards
from game_rules import calculate_hand_value, check_winner, hit, stand
from strategies import strategy_with_threshold, card_count_strategy, small_card_strategy

# Simulate 100,000 games
def simulate_games(strategy, num_games=100000, use_hand=False, use_deck=False):
    results = {"Player wins": 0, "Dealer wins": 0, "Tie": 0}
    for _ in range(num_games):
        deck = shuffle_deck(create_deck())
        player_hand = deal_cards(deck)
        dealer_hand = deal_cards(deck)

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

        if calculate_hand_value(player_hand) <= 21:
            while calculate_hand_value(dealer_hand) < 17:
                dealer_hand = hit(deck, dealer_hand)

            result = check_winner(player_hand, dealer_hand)
            if result == "Push":
                result = "Tie"
            results[result] += 1

    return results

def calculate_win_rates(results, num_games):
    player_win_rate = results["Player wins"] / num_games * 100
    return player_win_rate

if __name__ == "__main__":
    num_games = 100000

    # Store the results of different policies
    strategies = []
    player_win_rates = []

    # 1. Continuity strategy (based on 12-20 stop points)
    for threshold in range(12, 21):
        strategy = strategy_with_threshold(threshold)
        results = simulate_games(strategy, num_games)
        player_win_rate = calculate_win_rates(results, num_games)

        # Store results
        strategies.append(f"Threshold: {threshold}")
        player_win_rates.append(player_win_rate)

    # First graph: Draw a bar chart of continuous strategies
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(strategies, player_win_rates, color='blue', label='Player Win Rate')
    ax.set_xlabel('Strategies')
    ax.set_ylabel('Win Rate (%)')
    ax.set_title('Player Win Rate for Continuous Strategies (Threshold 14-20)')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Second chart: Select strategies with a win rate of more than 40% and draw a fine bar chart
    filtered_strategies = []
    filtered_win_rates = []

    for strategy, win_rate in zip(strategies, player_win_rates):
        if win_rate >= 40:
            filtered_strategies.append(strategy)
            filtered_win_rates.append(win_rate)

    # Only plot wins in the 40%-45% range
    if filtered_strategies:
        fig, ax = plt.subplots(figsize=(10, 6))

        ax.bar(filtered_strategies, filtered_win_rates, color='green', label='Player Win Rate (40%-45%)')
        ax.set_xlabel('Strategies')
        ax.set_ylabel('Win Rate (%)')
        ax.set_ylim(40, 45)
        ax.set_title('Filtered Player Win Rate (40%-45%) for Continuous Strategies')
        ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # Third picture: Add the other two strategies based on the second picture and apply 40%-45% filters
    other_strategies = ["Card Count Strategy", "Small Card Strategy"]
    other_win_rates = []

    # Card count strategy
    def card_count_wrapped_strategy(hand_value, player_hand):
        return card_count_strategy(hand_value, len(player_hand))

    results = simulate_games(card_count_wrapped_strategy, num_games, use_hand=True)
    player_win_rate = calculate_win_rates(results, num_games)
    other_win_rates.append(player_win_rate)

    # Small card strategy
    def small_card_wrapped_strategy(hand_value, player_hand, deck):
        small_card_count = sum(1 for card in deck if card[0] in ['2', '3', '4', '5', '6'])
        return small_card_strategy(hand_value, small_card_count, deck)

    results = simulate_games(small_card_wrapped_strategy, num_games, use_hand=True, use_deck=True)
    player_win_rate = calculate_win_rates(results, num_games)
    other_win_rates.append(player_win_rate)

    # Combine the previously screened strategies with two additional strategies and apply the 40%-45% range
    combined_strategies = filtered_strategies + other_strategies
    combined_win_rates = filtered_win_rates + [rate for rate in other_win_rates if 40 <= rate <= 45]

    # Draw the third picture
    if combined_strategies:
        fig, ax = plt.subplots(figsize=(10, 6))

        ax.bar(combined_strategies, combined_win_rates, color=['green' if s in filtered_strategies else 'red' for s in combined_strategies], label='Player Win Rate (All Strategies)')
        ax.set_xlabel('Strategies')
        ax.set_ylabel('Win Rate (%)')
        ax.set_ylim(40, 45)
        ax.set_title('Filtered Player Win Rate (40%-45%) for All Strategies')
        ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
