# All even numbers between n and m inclusive, separated by a single space

n, m = map(int, input().split())

if n % 2 != 0:
    n += 1

for i in range(n, m + 1, 2):
    print(i, end=" ")

