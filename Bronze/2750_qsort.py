def qsort(a, l, r):

    pr = r
    pl = l
    pt = (pr+pl)//2
    x = a[pt]

    while pl <= pr:
        while a[pl] < x : pl += 1
        while a[pr] > x : pr -= 1
        if pl<=pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if l < pr : qsort(a, l, pr)
    if pl < r : qsort(a, pl, r)

n = int(input())

a = []
for i in range(n):
    b = int(input())
    a.append(b)

# [5, 2, 4, 3, 1]
qsort(a, 0, len(a)-1)
# print(a)

for i in range(n):
    print(a[i])