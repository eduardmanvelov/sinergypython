class Kassa:
    def __init__(self):
        self.balance = 0

    def top_up(self, X):
        if X < 0:
            raise ValueError("Нельзя пополнить отрицательное количество денег")
        self.balance += X

    def count_1000(self):
        return self.balance // 1000

    def take_away(self, X):
        if X > self.balance:
            raise ValueError("Недостаточно денег в кассе")
        self.balance -= X