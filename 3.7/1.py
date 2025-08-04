s = input()

# Проверка, является ли строка палиндромом
if s == s[::-1]:
    print("yes")
else:
    print("no")