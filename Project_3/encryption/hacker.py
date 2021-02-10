"""Module: AbstractPerson: Hacker"""
from encryption.person import AbstractPerson
from encryption.receiver import Receiver
from encryption.sender import Sender
from encryption.unbreakable import Unbreakable
from encryption.affine import Affine
from encryption.caesar import Caesar
from encryption.multiplication import Multiplication


class Hacker(AbstractPerson):
    """A person who uses brute force to decrypt a message"""

    def __init__(self, cipher_algorithm):
        super().__init__(cipher_algorithm)

    def get_key(self):
        """Returns the encryption_key for this Person"""
        return self.key

    def operate_cipher(self, value):
        """This class' operations"""
        return self.cipher_algorithm.decode(value)

    def brute_force(self, encrypted_text):
        """Method used to try all of the possible keys to decode the encrypted text."""
        possible_keys = self.cipher_algorithm.possible_key()
        # print(possible_keys)
        possible_decode = ""
        hacked = False
        for key in possible_keys:
            self.set_key(key)
            possible_decode = self.operate_cipher(encrypted_text)
            # print(possible_decode)
            if self.verify_text(possible_decode):
                hacked = True
                break

        if hacked:
            print("Hacked! The decrypted text is", possible_decode)
        else:
            print("Brute Force failed!")

    def validate(self, decrypted_word):
        """Method used to validate a single word.
        Returns true if it a real word found in the txt-file."""
        english_dictionary = self.generate_dictionary()
        return decrypted_word in english_dictionary

    def verify_text(self, encrypted_text):
        """Method used to verify that an whole decrypted text is a meaningful text."""
        word_by_word = encrypted_text.split()
        for word in word_by_word:
            if not self.validate(word):
                return False
        return True

    @staticmethod
    def generate_dictionary():
        """Function that returns a list of many english words in lower case."""
        file = open("english_words.txt", "r")
        p_keys = []
        for line in file:
            s_line = line.strip()
            l_list = s_line.split()
            p_keys. append(l_list[0])
        return p_keys


def main():
    """Main Method used for testing"""
    print("Main Method")

    print("Caesar")
    test_algo = Caesar()
    test_text = "pizza"
    sender = Sender(test_algo, test_algo.encryption_key)
    receiver = Receiver(test_algo, test_algo.encryption_key)
    encrypted_text = sender.operate_cipher(test_text)
    print(encrypted_text)
    decrypted_by_receiver = receiver.operate_cipher(encrypted_text)
    print("Receiver decrypted message to: ", decrypted_by_receiver)
    hacker = Hacker(test_algo)
    hacker.brute_force(encrypted_text)

    print("Multiplication")
    test_algo = Multiplication()
    test_text = "pizza"
    sender = Sender(test_algo, test_algo.encryption_key)
    receiver = Receiver(test_algo, test_algo.encryption_key)
    encrypted_text = sender.operate_cipher(test_text)
    # print(encrypted_text)
    decrypted_by_receiver = receiver.operate_cipher(encrypted_text)
    print("Receiver decrypted message to: ", decrypted_by_receiver)
    hacker = Hacker(test_algo)
    hacker.brute_force(encrypted_text)

    print("Affine")
    test_algo = Affine()
    test_text = "pizza"
    sender = Sender(test_algo, test_algo.encryption_key)
    receiver = Receiver(test_algo, test_algo.encryption_key)
    encrypted_text = sender.operate_cipher(test_text)
    # print(encrypted_text)
    decrypted_by_receiver = receiver.operate_cipher(encrypted_text)
    print("Receiver decrypted message to: ", decrypted_by_receiver)
    hacker = Hacker(test_algo)
    hacker.brute_force(encrypted_text)

    print("Unbreakable")
    test_algo = Unbreakable()
    test_text = "pizza is very tasty"
    sender = Sender(test_algo, test_algo.encryption_key)
    receiver = Receiver(test_algo, test_algo.encryption_key)
    encrypted_text = sender.operate_cipher(test_text)
    # print(encrypted_text)
    decrypted_by_receiver = receiver.operate_cipher(encrypted_text)
    print("Receiver decrypted message to: ", decrypted_by_receiver)
    hacker = Hacker(test_algo)
    hacker.brute_force(encrypted_text)


if __name__ == '__main__':
    main()
