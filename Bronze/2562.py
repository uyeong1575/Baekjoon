arr = [None] * 9

for i in range(1,10):
    a = int(input())
    arr[i-1] = a

b = max(arr)
print(b)
print(arr.index(b)+1)