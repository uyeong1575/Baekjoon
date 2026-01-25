n = int(input())

k = int((2*n)**(0.5))+1

ans=0
result = 0
for i in range(1,k+1):
    ans += i
    if ans == n:
        result = i
        break
    elif ans > n:
        result = i-1
        break

print(result)