# 사칙연산을 상하좌우로 만들어 DFS진행,
# 한칸씩 갈때마다 사직연산 테이블 해당 원소 -1
# 끝까지 간 값을 ans array에 append
# ans 최대 최소 뽑기


import sys

input = sys.stdin.readline
n = int(input().strip())
arr = list(map(int, input().strip().split()))
ctable = list(map(int, input().strip().split()))
ans = []

def DFS(id, table, cal):
    if table[0] == 0 and table[1] == 0 and table[2] == 0 and table[3] == 0:
        ans.append(cal)
        return
    
    for i in range(4):
        if table[i] > 0:
            table[i] -= 1
            if i == 0:
                ncal = cal + arr[id+1]
            elif i == 1:
                ncal = cal - arr[id+1]
            elif i == 2:
                ncal = cal * arr[id+1]
            else:
                if cal > 0:
                    ncal = cal // arr[id+1]
                else:
                    ncal = abs(cal) // arr[id+1] * -1
            DFS(id+1, table, ncal)
            table[i] +=1

DFS(0, ctable, arr[0])

print(max(ans))
print(min(ans))