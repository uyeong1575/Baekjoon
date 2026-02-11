import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

N = int(input())
arr= list(map(int, input().split()))
delete_num = int(input())

adj = defaultdict(list)

for index, value in enumerate(arr):
    if value != -1:
        adj[value].append(index)
    else:
        root = index

def BFS_count(num):

    if num == delete_num:
        return 0

    dq = deque()
    dq.append(num)
    count = 0

    while dq:
        cur = dq.popleft()

        # adj에 있으면 자식 다시 큐에 넣기, delete_num이면 생략
        is_leaf = True # 자식이 있는데, delete여서 leaf일 수 있음
        if cur in adj:
            for child in adj[cur]:
                if child == delete_num:
                    continue
                dq.append(child)
                is_leaf = False # 하나라도 append 하면 leaf 아님

        if is_leaf:
            count += 1

    return count

print(BFS_count(root))


