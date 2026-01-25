n = int(input())

if n <= 99:
    print(n)
else:
    count = 99

    for j in range(100, n+1):

        l = [int(ch) for ch in str(j)]  # 3자리 n으로 리스트 만들기

        if l[1] - l[0] > 0:
            if l[2] - l[1] == l[1] - l[0]:
                count += 1


        elif l[1] == l[0]:
            if l[0] == l[1] == l[2]:
                count += 1
        
        else:
            if l[1] - l[2] == l[0] - l[1]:
                count += 1

    print(count)

    
    