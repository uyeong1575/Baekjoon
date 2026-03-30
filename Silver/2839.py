import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    cnt = 0

    # 3빼면서 5로 나눠서 떨어지는지 확인하기
    while n >= 0:

        if n % 5 == 0:
            cnt += (n // 5)
            print(cnt)
            return

        n -= 3
        cnt += 1

    print(-1)

solve()