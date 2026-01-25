import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().strip().split())

adj = {}
intable = [0] * (n+1)
for i in range(m):
    a, b = map(int, input().strip().split())
    intable[b] += 1
    adj.setdefault(a, []).append(b)

ans = []
dq = deque()
def gkatn():

    for i in range(1, len(intable)):
        if intable[i] == 0:
            dq.append(i)
    
    while dq:
        node = dq.popleft()
        ans.append(node)
        nxnode = adj.get(node, [])
        for j in nxnode:
            intable[j] -= 1
            if intable[j] == 0:
                dq.append(j)
    
gkatn()
print(*ans)