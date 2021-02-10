"""Module: AbstractCipher: Unbreakable"""
import random
from encryption.cipher import AbstractCipher


class Unbreakable(AbstractCipher):
    """Algorithm that encodes by using a word as key"""

    def __init__(self):
        super().__init__()

    def encode(self, clear_text):
        """The message encoding function"""
        return self.code(clear_text, self.encryption_key)

    def decode(self, encrypted_text):
        """The message decoding function"""
        return self.code(encrypted_text, self.decryption_key)

    def code(self, text, key):
        """Common encoding/decoding method"""
        return_text = ""
        for i in range(len(text)):
            encoded_char_value = ((ord(text[i]) + ord(key[i % len(key)])
                                   - self.alphabet_start_at * 2) % self.alphabet_lenght) \
                                 + self.alphabet_start_at

            return_text += chr(encoded_char_value)
        return return_text

    def generate_encryption_key(self):
        """Generates a random key that works with the algorithm"""
        possible_keys = self.possible_key()
        self.encryption_key = possible_keys[random.randint(
            0, len(possible_keys))]
        decryption_key = ""
        for char in self.encryption_key:
            decryption_key += chr((self.alphabet_lenght -
                                   ord(char) +
                                   self.alphabet_start_at) %
                                  self.alphabet_lenght +
                                  self.alphabet_start_at)
        self.decryption_key = decryption_key

    @staticmethod
    def possible_key():
        """Function that returns a list of all possible keys for this algorithm"""
        file = open("english_words.txt", "r")
        p_keys = []
        for line in file:
            s_line = line.strip()
            l_list = s_line.split()
            p_keys.append(l_list[0])
        return p_keys


def main():
    """Main Method used for testing"""
    unbreakable = Unbreakable()
    print("Verification passed:", unbreakable.verify("HEMMELIGHET"))
    unbreakable.possible_key()


if __name__ == '__main__':
    main()
