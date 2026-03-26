import sys

input = sys.stdin.readline

def count(board, n):
    max_cnt = 1
    for i in range(n):
        # 행
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
        max_cnt = max(max_cnt, cnt)
        
        # 열
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
        max_cnt = max(max_cnt, cnt)
    return max_cnt

def solve():
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]
    ans = 0

    for i in range(n):
        for j in range(n):
            # 1. 오른쪽 교환
            if j + 1 < n:
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                ans = max(ans, count(board, n))
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 원상복구
            
            # 2. 아래 교환
            if i + 1 < n:
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                ans = max(ans, count(board, n))
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j] # 원상복구
                
    print(ans)

solve()