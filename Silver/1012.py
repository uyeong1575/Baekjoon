import sys
from collections import deque
input = sys.stdin.readline

dq = deque()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS(x, y, M, N, graph):
    dq.append((x,y))
    graph[y][x] = 0

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                dq.append((nx, ny))

def solve():
    M, N, K = map(int, input().split()) # 가로길이, 세로길이, 배추 갯수
    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                BFS(j, i, M, N, graph)
                count += 1

    print(count)


T = int(input())
for _ in range(T):
    solve()