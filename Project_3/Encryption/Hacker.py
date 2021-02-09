from Encryption.Person import AbstractPerson


class Hacker(AbstractPerson):

    def __init__(self, cipher_algorithm):
        super().__init__(cipher_algorithm)

    def set_key(self):
        pass

    def get_key(self):
        pass

    def operate_cipher(self, value):
        return self.cipher_algorithm.encode(value)
