n = int(input())
arr = list(map(int, input().split()))

count = 0

for i in range(len(arr)):

    a= arr[i]

    if a ==1:
        continue

    elif a ==2:
        count += 1
        continue

    for j in range(2, a):
        if a%j==0:
            break

        if j+1 == a:
            count += 1

print(count)


# k = input()

# co = 0
# for j in list(map(int, input().split())):
#     if j == 1:
#         continue
#     for m in range(2,j):
#         if j%m == 0:
#             break
#     else:
#         co +=1
        

# print(co)
       



