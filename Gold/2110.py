n, c = map(int, input().split())
x = []

for _ in range(n):
    x.append(int(input()))
x.sort()
l = (max(x) - min(x))//(c-1) # 이론상 최대 거리

# 최소 target 길이를 가진 경우 있으면 True 없으면 False 
def pos(target):
    count = 1
    last = x[0]
    for i in range (1, len(x)):
        if x[i] - last >= target:
            count += 1
            last = x[i]
            if count == c:
                return True
    return False

def findlen(start, end):
    ans = 0
    while start <= end:
        mid = (start+end)//2

        if pos(mid) == True:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans

print(findlen(0, l))


    





