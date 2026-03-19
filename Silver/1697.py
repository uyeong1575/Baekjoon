import sys
from collections import deque

n, k = map(int, input().split())

MAX = 100001
visited = [False] * MAX
dq = deque()

visited[n] = True
dq.append((n, 0))
while dq:
    curr, count = dq.popleft()

    if curr == k:
        print(count)
        break

    for i in curr -1, curr + 1, curr * 2:
        if 0 <= i < MAX and not visited[i]:
            visited[i] = True
            dq.append((i, count + 1))