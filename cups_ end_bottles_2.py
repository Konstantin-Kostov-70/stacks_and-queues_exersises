from collections import deque

cups = deque(int(x)for x in input().split())
bottles = deque(int(x)for x in input().split())

wasted_water = 0

while cups and bottles:
    cup = cups.popleft() - bottles.pop()
    if cup > 0:
        cups.appendleft(cup)
    else:
        wasted_water += abs(cup)

if cups:
    print(f"Cups: {' '.join([str(x) for x in cups])}")

else:
    print(f"Bottles: {' '.join([str(x) for x in bottles])}")

print(f"Wasted litters of water: {wasted_water}")