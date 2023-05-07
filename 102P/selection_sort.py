# selection sort: from left to right, build the sorted section as
# the sorted section | the unsorted section

# Pick the smallest number from the unsorted part, then
#   put it to the beginning of the unsorted part, i.e. append to the end of the sorted part
# Repeat this process until the entire sequence is sorted

n = int(input())
numbers = list(map(int, input().split()))

# from left to right
for i in range(n - 1):
    # pick the smallest number in indexes [i, n-1]
    # temporarily assume index i has the smallest value
    position = i
    # look for even smaller value in [i+1, n-1]. keep the position only
    for j in range(i + 1, n):
        if numbers[j] < numbers[position]:
            position = j
    # exchange position to i
    numbers[i], numbers[position] = numbers[position], numbers[i]

print(*numbers)
