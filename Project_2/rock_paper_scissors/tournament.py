"""Module: rock_paper_scissors"""
import matplotlib.pyplot as plt
#from rock_paper_scissors.most_common_player import MostCommon
from rock_paper_scissors.sequential_player import Sequential
from rock_paper_scissors.historian_player import Historian
from rock_paper_scissors.single_game import SingleGame


class Tournament:
    """Used to arrange a tournament between two players for a given number for games."""

    def __init__(self, player1, player2, number_of_games):
        self.player1 = player1
        self.player2 = player2
        self.number_of_games = number_of_games
        self.player1_total_points = 0
        self.player1_y = []
        #self.player2_total_points = 0
        #self.player2_y = []
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
            #self.player2_total_points += singlegame.player2_points
            self.player1_y.append(self.player1_total_points / (i + 1))
            #self.player2_y.append(self.player2_total_points / (i + 1))

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



def main():
    """Used to test the code"""
    print("test")
    his1 = Historian("his1", 3)
    seq1 = Sequential("seq1")
    #mos1 = MostCommon("mos1")
    tour1 = Tournament(his1, seq1, 100)
    tour1.arrange_singlegame()
    tour1.arrange_tournament()


if __name__ == "__main__":
    main()