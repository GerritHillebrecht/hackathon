import prompts
from cocktails import cocktails
from game import play_round
from leaderboard import save_leaderboard, display_leaderboard

"""Multi round and multiplayer version with leaderboard"""


def play_game():
    """
    Runs the main game loop for a multiplayer game of "Cocktail Connoisseur".
    """
    print("Welcome to Cocktail Connoisseur!")

    # Get the number of players and their names
    num_players = prompts.prompt_number_of_players()
    players = prompts.prompt_player_names(num_players)

    # Prompt the user to select a difficulty level
    difficulty = prompts.prompt_difficulty(cocktails)

    # Prompt the user to enter the number of rounds
    num_of_rounds = prompts.prompt_number_of_rounds()

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
