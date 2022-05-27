from collections import deque

green_light_time = int(input())
yellow_light_time= int(input())
command = input()

cars = deque()
passed_cars = 0
green_light_counter = 0
yellow_light_counter = 0
car_is_crashed = False
green_light_counter_is_down = True

while True:

    if command == "green":
        yellow_light_counter = yellow_light_time
        if cars:
            if green_light_counter_is_down and command == 'green':
                green_light_counter = green_light_time
            current_car = deque(cars.popleft())
            copy_car = current_car.copy()

            while current_car and green_light_counter > 0:
                green_light_counter -= 1
                current_car.popleft()

            if not current_car:
                passed_cars += 1
            else:
                while yellow_light_counter > 0 and current_car:
                    current_car.popleft()
                    yellow_light_counter -= 1
                if current_car:
                    print("A crash happened!")
                    print(f"{''.join(copy_car)} was hit at {current_car.popleft()}.")
                    car_is_crashed = True
                    break
                else:
                    passed_cars += 1

            if car_is_crashed:
                break

            if green_light_counter > 0 and cars:
                green_light_counter_is_down = False
                continue
            else:
                green_light_counter_is_down = True

    elif command == "END":
        print("Everyone is safe.")
        print(f"{passed_cars} total cars passed the crossroads.")
        break

    else:
        cars.append(command)

    command = input()

