import sys
input = sys.stdin.readline

t = int(input())

case = []
max = 0
for i in range(t):
    n, m = map(int, input().split())
    case.append([n,m])
    if max < m:
        max = m

dp = [i for i in range(max+1)]

for i in range(3, max+1):
    dp[i] = dp[i] * dp [i-1]

for i in range(t):
    a = case[i][0]
    b = case[i][1]
    if a == b:
        print(1)
    else:
        print(dp[b]//dp[a]//dp[b-a])

