# MCTS Simulation with Modified Tic-Tac-Toe

This project implements a modified version of the classic Tic-Tac-Toe game, enhanced with a Monte Carlo Tree Search (MCTS) algorithm to simulate and find the best possible moves.

## Table of Contents
- [Introduction](#introduction)
- [Game Rules](#game-rules)
- [How to Play](#how-to-play)
- [Installation](#installation)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)

## Introduction
This modified Tic-Tac-Toe game uses MCTS to simulate moves, making it more challenging and providing insights into AI-based decision-making. It explores various strategies to maximize the winning potential of each move.
The repository includes a play file which can be used to play the modified 4v4 version of Tic-Tac-Toe.
The rest is simulation files, data and MCTS strategies. They serve the purpose to see if the first or the second player has an advantage in the game and if playing with specific strategies would change those results.

## Game Rules
The rules follow the traditional Tic-Tac-Toe structure with some modifications:
1. Players take turns placing their marks (`X` and `O`) on a 4x4 grid.
2. The game is played until all squares are filled.
3. The person to have more 3 in a row (diagonally, horizontally or vertically) marks wins, else it is a draw.

## How to Play
1. Run the `play.py` script to start the game.
2. You will be prompted to select to play vs another person or vs the MCTS algorithm.
3. If the latter is chosen you'd be promped to choose difficulty and wheteher you want to be first or second.
4. Play the game until all squares are filled.

## Installation
To get started:
1. Clone the repository:
   ```bash
   git clone https://github.com/vladigt9/Advanced-tictactoe-with-MCTS-AI.git
