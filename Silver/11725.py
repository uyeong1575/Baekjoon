#간선 (u,v)를 받아서 무방향 인접 리스트 만들고,
# BFS로 탐색하면서 부모노드 배열에 채우기

import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
adj = {}
for i in range(n-1):
    a, b = map(int, input().strip().split())
    adj.setdefault(a, []).append(b)
    adj.setdefault(b, []).append(a)

parent = [None] * (n+1)
visited = set()
dq = deque()
def BFS(start):
    dq.append(start)
    visited.add(start)

    while dq:
        node = dq.popleft()
        nxnode = adj.get(node, [])
        for i in nxnode:
            if i not in visited:
                dq.append(i)
                parent[i] = node
                visited.add(i)

BFS(1)
for i in range(2, len(parent)):
    print(parent[i])




