n = int(input())

min_cap = 0 

population = 0

for _ in range(n):
    exit, enter = map(int, input().split())
    population += enter - exit

    min_cap = max(min_cap, population)

print(min_cap)
