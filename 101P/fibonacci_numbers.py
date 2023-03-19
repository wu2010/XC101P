# print the sequence up to the first n items

N = int(input())
x1 = x2 = 1

for i in range(1, N + 1):
    # no change to 1st, 2nd terms
    if i >= 3:
        # start the recursion since 3rd term
        x1, x2 = x2, x1 + x2

    # always print the latest term
    print(x2, end=' ')
