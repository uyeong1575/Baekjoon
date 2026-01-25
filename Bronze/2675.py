num = int(input())

for i in range(num):
    a = list((input().split()))


    l = int(a[0])
    str = a[1]

    for i in str:
        print(f'{l * i}', end='')
    print()