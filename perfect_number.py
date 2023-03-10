# a perfect number is a positive integer that is equal to the sum of its all positive divisors,
# excluding the number itself.
# For a given positive integer n, output all the perfect numbers between 1 and n

n = int(input())

# skip 1-5 since they are not perfect numbers
for x in range(6, n + 1):
    sum = 1
    # check divisor
    for f in range(2, x // 2 + 1):
        if x % f == 0:
            sum += f
    # check definition
    if sum == x:
        print(x)
