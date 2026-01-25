n = int(input())

Flag_i = [None] * n          # i 열에 있는지 여부
Flag_j = [False] * n         # j 행에 있는지 여부
Flag_a = [False] * (2*n-1)   # 오른쪽 아래 대각선
Flag_b = [False] * (2*n-1)   # 왼쪽 아래 대각선


def NQ(i):
    if i == n:
        return 1

    total = 0
    for j in range(n):
        if (not Flag_j[j] and not Flag_a[j-i+n-1] and not Flag_b[i+j]):

            Flag_i[i] = True              
            Flag_j[j] = Flag_a[j-i+n-1] = Flag_b[i+j] = True
            total += NQ(i+1)
            Flag_j[j] = Flag_a[j-i+n-1] = Flag_b[i+j] = False
    return total

print(NQ(0))

