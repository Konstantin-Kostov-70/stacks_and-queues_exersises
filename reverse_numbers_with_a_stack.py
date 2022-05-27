data = input().split()

stack = []

for _ in range(len(data)):
    stack.append(data.pop())

print(' '.join(stack))

