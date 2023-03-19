# find the greatest common divisor (GCD) of two positive integers

a, b = map(int, input().split())
while b > 0:
    r = a % b
    a, b = b, r
    print([a, b])
# now b == 0
print(a)
