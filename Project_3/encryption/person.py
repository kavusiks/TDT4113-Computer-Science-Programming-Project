"""Module: AbstractPerson"""
from abc import ABC, abstractmethod


class AbstractPerson(ABC):
    """Abstract class used by Sender, Receiver and Hacker"""

    def __init__(self, cipher_algorithm):
        self.key = None
        self.cipher_algorithm = cipher_algorithm

    def set_key(self, key):
        """Sets the encryption_key for this Person"""
        self.key = key

    @abstractmethod
    def get_key(self):
        """Returns the encryption_key for this Person"""

    @abstractmethod
    def operate_cipher(self, value):
        """This class' operations"""
