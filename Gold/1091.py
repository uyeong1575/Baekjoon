import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, (input().split())))
S = list(map(int, (input().split())))

card = [i for i in range(N)] # 처음 순서 배열
original = [i for i in range(N)]

flag = True
cnt = 0

while True:

    # % 가 P인지 확인
    flag = True
    for i in range(N):
        if i % 3 != P[card[i]]:
            flag = False
            break

    if flag == True:
        print(cnt)
        break

    # S대로 섞기 
    new_card = [0] * N
    for i in card:
        new_card[S[i]] = card[i]
    card = new_card    

    cnt += 1

    if card == original:
        print(-1)
        break
    
    