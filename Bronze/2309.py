a = []
sum = 0
for _ in range(9):

    x = int(input())
    a.append(x)
    sum += x

f = sum - 100

for i in range(9):

    for j in range(i+1,9):
        if (a[i]+a[j]) == f:
            i1 = a[i]
            j1 = a[j]

a.remove(i1)
a.remove(j1)
a.sort()

for i in range(7):
    print(a[i])