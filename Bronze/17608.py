from collections import deque
import sys

n = int(sys.stdin.readline().strip())

stack = []
stk = deque(stack)


for i in range(n):
    x = int(sys.stdin.readline().strip())

    if i == 0:
        stk.append(x)
    else: # 지금 넣는 값보다 작은 값들 전부 pop, 아니면 append
        while stk[-1] <= x:
            stk.pop()
            if len(stk) == 0:
                break
        stk.append(x)

print(len(stk))
    

    
