from math import ceil

class Tortoise:
    def __init__(self, x=0, y=0, s=1):
        if s <= 0:
            raise ValueError("Количество клеточек s должно быть положительным")
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s <= 1:
            raise ValueError("Невозможно уменьшить s ниже 1")
        self.s -= 1

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        moves_x = ceil(dx / self.s) if dx != 0 else 0
        moves_y = ceil(dy / self.s) if dy != 0 else 0
        return max(moves_x, moves_y)