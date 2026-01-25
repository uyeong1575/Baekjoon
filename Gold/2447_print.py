n = int(input())
center = (n-1)//2
w = [[0] * n for _ in range(n)] #  0 채운 행렬 만들기

di = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

def printstar(x, y, n):
    if n == 1:
        w[x][y] = 1
        return

    # 각 위치로 가서 print 재귀 들어가기
    diff = n//3
    for k in range(9):
        if k != 4:
            printstar(x + diff * di[k], y + diff * dj[k], n//3)

printstar(center,center,n)

for i in range(n):
    for j in range(n):
        if w[i][j] == 1:
            print("*", end ="")
        else:
            print(" ", end ="")
    print("")