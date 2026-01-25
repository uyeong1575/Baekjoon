# 성공
import sys
from collections import deque

n = int(input())

arr = [[] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int,sys.stdin.readline().strip()))

flag = [[False for _ in range(n)] for _ in range(n)]

dq= deque()
dy = [0, -1, 0 ,1]
dx = [1, 0, -1, 0]
ans = []

def BFS(i, j):
    dq.append((i,j))
    flag[i][j] = True
    count = 1

    while dq:
        (y,x) = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=nx<n and 0<=ny<n and flag[ny][nx] == False and arr[ny][nx] == 1:
                flag[ny][nx] = True
                dq.append((ny,nx))
                count += 1
    ans.append(count)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and flag[i][j] == False:
            BFS(i,j)

ans.sort()
l = len(ans)
print(l)
for i in range(l):
    print(ans[i])
