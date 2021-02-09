from Encryption.Cipher import AbstractCipher
from Encryption.Sender import Sender
from Encryption.Receiver import Receiver
from supplemental_files import crypto_utils
from Encryption.Caesar import Caesar
from Encryption.Multiplication import Multiplication


class Affine(AbstractCipher):
    def __init__(self, key1, key2):
        self.caesar = None
        self.multi = None
        self.generate_encryption_key(key1, key2)

    def encode(self, clear_text, key):
        return self.caesar.encode(self.multi.encode(clear_text, self.encryption_key[0]), self.encryption_key[1])

    def decode(self, encrypted_text, key):
        return self.multi.decode(self.caesar.decode(encrypted_text, self.encryption_key[1]), self.encryption_key[0])

    def generate_encryption_key(self, value1, value2):
        self.multi = Multiplication(value1)
        self.caesar = Caesar(value2)
        self.encryption_key = (value1, value2)


def main():
    key = 4
    affine = Affine(2,3)
    sender = Sender(affine, key)
    receiver = Receiver(affine, key)
    test_value = "CODE a A Dette Er eN Testkode NumMer 1.N"
    #receiver.operate_cipher(sender.operate_cipher(test_value))
    print("Verification passed:", affine.verify(test_value))


if __name__ == '__main__':
    main()
