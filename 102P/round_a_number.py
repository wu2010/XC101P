# round it to the nearest ten.
# 12344-> 12340

n = int(input())

a = n // 10
b = n % 10

if b >= 5:
    a += 1
print(a * 10)

# how about the nearest 1000?

n = int(input())
m = 1000

a = n // m
b = n % m

if b >= (m/2):  # half way
    a += 1
print(a * m)
