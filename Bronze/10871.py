n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(1,n+1):
    num = a[i-1]
    if num < x:
        print(num, end=" ")