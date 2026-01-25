# BFS와 DFS

import sys
sys.setrecursionlimit(10**4)
from collections import deque

n, e, n1 = map(int, sys.stdin.readline().strip().split())
adj = {}
for line in sys.stdin:
    u, v = map(int, line.strip().split())
    adj.setdefault(u, []).append(v)
    adj.setdefault(v, []).append(u)

for key in adj:
    adj[key].sort()


DFS_sq = []
dvisited = set()

def DFS(start):
    # 시작 노드부터 들어가서 인접 노드로 재귀적으로 들어감
    DFS_sq.append(start)
    dvisited.add(start)

    for nx_node in adj.get(start, []):
        if nx_node not in dvisited:
            DFS(nx_node)
    return

DFS(n1)
print(*DFS_sq)


BFS_sq = []
dq = deque()
bvisited = set()

def BFS(start):
    dq.append(start)
    bvisited.add(start)
    while dq:
        node = dq.popleft()
        BFS_sq.append(node)
        for i in adj.get(node, []):
            if i not in bvisited:
                bvisited.add(i)
                dq.append(i)
    return

BFS(n1)
print(*BFS_sq)