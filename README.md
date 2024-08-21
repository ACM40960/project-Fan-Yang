# Blackjack Monte Carlo Simulation

This project simulates multiple games of Blackjack using Monte Carlo methods to evaluate different player strategies and their impact on win rates. The simulation tests a variety of player strategies, focusing on both simple threshold-based strategies and more complex strategies that take into account the number of cards held and the frequency of small cards in the deck.

## Features

- **Card Deck and Game Mechanics**: Simulates a Blackjack deck with standard rules for shuffling, dealing cards, and calculating hand values.
- **Strategy Implementation**: Includes various player strategies:
  - **Continuous Strategies**: The player stops drawing cards when the hand reaches a certain value, ranging from 12 to 20.
  - **Card Count Strategy**: The player's decision to stop drawing cards is based on the total number of cards already held.
  - **Small Card Strategy**: The player makes more aggressive decisions when a large number of small cards (2-6) have already appeared in the deck.
- **Monte Carlo Simulations**: The project runs 100,000 simulations per strategy to evaluate performance and calculate win rates.
- **Visualization**: Bar charts are generated to compare the win rates of various strategies, with special focus on the most successful strategies.
- **Numerical Outputs (via main2.py)**: Provides detailed numerical results for the player win rate, dealer win rate, and tie rate across all strategies.

## Files

- **main.py**: Contains the core logic for running the Monte Carlo simulations. It includes functions for simulating games, calculating win rates, and plotting the results.
- **main2.py**: Focuses on outputting numerical results, including win, tie, and loss rates for all strategies. The numerical results provide a deeper statistical analysis of how each strategy performs.
- **deck.py**: Implements the logic for creating, shuffling, and dealing a deck of cards.
- **game_rules.py**: Defines the game rules such as calculating hand values, determining winners, and handling the "hit" and "stand" actions.
- **strategies.py**: Contains the different player strategies used in the simulations, including continuous, card count, and small card strategies.

## How to Run

1. Clone the repository to your local machine.
2. Install the required dependencies by running:
   ```bash
   pip install matplotlib
3. Run the simulation by executing the main.py or main2.py file depending on your interest:
  - To generate visualizations:
   ```bash
   python main.py
   ```
  - To output numerical results (win rates, tie rates, and loss rates):
   ```bash
   python main2.py
   ```
4. Output
  - The visualizations include:
   - The win rates for continuous strategies.
   - A filtered bar chart showing strategies with a win rate between 40% and 45%.
   - A final chart comparing continuous strategies with the card count and small card strategies.
  - The numerical outputs in main2.py include:
   - Player win rate, dealer win rate, and tie rate for each strategy.
   
## Key Results

- **Continuous Strategies:** Thresholds ranging from 12 to 20 were tested. Strategies where players stop drawing cards at 13, 14, and 15 thresholds generally perform better.
- **Card Count Strategy:** This strategy performs better when the player holds more cards and has a relatively high hand value, achieving a player win rate of 42.36%.
- **Small Card Strategy:** Players were more aggressive when many small cards (2-6) had already been drawn, resulting in a player win rate of 42.04%.

## Future Enhancements

- Implement more sophisticated strategies that take into account the dealer's upcard.
- Explore reinforcement learning to optimize the player's decision-making process.
- Add more detailed logging and analysis of individual game outcomes.

## Conclusion

This project provides insights into how different strategies can affect the outcome of Blackjack games. By simulating thousands of games, we can identify which strategies are most likely to increase the player's chances of winning against the dealer. The results suggest that careful consideration of hand values, the number of cards held, and the distribution of small cards may improve win rates (compared to the continuous strategy with the highest win rates). Additionally, numerical analysis from main2.py further supports the strategy evaluation with detailed statistical breakdowns.
