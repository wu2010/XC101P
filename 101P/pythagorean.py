sides = list(map(int, input().split()))

if len(sides) != 3:
    print('not a triangle')

sides.sort()

hypotenuse = sides[-1]  # the longest side
a = sides[0]
b = sides[1]

if a + b <= hypotenuse:
    print('not a triangle')
else:  # a + b > hypotenuse
    test = a ** 2 + b ** 2 - hypotenuse ** 2

    if test == 0:
        print('right triangle')
    elif test > 0:
        print('acute triangle')
    else:
        print('obtuse triangle')
