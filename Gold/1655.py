import sys
import heapq

n = int(sys.stdin.readline().strip())
maxheap = []
minheap = []

q = int(sys.stdin.readline().strip())
heapq.heappush(maxheap, -q)

if n == 1:
    print(-maxheap[0])

if n >= 2:
    print(-maxheap[0])
    for _ in range(n-1):
        tmp = int(sys.stdin.readline().strip())

        if len(maxheap) - len(minheap) == 1:
            heapq.heappush(minheap, tmp)
        else:
            heapq.heappush(maxheap, -tmp)

        if -maxheap[0] > minheap[0]:
            tmp1 = heapq.heappop(maxheap)
            tmp2 = heapq.heappop(minheap)
            heapq.heappush(minheap, -tmp1)
            heapq.heappush(maxheap, -tmp2)

        print(-maxheap[0])

