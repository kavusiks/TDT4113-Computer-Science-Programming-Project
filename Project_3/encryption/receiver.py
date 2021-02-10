"""Module: AbstractPerson: Receiver"""
from encryption.person import AbstractPerson


class Receiver(AbstractPerson):
    """The person who decodes a message"""

    def __init__(self, cipher_algorithm, key):
        super().__init__(cipher_algorithm)
        self.set_key(key)

    def set_key(self, key):
        """Sets the encryption_key for this Person"""
        self.key = key

    def get_key(self):
        """Returns the encryption_key for this Person"""
        return self.key

    def operate_cipher(self, value):
        """This class' operations"""
        return self.cipher_algorithm.decode(value)
