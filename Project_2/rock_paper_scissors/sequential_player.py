"""Module: rock_paper_scissors"""
from rock_paper_scissors.abstract_player import AbstractPlayer


class Sequential(AbstractPlayer):
    """Plays rock, scissors, paper sequential"""

    def __init__(self, name):
        self.enter_name(name)
        self.last_played = None

    def select_action(self):
        """Selects which action to perform and returns it"""
        to_play_next = self.find_next_play()
        return to_play_next

    def receive_result(self, chosen_by_opponent):
        """The player receive the result from last single game"""

    def find_next_play(self):
        """Finds next play by checking what it played last round"""
        if self.last_played is None:
            self.last_played = 0
        elif self.last_played == 0 or self.last_played == 1:
            self.last_played += 1
        elif self.last_played == 2:
            self.last_played = 0
        return self.last_played


def main():
    """Used for testing"""
    print("test")
    test = Sequential("ole")
    print(test.get_name())
    print(test.select_action())
    print(test.select_action())
    print(test.select_action())
    print(test.select_action())


if __name__ == "__main__":
    main()