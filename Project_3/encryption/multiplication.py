"""Module: AbstractCipher: Multiplication"""
import math
import random
from encryption.cipher import AbstractCipher
from encryption.sender import Sender
from encryption.receiver import Receiver
from supplemental_files import crypto_utils


class Multiplication(AbstractCipher):
    """Algorithm that encodes by using multiplication with a key"""

    def __init__(self):
        super().__init__()
        self.generate_encryption_key()

    def encode(self, clear_text):
        """The message encoding function"""
        return self.code(clear_text, self.encryption_key)

    def decode(self, encrypted_text):
        """The message decoding function"""
        return self.code(encrypted_text, self.decryption_key)

    def code(self, text, key):
        """Common encoding/decoding method"""
        return_text = ""
        # print(clear_text)
        for char in text:
            # print(char)
            if not self.alphabet_end_at >= ord(char) >= self.alphabet_start_at:
                print(char, "is not in the given alphabet")
                raise ValueError
            # print("char_value", ord(char))
            encoded_char_value = ((ord(char) - self.alphabet_start_at)
                                  * key) % self.alphabet_lenght + self.alphabet_start_at
            # print("Encoder_char_value", encoded_char_value)
            return_text += chr(encoded_char_value)
        return return_text

    def generate_encryption_key(self):
        """Generates a random key that works with the algorithm"""
        possible_keys = self.possible_key()
        self.encryption_key = possible_keys[random.randint(
            0, len(possible_keys) - 1)]
        self.decryption_key = crypto_utils.modular_inverse(
            self.encryption_key, self.alphabet_lenght)

    def possible_key(self):
        """Function that returns a list of all possible keys for this algorithm"""
        p_keys = []
        for i in range(0, self.alphabet_lenght):
            # print(i)
            while math.gcd(i, self.alphabet_lenght) == 1:
                # print(i)
                p_keys.append(i)
                break
        return p_keys


def main():
    """Main Method used for testing"""
    multi = Multiplication()
    sender = Sender(multi, multi.encryption_key)
    receiver = Receiver(multi, multi.encryption_key)
    test_value = "pizza CODE a A Dette Er e NumMer 1."
    receiver.operate_cipher(sender.operate_cipher(test_value))
    print("Verification passed:", multi.verify(test_value))
    # print(multi.possible_key())


if __name__ == '__main__':
    main()
