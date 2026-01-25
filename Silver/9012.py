from collections import deque

stack = []
stk = deque(stack)

n = int(input())


def checkstk(vps:list):
    for i in range(len(vps)):
        if vps[i] == '(':
            stk.append(1)
        else:
            if len(stk) == 0:
                print('NO')
                return 0
            stk.pop()

    if len(stk) == 0:
        print('YES')
        return 0
    else:
        print('NO')
        return 0

for i in range(n):
    vps = list(input())
    checkstk(vps)
    stk.clear()
