"""Module: rock_paper_scissors"""
import matplotlib.pyplot as plt

from rock_paper_scissors.historian_player import Historian
from rock_paper_scissors.most_common_player import MostCommon
from rock_paper_scissors.random_player import Random
from rock_paper_scissors.sequential_player import Sequential
from rock_paper_scissors.single_game import SingleGame


class Tournament:
    """Used to arrange a tournament between two players for a given number for games."""

    def __init__(self, player1, player2, number_of_games):
        self.player1 = player1
        self.player2 = player2
        self.number_of_games = number_of_games
        self.player1_total_points = 0
        self.player1_y = []
        # self.player2_total_points = 0
        # self.player2_y = []
        self.players_x = []

    def arrange_singlegame(self):
        """Used to play a single game between the players"""
        singlegame = SingleGame(self.player1, self.player2)
        singlegame.perform_game()

    def arrange_tournament(self):
        """Used to start the tournament. Show to win percentage in a graph."""
        singlegame = SingleGame(self.player1, self.player2)
        for i in range(self.number_of_games):
            print("Game: ", i + 1)
            self.players_x.append(i + 1)
            singlegame.perform_game()
            self.player1_total_points += singlegame.player1_points
            # self.player2_total_points += singlegame.player2_points
            self.player1_y.append(self.player1_total_points / (i + 1))
            # self.player2_y.append(self.player2_total_points / (i + 1))

        self.show_graph()

    def show_graph(self):
        """Used to plot the win percentage graph"""
        plt.plot(self.players_x, self.player1_y)
        plt.xlabel("x - number of games")
        plt.ylabel("y - win percent")
        plt.title("Player 1 - win percentage")
        plt.xlim(0, self.number_of_games)
        plt.ylim(0, 1)
        plt.show()


def check_correct_type_of_player(player: str):
    """ Checks that the typed in player type i within the available characters"""
    available_characters = ("random", "sequential", "most common", "historian")
    if player.lower() in available_characters:
        return player.lower()
    return "not_set"


def enter_character_name():
    """Function used to enter in type of character"""
    character = "not_set"
    first_try = True
    is_set = False
    while not is_set:
        if not first_try:
            print(
                "Wrong character name. Type in either 'Random', 'Sequential', "
                "'Most common' or 'Historian' for the player again:")
        character = input("Enter name of the character you want to set up: ")
        character = check_correct_type_of_player(character)
        if character != "not_set":
            is_set = True
        first_try = False
    return character


def get_input_as_integer():
    """Function user to get user input and verify that it is an integer"""
    count = input("Enter a number for the count: ")
    while not count.isdigit():
        print("That was not an integer. Try again")
        count = input("Enter a number for the count: ")
    return int(count)


def set_remember_for_historian(player):
    """Used to get user's count for remember if player is 'Historian'."""
    remember = None
    if player == "historian":
        print("This player is 'Historian', what should the count be for 'remember'?")
        remember = get_input_as_integer()
    return remember


def create_player_by_name(player: str, player_name: str, remember):
    """Used to create character based on the chosen type."""
    if player == "random":
        return Random(player_name)
    if player == "sequential":
        return Sequential(player_name)
    if player == "most common":
        return MostCommon(player_name)
    if player == "historian":
        return Historian(player_name, remember)


def start_play(game_type, player1, player2):
    """Funcionn used to start a single game or tournament by user's choice"""
    game_types = ("single game", "tournament")
    while game_type.lower() not in game_types:
        print("Wrong input! Try again")
        game_type = input("type in 'singlegame' or 'tournament': ")
    if game_type == "tournament":
        print("How many rounds do you want in the tournament? ")
        amount = get_input_as_integer()
        tour = Tournament(player1, player2, amount)
        tour.arrange_tournament()
    else:
        single_game = SingleGame(player1, player2)
        single_game.perform_game()


def text_based_interface():
    """ Text based user interactions interface"""
    character1 = enter_character_name()
    player1_name = input("Enter your " + character1 + "´s " + "name: ")
    remember1 = set_remember_for_historian(character1)
    character2 = enter_character_name()
    player2_name = input("Enter your " + character2 + "´s " + "name: ")
    remember2 = set_remember_for_historian(character2)
    player1 = create_player_by_name(character1, player1_name, remember1)
    player2 = create_player_by_name(character2, player2_name, remember2)
    print(
        "The Players are set:",
        "player1",
        character1,
        player1_name,
        "and",
        "player2",
        character2,
        player2_name)

    same_game = True
    while same_game:
        start_play(
            input("type in 'single game' or 'tournament': "),
            player1,
            player2)
        continue_same_game = input(
            "New round with the same players? (y/n)")
        if continue_same_game.lower() == "n":
            new_players = input("Set up new players? (y/n)")
            if new_players.lower() == "y":
                same_game = False
            else:
                print("Bye!")
                exit()


def main():
    """Main method"""


while True:
    text_based_interface()

if __name__ == "__main__":
    main()
