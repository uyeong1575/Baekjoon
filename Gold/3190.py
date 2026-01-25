import sys
from collections import deque

pi = 0
pointi = 0
count = 0
x = 1
y = 1
dx = [1, 0 ,-1, 0]
dy = [0, 1, 0, -1]
sn = [[1,1]]
snake = deque(sn)
apple = []
point = []

n = int(sys.stdin.readline().strip())

k = int(sys.stdin.readline().strip())
for _ in range(k):
    a, b = map(int, sys.stdin.readline().strip().split())
    apple.append([a,b])

l = int(sys.stdin.readline().strip())
for _ in range(l):
    a, b = map(str, sys.stdin.readline().strip().split())
    point.append([int(a),b])
point.append([None,None])

while True:
    count += 1
    # # 방향 전환을 확인해서 pointi 값 업데이트
    if count -1 == point[pi][0]:
        if point[pi][1] == 'L':            
            pointi = (pointi - 1)%4
        if point[pi][1] == 'D':
            pointi = (pointi + 1)%4
        pi += 1
    x = x + dx[pointi]
    y = y + dy[pointi]
    # 종료 확인
    if x <= 0 or x > n or y <= 0 or y > n:
        break
    if [y,x] in snake:
        break
    snake.append([y,x])
    if not [y,x] in apple:
        snake.popleft()
        continue
    apple[apple.index([y,x])] = 0
    
print(count)