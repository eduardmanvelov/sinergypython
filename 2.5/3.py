X = float(input("Введите минимальную сумму инвестиций X: "))
A = float(input("Сумма инвестиций Майкла A: "))
B = float(input("Сумма инвестиций Ивана B: "))

can_mike = A >= X
can_ivan = B >= X

if can_mike and can_ivan:
    print(2)
elif can_mike:
    print("Mike")
elif can_ivan:
    print("Ivan")
elif (A + B) >= X:
    print(1)
else:
    print(0)