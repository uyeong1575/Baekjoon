# 시간부족
# bomb의 마지막 문자열과 s의 문자열을 비교
# 일치하지 않으면 stk에 넣고, 일치하면 앞으로 가며 비교해서 모두 일치하면 길이만큼 pop

from collections import deque

stk = deque()
s = list(input()) # 입력 문자열 리스트
bomb = list(input()) # 폭탄 문자열 리스트
bomblen = len(bomb)

for i in range(len(s)):


    stk.append(s[i])
    if len(stk) >= bomblen and i >= bomblen-1 and stk[-1] == bomb[-1]:
        # 뒤로 가면서 비교
        lc = 1
        while lc < bomblen:
            if stk[-1-lc] == bomb[-1-lc]:
                lc += 1
            else:
                break
        if lc == bomblen:
            for _ in range(bomblen):
                stk.pop()

if len(stk) == 0:
    print('FRULA')
else: print(''.join(stk))