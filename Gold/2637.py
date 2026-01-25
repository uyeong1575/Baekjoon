import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

adj = {}
intable = [0] * (n+1)
outtable = [0] * (n+1)
ctable = [0] * (n+1)
dq = deque()

for i in range(m):
    u, v, w = map(int, input().strip().split())
    adj.setdefault(u, []).append((v,w))
    intable[v] += 1
    outtable[u] += 1

dq.append((n, 1))

while dq:
    (node, we) = dq.popleft()
    nxnode = adj.get(node,[])
    for a, b in nxnode:
        ctable[a] += we*b
        # nw = ctable[a]
        intable[a] -= 1
        if intable[a] == 0:
            dq.append((a,ctable[a]))

for i in range(1, n+1):
    if outtable[i] == 0:
        print(i, ctable[i])



