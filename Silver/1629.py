a, b, c = map(int, input().split())

def modpow(a, b, c):
    if b == 1:
        return a%c
    
    else:
        if b%2 == 0:
            return modpow(a,b//2,c) ** 2 % c
        else:
            return a * modpow(a, (b-1)//2, c)**2 % c

print(modpow(a, b, c))