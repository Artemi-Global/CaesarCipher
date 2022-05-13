import string

class Caesar:
    def __init__(self) -> None:
        self.abc = string.ascii_lowercase           # Английский алфавит
        self.modes = [self.encrypt, self.decrypt]   # Функции перевода

    # Возвращает сдвинутый алфавит на n единиц
    def shifted_abc(self, n):
        return self.abc[n:] + self.abc[:n]

    # Шифровка
    def encrypt(self, message, n):
        table = str.maketrans(self.abc, self.shifted_abc(n))
        return message.lower().translate(table)
        
    # Расшифровка
    def decrypt(self, message, n):
        table = str.maketrans(self.shifted_abc(n), self.abc)
        return message.lower().translate(table)
