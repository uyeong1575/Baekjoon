from collections import deque
k = int(input())

stack = []
stk = deque(stack)

for i in range(k):
    tmp = int(input())
    if tmp == 0:
        stk.pop()
    else:
        stk.append(tmp)

sum = 0
for i in range(len(stk)):
    sum += stk[i]
print(sum)