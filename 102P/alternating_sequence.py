
# Assuming there are n integers, to make an alternating sequence,
# the 1st number of the sequence is the largest in all the numbers, and
# the 2nd number is the smallest, and
# the 3rd number is the second largest, and
# the 4th number is the second smallest, and so on.
# Each number can be taken only once. Do this until all numbers have been used exactly once.

n = int(input())
numbers = list()
for num in range(n):
    numbers.append(int(input()))

sign = 1  # positive is max; negative is min
# Selection Sort
for i in range(n - 1):
    index = i
    for j in range(i + 1, n):
        if sign * (numbers[j] - numbers[index]) > 0:
            index = j
    numbers[i], numbers[index] = numbers[index], numbers[i]
    sign *= -1  # switch min and max

for num in numbers:
    print(num)


# input:
#
# 5
# 10
# -1
# 3
# 3
# -9

# output:
# 10
# -9
# 3
# -1
# 3
