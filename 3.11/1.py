def factorial(n):
    """Вычисляет факториал числа n."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def list_factorials_desc(n):
    """Создает список факториалов чисел от n до 1 в убывающем порядке."""
    return [factorial(i) for i in range(n, 0, -1)]

# Пример использования:
num = int(input("Введите натуральное число: "))
fact = factorial(num)
print(f"Факториал числа {num} равен {fact}")
print("Список факториалов в убывающем порядке:", list_factorials_desc(fact))