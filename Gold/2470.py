n = int(input())

a = list(map(int, input().split()))
a.sort()


def bifind(target, start, end):

    best_min = float('inf')
    while start <= end:
        
        mid = (start+end)//2
        current_min = abs(a[mid] + target)
        if current_min < best_min:
            best_min = current_min
            ans = mid

        if a[mid] == - target:
            return list((target, a[ans]))
        elif a[mid] < - target:
            start = mid + 1
        else: # mid > target:
            end = mid - 1
    return list((target, a[ans]))

r = []
an = []
for i in range(len(a)-1):
    tmp = (bifind(a[i], i+1, len(a)-1))
    an.append(tmp)
    r.append(abs(tmp[0]+tmp[1]))

print(*an[r.index(min(r))])

# for i in range(len(a)-1):
#     print(bifind(a[i], i, len(a)-1))
