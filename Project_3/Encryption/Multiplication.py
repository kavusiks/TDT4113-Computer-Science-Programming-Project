from Encryption.Cipher import AbstractCipher
from Encryption.Sender import Sender
from Encryption.Receiver import Receiver
from supplemental_files import crypto_utils


class Multiplication(AbstractCipher):
    def __init__(self, key):
        super().__init__()
        self.generate_encryption_key(key)

    def encode(self, clear_text, key):
        return_text = ""
        print(clear_text)
        for char in clear_text:
            # print(char)
            if not self.alphabet_end_at >= ord(char) >= self.alphabet_start_at:
                print(char, "is not in the given alphabet")
                exit()
            print("char_value", ord(char))
            encoded_char_value = (((ord(
                char) - self.alphabet_start_at) * key) % self.alphabet_lenght) + self.alphabet_start_at
            print("Encoder_char_value", encoded_char_value)
            return_text += chr(encoded_char_value)
        return return_text

    def decode(self, encrypted_text, key):
        return self.encode(encrypted_text, crypto_utils.modular_inverse(self.encryption_key, self.alphabet_lenght))

    def generate_encryption_key(self, value):
        key = value
        while crypto_utils.modular_inverse(key, self.alphabet_lenght) == 1:
            key += 1
            print("Key increaded with one")
        self.encryption_key = key
        self.paired_key = crypto_utils.modular_inverse(key, self.alphabet_lenght)


def main():
    key = 4
    multi = Multiplication(3)
    sender = Sender(multi, key)
    receiver = Receiver(multi, key)
    test_value = "CODE a A Dette Er eN Testkode NumMer 1."
    receiver.operate_cipher(sender.operate_cipher(test_value))
    print("Verification passed:", multi.verify(test_value))


if __name__ == '__main__':
    main()
