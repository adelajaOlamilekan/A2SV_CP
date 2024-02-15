n = int(input())

boxes = list(map(int, input().split()))

box_map = {}

for i in boxes:
    if i in box_map:
        box_map[i] += 1
    else:
        box_map[i] = 1

freq = list(box_map.values())

print(max(freq))
