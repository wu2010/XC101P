# Input
# 5
# 100 -100 50 0 -50

n = int(input())
alist = list(map(int, input().split()))

# start two positions with max and min
# assume max, min. if not, swap
if alist[0] < alist[1]:
    alist[1], alist[0] = alist[0], alist[1]
max_pos = 0
min_pos = 1

# look for bigger max and smaller min at the same time
for i in range(2, n):
    if alist[max_pos] < alist[i]:
        max_pos = i
    if alist[min_pos] > alist[i]:
        min_pos = i

# swap to two ends.
# note: the greatest and smallest have different indexes
alist[0], alist[max_pos] = alist[max_pos], alist[0]
alist[n - 1], alist[min_pos] = alist[min_pos], alist[n - 1]

print(*alist)
