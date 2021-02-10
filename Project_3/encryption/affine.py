"""Module: AbstractCipher: Affine"""
from encryption.caesar import Caesar
from encryption.cipher import AbstractCipher
from encryption.multiplication import Multiplication


class Affine(AbstractCipher):
    """Algorithm that encodes by using a combination of Caesar and Multiplication"""

    def __init__(self):
        self.caesar = None
        self.multi = None
        super().__init__()

    def encode(self, clear_text):
        """The message encoding function"""
        return self.caesar.encode(
            self.multi.encode(
                clear_text))

    def decode(self, encrypted_text):
        """The message decoding function"""
        return self.multi.decode(
            self.caesar.decode(
                encrypted_text))

    def generate_encryption_key(self):
        """Generates a random key that works with the algorithm"""
        self.multi = Multiplication()
        self.multi.generate_encryption_key()
        self.caesar = Caesar()
        self.caesar.generate_encryption_key()
        self.encryption_key = (
            self.multi.encryption_key,
            self.caesar.encryption_key)

    def possible_key(self):
        """Function that returns a list of all possible keys for this algorithm"""
        p_multi = self.multi.possible_key()
        p_caeser = self.caesar.possible_key()
        possible_keys = []
        for key1 in p_multi:
            for key2 in p_caeser:
                possible_keys.append((key1, key2))
        return possible_keys


def main():
    """Main Method used for testing"""
    affine = Affine()
    test_value = "CODE a A Dette Er eN Testkode NumMer 1.N"
    # receiver.operate_cipher(sender.operate_cipher(test_value))
    print("Verification passed:", affine.verify(test_value))


if __name__ == '__main__':
    main()
