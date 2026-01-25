n, m = map(int, input().split())

a = list(map(int, input().split()))
a.sort()
mx = max(a)

def take(m): 
    sum = 0
    for i in range(len(a)):
        if a[i] > m:
            sum += a[i] - m
    return sum

def bifind(target, start, end):

    while start <= end:

        mid = (start+end)//2
        t = take(mid)

        if t >= target: # 너무 많이 자름 m 더 높일 수 있음
            start = mid + 1      
        elif t < target: # 너무 조금 자름 m 더 낮출 수 있음
            end = mid - 1

    for i in range(mid-1, mid+2):
        if take(i) < m:
            return i-1
            
print(bifind(m, 0, mx))

 # print(mid)
    # print(take(mid))

    # for i in range(mid-1, mid+2):
    #     if take(i) < m:
    #         return i-1
