from collections import deque

bullets_price = int(input())
gun_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
value = int(input())

all_bullets = len(bullets)
bullets_counter = 0
gun_size_counter = gun_size
all_is_unlocked = True

while locks:
    if not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        all_is_unlocked = False
        break
    else:
        bullets_counter += 1
        gun_size_counter -= 1

        if bullets[-1] > locks[0]:
            bullets.pop()
            print('Ping!')

        elif bullets[-1] <= locks[0]:
            bullets.pop()
            locks.popleft()
            print("Bang!")

    if gun_size_counter == 0 and bullets:
        gun_size_counter = gun_size
        print("Reloading!")

bullets_left = all_bullets - bullets_counter
price = value - (bullets_counter * bullets_price)

if all_is_unlocked:
    print(f"{bullets_left} bullets left. Earned ${price}")