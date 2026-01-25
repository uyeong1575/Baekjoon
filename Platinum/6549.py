# 특정 i에서 좌우로 확인하며,그 값보다 높거나 같으면 +1 작으면 멈춤
import sys

def xln(i):
    ln = 1
    kr = i+1
    kl = i-1
    while kr < len(a) and a[i] <= a[kr]:
        ln +=1
        kr += 1
    while kl >= 0 and a[i] <= a[kl]:
        ln += 1
        kl -= 1
    return a[i] * ln

while True:
    tmp = list(map(int, sys.stdin.readline().strip().split()))
    if tmp[0] == 0:
        break
    n = tmp[0]
    a = tmp[1:len(tmp)]

    ans = 0
    for i in range(n):
        if ans < xln(i):
            ans = xln(i)
    print(ans)