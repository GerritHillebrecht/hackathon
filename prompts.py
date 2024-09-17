"""
Prompts Module
==============

This module provides various prompt functions to interact with the user for setting up the game.

Functions:
----------
- prompt_player_names(num_players: int) -> list:
    Prompts each player to enter their name and returns a list of player names.

- prompt_difficulty(cocktails: dict) -> str:
    Prompts the user to select a difficulty level (easy, medium, or hard) and returns the selected level.

- prompt_number_of_rounds() -> int:
    Prompts the user to enter the number of rounds to play and returns the chosen number.

- prompt_number_of_players() -> int:
    Prompts the user to enter the number of players and returns the chosen number.

Usage:
------
To set up the game, call the respective prompt functions to gather necessary information from the user, such as player names, difficulty level, number of rounds, and number of players.

Example:
--------
>>> from prompts import prompt_player_names, prompt_difficulty, prompt_number_of_rounds, prompt_number_of_players
>>> player_names = prompt_player_names(3)
Enter the name for player 1: Alice
Enter the name for player 2: Bob
Enter the name for player 3: Charlie
>>> difficulty = prompt_difficulty(cocktails)
Choose a difficulty level (easy, medium, hard): medium
>>> num_rounds = prompt_number_of_rounds()
Enter the number of rounds: 5
>>> num_players = prompt_number_of_players()
Enter the number of players: 3
"""


def prompt_player_names(num_players: int) -> list:
    """
    Prompts each player to enter their name.

    :param num_players: The number of players.
    :returns: A list of player names.
    """
    return [
        input(f"Enter the name for player {i + 1}: ").strip()
        for i in range(num_players)
    ]


def prompt_difficulty(cocktails: dict):
    """
    Prompts the user to select a difficulty level.

    :returns: str
    :return: The selected difficulty level (easy, medium, or hard).
    """
    while True:
        level_selection = input("Choose a difficulty level (easy, medium, hard): ").strip().lower()

        if level_selection not in cocktails:
            print("Invalid input! Please choose easy, medium, or hard.")
            continue
        
        return level_selection


def prompt_number_of_rounds():
    """
    Prompts the user to enter the number of rounds to play.

    :return: The number of rounds chosen by the user.
    :returns: int
    """
    while True:
        try:
            num_of_rounds = int(input("Enter the number of rounds: ").strip())
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if not num_of_rounds > 0:
            print("Invalid input! Please enter a positive number.")

        return num_of_rounds


def prompt_number_of_players() -> int:
    """
    Prompts the user to enter the number of players.

    :returns: The number of players chosen by the user.
    """
    while True:
        try:
            num_of_players = int(input("Enter the number of players: ").strip())
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if not num_of_players > 0:
            print("Invalid input! Please enter a positive number.")

        return num_of_players
