import sys
input = sys.stdin.readline

N = (input())
F = int(input())

N = int(N[:-3] + '00')

x = N % F

if x == 0:
    print('00')
else:
    ans = str(F - x)
    if len(ans) == 1:
        print('0'+ans)
    else:
        print(ans)

