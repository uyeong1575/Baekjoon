import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())

arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

dq = deque()
visited = set()

def BFS(x,y,dist):
    dq.append((x,y,dist))
    visited.add((x,y))

    while dq:
        x,y,d = dq.popleft()

        if x == m-1 and y == n-1:
            return d

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n and arr[ny][nx] == 1 and (nx,ny) not in visited:
                visited.add((nx,ny))
                dq.append((nx,ny,d+1))

print(BFS(0,0,1))

