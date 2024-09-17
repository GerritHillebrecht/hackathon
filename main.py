import wptools
import random
import os
from cocktails import cocktails

"""Multi round and multiplayer version with leaderboard"""


def get_cocktail_ingredients(cocktail_wikipedia):
    """
    Fetches and cleans cocktail ingredients from Wikipedia.

    Args:
        cocktail_wikipedia (str): The Wikipedia page title for the cocktail.

    Returns:
        list: A list of cleaned ingredients if found, otherwise None.
    """
    try:
        # Fetch the Wikipedia page
        page = wptools.page(cocktail_wikipedia).get_parse()
        ingredients = page.data['infobox']["ingredients"]

        # Clean the ingredients by removing unwanted characters
        cleaned_ingredients = [
            ingredient.replace("&nbsp;", " ").replace("[[", "").replace("]]", "").strip()
            for ingredient in ingredients.split("\n")
        ]

        return cleaned_ingredients if cleaned_ingredients else None
    except KeyError:
        print(f"No ingredients found in the infobox for {cocktail_wikipedia}.")
        return None
    except Exception as e:
        print(f"Error fetching cocktail ingredients: {e}")
        return None


def play_round(player, difficulty):
    """
    Plays a single round of the game by selecting a random cocktail from the given difficulty.

    Args:
        player (str): The name of the player.
        difficulty (str): The selected difficulty level (easy, medium, hard).

    Returns:
        int: 1 point for a correct guess, 0 for an incorrect guess or if ingredients are not found.
    """
    cocktail_data = random.choice(cocktails[difficulty])
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


def prompt_difficulty():
    """
    Prompts the user to select a difficulty level.

    Returns:
        str: The selected difficulty level (easy, medium, or hard).
    """
    while True:
        level_selection = input("Choose a difficulty level (easy, medium, hard): ").strip().lower()
        if level_selection not in cocktails:
            print("Invalid input! Please choose easy, medium, or hard.")
        else:
            return level_selection


def get_number_of_rounds():
    """
    Prompts the user to enter the number of rounds to play.

    Returns:
        int: The number of rounds chosen by the user.
    """
    while True:
        rounds_selection = input("Enter the number of rounds: ").strip()
        try:
            num_of_rounds = int(rounds_selection)
            if num_of_rounds > 0:
                return num_of_rounds
            print("Invalid input! Please enter a positive number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_number_of_players():
    """
    Prompts the user to enter the number of players.

    Returns:
        int: The number of players chosen by the user.
    """
    while True:
        players_selection = input("Enter the number of players: ").strip()
        try:
            num_of_players = int(players_selection)
            if num_of_players > 0:
                return num_of_players
            print("Invalid input! Please enter a positive number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_player_names(num_players):
    """
    Prompts each player to enter their name.

    Args:
        num_players (int): The number of players.

    Returns:
        list: A list of player names.
    """
    players = []
    for i in range(num_players):
        name = input(f"Enter the name for player {i + 1}: ").strip()
        players.append(name)
    return players


def display_leaderboard(scores):
    """
    Displays the leaderboard with players' scores and announces the winner.

    Args:
        scores (dict): A dictionary with player names as keys and their scores as values.
    """
    print("\n=== Leaderboard ===")
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    for player, score in sorted_scores:
        print(f"{player}: {score} points")

    winner = sorted_scores[0]
    print(f"\nThe winner is {winner[0]} with {winner[1]} points! Congratulations!")


def save_leaderboard(scores, filename="leaderboard.txt"):
    """
    Saves the leaderboard to a file.

    Args:
        scores (dict): A dictionary with player names as keys and their scores as values.
        filename (str): The name of the file to save the leaderboard to.
    """
    with open(filename, "a") as f:
        for player, score in scores.items():
            f.write(f"{player}: {score}\n")


def play_game():
    """
    Runs the main game loop for a multiplayer game of "Cocktail Connoisseur".
    """
    print("Welcome to Cocktail Connoisseur!")

    # Get the number of players and their names
    num_players = get_number_of_players()
    players = get_player_names(num_players)

    # Prompt the user to select a difficulty level
    difficulty = prompt_difficulty()

    # Prompt the user to enter the number of rounds
    num_of_rounds = get_number_of_rounds()

    # Initialize the players' scores
    scores = {player: 0 for player in players}

    # Play the specified number of rounds
    for round_num in range(num_of_rounds):
        print(f"\n=== Round {round_num + 1} ===")
        for player in players:
            print(f"\n{player}'s turn:")
            scores[player] += play_round(player, difficulty)

    # Display the leaderboard and announce the winner
    display_leaderboard(scores)

    # Save the leaderboard to a file
    save_leaderboard(scores)


# Run the game
if __name__ == "__main__":
    play_game()
