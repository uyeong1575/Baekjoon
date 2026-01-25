import sys
sys.setrecursionlimit(10**5)

n, k = map(int, sys.stdin.readline().split())
arr = [None for _ in range(n)]

for i in range(n):
    arr[i] = int(sys.stdin.readline())
arr.append(0)
ans = 0 # 몫 기록

def div(value):
    global ans
    if value == 0:
        return -1
    
    for i in range(n+1):
        if arr[i] > value or i==n:
            ans += value//arr[i-1]
            break
    return div(value%arr[i-1])

div(k)
print(ans)
