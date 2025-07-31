m = int(input())
n = int(input())
weights = [int(input()) for _ in range(n)]

weights.sort()

boats = 0
left, right = 0, n - 1

while left <= right:
    if left == right:
        # Остался один человек
        boats += 1
        break
    if weights[left] + weights[right] <= m:
        # Можно посадить двух человек
        left += 1
        right -= 1
        boats += 1
    else:
        # Везем только самого тяжелого
        right -= 1
        boats += 1

print(boats)