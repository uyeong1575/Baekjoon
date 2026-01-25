import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().strip().split())

arr = [[] for _ in range(n)]

for i in range(n):
    arr[i] = list(map(str, input().strip()))

dq = deque()

for i in range(n): # 초기 값 넣기
    for j in range(m):
        if arr[i][j] == '*':
            dq.appendleft((i,j,0,'*'))
        elif arr[i][j] == 'S':
            dq.append((i,j,0,'S'))

ans = 0
found = False
while dq:
    (y,x,day,what) = dq.popleft()
    for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
        ny, nx = y+dy, x+dx
        if 0<= ny < n and 0 <= nx < m: # 범위 확인
            if what == '*' and (arr[ny][nx] == '.' or arr[ny][nx] == 'S'):
                arr[ny][nx] = '*'
                dq.append((ny,nx,day+1,'*'))
            if what == 'S':
                if arr[ny][nx] == '.':
                    arr[ny][nx] = 'S'
                    dq.append((ny,nx,day+1,'S'))
                elif arr[ny][nx] == 'D':
                    ans = day+1
                    found = True
                    break
    if found == True:
        break

if ans == 0:
    print('KAKTUS')
else:
    print(ans)
