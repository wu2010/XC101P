# find the greatest common divisor (GCD) of two positive integers

a, b = map(int, input().split())
while b > 0:
    a = a % b
    a, b = b, a
# now b == 0
print(a)
