class unionfind():
    def __init__(self,size):
        self.parent = list(range(size))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        rootu = self.find(u)
        rootv = self.find(v)
        if rootu != rootv:
            self.parent[rootv] = rootu

import sys

N, M = map(int, sys.stdin.readline().strip().split())
uf = unionfind(N+1)
uvlist = []

for _ in range(M):
    a ,b = map(int, sys.stdin.readline().strip().split())
    uvlist.append((a,b))

for i in range(len(uvlist)):
    uf.union(uvlist[i][0], uvlist[i][1])

for i in range(len(uvlist)):
    uf.union(uvlist[i][0], uvlist[i][1])

ans = set()
for i in range(1, len(uf.parent)):
    ans.add(uf.parent[i])

print(len(ans))



