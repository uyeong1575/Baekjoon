import sys

n = int(input())
a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))

a.sort()
# print(a)
for i in range(n):
    print(a[i])