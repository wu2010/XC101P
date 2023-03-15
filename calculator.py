# input: 1 + 2

a, op, b = map(str, input().split())

x = int(a)
y = int(b)

# handle operator op
if op not in ('+', '-', '*', '/'):
    print("Invalid operator!")
elif op == '+':
    print(x + y)
elif op == '-':
    print(x - y)
elif op == '*':
    print(x * y)
elif op == '/':
    if y == 0:
        print("Divided by zero!")
    else:
        print(x / y)
