# the reciprocals of the terms in a harmonic sequence are in arithmetic progression
# i.e. harmonic sequence a, b, c can have the harmonic mean 2/b = 1/a + 1/c relationship

# e.g. S(n) = 1 + 1/2 + 1/3 + ... + 1/n
# find the minimum n so that S(n) > K

k = int(input())

s = 0
n = 0
while s <= k:
    n += 1
    s += 1 / n
# out of loop -> s > k

print(n)
