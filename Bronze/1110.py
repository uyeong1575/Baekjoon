n = int(input())
n1 = n


def ps(x, c):
    if x == n1 and c != 0:
        return c

    else:
        if x >= 10:
            tmp = (x//10) + (x%10)
            return ps((x%10)*10 + tmp%10, c+1)

        else: # n이 10보다 작으면
            return ps(10*x+x, c+1)

print(ps(n,int(0)))