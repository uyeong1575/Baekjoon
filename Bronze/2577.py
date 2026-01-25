
a=int(input())
b=int(input())
c=int(input())

numstr = str(a*b*c)

for i in '0123456789':
    count = 0
    for j in numstr:
        if j == i:
            count += 1
    
    print(count)
