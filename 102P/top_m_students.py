# students are ranked by average test score,
# if the average score is the same, then the variance is calculated and
#   the students with smaller variance are ranked first.
# If the variance is also the same, they are arranged according to the order of the test number (smaller first).

# The average and variance of the fractional part are ignored (that is, round down to the nearest whole number)


# The first three numbers n (n <= 1000), m (m <= 60), k (k <= 10),
# where n represents the number of students,
# m represents the number of students who can obtain a scholarship,
# k represents the number of subjects tested in the mid-term exam.
# The next n rows, each row k numbers, the i-th row, the j-th column shows
#   the score x on jth subject of student with test number i (x<=100)
# 5 3 3
# 99 92 71
# 98 98 98
# 80 93 72
# 98 98 98
# 97 98 99


n, m, k = map(int, input().split())
students = list()

# test number = num + 1
for num in range(n):
    numbers = list(map(int, input().split()))
    # get average
    avg = sum(numbers) // k  # round down

    # get variance
    variance = 0
    for number in numbers:
        variance += number ** 2
    variance = (variance - k * avg ** 2) // k  # round down

    # tuple (average, variance, test num)
    students.append((avg, variance, num + 1))

    # try insertion
    for j in range(len(students) - 1, 0, -1):
        i = j - 1  # j >= 1
        # stop when it is in the correct position
        if students[i][0] > students[j][0] or \
                students[j][0] == students[i][0] and students[i][1] <= students[j][1]:
            break
        students[j], students[i] = students[i], students[j]

    # keep the size m
    if len(students) > m:
        students.pop()

for student in students:
    print(student[2], end=' ')
