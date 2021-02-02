"""Module: rock_paper_scissors"""


class Action:
    """Representation of a selection/move. Usefull to make a seperate class
    so that we can define equality and ordering operators"""
    action_values = {'Rock': 0, 'Scissors': 1, 'Paper': 2}
    action_names = {val: name for name, val in action_values.items()}

    def __init__(self, value):
        if isinstance(value, str):
            # We support creator call with text
            # 'Rock', 'Scissors', 'Paper' og integer in [0, 2]
            value = self.action_values[value]
        assert isinstance(value, int) & (value >= 0) & (value < 3)
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        # A move wins the next in modulo 3; otherwise it is a draw or loss
        return (self.value + 1) % 3 == other.value

    def __str__(self):
        return self.action_names[self.value]

    def who_beats_me(self):
        """:returns the value of the number that would beat this instance"""
        # A move wins the next of next in modulo 3
        return (self.value + 2) % 3
