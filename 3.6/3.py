A, B = map(int, input().split())
for num in range(A, B + 1):
    if num % 2 == 0:
        print(num, end=' ')