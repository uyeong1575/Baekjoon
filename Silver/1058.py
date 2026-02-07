# A가 x와 친구일때, x와 친구인 모든 사람은 a와 친구다

# import sys
# input = sys.stdin.readline

# N = int(input())

# arr = [list(input().strip()) for _ in range(N)]
# max_count = 0

# for i in range(N):
#     tmp = set()
#     for index, value in enumerate(arr[i]):
#         if value == 'Y':
#             tmp.add(index)
#             for index2, value2 in enumerate(arr[index]):
#                 if value2 == 'Y':
#                     tmp.add(index2)
#     tmp.discard(i)

#     c = len(tmp)
#     if max_count < c:
#         max_count = c

# print(max_count)

#===========================================

# 플루이드 워셜 알고리즘으로 풀이
# 최단거리가 2 이하인 경우만 더하면 된다.

import sys
input = sys.stdin.readline

N = int(input())
dist = [[float('inf')] * N for _ in range(N)]
max_count = 0

for i in range(N):
    arr = list(input().strip())
    for index, value in enumerate(arr):
        if value == 'Y':
            dist[i][index] = 1
    dist[i][i] = 0

for k in range(N):
    for j in range(N):
        for i in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for row in dist:
    count = 0
    for x in row:
        if 0 < x <= 2:
            count += 1

    if max_count < count:
        max_count = count

print(max_count)

    