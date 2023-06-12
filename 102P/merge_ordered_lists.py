# Given two sorted arrays, both in descending order.
# Merge these two arrays into a new ordered array in descending order and output

a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
j = 0
c = []

while i < len(a) and j < len(b):
    if a[i] > b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

# now, i >= len(a) or j >= len(b)
if i == len(a):
    for k in range(j, len(b)):
        c.append(b[k])
else:
    for k in range(i, len(a)):
        c.append(a[k])

print(*c)

# input
# 8 5 4
# 7 6 3 1

# output
# 8 7 6 5 4 3 1
