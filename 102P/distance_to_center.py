# input a 5*5 matrix, in this matrix only one cell is 1, all the other cells are 0.
# We call a matrix  "beautiful" if the center of the matrix (the position is row 3,column 3)
# is 1 while the others are 0.
# Every time you can exchange two numbers with the two adjacent positions.

# now consider it is n*n matrix where n is odd
# Please calculate how many steps are required to make a matrix "beautiful".

n = 5
center = n // 2

matrix = []
for _ in range(5):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            # compute the distance
            print(abs(i - center) + abs(j - center))
            break
