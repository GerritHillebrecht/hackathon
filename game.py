"""
Cocktail Guessing Game Module
=============================

This module provides functionality for a cocktail guessing game where players try to guess the name of a cocktail based on its ingredients.

Functions:
----------
- play_round(player: str, difficulty: str, cocktails=cocktails_dict) -> int:
    Plays a single round of the game by selecting a random cocktail from the given difficulty level and asking the player to guess its name based on the ingredients.

Dependencies:
-------------
- random.choice: Used to select a random cocktail from the list.
- wikipedia.get_cocktail_ingredients: Custom function to fetch and clean cocktail ingredients from Wikipedia.
- cocktails: Dictionary containing cocktail data categorized by difficulty levels.

Usage:
------
To play a round of the game, call the `play_round` function with the player's name and the desired difficulty level (easy, medium, hard). The function will return 1 point for a correct guess and 0 for an incorrect guess or if ingredients are not found.

Example:
--------
>>> from game import play_round
>>> play_round("Alice", "medium")
Alice, here are the ingredients for this cocktail:
- Ingredient 1
- Ingredient 2
- Ingredient 3

Guess the cocktail: Margarita
Correct! The cocktail is Margarita.
1
"""

from random import choice
from wikipedia import get_cocktail_ingredients
from cocktails import cocktails as cocktails_dict


def play_round(player: str, difficulty: str, cocktails=cocktails_dict) -> int:
    """
    Plays a single round of the game by selecting a random cocktail from the given difficulty.

    :param player: The name of the player.
    :param difficulty: The selected difficulty level (easy, medium, hard).
    :param cocktails: The dictionary of cocktails separated by difficulty.

    :return: 1 point for a correct guess, 0 for an incorrect guess or if ingredients are not found.
    """
    cocktail_data = choice(cocktails[difficulty])
    cocktail_name = cocktail_data["name"]
    cocktail_wikipedia = cocktail_data["wikipedia"]

    # Fetch and clean the ingredients from Wikipedia
    ingredients = get_cocktail_ingredients(cocktail_wikipedia)

    if ingredients is None:
        print(f"Could not find ingredients for {cocktail_name}. Skipping...")
        return 0

    print(f"\n{player}, here are the ingredients for this cocktail:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

    # Get the player's guess
    guess = input("\nGuess the cocktail: ").strip()

    # Check if the guess is correct
    if guess.lower() == cocktail_name.lower():
        print(f"Correct! The cocktail is {cocktail_name}.")
        return 1  # Return 1 point for a correct guess
    else:
        print(f"Wrong! The correct cocktail was {cocktail_name}.")
        return 0  # No points for a wrong guess
