'''Module: rock_paper_scissors'''
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
            #print("history", self.opponents_history)
            self.update_subsequence()
            self.find_last_indices_of_subsequence_in_history()
        #action = None
        if len(self.last_indices_of_subsequence_in_history) == 0:
            print("randomt tall")
            return random.randint(0, 2)
        else:
            action = Action(self.find_most_frequent())
            print(action)
            return action.who_beats_me()

    def receive_result(self, chosen_by_opponent):
        """The player receive the result from last single game"""
        self.opponents_history.append(chosen_by_opponent)

    def update_subsequence(self):
        self.subsequence = []
        self.last_indices_of_subsequence_in_history = []
        if len(self.opponents_history) < self.remember:
            return
        for i in range(len(self.opponents_history) -
                       self.remember, len(self.opponents_history)):
            self.subsequence.append(self.opponents_history[i])
        # print(self.sequence)

    def find_last_indices_of_subsequence_in_history(self):

        if len(self.opponents_history) < self.remember:
            return
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
        #print("history", self.opponents_history)
        #print("utenory", history_without_subsequence)
        #print("subseq", self.subsequence)
        #print("index på siste", self.last_indices_of_subsequence_in_history)

    def find_most_frequent(self):
        opponent_most_likely_to_chose_next = []
        for x in self.last_indices_of_subsequence_in_history:
            opponent_most_likely_to_chose_next.append(
                self.opponents_history[x + 1])
        zero = 0
        one = 0
        two = 0
        for x in opponent_most_likely_to_chose_next:
            if x == 0:
                zero += 1
            if x == 1:
                one += 1
            if x == 2:
                two += 1
        #print("max", max(zero, one, two))
        most_frequent = max(zero, one, two)
        if most_frequent == zero:
            return 0
        if most_frequent == one:
            return 1
        if most_frequent == two:
            return 2

    def cleanup_list(self, list_to_clean: list):
        cleaned_list = list_to_clean.copy()
        # removing duplicates
        cleaned_list = sorted(dict.fromkeys(cleaned_list))
        final_cleaned_list = cleaned_list.copy()
        indices_to_remove = []
        print("cleaned", cleaned_list)
        for i in range(len(cleaned_list) - self.remember):
            print(i)
            for j in range(1, self.remember):
                print(j)
                if cleaned_list[i + j] != cleaned_list[i] + j:
                    # indices_to_remove.append(i)
                    final_cleaned_list.pop(i)
        list_length = len(cleaned_list)
        """for i in range(list_length):
            cleaned_list.remove(indices_to_remove[i])"""
        return final_cleaned_list


def main():
    print("test")
    his1 = Historian("his1", 3)
    for i in range(10):
        his1.receive_result(i % 3)
        print(his1.select_action())


if __name__ == "__main__":
    main()
