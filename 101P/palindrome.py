# given an integer n, please find all the palindrome numbers which are smaller than or equal to n.

n = int(input())

for m in range(1, n + 1):
    x = m
    y = 0
    while x > 0:
        # move 1 digit from x to y on the right
        y = 10 * y + x % 10
        x = x // 10
    # now x == 0
    # y is a rearrangement of digits of m in reverse order
    if y == m:
        print(m)
