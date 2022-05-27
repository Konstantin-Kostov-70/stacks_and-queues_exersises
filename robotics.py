from collections import deque
from datetime import datetime, timedelta


def robo_logic():
    current_robot = free_robots.popleft()
    current_robot['work_time'] = time + timedelta(seconds=current_robot['proces_time'])

    # robot = [el for el in robots if el == current_robot]
    for el in robots:
        if el['name'] == current_robot['name']:
            el['work_time'] = current_robot['work_time']

    print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")


data = input().split(';')
time = datetime.strptime(input(), '%H:%M:%S')
product = input()

products = deque()
robots = []
free_robots = deque()

for info in data:
    name, proces_time = info.split('-')
    work_time = time
    robot = {'name': name, 'proces_time': int(proces_time), 'work_time': work_time}
    robots.append(robot)
    free_robots.append(robot)

while not product == "End":
    products.append(product)

    product = input()

time += timedelta(seconds=1)

while len(products) > 0:
    current_product = products.popleft()
    if free_robots:
        robo_logic()

    else:
        for elem in robots:
            if time >= elem['work_time']:
                free_robots.append(elem)

        if not free_robots:
            products.append(current_product)

        else:
            robo_logic()

    time += timedelta(seconds=1)

