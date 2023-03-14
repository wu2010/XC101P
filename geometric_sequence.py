# Xiaoyu is swimming, but sadly she finds that she is getting tired quickly.
# Xiaoyu swam 2 meters in the first stroke, and
# with each stroke, she could only swim 98% of the distance as the previous stroke.
# Xiaoyu wants to know how many strokes are needed if she wants to swim x meters.

x = float(input())

# in the first stroke
n = 1
# swam 2 meters
s = 2
d = s

# continue to swim if not yet reach x
while d < x:
    # with each stroke
    n = n + 1
    # swim 98% of the distance as the previous
    s = s * 0.98
    # the total distance
    d = d + s

print(n)
