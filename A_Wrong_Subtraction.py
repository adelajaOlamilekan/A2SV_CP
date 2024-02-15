num, count = list(map(int, input().split()))

for _ in range(count):
    if num % 10 != 0:
        num -= 1
    else:
        num //= 10

print(num)