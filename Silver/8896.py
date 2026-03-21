import sys
input = sys.stdin.readline

t = int(input())

def solve():
    n = int(input())
    robot = [input().strip() for _ in range(n)]

    alive = list(range(n))
    round_count = len(robot[0])

    for i in range(round_count):

        if len(alive) <= 1:
            break

        curr = set()
        for idx in alive:
            curr.add(robot[idx][i])
        
        if len(curr) != 2:
            continue

        # R, S, P 중 무엇이 졌는지 확인
        if 'R' in curr and 'S' in curr:
            loser = 'S'
        elif 'S' in curr and 'P' in curr:
            loser = 'P'
        elif 'P' in curr and 'R' in curr:
            loser = 'R'
    
        # 진 로봇 제거
        alive = [idx for idx in alive if robot[idx][i] != loser]

    if len(alive) == 1:
        print(alive[0] + 1)
    else:
        print(0)

for i in range(t):
    solve()