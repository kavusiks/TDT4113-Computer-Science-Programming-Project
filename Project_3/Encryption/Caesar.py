from Encryption.Cipher import AbstractCipher
from Encryption.Sender import Sender
from Encryption.Receiver import Receiver


class Caesar(AbstractCipher):
    def __init__(self, key):
        super().__init__()
        self.generate_encryption_key(key)

    def encode(self, clear_text, key):
        return_text = ""
        for char in clear_text:
            if not self.alphabet_end_at >= ord(char) >= self.alphabet_start_at:
                print(char, "is not in the given alphabet")
                exit()
            print("char_value", ord(char))
            encoded_char_value = ((ord(
                char) - self.alphabet_start_at + key) % self.alphabet_lenght) + self.alphabet_start_at
            print("Encoder_char_value", encoded_char_value)
            return_text += chr(encoded_char_value)
        return return_text
    def decode(self, encrypted_text, key):
        return self.encode(encrypted_text, (self.alphabet_lenght - key))


    def generate_encryption_key(self, value):
        self.encryption_key = value
        pass



def main():
    key = 4
    caesar = Caesar(key)
    sender = Sender(caesar, key)
    receiver = Receiver(caesar, key)
    test_value = "Dette Er eN Testkode NumMer 1."
    receiver.operate_cipher(sender.operate_cipher(test_value))
    print("Verification passed:", caesar.verify(test_value) )


if __name__ == '__main__':
    main()
