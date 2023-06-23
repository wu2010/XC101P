# Input an n * n matrix.
# If two different points A(x1, y1), B (x2, y2) satisfy
# x1 + x2 = n - 1, y1 + y2 = n - 1,
# the number at positions A and B are the same,
# then we say the pair (A, B) is called a symmetric pair.
# which means A(x1, y1) == B (?, ?)

# Find the number of symmetric pairs.

# input:
# 5
# 3 3 3 4 1
# 2 0 0 3 1
# 0 3 1 4 1
# 3 4 3 3 1
# 1 0 3 3 1

n = int(input())
M = []
for _ in range(n):
    M.append(list(map(int, input().split())))

sym_pairs = 0
# we want to create a boundary such that we will not double count
for x1 in range(n//2):
    for y1 in range(n):
        x2 = n - 1 - x1
        y2 = n - 1 - y1
        if M[x1][y1] == M[x2][y2]:
            sym_pairs += 1

# for odd size, handle the middle line in the center
if n % 2 == 1:
    x1 = x2 = n//2
    for y1 in range(n//2):  # avoid the center
        y2 = n - 1 - y1
        if M[x1][y1] == M[x2][y2]:
            sym_pairs += 1

print(sym_pairs)