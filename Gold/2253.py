import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trap = set()
for i in range(m):
    trap.add(int(input()))

maxjump = int((2*n)**0.5)
INF = int(10**4)
dp = [[INF for _ in range(n+1)] for _ in range(maxjump+2)]
# dp[v][n] 은 v의 속도로 n번쨰 돌로 도착한 경우의 점프 횟수
if 2 not in trap:
    dp[1][2] = 1

for j in range(2, n+1): # j번쨰 돌에
    for i in range(1, maxjump+1): # i의 속도로 위치한 경우는
        if j in trap or j-i <= 1:
            continue
        dp[i][j] = min(dp[i][j-i], dp[i+1][j-i], dp[i-1][j-i]) + 1

ans = []
for i in range(maxjump+1):
    ans.append(dp[i][n])

if min(ans) >= 10**4:
    print(-1)
else:
    print(min(ans))
        
