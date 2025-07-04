number = int(input("Введите пятизначное число: "))

if len(number) != 5 or not number.isdigit():
    print("Ошибка: введите именно пятизначное число.")
else:

    # Получаем цифры по разрядам с помощью деления и остатка
    thousands_tenth = number // 10000          # десятки тысяч
    thousands = (number // 1000) % 10          # тысячи
    hundreds = (number // 100) % 10            # сотни
    tens = (number // 10) % 10                 # десятки
    units = number % 10                        # единицы

    # Возводим в степень количество десятков (tens) число единиц (units)
    power_result = tens ** units

    # Умножаем результат на количество сотен
    multiplied = power_result * hundreds

    # Находим разность между десятками тысяч и тысячами
    denominator = thousands_tenth - thousands

    if denominator == 0:
        print("Ошибка: деление на ноль.")
    else:
        result = multiplied / denominator
        print(f"Результат: {result}")