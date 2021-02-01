from ProgramFiles.Random import Random
from ProgramFiles.MostCommon import MostCommon
from ProgramFiles.Sequential import Sequential
from ProgramFiles.Action import Action


class SingleGame:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_choice = None
        self.player2_choice = None
        self.player1_points = 0
        self.player2_points = 0

    def perform_game(self):
        self.player1_choice = self.player1.select_action()
        self.player2_choice = self.player2.select_action()
        action1 = Action(self.player1_choice)
        action2 = Action(self.player2_choice)
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
        if isinstance(self.player1, MostCommon):
            #print("funket instans")
            self.player1.receive_result(self.player1_choice, self.player2_choice)

        if isinstance(self.player2, MostCommon):
            #print("funket instans")
            self.player2.receive_result(self.player2_choice, self.player1_choice)

    def show_result(self):
        action1 = Action(self.player1_choice)
        action2 = Action(self.player2_choice)
        if self.player1_points == self.player2_points:
            # print("player 1 har: ", self.player1_points, "player 2 har: ", self.player2_points)
            print("Draw, both chose:", action1.__str__(), action2.__str__())
        elif self.player1_points > self.player2_choice:
            print(self.player1.get_name(), "won this game.", self.player1.get_name(), "chose",
                  action1.__str__(), "and", self.player2.get_name(), "chose", action2.__str__())
        else:
            print(self.player2.get_name(), "won this game.", self.player2.get_name(), "chose",
                  action2.__str__(), "and", self.player1.get_name(), "chose", action1.__str__())

        self.reset_score()

    def reset_score(self):
        # Only used for testing
        self.player1_points = 0
        self.player2_points = 0


def main():
    print("test:")
    random = Random("ran1")
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
    #tester mostcommon sin historikkmetode
    print("tester historikkmetoden i MostCommon")
    print("Andre runde")
    sg3.perform_game()
    sg3.show_result()
    print("tredje runde")
    sg3.perform_game()
    sg3.show_result()
    print("fjerde runde")
    sg3.perform_game()
    sg3.show_result()


if __name__ == "__main__":
    main()
