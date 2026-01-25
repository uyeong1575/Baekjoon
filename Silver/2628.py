x, y = map(int, input().split())

n = int(input())

x_list = [0, x]
y_list = [0, y]

for i in range(1, n+1):
    
    a, b = map(int, input().split())

    if a == 0:
        # x의 list에 넣기
        y_list.append(b)

    else:
        # y의 list에 넣기
        x_list.append(b)


x_list.sort()
y_list.sort()

# print(x_list)
# print(y_list)

val_x = []
val_y = []

for i in range(len(x_list)):
    val_x.append(x_list[i] - x_list[i-1])

for i in range(len(y_list)):
    val_y.append(y_list[i] - y_list[i-1])

# print(max(val_x))
# print(max(val_y))
print(max(val_x)*max(val_y))