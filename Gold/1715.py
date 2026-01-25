import sys
import heapq

n = int(sys.stdin.readline().strip())

a = [int(sys.stdin.readline().strip()) for _ in range (n)]
a.sort()
heapq.heapify(a)
ans = []
r = 0

if n == 1:
    print(0)
else:
# 앞에 두개 더한 값을 뒤에 append하고 앞의 두개는 빼기, 뺀 값은 ans에 저장
    while True:
        tmp1 = heapq.heappop(a)
        tmp2 = heapq.heappop(a)
        tmp = tmp1 +tmp2
        ans.append(tmp)
        if len(a) == 0:
            break
        heapq.heappush(a, tmp)
    
    for i in range(len(ans)):
        r += ans[i]

    print(r)
