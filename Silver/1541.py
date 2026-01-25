# - 뒤에 +오면 -나올때까지 묶어
# 연산자 리스트 뒤에서부터 확인하며 -를 찾는다. - 찾으면 그 뒤의 숫자들을 더해서 저장


import re

s = input()

num = list(map(int, re.findall(r"\d+", s)))   # 숫자만
op = re.findall(r"[+-]", s)                # 연산자만


dp = 0
ans = []

for i in range(len(op)-1, -1, -1):
    
    if op[i] == '+':
        dp += num[i+1]
    elif op[i] == '-':
        ans.append(-(dp+num[i+1]))
        dp = 0
    
    if i == 0:
        ans.append(dp + num[0])

r = 0    
for i in range(len(ans)):
    r += ans[i]

if not op:
    print(num[0])
else: 
    print(r)
