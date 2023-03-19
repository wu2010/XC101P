# First they tried to form 4 rows but 3 soldiers are left out;
# then they tried to line up in 5 rows and 4 soldiers were left out.
# Finally, they formed x rows without any extra.
# What is the minimum number of these soldiers?

x = int(input())
# The minimum of 20*k + 19 is 19.
y = 19
while y % x != 0:
    y += 20
# Here (20*k + 19) % x == 0
print(y)