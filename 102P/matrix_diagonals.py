# Read in an n*n matrix
# Print out two diagonals of the matrix
# - upper left to lower right diagonal.
# - bottom left diagonal to the top right diagonal.

# Sample Input:
# 3
# 1 2 3
# 4 5 6
# 7 8 9

# Sample Output:
# 1 5 9
# 7 5 3

n = int(input())
M = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    print(M[i][i], end=' ')

print()

for i in range(n):
    print(M[n - 1 - i][i], end=' ')


# Enter a number m and output an (m*2 + 1) * (m*2 + 1) matrix
# composed of o and x to make an X diagram
m = int(input())
n = 2 * m + 1

for i in range(n):
    row = ["o" for r in range(n)]
    row[i] = "x"
    j = n - 1 - i
    row[j] = "x"
    for item in row:
        print(item, end="")
    print()
