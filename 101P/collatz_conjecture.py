# Consider the following operation on an arbitrary positive integer:
# If the number is even, divide it by two.
# If the number is odd, triple it and add one.

# The Collatz conjecture is: This process will eventually reach the number 1,
# regardless of which positive integer is chosen initially.

n = int(input())

t = 0
while n > 1:
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1
    # always +1 for each loop
    t += 1
# now n == 1
print(t)
