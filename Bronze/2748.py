# 피보나치 함수 구현
n = int(input())

# 재귀(top down 방식)

# def fibo_TD(x):
#     if x == 1 or x == 2:
#         return 1

#     return fibo_TD(x-1) + fibo_TD(x-2)

# print(fibo_TD(n))
n = int(input())
def fibo_BU(x):
    dp = [[] for _ in range(x+1)]

    dp[1] = 1
    if x > 1:
        dp[2] = 1
    if x >= 3:
        for i in range(3, x+1):
            dp[i] = dp[i-1] + dp[i-2] 

    return dp[x]

print(fibo_BU(n))