"""Module: AbstractCipher"""
import random
from encryption.cipher import AbstractCipher
from encryption.sender import Sender
from encryption.receiver import Receiver


class Caesar(AbstractCipher):
    """Algorithm that encodes by using addition with a key"""

    def encode(self, clear_text):
        """The message encoding function"""
        return self.code(clear_text, self.encryption_key)

    def decode(self, encrypted_text):
        """The message decoding function"""
        return self.code(encrypted_text, self.decryption_key)

    def code(self, text, key):
        """Common encoding/decoding method"""
        return_text = ""
        for char in text:
            if not self.alphabet_end_at >= ord(char) >= self.alphabet_start_at:
                print(char, "is not in the given alphabet")
                break
                # exit()
            #print("char_value", ord(char))
            encoded_char_value = (
                (ord(char) - self.alphabet_start_at + key) %
                self.alphabet_lenght) + self.alphabet_start_at
            #print("Encoder_char_value", encoded_char_value)
            return_text += chr(encoded_char_value)
        return return_text

    def generate_encryption_key(self):
        """Generates a random key that works with the algorithm"""
        possible_keys = self.possible_key()
        self.encryption_key = random.randint(
            possible_keys[0], possible_keys[self.alphabet_lenght - 1])
        self.decryption_key = self.alphabet_lenght - self.encryption_key

    def possible_key(self):
        """Function that returns a list of all possible keys for this algorithm"""
        p_keys = []
        for i in range(0, self.alphabet_lenght):
            p_keys.append(i)
        return p_keys


def main():
    """Main Method used for testing"""
    caesar = Caesar()
    sender = Sender(caesar, caesar.encryption_key)
    receiver = Receiver(caesar, caesar.encryption_key)
    test_value = "Dette Er eN Testkode NumMer 1."
    receiver.operate_cipher(sender.operate_cipher(test_value))
    print("Verification passed:", caesar.verify(test_value))


if __name__ == '__main__':
    main()
