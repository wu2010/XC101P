fahrenheit = float(input())

celsius = 5 / 9 * (fahrenheit - 32)

# round to three digits after the decimal point.
print(round(celsius, 3))
# display 3 digits after the decimal point.
print('%.3f' % round(celsius, 3))

# e.g. input 41 will get
# 5.0
# 5.000