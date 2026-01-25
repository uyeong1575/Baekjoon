
import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a,b])

arr.sort(key=lambda x: (x[1] , x[0]))

ans = 1
index = 0

for i in range(1, len(arr)):
    if arr[i][0] >= arr[index][1]:
        ans += 1
        index = i

print(ans)