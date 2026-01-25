
import sys
from collections import deque

n = int(sys.stdin.readline().strip())
circle = []
s = []
stk = deque(s)
count = 1

for _ in range(n):
    x, r = map(int, sys.stdin.readline().split())
    circle.append((x-r, x+r, r+r))
circle.sort(key=lambda circle: (circle[1], circle[2])) 
# 입력 변환, 정렬 완료

for i in range(len(circle)):
    if len(stk) == 0: # 처음 넣을 때
        count += 1
        # print('처음')
        stk.append(circle[i])

    else:
        if stk[-1][1] == circle[i][1]: #R 겹치면 
            sumlen = 0
            while stk and stk[-1][0] >= circle[i][0]: # 추가하려는 원의 왼쪽 밖으로 나가기전까지 pop
                sumlen += stk[-1][2]
                stk.pop()
            if sumlen == circle[i][2]:
                count += 2
                # print('감싸고 2개')
                stk.append(circle[i])
            else: 
                count += 1
                # print('감싸고 1개')
                stk.append(circle[i])
       
        elif circle[i][0] <= stk[-1][0]: # R 안겹치고 왼쪽으로 감싸는 경우
                while stk and stk[-1][0] >= circle[i][0]:
                    stk.pop()
                count += 1
                # print('겹 ㄴ 감싸고 1개')
                stk.append(circle[i])
    
        else:
            count += 1
            # print('오른쪽에 한개')
            stk.append(circle[i])
    
print(count)