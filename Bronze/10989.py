import sys

arr = [0] * 10001
t = int(sys.stdin.readline())


for i in range(t):
    num = int(sys.stdin.readline())
    arr[num] += 1


for i in range(1, 10001):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)


