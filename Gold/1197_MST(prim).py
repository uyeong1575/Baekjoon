# 프림 알고리즘으로 MST 구하기
import sys
import heapq

V, E = map(int, sys.stdin.readline().strip().split())

adj = {}

for line in sys.stdin:           # 더 이상 읽을 줄이 없으면 종료
    u, v, w = map(int, line.strip().split())
    adj.setdefault(u,[]).append((w,v))
    adj.setdefault(v,[]).append((w,u))

def MST(start:int):
    # 시작 노드를 넣고 팝한 후 리턴 값을 받는다
    # 받은 리턴값을 확인 후 visited가 아니면 visited에 추가하고
    # 인접 노드를 for문으로 확인한다.
    mst_weight = 0
    mst = []
    visited = [False] * (V+1)
    heapq.heappush(mst, (0,start))

    while mst:
        weight, v = heapq.heappop(mst)
        if visited[v]:
            continue

        visited[v] = True
        mst_weight += weight
        for a,b in adj.get(v,[]):
            if not visited[b]:
                heapq.heappush(mst, (a,b))
    return mst_weight

print(MST(1))

