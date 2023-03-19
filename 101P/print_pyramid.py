# input: 4
#    *
#   * *
#  * * *
# * * * *

n = int(input())

alist = []
spaces = n
for i in range(n):
    alist.append('*')
    spaces -= 1
    print(' ' * spaces, end='')
    print(*alist)
