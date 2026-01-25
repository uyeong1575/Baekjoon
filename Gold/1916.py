import sys
import heapq

input = sys.stdin.readline
n = int(input().strip())
m = int(input().strip())
adj ={}
for _ in range(m):
    u, v, w = map(int, input().strip().split())
    adj.setdefault(u, []).append((v,w))

a, b = map(int, input().strip().split())
INF = int(1e9)
dis = [INF] * (n+1)

def dijk(start):
    q=[]
    heapq.heappush(q, (0,start))
    dis[start] = 0

    while q:
        (dist, node) = heapq.heappop(q)
        if dis[node] < dist:
            continue
        for target, cost in adj.get(node, []):
            ndist = dist + cost
            if dis[target] > ndist:
                dis[target] = ndist
                heapq.heappush(q, (ndist, target))

dijk(a)
print(dis[b])


