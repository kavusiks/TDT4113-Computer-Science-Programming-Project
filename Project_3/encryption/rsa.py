"""Module: AbstractCipher: RSA"""
import math
import random
from encryption.cipher import AbstractCipher
from supplemental_files import crypto_utils


class RSA(AbstractCipher):
    """Algorithm that encodes by using a key specified by the receiver of the message"""

    def __init__(self):
        super().__init__()

    def encode(self, clear_text):
        """The message encoding function"""
        blocks = crypto_utils.blocks_from_text(clear_text, 1)
        c_blocks = []
        for block in blocks:
            c_blocks.append(self.encryption_of_integer(block))
        return c_blocks

    def decode(self, encrypted_text):
        """The message decoding function"""
        t_block = []
        for block in encrypted_text:
            t_block.append(self.decryption_of_integer(block))
        return crypto_utils.text_from_blocks(t_block, 8)

    def generate_encryption_key(self):
        """Generates a random key that works with the algorithm"""
        prime_p = crypto_utils.generate_random_prime(8)
        prime_q = crypto_utils.generate_random_prime(8)
        while prime_p == prime_q:
            prime_q = crypto_utils.generate_random_prime(8)
        int_n = prime_p * prime_q
        int_phi = (prime_p - 1) * (prime_q - 1)
        int_e = random.randint(3, int_phi - 1)
        while math.gcd(int_e, int_phi) != 1:
            int_e = random.randint(3, int_phi - 1)
        int_d = crypto_utils.modular_inverse(int_e, int_phi)
        self.encryption_key = (int_n, int_e)
        self.decryption_key = (int_n, int_d)

    def encryption_of_integer(self, int_t):
        """Encrypts by integer. Used as help-function in encode."""
        return pow(int_t, self.encryption_key[1], self.encryption_key[0])

    def decryption_of_integer(self, int_t):
        """Decrypts by integer. Used as help-function in decode."""
        return pow(int_t, self.decryption_key[1], self.decryption_key[0])


def main():
    """Main Method used for testing"""
    rsa = RSA()
    print("Verification passed:", rsa.verify("hra deTTe er 1 test sajJKJKJKL"))


if __name__ == '__main__':
    main()
