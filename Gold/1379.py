import sys
import heapq
input = sys.stdin.readline

n = int(input())
time = []
for i in range(n):
    num, start, end = map(int, input().split())
    time.append((start,end,num))
time.sort(key=lambda x:(x[0], x[1]))
    









