from collections import deque

cups = deque(int(x) for x in input().split())
bottles = [int(x) for x in input().split()]

wasted_water = 0

while cups and bottles:
    if bottles[-1] >= cups[0]:
        wasted_water += bottles[-1] - cups[0]
        cups.popleft()
        bottles.pop()

    else:
        while cups[0] >= bottles[-1]:
            cups[0] -= bottles.pop()
        if cups[0] == 0:
            cups.popleft()

cups = [str(x) for x in cups]
bottles = [str(x) for x in bottles]


if len(cups) > 0:
    print(f"Cups: {' '.join(cups)}")
else:
    print(f"Bottles: {' '.join(bottles)}")

print(f"Wasted litters of water: {wasted_water}")







