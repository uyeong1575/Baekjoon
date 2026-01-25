# 받은 배열 정렬 
# 처음 원소를 기준으로 순차적으로 비교, 만약 arr[][1]도 크면 -1
# 작은 값을 만나면 그 작은 값을 기준으로 비교하도록 업데이트

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    # 입력 정렬
    n = int(input())
    arr = []
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append([a,b])
    arr.sort()

    # 선발 인원수 구하기
    index = 0
    ans = n
    for i in range(n):
        if arr[i][1] > arr[index][1]:
            ans -= 1
        else: index = i
    
    print(ans)