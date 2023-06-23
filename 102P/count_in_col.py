n, m = map(int, input().split())

colsum = [0 for _ in range(m)]
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        colsum[j] += row[j]

print(*colsum)

# input
# 3 5
# 0 0 1 1 0
# 0 1 1 0 1
# 1 0 0 1 0

# 5 8
# 1 1 1 0 0 1 0 1
# 0 0 1 1 1 0 1 1
# 1 0 0 1 1 0 1 0
# 0 0 0 0 1 1 1 1
# 0 0 1 1 1 1 1 0