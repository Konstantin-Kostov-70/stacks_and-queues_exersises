from collections import deque

quantity = int(input())

orders = deque(input().split())

max_order = 0

while len(orders) > 0:
    order = int(orders[0])

    if order > max_order:
        max_order = order

    if quantity - order < 0:

        break
    else:
        quantity -= order
        orders.popleft()

print(max_order)

if len(orders) > 0:
    print(f"Orders left: {' '.join(orders)}")

else:
    print('Orders complete')







