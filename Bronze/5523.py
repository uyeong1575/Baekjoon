import sys
input = sys.stdin.readline

N = int(input())
win_a = 0
win_b = 0

for _ in range(N):
    a, b = map(int, input().split())
    if a > b:
        win_a += 1
    elif a < b:
        win_b += 1

print(win_a, win_b)