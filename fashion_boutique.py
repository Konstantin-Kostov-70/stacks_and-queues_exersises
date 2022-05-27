clothes = input().split()
capacity = int(input())

boxes = 1
current_capacity = 0

while len(clothes) > 0:
    cloth = int(clothes.pop())
    if current_capacity + cloth > capacity:
        current_capacity = 0
        boxes += 1

    current_capacity += cloth

print(boxes)

