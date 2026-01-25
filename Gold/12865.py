import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 물품의수, 최대 무게
th = [] # 무게, 가치 list

for i in range(n):
    w, v = map(int, input().split())
    th.append((w,v))
th.sort()

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1): # i = 물건 index
    for j in range(1, k+1): # j = 무게
        if j >= th[i-1][0]: # 지금 넣으려는 물건의 무게가 가능할때
            dp[i][j] = max(dp[i-1][j], th[i-1][1]+dp[i-1][j-th[i-1][0]])
        else:
            dp[i][j] = dp[i-1][j]

for row in dp:
    print(row)

maxvalue = max(max(row) for row in dp)
print(maxvalue)