import sys

input  = sys.stdin.readline

arr = list(map(int, input().split()))

x = arr[1]
y = arr[2]

count = 0

while x != y:
    x = (x + 1) // 2
    y = (y + 1) // 2
    count += 1

print(count)