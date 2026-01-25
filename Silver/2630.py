n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

countw = 0
countb = 0

def cut(N, y1, y2, x1, x2):
    global countw, countb
    if N == 1:
        if a[y1][x1] == 1:
            countb += 1
            return 1
        else:
            countw += 1
            return 1
    else:
        ac = 0
        base = a[y1][x1]
        for i in range(y1, y2):
            for j in range(x1, x2):
                if a[i][j] != base:
                    continue
                else:
                    ac += 1

        if ac == N**2:
            if base == 1:
                countb += 1
                return 1
            else:
                countw += 1
                return 1

    ym = (y1 + y2) // 2
    xm = (x1 + x2) // 2
    cut(N//2, y1, ym, x1, xm)
    cut(N//2, y1, ym, xm, x2)
    cut(N//2, ym , y2, x1, xm)
    cut(N//2, ym , y2, xm, x2)

cut(n, 0, n, 0, n)

print(countw)
print(countb)