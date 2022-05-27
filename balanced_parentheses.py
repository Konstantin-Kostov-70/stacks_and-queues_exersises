parentheses = input()
open_parentheses = []

balanced = {'(': ')', '{': '}', '[': ']'}

is_balanced = True

for char in parentheses:
    if char in '({[':
        open_parentheses.append(char)
    else:
        if not open_parentheses:
            is_balanced = False
            break
        else:
            if balanced[open_parentheses[-1]] == char:
                open_parentheses.pop()
            else:
                is_balanced = False
                break

if is_balanced:
    print('YES')
else:
    print('NO')

