# a matrix of N * M size.
# we want to know the sum of values in each row of the matrix, and
# hopes to find the row number where the maximum sum is located.

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# row 0
max_value = sum(matrix[0])
max_pos = 0
print(max_value)

# row 1 and beyond
for i in range(1, n):
    Sum = sum(matrix[i])
    print(Sum)
    if max_value < Sum:
        max_value = Sum
        max_pos = i

print(max_pos + 1)

# input
# 4 5
# -1 0 1 2 3
# 1 2 3 4 5
# 5 4 3 2 1
# 0 0 2 3 -2

# output：
# 5
# 15
# 15
# 3
# 2
