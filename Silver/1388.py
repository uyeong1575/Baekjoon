import sys
from collections import deque

n, m = map(int, input().split())

arr = [[]for _ in range(n)]

for i in range(n):
    arr[i] = list(map(str, sys.stdin.readline().strip()))

flag = [[False for _ in range(m)] for _ in range(n)]
dq = deque()
count = 0

def BFS(y,x):
    global count

    if arr[y][x] == '-':
        dq.append((y,x))
        flag[y][x] = True


        while dq:
            (y,x) = dq.popleft()
            for dy, dx in [(0,1), (0,-1)]:
                ny,nx = y+dy, x+dx
                if 0<=nx<m and 0<=ny<n and flag[ny][nx] == False and arr[ny][nx] == '-':
                    dq.append((ny,nx))
                    flag[ny][nx] = True 
        count += 1

    elif arr[y][x] == '|':
        dq.append((y,x))
        flag[y][x] = True

        while dq:
            (y,x) = dq.popleft()
            for dy, dx in [(1,0), (-1,0)]:
                ny,nx = y+dy, x+dx
                if 0<=nx<m and 0<=ny<n and flag[ny][nx] == False and arr[ny][nx] == '|':
                    dq.append((ny,nx))
                    flag[ny][nx] = True 
        count += 1

for i in range(n):
    for j in range(m):
        if flag[i][j] == False:
            BFS(i,j)

print(count)
