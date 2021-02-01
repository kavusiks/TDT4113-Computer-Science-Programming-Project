import random
from rock_paper_scissors.abstract_player import AbstractPlayer
from rock_paper_scissors.action import Action


class MostCommon(AbstractPlayer):

    def __init__(self, name):
        # AbstractPlayer.__init__(self)
        #AbstractPlayer.enter_name(self, name)
        self.enter_name(name)
        self.opponents_history = []
        self.opponent_most_played = None

    def select_action(self):
        """Selects which action to perform and returns it"""
        self.update_opponent_most_played()
        if self.opponent_most_played is None:
            return random.randint(0, 2)
        else:
            action = Action(self.opponent_most_played)
            return action.who_beats_me()

    def receive_result(self, chosen_by_opponent):
        """The player receive the result from last single game"""
        self.opponents_history.append(chosen_by_opponent)

    def update_opponent_most_played(self):
        if len(self.opponents_history) > 0:
            rock_count = self.opponents_history.count(0)
            scissors_count = self.opponents_history.count(1)
            paper_count = self.opponents_history.count(2)
            #print("rockantall", rock_count)
            #print("scissorantall", scissors_count)
            #print("paperantall", paper_count)
            if rock_count > scissors_count and rock_count > paper_count:
                self.opponent_most_played = 0
            if scissors_count > paper_count and scissors_count > rock_count:
                self.opponent_most_played = 1
            if paper_count > rock_count and paper_count > scissors_count:
                self.opponent_most_played = 2


def main():
    print("test")


if __name__ == "__main__":
    main()
