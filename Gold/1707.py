import sys
from collections import deque
input = sys.stdin.readline

k = int(input().strip())

for _ in range(k):
    adj = {}

    v, e = map(int, input().strip().split())
    for i in range(e):
        a, b = map(int, input().strip().split())
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)

    dq = deque()
    color = [0] * (v+1)

    def BFS(start, level):
        dq.append((start, level))
        color[start] = 1

        while dq:
            (node, l) = dq.popleft()
            nxnode = adj.get(node, [])
            if l%2 == 0: #짝수
                for i in nxnode:
                    if color[i] == 1:               
                        return 'NO'
                    if color[i] == 0:
                        dq.append((i, l+1))
                        color[i] = -1
            else: # 홀수
                for i in nxnode:
                    if color[i] == -1:
                        return 'NO'
                    if color[i] == 0:
                        dq.append((i, l+1))
                        color[i] = 1
        dq.clear()

    for i in range(1, v+1):
        if color[i] == 0:
            a = BFS(i, 0)
            if a == 'NO':
                print('NO')
                break
    else:
        print('YES')
    
