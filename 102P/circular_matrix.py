# input 4
# 1 1 1 1
# 1 2 2 1
# 1 2 2 1
# 1 1 1 1

# input 5
# 1 1 1 1 1
# 1 2 2 2 1
# 1 2 3 2 1
# 1 2 2 2 1
# 1 1 1 1 1

import math

n = int(input())

# center (c, c)
c = (n - 1) / 2

M = []
# populate an matrix
for i in range(n):
    row = []
    for j in range(n):
        a = math.floor(c + 1 - abs(i - c))
        b = math.floor(c + 1 - abs(j - c))
        row.append(min(a, b))
    M.append(row)

for i in range(n):
    print(*M[i])

