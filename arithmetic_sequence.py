# mingming loves candies very much. It is known that he eats one candy on the first day,
# two candies on the second day, three candies on the third day, four candies on
# the fourth day, and so on.
# If the candies he ate accumulated to one thousand, his mouth will be full of cavities,
# which day will he have a mouth full of cavities?

day = 0
sum = 0

while sum < 1000:
    day += 1
    sum += day
# now sum >= 1000
print(day)
