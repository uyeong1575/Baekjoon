def zfind(n, i, j):
    if n == 0:
        return 0
    
    t = 2**(n-1)
    sum = 0

    if i < t and j < t:
        sum += 0

    elif i >= t and j < t:
        sum += 1 * (4**(n-1))
        i -= t

    elif i < t and j >= t:
        sum += 2 * (4**(n-1))
        j -= t

    else: # i >= t and j >= t:
        sum += 3 * (4**(n-1))
        i -= t
        j -= t

    return sum + zfind(n-1, i, j)

a, b, c = map(int, input().split())

print(zfind(a, c, b))

