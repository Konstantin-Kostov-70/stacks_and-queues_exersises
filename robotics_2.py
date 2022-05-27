from collections import deque
from datetime import datetime, timedelta


class Robot:
    def __init__(self, name, processing):
        self.name = name
        self.processing = processing
        self.busy = datetime.strptime('00:00:00', '%H:%M:%S')


data = input().split(';')
real_time = datetime.strptime(input(), '%H:%M:%S')
robots = []

for info in data:
    robots_name, processing_time = info.split('-')
    robots.append(Robot(robots_name, int(processing_time)))

items = deque()
product = input()

while not product == 'End':
    items.append(product)

    product = input()


while items:
    current_item = items[0]
    real_time += timedelta(seconds=1)
    robot_is_not_free = False

    for robot in robots:
        if real_time >= robot.busy:
            robot.busy = real_time + timedelta(seconds=robot.processing)
            robot_is_not_free = True
            print(f"{robot.name} - {current_item} [{real_time.strftime('%H:%M:%S')}]")
            break
    if robot_is_not_free:
        items.popleft()
    else:
        items.append(items.popleft())









