import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    cnt = 0
    while n >= 0:

        if n % 5 == 0:
            cnt += (n // 5)
            print(cnt)
            return

        n -= 3
        cnt += 1

    print(-1)

solve()