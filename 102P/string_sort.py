# insertion_sort
# sort_characters

# input
# 3
# abd
# abc
# bcd

# return True if s < t as string
def compare_string_smaller(s, t):
    len_s = len(s)
    len_t = len(t)
    # pairwise comparison until min(len_s, len_t)
    for i in range(min(len_s, len_t)):
        if s[i] < t[i]:
            return True
        elif s[i] > t[i]:
            return False
        # otherwise, continue
    # so far, s and t are identical until min(len_s, len_t)
    # shorter one is smaller
    return len_s < len_t


n = int(input())
alist = [input()]

# a list of size 1 (i.e. index 0) is already sorted. say it is minimum.
for j in range(1, n):
    alist.append(input())

    # j is the first number from unsorted section on the right
    # look at the item on the left (in the sorted section)
    i = j - 1
    # continue to shift the new value to the left position if it is smaller
    while i >= 0 and compare_string_smaller(alist[i + 1], alist[i]):
        alist[i], alist[i + 1] = alist[i + 1], alist[i]
        i -= 1
    # out of the loop: it means alist[i] < alist[i + 1], which is correct order

for j in range(n):
    print(alist[j])
