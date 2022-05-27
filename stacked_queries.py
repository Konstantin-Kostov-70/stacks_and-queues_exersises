count = int(input())
stack = []

for _ in range(count):
    command = input().split()
    action = command[0]
    if action == '1':
        item = int(command[1])
        stack.append(item)

    elif action == '2':
        if len(stack) > 0:
            stack.pop()

    elif action == '3':
        if len(stack) > 0:
            print(max(stack))

    elif action == '4':
        if len(stack) > 0:
            print(min(stack))

stack = [str(x) for x in stack]
print(', '.join(stack[::-1]))
