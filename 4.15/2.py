# Родительский класс
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"

# Наследуемый класс Autobus
class Autobus(Transport):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

# Создаем объект автобуса
autobus = Autobus("Renaul Logan", 180, 12)

# Выводим результат
print(autobus.seating_capacity())