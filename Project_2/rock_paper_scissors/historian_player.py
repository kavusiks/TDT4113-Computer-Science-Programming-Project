"""Module: rock_paper_scissors"""
import random

from rock_paper_scissors.abstract_player import AbstractPlayer
from rock_paper_scissors.action import Action


class Historian(AbstractPlayer):
    """Player who can remember opponents lasts choices"""

    def __init__(self, name, remember):
        self.enter_name(name)
        self.opponents_history = []
        self.remember = remember
        self.subsequence = []
        self.last_indices_of_subsequence_in_history = []

    def select_action(self):
        """Selects which action to perform and returns it"""
        if len(self.opponents_history) != 0:
            # print("history", self.opponents_history)
            self.update_subsequence()
            self.find_last_indices_of_subsequence_in_history()
        # action = None
        if len(self.last_indices_of_subsequence_in_history) == 0:
            print("randomt tall")
            return random.randint(0, 2)
        else:
            action = Action(self.find_most_frequent())
            #print(action)
            return action.who_beats_me()

    def receive_result(self, chosen_by_opponent):
        """The player receive the result from last single game"""
        self.opponents_history.append(chosen_by_opponent)

    def update_subsequence(self):
        """Used to fin the current subsequence we are looking for"""
        self.subsequence = []
        self.last_indices_of_subsequence_in_history = []
        if len(self.opponents_history) < self.remember:
            return
        for i in range(len(self.opponents_history) -
                       self.remember, len(self.opponents_history)):
            self.subsequence.append(self.opponents_history[i])
        # print(self.sequence)

    def find_last_indices_of_subsequence_in_history(self):
        """Finds the last index of all the subsequences found in opponents_history"""

        if len(self.opponents_history) < self.remember:
            return None
        history_without_subsequence = self.opponents_history.copy()
        for i in range(len(self.opponents_history) -
                       self.remember, len(self.opponents_history)):
            history_without_subsequence.pop()
        for i in range(len(history_without_subsequence) -
                       len(self.subsequence) + 1):
            for j in range(len(self.subsequence)):
                if history_without_subsequence[i + j] != self.subsequence[j]:
                    break
            else:
                self.last_indices_of_subsequence_in_history.append(i + j)
        # print("history", self.opponents_history)
        # print("utenory", history_without_subsequence)
        # print("subseq", self.subsequence)
        # print("index på siste", self.last_indices_of_subsequence_in_history)

    def find_most_frequent(self):
        """Returns the most frequent value of all
        the possible plays by opponent for the coming round"""
        opponent_most_likely_to_chose_next = []
        for index in self.last_indices_of_subsequence_in_history:
            opponent_most_likely_to_chose_next.append(
                self.opponents_history[index + 1])
        zero = 0
        one = 0
        two = 0
        for value in opponent_most_likely_to_chose_next:
            if value == 0:
                zero += 1
            if value == 1:
                one += 1
            if value == 2:
                two += 1
        # print("max", max(zero, one, two))
        most_frequent = max(zero, one, two)
        if most_frequent == zero:
            return 0
        if most_frequent == one:
            return 1
        if most_frequent == two:
            return 2


def main():
    """testing method used for debugging"""
    print("test")
    his1 = Historian("his1", 3)
    for i in range(10):
        his1.receive_result(i % 3)
        print(his1.select_action())


if __name__ == "__main__":
    main()
