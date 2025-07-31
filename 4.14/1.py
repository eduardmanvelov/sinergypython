my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def print_elements(index):
    # Проверяем, не вышли ли за границы списка
    if index >= len(my_list):
        print("Конец списка")
        return
    # Выводим текущий элемент
    print(my_list[index])
    # Рекурсивно вызываем для следующего элемента
    print_elements(index + 1)

# Запускаем функцию с первого элемента (индекс 0)
print_elements(0)