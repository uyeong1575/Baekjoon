s = input().split('.')

ans = []
flag = 0
for x in s:
    if len(x) >= 4 and len(x)%2 == 0:
        ans.append('AAAA'*(len(x)//4)+'B'*(len(x)%4))
    elif len(x) == 2:
        ans.append('BB'*(len(x)//2))
    elif len(x) == 0:
        continue
    else:
        flag = 1

if flag == 0:
    index = 0
    for i in range(len(s)):
        if len(s[i]) > 0:
            s[i] = ans[index]
            index += 1

    result = '.'.join(s)
    print(result)
else:
    print(-1)

