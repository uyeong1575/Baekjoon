import sys

input = sys.stdin.readline

N, M = map(int, input().split())
J = int(input())

arr = [ int(input()) for _ in range(J) ] # 사과 떨어지는 위치 순서대로

left = 1
right = M
move_count = 0

for apple in arr:
    # 오른쪽 이동
    if apple > right:
        diff = apple - right
        right = apple
        left += diff
        move_count += diff
    # 왼쪽 이동
    elif apple < left:
        diff = left - apple
        left = apple
        right -= diff
        move_count += diff

print(move_count)



