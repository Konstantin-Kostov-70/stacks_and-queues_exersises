from collections import deque

count = int(input())
pumps = deque()

is_tour = True

for _ in range(count):
    pumps.append(input())

for num_of_pump in range(len(pumps)):
    is_tour = True
    tank = 0

    for tour in pumps:
        petrol, distance = tour.split()
        tank += int(petrol)
        distance = int(distance)

        if tank >= distance:
            tank -= distance
            continue
        else:
            pumps.rotate(-1)
            tank = 0
            is_tour = False
            break
    if is_tour:
        print(num_of_pump)
        break


