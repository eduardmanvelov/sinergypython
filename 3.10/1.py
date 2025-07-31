# Создаем пустой словарь
pets = {}

# Запрашиваем у пользователя имя питомца
name_pet = input("Введите имя питомца: ")

# Заполняем словарь для этого питомца
pets[name_pet] = {
    'Вид питомца': input("Введите вид питомца (например, Собака, Кошка): "),
    'Возраст питомца': int(input("Введите возраст питомца: ")),
    'Имя владельца': input("Введите имя владельца: ")
}

# Получаем возраст для склонения
age = pets[name_pet]['Возраст питомца']

# Определяем правильное слово для "год"
if 11 <= age % 100 <= 14:
    year_word = "лет"
else:
    last_digit = age % 10
    if last_digit == 1:
        year_word = "год"
    elif last_digit in [2,3,4]:
        year_word = "года"
    else:
        year_word = "лет"

# Выводим информацию о питомце
print(f"Это {name_pet}.")
print(f"{name_pet} — {pets[name_pet]['Вид питомца']}.")
print(f"Его возраст: {age} {year_word}.")
print(f"Имя владельца: {pets[name_pet]['Имя владельца']}.")

# Также выводим всю информацию через keys() и values()
keys_list = list(pets[name_pet].keys())
values_list = list(pets[name_pet].values())

print("\nИнформация о питомце:")
print("Ключи:", keys_list)
print("Значения:", values_list)