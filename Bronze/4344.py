c = int(input())

for i in range(c):

    arr = list(map(int, input().split()))
    l = len(arr)
    sum = 0
    for j in range(1,l):
        sum += arr[j]

    avr = sum/(l-1)
    num = 0
    for k in range(1,l):
        if arr[k] > avr:
            num += 1
    ans = num/arr[0]*100 

    print(f'{ans:.3f}%')