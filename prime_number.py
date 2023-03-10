# A prime number is a positive integer greater than 1 whose factors are only 1 and iteself.
# is N a prime?

import math

N = int(input())

size = 1
primes = [2]

i = 3
while math.pow(i, 2) <= N:
    is_i_prime = True
    for prime in primes:
        if i % prime == 0:
            is_i_prime = False
            break
    if is_i_prime:
        primes.append(i)
        size += 1
    i += 2

# print(primes)


if N <= 2:
    print('Yes')
else:
    is_n_prime = True
    for prime in primes:
        if N % prime == 0:
            is_n_prime = False
            break
    print('Yes' if is_n_prime else 'No')
