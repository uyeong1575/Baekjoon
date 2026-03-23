import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    x = int(sys.stdin.readline().strip())
        
    standard = 10
    while x > standard:
        if x % standard >= standard // 2:
            x = (x // standard + 1) * standard # 올림
        else:
            x = (x // standard) * standard # 내림
        
        standard *= 10

    print(x)


