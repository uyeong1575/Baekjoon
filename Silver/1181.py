import sys


n = int(sys.stdin.readline())
arr = [[] for _ in range(51)]

for _ in range(n):

    s = input()
    l = len(s)
    if s not in arr[l]:
        arr[l].append(s)

for i in range(1, 51):
    arr[i].sort()

for i in range(51):
    for j in range(len(arr[i])):
        print(arr[i][j])
