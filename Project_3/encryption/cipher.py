"""Module: AbstractCipher"""
from abc import ABC, abstractmethod


class AbstractCipher(ABC):
    """Abstract class used by all of the crypto-algorithms"""

    def __init__(self):
        self.alphabet_start_at = 32
        self.alphabet_end_at = 126
        self.alphabet_lenght = int(
            self.alphabet_end_at - self.alphabet_start_at + 1)
        self.encryption_key = None
        self.decryption_key = None
        self.generate_encryption_key()

    @abstractmethod
    def encode(self, clear_text):
        """The message encoding function"""

    @abstractmethod
    def decode(self, encrypted_text):
        """The message decoding function"""

    def verify(self, clear_text):
        """Method used to verify encode and decode."""
        encoded_text = self.encode(clear_text)
        decoded_text = self.decode(encoded_text)
        #print("Clear_text:", clear_text)
        #print("Encoded_text:", encoded_text)
        #print("Decoded_text:", decoded_text)
        return (clear_text == decoded_text) and (encoded_text != decoded_text)

    @abstractmethod
    def generate_encryption_key(self):
        """Generates a random key that works with the algorithm"""
