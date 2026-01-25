# '끝자리 1이면 나누기10', '짝수면 나누기2' 의 연산은 동시에 가능한 경우가 없다.
# 따라서 '10으로 나눴다가 실패했는데 2로 나누면 성공' 같은 반례가 존재할 수 없다.
# 그리디로 해결 가능하다.

import sys
sys.setrecursionlimit(10**5)

a, b = map(int,input().split())

def gkatn(start, count):
    if start == a:
        return count
    
    if start < a:
        return -1
    
    if (start-1)%10 == 0:
        return gkatn(start//10, count+1)

    if start%2 == 0:
        return gkatn(start//2, count+1)
    
    return -1

print(gkatn(b,1))

