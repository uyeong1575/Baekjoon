# 갯수 세는 차수 테이블 만들기
# n개 만큼 멀티탭 집합 만들기

# 집합에 [어떤행동, 남은 갯수, 가장 가까운 순번]이 들어가도록?



import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = list(map(int, input().split()))

adj = {}
for i in range(len(arr)):
    adj.setdefault(arr[i], []).append(i)

mlt = set()
for i in range(len(arr)):


    mlt.add(arr[i]) #넣을 수 이
    adj[arr[i]].remove(i)