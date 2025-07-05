n = int(input())
count_zero = 0
for _ in range(n):
    num = int(input())
    if num == 0:
        count_zero += 1
print(count_zero)