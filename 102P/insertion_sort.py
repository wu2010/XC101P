# insertion sort: from left to right, build the sorted section as
# the sorted section | the unsorted section

# from left to right, consider the first item is sorted.
# At each step, take the first number from unsorted section and insert into the sorted section.
# Repeat until all the numbers in sequence are sorted.

# input
# 5
# 1 4 2 3 5

n = int(input())
alist = list(map(int, input().split()))

# a list of size 1 (i.e. index 0) is already sorted. say it is minimum.
for j in range(1, n):
    # j is the first number from unsorted section on the right
    # look at the item on the left (in the sorted section)
    i = j - 1
    # continue to shift the new value to the left position if it is smaller
    while i >= 0 and alist[i + 1] < alist[i]:
        alist[i], alist[i + 1] = alist[i + 1], alist[i]
        i -= 1
    # out of the loop: it means alist[i] < alist[i + 1], which is correct order

print(*alist)
