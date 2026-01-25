n = int(input())

pr = 0
pl = n-1

if (pl - pr)%2 == 0: # 짝수면
    print('Goose')
else:
    print('Duck')

