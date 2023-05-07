n = int(input())
numbers = list(map(int, input().split()))

numbers.sort()

if n % 2 == 0:
    d1 = numbers[n / 2 - 1]
    d2 = numbers[n / 2]
    # the average of two
    median = (d1 + d2) / 2
else:
    index = (n - 1) // 2
    median = numbers[index]

print(median)