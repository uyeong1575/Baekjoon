n = int(input())

w = [None] * n

for i in range(n): 
    w[i] = list(map(int, input().split()))  # 행렬 만들었음

INF = 10**7

def minf(check: list):
    if len(check) == n:
        if w[check[-1]][check[0]] != 0:
            return w[check[-1]][check[0]]
        return INF
    
    compare = []
    for i in range(n):
        if i not in check:
            if w[check[-1]][i] == 0:
                continue
            tmp = w[check[-1]][i] + minf(check + [i])
            compare.append(tmp)

    return min(compare) if compare else INF

result = []
for i in range(n):
    result.append(minf([i]))
print(min(result))

