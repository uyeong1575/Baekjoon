import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().strip().split())

arr = [[] for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int, input().strip().split()))

s, a, b = map(int, input().strip().split())

dlist = []
dq = deque()
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            dlist.append((arr[i][j], i, j, 0))
dlist.sort()
dq = deque(dlist)

while dq:
    (value, y, x, time) = dq.popleft()
    if time == s:
        break

    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        ny, nx = y+dy, x+dx
        if 0<=nx<n and 0<=ny<n and arr[ny][nx] == 0:
            dq.append((value, ny, nx, time+1))
            arr[ny][nx] = value

print(arr[a-1][b-1])
