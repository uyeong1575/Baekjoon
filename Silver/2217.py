import sys
input = sys.stdin.readline

n = int(input())
arr = []
ans = []
for i in range(n):
    arr.append(int(input()))
arr.sort()

for i in range(1,n+1):
    ans.append(arr[-i]*i)
print(max(ans))