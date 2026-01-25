import sys

n = int(input())
c = list(map(int, sys.stdin.readline().strip().split()))
c.sort()
m = int(input())
a = list(map(int, sys.stdin.readline().strip().split()))

def bifind(target, start, end):
    while start <= end:
        mid = (start+end)//2

        if target > c[mid]:
            start = mid + 1  
        elif target < c[mid]: 
            end = mid - 1
        else:
            return 1
    return 0

ans = []
for i in range(m):
    ans.append(bifind(a[i], 0, len(c)-1))

print(*ans)