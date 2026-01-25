def hanoi(n,a,b): #n개의 탑, a에서 b로 옮김
   
    if n > 1:
        hanoi(n-1, a, 6-a-b)

    print(a, b)

    if n > 1:
        hanoi(n-1, 6-a-b, b)

num = int(input())

print(2**num-1)

if num <= 20:
    hanoi(num, int(1), int(3))