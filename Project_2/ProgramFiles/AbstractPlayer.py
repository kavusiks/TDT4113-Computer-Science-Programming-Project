from abc import ABC, abstractmethod


class AbstractPlayer(ABC):

    def __init__(self):
        self.action_by_number = {"rock": 0, "paper": 1, "scissor": 2}
        self.name = NotImplemented

    @abstractmethod
    def select_action(self):
        """Selects which action to perform and returns it"""
        pass

    @abstractmethod
    def receive_result(self, chosen_by_me, chosen_by_opponent):
        """The player receive the result from last single game"""
        pass

    def enter_name(self, name):
        """The name of the class that inherit this class"""
        self.name = name

    def get_name(self):
        """Return the name of the current class"""
        return self.name
