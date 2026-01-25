import sys
from collections import deque

n, m, k, x = map(int, input().split())
dq = deque()
visited = set()
ans = []

adj = {}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    adj.setdefault(a, []).append(b)

def BFS(start, dist):
    dq.append((start, dist))
    visited.add(start)

    while dq:
        node, d = dq.popleft()
        if d == k:
            ans.append(node)

        nxnode = adj.get(node, [])
        for i in nxnode:
            if i not in visited:
                visited.add(i)
                dq.append((i, d+1))

BFS(x,0)
ans.sort()
if not ans:
    print(-1)
else:
    for i in range(len(ans)):
        print(ans[i])