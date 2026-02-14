import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = set()
dx = [0, 0, -1, 1, -1, 1, 1, -1]
dy = [1, -1, 0, 0, 1, 1, -1, -1]

# 순회하면서 같은 크기는 묶어서 확인
# 8방에 하나라도 높은거 있으면 봉우리 X
# 순회한 곳은 visited 넣기
def BFS(x, y):
    dq = deque()
    dq.append((x, y))
    visited.add((x, y))
    cur_h = arr[y][x]
    is_peak = True

    while dq:
        x, y = dq.popleft()

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if arr[ny][nx] > cur_h:
                    is_peak = False
                if (nx, ny) not in visited and arr[ny][nx] == cur_h:
                    visited.add((nx, ny))
                    dq.append((nx, ny))
    return is_peak

count = 0

for i in range(N):
    for j in range(M):
        if (j, i) not in visited and BFS(j, i):
            count += 1

print(count)
