import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())

color = list(map(int, input().strip()))

adj ={}
for line in sys.stdin:
    a, b = map(int, line.strip().split())
    adj.setdefault(a, []).append(b)
    adj.setdefault(b, []).append(a)

count = 0
dq = deque()
visited = set()

for i in range(1, n+1): # 시작점 돌아가며 BFS
    if color[i-1] == 1:
        dq.append(i)
        visited.add(i)

        while dq:
            node = dq.popleft()
            if node != i and color[node-1] == 1:
                count += 1
                continue
            nxnode = adj.get(node, [])
            for j in nxnode:
                if j not in visited:
                    visited.add(j)
                    dq.append(j)
        dq.clear()
        visited.clear()

print(count)



