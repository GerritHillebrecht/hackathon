"""
Leaderboard Module
==================

This module provides functionality for saving and displaying a leaderboard for a game.

Functions:
----------
- save_leaderboard(scores: dict, filename="leaderboard.txt"):
    Saves the leaderboard to a specified file. The scores are appended to the file.

- display_leaderboard(scores: dict) -> None:
    Displays the leaderboard with players' scores in descending order and announces the winner.

Usage:
------
To save the leaderboard, call the `save_leaderboard` function with a dictionary of player scores and an optional filename. To display the leaderboard, call the `display_leaderboard` function with a dictionary of player scores.

Example:
--------
>>> from leaderboard import save_leaderboard, display_leaderboard
>>> scores = {"Alice": 10, "Bob": 8, "Charlie": 12}
>>> save_leaderboard(scores)
>>> display_leaderboard(scores)

=== Leaderboard ===
Charlie: 12 points
Alice: 10 points
Bob: 8 points

The winner is Charlie with 12 points! Congratulations!
"""

def save_leaderboard(scores: dict, filename="leaderboard.txt"):
    """
    Saves the leaderboard to a file.

    :param scores: A dictionary with player names as keys and their scores as values.
    :param filename: The name of the file to save the leaderboard to.

    """
    with open(filename, "a") as f:
        for player, score in scores.items():
            f.write(f"{player}: {score}\n")


def display_leaderboard(scores) -> None:
    """
    Displays the leaderboard with players' scores and announces the winner.

    :type scores: dict
    :param scores: A dictionary with player names as keys and their scores as values.
    """
    print("\n=== Leaderboard ===")
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    for player, score in sorted_scores:
        print(f"{player}: {score} points")

    winner = sorted_scores[0]
    print(f"\nThe winner is {winner[0]} with {winner[1]} points! Congratulations!")
