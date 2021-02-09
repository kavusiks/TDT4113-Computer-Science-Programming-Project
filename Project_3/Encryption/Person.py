"""Module: Encryption"""
from abc import ABC, abstractmethod


class AbstractPerson(ABC):

    def __init__(self, cipher_algorithm):
        self.key = None
        self.cipher_algorithm = cipher_algorithm

    @abstractmethod
    def set_key(self):
        pass

    @abstractmethod
    def get_key(self):
        pass

    @abstractmethod
    def operate_cipher(self, value):
        pass
