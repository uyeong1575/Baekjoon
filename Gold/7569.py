import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().strip().split())
arr = [[[] for _ in range(n)] for _ in range(h)]

for j in range(h):
    for i in range(n):
        arr[j][i] = list(map(int, input().strip().split()))

dm = [1,0,-1,0,0,0]
dn = [0,1,0,-1,0,0]
dh = [0,0,0,0,1,-1]
ncount = 0
dq = deque()

def BFS(n,m,h):
    global ncount
    day = -1
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 1: # 순회하면서 1 일괄 등록
                    dq.append((k, j, i, 0))
                elif arr[i][j][k] == 0:
                    ncount += 1

    while dq:
        (x, y, z, day) = dq.popleft()
        for i in range(6):
            nm = x + dm[i]
            nn = y + dn[i]
            nh = z + dh[i]
            if 0<=nm<m and 0<=nn<n and 0<=nh<h and arr[nh][nn][nm] == 0:
                arr[nh][nn][nm] = 1
                ncount -= 1
                dq.append((nm,nn,nh,day+1))        
    return day

a = BFS(n,m,h)
if ncount > 0:
    print(-1)
else:
    print(a)