# bubble sort: from right to left, build the sorted section as
# the sorted section | the unsorted section
# OR
# from left to right, build the sorted section as
# the unsorted section | the sorted section

# Compare two adjacent numbers: if the order is incorrect, then swap them
# Repeat until all the number in sequence is in order

# input:
# 4
# 4 3 2 1

n = int(input())
numbers = list(map(int, input().split()))

swaps = 0

# the size of the sorted section on the right. start with 0
for i in range(n - 1):
    # from left to right
    for j in range(n - 1 - i):
        # when the order is incorrect
        if numbers[j] > numbers[j + 1]:
            # such swap is the minimum number of swaps needed to sort a list
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swaps += 1

print(*numbers)
print(swaps)