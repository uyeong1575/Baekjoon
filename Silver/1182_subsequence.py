n, s = map(int, input().split())

a = list(map(int, input().split()))

def allf(start, check:list, s1): # 특정 시작 원소에 대해 부분 수열 확인
    total = 0
    if s1 == s:
        total += 1

    if start == n-1:
        return total

    for i in range(start+1, n): # 트리 한단계 들어가기
        n_check = check + [i]
        new_sum = s1 + a[i]
        total += allf(n_check[-1], n_check, new_sum)

    return total

result = 0
for i in range(n):
    result += (allf(i, [i], a[i]))

print(result)