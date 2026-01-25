import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

dph = [1]*n
dpl = [1]*n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dph[i] = max(dph[j]+1, dph[i])

for i in range(n-1,-1,-1):
    for j in range(n-1,i-1,-1):
        if a[i] > a[j]:
            dpl[i] = max(dpl[j]+1, dpl[i])

ans = 0
for i in range(n):
    if ans < (dph[i] + dpl[i]):
        ans = (dph[i] + dpl[i])

print(ans-1)