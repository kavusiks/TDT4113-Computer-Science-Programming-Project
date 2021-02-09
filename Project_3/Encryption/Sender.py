from Encryption.Person import AbstractPerson


class Sender(AbstractPerson):

    def __init__(self, cipher_algorithm, key):
        super().__init__(cipher_algorithm)
        self.set_key(key)

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def operate_cipher(self, value):
        return self.cipher_algorithm.encode(value, self.get_key())
