my_dict = {}

for i in range(10, -6, -1):  # от 10 до -5 включительно
    # Возводим число i в степень i
    value = i ** i
    
    # Для отрицательных степеней результат будет дробным
    my_dict[i] = value

# Выводим полученный словарь
for key, val in my_dict.items():
    print(f"{key}: {val}")