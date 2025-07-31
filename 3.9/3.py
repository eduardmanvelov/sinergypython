sequence = list(map(int, input().split()))
seen = set()

for num in sequence:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)