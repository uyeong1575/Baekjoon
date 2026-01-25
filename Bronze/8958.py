n = int(input())

for i in range(n):
    a = 0
    sum = 0

    q = input()
    for j in q:   
        if j == 'O':
            a += 1
            sum += a
        else:
            a = 0
            sum += a
    
    print(sum)
        
