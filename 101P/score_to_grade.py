# score in [0, 100]
score = int(input())

tens = score // 10
# not exactly tens as 100 -> 10

if tens >= 9:
    print('A')
elif tens == 8:
    print('B')
elif tens == 7:
    print('C')
elif tens == 6:
    print('D')
else:  # tens < 6
    print('E')
