import sys
from collections import deque

num = int(sys.stdin.readline().strip())

for i in range(num):
    #입력 2줄 받음
    n, s = map(int, sys.stdin.readline().strip().split()) # 문서수, 몇번째
    m = list(map(int, sys.stdin.readline().strip().split()))

    for i in range(len(m)): # 같은 우선순위 구별
        if i == s:
            m[s] = [m[s],1]
        else:
            m[i] = [m[i],0]

    target = m[s]
    mc = deque(m)
    count = 0

    while target in mc:
        i = 1
        while i < len(mc) and mc[0][0] >= mc[i][0]:
            i += 1
        if i >= len(mc):
            #없으면 앞에 pop
            mc.popleft()
            count += 1
        elif mc[0][0] < mc[i][0]:
            # 앞에 pop 뒤에 append
            mc.append(mc.popleft())

    print(count)