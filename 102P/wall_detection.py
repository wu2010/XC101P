# Given a n*m area, where some places have a wall.
# If you put a bomb at position (i,j), then
# the wall in i-th row and j-th column would all be destroyed.
# Now you want to know whether all the walls can be destroyed using only one bomb.

# Input
# The first line is an integer T representing the number of groups of testing data.
# For each group of testing data, the first line enters two numbers n, m representing an n*m area.
# The next n lines, each line contains m characters of '*' representing the wall and '.' representing space.
# 1<=n,m<=1000

# 2
# 3 4
# .*..
# ....
# .*..
# 3 3
# ..*
# .*.
# *..


# Output
# In the first line, there's way to destroy all walls by only one bomb, output "YES", otherwise output "NO".
# If the answer is "YES", please output the position of bomb x,y in the second line separated by space.
#
# Notice:If you have several ways to solve the problem, output the one who has the smallest row number,
# then, if there are still several ways, output the one which has the smallest column number.

# YES
# 1 2
# NO

groups = int(input())

for g in range(groups):
    n, m = map(int, input().split())

    matrix = []
    star_count_in_row = [0 for _ in range(n)]
    star_count_in_col = [0 for _ in range(m)]
    for i in range(n):
        row = input()
        digits = [(1 if item == '*' else 0) for item in row]
        matrix.append(digits)
        # start the counting for row/col
        star_count_in_row[i] = sum(digits)
        if star_count_in_row[i] > 0:
            for j in range(m):
                star_count_in_col[j] += digits[j]

    # the number of row/col count > 1 cannot be more than 1
    density_in_row = [(1 if i > 1 else 0) for i in star_count_in_row]
    density_in_col = [(1 if j > 1 else 0) for j in star_count_in_col]
    if sum(density_in_row) > 1 or sum(density_in_col) > 1:
        print('NO')

    # now at most 1 row/col count > 1
    elif sum(density_in_row) == 1:
        a = -1
        threshold = 2
        for i in range(n):
            if star_count_in_row[i] >= threshold:
                a = i
                break

        b = -1
        flag = True
        # re-count after removing row a
        for j in range(m):
            star_count_in_col[j] -= matrix[a][j]
            # check whether all in the same col
            if star_count_in_col[j] > 0:
                if b < 0:  # first time
                    b = j
                else:  # second time
                    flag = False
                    break
        if flag:
            print('YES')
            b = max(b, 0)  # in case nothing left after removing row a
            print(f'{a + 1} {b + 1}')
        else:
            print('NO')

    elif sum(density_in_col) == 1:
        b = -1
        threshold = 2
        for j in range(m):
            if star_count_in_col[j] >= threshold:
                b = j
                break

        a = -1
        flag = True
        # re-count after removing col b
        for i in range(n):
            star_count_in_row[i] -= matrix[i][b]
            # check whether all in the same row
            if star_count_in_row[i] > 0:
                if a < 0:  # first time
                    a = i
                else:  # second time
                    flag = False
                    break
        if flag:
            print('YES')
            a = max(a, 0)  # in case nothing left after removing col b
            print(f'{a + 1} {b + 1}')
        else:
            print('NO')

    else:
        # at most 1 per col or row
        if sum(star_count_in_row) > 2:
            print('NO')
            continue

        a = -1
        b = -1

        threshold = 1
        for i in range(n):
            if star_count_in_row[i] >= threshold:
                a = i
                break

        threshold = 1
        for j in range(m):
            if star_count_in_col[j] >= threshold:
                b = j
                break

        print('YES')
        print(f'{a+1} {b+1}')

