import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

adj = [[] for _ in range(N + 1)]


def BFS(start, end, adj):
    dq = deque()
    dq.append((start, 0))
    visited = set()
    visited.add(start)

    while dq:
        cur_node, cur_dist = dq.popleft()

        if cur_node == end:
            return cur_dist
        
        for node, weight in adj[cur_node]:
            if node not in visited:
                visited.add(node)
                dq.append((node, cur_dist+weight))
    return 0

# adj 만들기
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

# 최종 출력 생성
for _ in range(M):
    n1, n2 = map(int, input().split())
    print(BFS(n1, n2, adj))
