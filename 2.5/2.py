word = input("Введите слово из маленьких латинских букв: ")

# Множество гласных
vowels = {'a', 'e', 'i', 'o', 'u'}

# Подсчет общего количества гласных и согласных
vowel_count = 0
consonant_count = 0

# Подсчет каждой гласной буквы
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

for ch in word:
    if ch in vowels:
        vowel_count += 1
        # Подсчет каждой гласной
        if ch == 'a':
            a_count += 1
        elif ch == 'e':
            e_count += 1
        elif ch == 'i':
            i_count += 1
        elif ch == 'o':
            o_count += 1
        elif ch == 'u':
            u_count += 1
    else:
        consonant_count += 1

# Вывод общего количества гласных и согласных
print(f"Гласных букв: {vowel_count}")
print(f"Согласных букв: {consonant_count}")

# Вывод количества каждой гласной или False, если она не встречалась
print(f"a: {a_count if a_count > 0 else False}")
print(f"e: {e_count if e_count > 0 else False}")
print(f"i: {i_count if i_count > 0 else False}")
print(f"o: {o_count if o_count > 0 else False}")
print(f"u: {u_count if u_count > 0 else False}")