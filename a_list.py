# input: 3
# 11 23 45

n = int(input())
alist = list(map(int, input().split()))

for item in alist:
    print(item, end=" ")
print()

print(*alist)

alist.reverse()
print(*alist)