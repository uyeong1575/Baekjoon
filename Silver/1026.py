import sys
input = sys.stdin.readline

# A와 B를 반대로 정렬해서 곱하면 결과적으로 최솟값이 나옴
def solve():
    
    n = int(input().strip())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    a_list.sort()
    b_list.sort(reverse=True)

    ans = 0
    for i in range(n):
        ans += a_list[i] * b_list[i]
    
    print(ans)

solve()