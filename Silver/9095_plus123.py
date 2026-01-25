# 처음 코인을 제외하고 합하기

""" 순서 상관 안하는

n = int(input())

a = [int(input()) for i in range(n)] # amount 값으로 list 만들기


def coin_change(amount, coin:list):
    if amount == 0:
        return 1
    if amount < 0 or len(coin) == 0:
        return 0
    
    return coin_change(amount, coin[1:]) + coin_change(amount-coin[0], coin)

x = [1,2,3]
for i in range (n):
    print(coin_change(a[i], x))

"""
n = int(input())

a = [int(input()) for i in range(n)] # amount 값으로 list 만들기

def count(n):
    if n == 0:
        return 1
    if n < 0:
        return 0   

    return count(n-1)+count(n-2)+count(n-3)

for i in range(n):
    print(count(a[i]))
