import collections

# Исходный словарь с данными о питомцах
pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def get_pet(ID):
    """Возвращает информацию о питомце по ID или False, если питомец не найден."""
    return pets.get(ID, False)

def get_suffix(age):
    """Определяет правильный суффикс для слова 'год' в зависимости от возраста."""
    age = abs(age)  # на случай отрицательных значений
    last_two_digits = age % 100
    last_digit = age % 10

    if 11 <= last_two_digits <= 14:
        return 'лет'
    if last_digit == 1:
        return 'год'
    elif 2 <= last_digit <= 4:
        return 'года'
    else:
        return 'лет'

def pets_list():
    """Выводит список всех питомцев."""
    for ID in pets:
        for name, info in pets[ID].items():
            print(f"ID: {ID}")
            print(f"Это {info['Вид питомца']} по кличке \"{name}\". Возраст питомца: {info['Возраст питомца']} {get_suffix(info['Возраст питомца'])}. Имя владельца: {info['Имя владельца']}")
            print("-" * 50)

def create():
    """Создает новую запись о питомце и добавляет ее в словарь."""
    # Получение последнего ID
    if pets:
        last_id = collections.deque(pets, maxlen=1)[0]
    else:
        last_id = 0
    new_id = last_id + 1

    name = input("Введите имя питомца: ")
    вид = input("Введите вид питомца: ")
    возраст = int(input("Введите возраст питомца (в годах): "))
    owner = input("Введите имя владельца: ")

    # Создаем новую запись
    pets[new_id] = {
        name: {
            "Вид питомца": вид,
            "Возраст питомца": возраст,
            "Имя владельца": owner
        }
    }
    print(f"Питомец '{name}' добавлен с ID {new_id}.")

def read():
    """Отображает информацию о запрашиваемом питомце."""
    try:
        ID = int(input("Введите ID питомца для просмотра: "))
        pet_info = get_pet(ID)
        if not pet_info:
            print("Питомец с таким ID не найден.")
            return
        for name, info in pet_info.items():
            print(f"Это {info['Вид питомца']} по кличке \"{name}\". Возраст питомца: {info['Возраст питомца']} {get_suffix(info['Возраст питомца'])}. Имя владельца: {info['Имя владельца']}")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите числовой ID.")

def update():
    """Обновляет информацию о существующем питомце."""
    try:
        ID = int(input("Введите ID питомца для обновления: "))
        pet_info = get_pet(ID)
        if not pet_info:
            print("Питомец с таким ID не найден.")
            return
        for name in list(pet_info.keys()):
            print(f"Обновление информации о {name}:")
            new_name = input(f"Введите новое имя (или оставьте пустым чтобы оставить '{name}'): ")
            new_vid = input("Введите новый вид (или оставьте пустым): ")
            new_age_input = input("Введите новый возраст (или оставьте пустым): ")
            new_owner = input("Введите новое имя владельца (или оставьте пустым): ")

            # Обновление данных
            if new_name:
                pet_info[name]["Имя"] = new_name
                name_to_use = new_name
            else:
                name_to_use = name

            if new_vid:
                pet_info[name]["Вид питомца"] = new_vid
            if new_age_input:
                try:
                    new_age = int(new_age_input)
                    pet_info[name]["Возраст питомца"] = new_age
                except ValueError:
                    print("Некорректный возраст. Оставлено без изменений.")
            if new_owner:
                pet_info[name]["Имя владельца"] = new_owner

            # Если имя изменилось, нужно обновить ключ в словаре
            if name != name_to_use:
                pet_info[name_to_use] = pet_info.pop(name)
                print(f"Имя животного обновлено на '{name_to_use}'.")
        print("Информация обновлена.")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите числовой ID.")

def delete():
    """Удаляет запись о существующем питомце."""
    try:
        ID = int(input("Введите ID питомца для удаления: "))
        if ID in pets:
            del pets[ID]
            print(f"Питомец с ID {ID} удален.")
        else:
            print("Питомец с таким ID не найден.")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите числовой ID.")

# Основной цикл программы
while True:
    command = input("\nВведите команду (create/read/update/delete/list/stop): ").strip().lower()
    
    if command == 'stop':
        print("Завершение работы программы.")
        break
    elif command == 'create':
        create()
    elif command == 'read':
        read()
    elif command == 'update':
        update()
    elif command == 'delete':
        delete()
    elif command == 'list':
        pets_list()
    else:
        print("Неизвестная команда. Попробуйте снова.")