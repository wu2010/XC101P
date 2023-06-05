
# Given an n*m matrix, output its absolute matrix. An absolute matrix is defined as
# a matrix in which each element is the absolute value of the original element
# in the input matrix.
#
# Input:
# The first row contains two integers n, m representing the dimensions of the input matrix.

n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        matrix[i][j] = abs(matrix[i][j])

for i in matrix:
    print(*i)


# Lists : – Accessing element in a list takes linear time because all the element in the lists
# are linked with each other for accessing ith element we have to traverse all the previous
# elements in a list.
# However, insertion and deletion in a list takes constant(which is not expensive at all) time
# as all the element are linked with each other for adding or removing new element

n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

transpose = []
# set the initial list for each row in the new transpose
for entry in matrix[0]:
    transpose.append([entry])  # a new list

# iterate over columns (matrix[_][j]) in the matrix
# append the value into rows (transpose[j])
for i in range(1, n):
    for j in range(m):
        transpose[j].append(matrix[i][j])

for j in transpose:
    print(*j)

