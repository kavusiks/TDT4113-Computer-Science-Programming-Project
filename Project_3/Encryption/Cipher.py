"""Module: Encryption"""
from abc import ABC, abstractmethod


class AbstractCipher(ABC):

    def __init__(self):
        self.alphabet_start_at = 32
        self.alphabet_end_at = 126
        self.alphabet_lenght = int(self.alphabet_end_at - self.alphabet_start_at + 1)
        self.encryption_key = None
        pass

    @abstractmethod
    def encode(self, clear_text, key):
        pass

    @abstractmethod
    def decode(self, encrypted_text, key):
        pass

    def verify(self, clear_text):
        encoded_text = self.encode(clear_text, self.encryption_key)
        decoded_text = self.decode(encoded_text, self.encryption_key)
        print("Clear_text:", clear_text)
        print("Encoded_text:", encoded_text)
        print("Decoded_text:", decoded_text)
        return (clear_text == decoded_text) and (encoded_text != decoded_text)

    @abstractmethod
    def generate_encryption_key(self, value):
        pass


