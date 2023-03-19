# the sum of inverses of alternating sum of odd numbers
# e.g. 1+1/(1−3)+1/(1−3+5)+......+1/(1−3+5−...+2n−1).
# which is alternating sum of inverses of natural numbers
# = 1 - 1/2 + 1/3 - 1/4

n = int(input())

sum = 0
# i is for the index of terms
for i in range(1, n + 1):
    # j is each term in the sequence on the denominator
    sign = 1
    subsum = 0
    for j in range(1, 2 * i, 2):
        subsum += sign * j
        sign *= -1
    sum += 1.0 / subsum

print('%.3f' % sum)
