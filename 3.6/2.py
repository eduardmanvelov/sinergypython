X = int(input())
count_divisors = 0
i = 1
while i * i <= X:
    if X % i == 0:
        count_divisors += 1
        if i != X // i:
            count_divisors += 1
    i += 1
print(count_divisors)
