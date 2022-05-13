import string

class Caesar:
    def __init__(self) -> None:
        self.abc = string.ascii_lowercase
        self.modes = [self.encrypt, self.decrypt]

    # Возвращает сдвинутый алфавит на n единиц
    def shifted_abc(self, n):
        return self.abc[n:] + self.abc[:n]

    def encrypt(self, message, n):
        table = str.maketrans(self.abc, self.shifted_abc(n))
        return message.lower().translate(table)

    def decrypt(self, message, n):
        table = str.maketrans(self.shifted_abc(n), self.abc)
        return message.lower().translate(table)

c = Caesar()

original = "This text will be encrypted"