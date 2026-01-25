
n = int(input())

a= list(map(int, input().split())) #받은 값으로 list 만들기

def maxsub(check:list):

    if len(check) == n:
        return 0

    compare = []
    for i in range(n):
        if not i in check:
            tmp = abs(a[check[-1]] - a[i]) + maxsub(check + [i])
            compare.append(tmp)
    
    return max(compare)

result = []
for i in range(n):
    result.append(maxsub([i]))

print(max(result))

