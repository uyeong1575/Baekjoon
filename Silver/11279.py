import heapq
import sys

n = int(sys.stdin.readline().strip())
arr = []

for i in range(n):
    a = int(sys.stdin.readline().strip())
    if a == 0 and len(arr) == 0:
        print(0)
    elif a == 0 and len(arr) != 0:
        print(-arr[0])
        heapq.heappop(arr)
    heapq.heappush(arr, -a)