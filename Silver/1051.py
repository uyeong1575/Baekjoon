import sys
input = sys.stdin.readline

N, M = map(int, input().split())
max_len = min(N, M)
grid = [list(map(int, input().strip())) for _ in range(N)]

ans = 1
for y in range(N):
    for x in range(M):

        for i in range(1, max_len):
            if y + i < N and x + i < M:
                if grid[y][x] == grid[y+i][x] == grid[y][x+i] == grid[y+i][x+i]:
                    ans = max(ans, i + 1)

print(ans * ans)



