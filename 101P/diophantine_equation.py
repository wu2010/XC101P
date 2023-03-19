# Each attack by Sunwukong can make a damage,
# and each attack by you can make b damage.
# And the White Bone Demon has c health.
# The White Bone Demon knows black magic, so it can only be killed when the life value is exactly zero.
# calculate if it's possible to kill the White Bone Demon or not.

a, b, c = map(int, input().split())

found = False
# determine the range for x
for x in range(c // a + 1):
    # test if we have an answer
    if (c - a * x) % b == 0:
        found = True
        break

print("Yes" if found else "No")
