# 크루스칼 알고리즘 MST 구현

import sys
sys.setrecursionlimit(10**4)

V, E = map(int, sys.stdin.readline().strip().split())

adj = []
for line in sys.stdin:
    u, v, w = map(int, line.strip().split())
    adj.append([u,v,w])
    adj.append([v,u,w])

class unionfind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, u): # union된 루트 노드 찾기
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u

def Kru(graph, num_Vertex):
    # 간선을 가중치로 정렬
    # 간선을 하나씩 순회하면서 조건에 부합하면 union하고 가중치 +=
    # 조건은 find가 같지 않아야 한다.(사이클 확인)
    mst_weight = 0
    uf = unionfind(num_Vertex)
    graph.sort(key=lambda x:x[2])

    for u, v, weight in graph:
        if uf.find(u) != uf.find(v):
            uf.union(u,v)
            mst_weight += weight

    return mst_weight

print(Kru(adj, V+1))
    

