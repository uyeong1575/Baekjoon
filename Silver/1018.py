import sys
input = sys.stdin.readline

def check(n, m):
    countb = 0
    countw = 0
    for i in range(n, n+8):
        for j in range(m, m+8):
            if (i + j) % 2 == 0: # 짝수면
                if arr[i][j] != 'B': countb += 1
                if arr[i][j] != 'W': countw += 1
            else:
                if arr[i][j] != 'W': countb += 1
                if arr[i][j] != 'B': countw += 1
    
    return min(countb, countw)

N, M = map(int, input().split())
arr = []
for i in range(N):
    a = list(map(str, input().strip()))
    arr.append(a)

min_count = float('inf')

for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        count = check(i, j)
        if count < min_count:
            min_count = count

print(min_count)
            
        
