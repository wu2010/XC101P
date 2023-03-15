# It will take some time to find an available bicycle, unlock, park, lock the car, etc.
# Suppose it takes 27 seconds to find a bicycle and unlock it,
# and parking and locking take another 23 seconds,
# while the speed of walking is 1.2 yards per second and
# the speed of cycling is 3.0 yards per second.
# Write a program to compute whether cycling is faster or walking is faster at different distances.

distance = int(input())

# difference in time
dt = distance / 3 + (27 + 23) - distance / 1.2

if dt < 0:
    print("Bike")
elif dt == 0:
    print("All")
else:
    print("Walk")