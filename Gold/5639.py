# 재귀적으로 범위를 나누기

import sys
sys.setrecursionlimit(10**4)

pre = []
for line in sys.stdin:  # 더 이상 읽을 줄이 없으면 종료
    data = line.strip()
    pre.append(int(data))

def solve(l, r): #left, right 받기
    if l >= r:  # 종료 조건
        return
    
    root = pre[l]
    m = r
    for i in range(l+1, r):
        if pre[i] > root:
            m = i
            break

    solve(l+1, m)
    solve(m, r)
    print(root)

solve(0,len(pre))
    




