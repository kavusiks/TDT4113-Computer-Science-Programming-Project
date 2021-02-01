import random
from rock_paper_scissors.abstract_player import AbstractPlayer


class Random(AbstractPlayer):

    def __init__(self, name):
        # AbstractPlayer.__init__(self)
        #AbstractPlayer.enter_name(self, name)
        self.enter_name(name)

    def select_action(self):
        """Selects which action to perform and returns it"""
        return random.randint(0, 2)

    def receive_result(self, chosen_by_opponent):
        """The player receive the result from last single game"""
        pass


def main():
    print("test")
    test = Random("ole")
    print(test.get_name())
    print(test.select_action())


if __name__ == "__main__":
    main()
