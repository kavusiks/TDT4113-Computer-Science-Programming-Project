from rock_paper_scissors.random_player import Random
from rock_paper_scissors.most_common_player import MostCommon
from rock_paper_scissors.sequential_player import Sequential
from rock_paper_scissors.historian_player import Historian
from rock_paper_scissors.action import Action


class SingleGame:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_choice = None
        self.player2_choice = None
        self.player1_points = 0
        self.player2_points = 0

    def perform_game(self):
        self.reset_score()
        self.player1_choice = self.player1.select_action()
        self.player2_choice = self.player2.select_action()
        action1 = Action(self.player1_choice)
        #print("Sp1,", action1)
        action2 = Action(self.player2_choice)
        #print("Sp2,", action2)
        if action1.__eq__(action2):
            # print(self.player1.get_name(), action1.__str__(), "value:", self.player1_choice)
            # print(self.player2.get_name(), action2.__str__(), "value:", self.player2_choice)
            self.player1_points += 0.5
            self.player2_points += 0.5
        elif action1.__gt__(action2):
            # print(self.player1.get_name(), action1.__str__(), "value:", self.player1_choice)
            # print(self.player2.get_name(), action2.__str__(), "value:", self.player2_choice)
            self.player1_points += 1
        else:
            # print(self.player1.get_name(), action1.__str__(), "value:", self.player1_choice)
            # print(self.player2.get_name(), action2.__str__(), "value:", self.player2_choice)
            self.player2_points += 1

        self.player1.receive_result(self.player2_choice)

        self.player2.receive_result(self.player1_choice)
        #print("p1-poeng", self.player1_points)
        #print("p2-poeng", self.player2_points)
        self.show_result()

    def show_result(self):
        action1 = Action(self.player1_choice)
        action2 = Action(self.player2_choice)
        if self.player1_points == self.player2_points:
            #print("player 1 har: ", self.player1_points, "player 2 har: ", self.player2_points)
            print("Draw, both chose:", action1.__str__(), action2.__str__())
        elif self.player1_points > self.player2_points:

            #print("player 1 har: ", self.player1_points, "player 2 har: ", self.player2_points)
            print(
                self.player1.get_name(),
                "won this game.",
                self.player1.get_name(),
                "chose",
                action1.__str__(),
                "and",
                self.player2.get_name(),
                "chose",
                action2.__str__())
        else:

            #print("player 1 har: ", self.player1_points, "player 2 har: ", self.player2_points)
            print(
                self.player2.get_name(),
                "won this game.",
                self.player2.get_name(),
                "chose",
                action2.__str__(),
                "and",
                self.player1.get_name(),
                "chose",
                action1.__str__())

    def reset_score(self):
        # Only used for testing
        self.player1_points = 0
        self.player2_points = 0


def main():
    print("test:")
    """random = Random("ran1")
    seqiential = Sequential("seq1")
    mostcommon2 = MostCommon("mos2")
    mostcommon = MostCommon("mos1")
    sg1 = SingleGame(random, seqiential)
    sg1.perform_game()
    print("game1: ")
    sg1.show_result()

    sg2 = SingleGame(seqiential, mostcommon2)
    sg2.perform_game()
    print("game2: ")
    sg2.show_result()
    print(" ")
    sg3 = SingleGame(random, mostcommon)
    sg3.perform_game()
    print("game3: ")
    sg3.show_result()
    # tester mostcommon sin historikkmetode
    print("tester historikkmetoden i MostCommon")
    print("Andre runde")
    sg3.perform_game()
    sg3.show_result()
    print("tredje runde")
    sg3.perform_game()
    sg3.show_result()
    print("fjerde runde")
    sg3.perform_game()
    sg3.show_result()"""

    print(" ")
    print("Historian vs MostCommon")
    historian = Historian("His1", 10)
    sequential2 = Sequential("Seq2")
    sg4 = SingleGame(historian, sequential2)
    for i in range(50):
        print("runde: ", i)
        sg4.perform_game()


if __name__ == "__main__":
    main()
