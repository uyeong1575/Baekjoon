import sys
sys.setrecursionlimit(10**6)

n = int(input()) 
w = [None] * n

for i in range(n):
    w[i] = list(map(int, input().split())) # input 행령 생성 완료

'''Sink check flag 행렬 만들기'''
scheck = [ [False] * n for _ in range(n)] # n*n False 행렬 만들기
'''=== 생성 완료 ===='''

'''방문check flag 행렬 만들기'''
gcheck = [ [False] * n for _ in range(n)]
''' === 생성 완료 ==='''

dx = [1, 0, -1, 0]
dy = [0, -1, 0 ,1]

def DFS(x, y): # 시작점(x,y)를 기준으로 방문 안한곳 DFS 탐색, 방문시마다 문 닫음
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<n: 
            if gcheck[nx][ny] == False and scheck[nx][ny] == False: # 방문ㄴ and sinkㄴ
                gcheck[nx][ny] = True
                DFS(nx, ny)

def safearea(hight):
    count = 0
    for i in range(n):
        for j in range(n):
            if w[i][j] > hight:
                scheck[i][j] = False
            else:
                scheck[i][j] = True

    # 만약 해당칸이 활성화면 count 하나 올리고 DFS로 문 다 닫기 
    for i in range(n):
        for j in range(n):
            if gcheck[i][j] == False and scheck[i][j] == False:
                count += 1
                gcheck[i][j] = True
                DFS(i,j)
        
    for i in range(n): # 끝까지 간 후 방문기록 초기화
        for j in range(n):
            gcheck[i][j], scheck[i][j] = False, False

    return(count)

maxh = max(max(i) for i in w)
print(max(safearea(i) for i in range(0, maxh+1)))