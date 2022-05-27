from collections import deque

green_light_time = int(input())
yellow_light_time = int(input())

cars = deque()
passed_cars = 0
is_crashed = False

while True:
    command = input()

    if command == 'END':
        break

    elif command == "green":
        current_time = green_light_time

        while cars and current_time > 0:
            car = cars.popleft()
            if current_time >= len(car) or (current_time + yellow_light_time) >= len(car):
                current_time -= len(car)
                passed_cars += 1

            else:
                index = current_time + yellow_light_time
                print("A crash happened!")
                print(f"{car} was hit at {car[index]}.")
                is_crashed = True
                break

    else:
        cars.append(command)

    if is_crashed:
        break


if not is_crashed:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")

