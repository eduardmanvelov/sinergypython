import random

def generate_matrix(rows, cols, min_value=-100, max_value=100):
    """
    Генерирует матрицу размером rows x cols со случайными числами в диапазоне [min_value, max_value].
    """
    return [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]

def add_matrices(matrix_a, matrix_b):
    """
    Складывает две матрицы одинаковых размеров.
    Возвращает новую матрицу как результат.
    """
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    return result

# Задаем размеры матриц
rows, cols = 10, 10

# Генерируем две матрицы
matrix_1 = generate_matrix(rows, cols)
matrix_2 = generate_matrix(rows, cols)

# Складываем матрицы
matrix_sum = add_matrices(matrix_1, matrix_2)

# Выводим результаты
print("Матрица 1:")
for row in matrix_1:
    print(row)

print("\nМатрица 2:")
for row in matrix_2:
    print(row)

print("\nСумма матриц:")
for row in matrix_sum:
    print(row)