import sys
input = sys.stdin.readline

s = list(map(int, input().strip()))

count0 = 0
count1 = 0

for i in range(1, len(s)):
    if s[i-1] == 0 and s[i] == 1: # 0에서 1로 바뀜
        count1 += 1
    elif s[i-1] == 1 and s[i] == 0:
        count0 += 1

if s[0] == 0:
    count0 += 1
else:
    count1 += 1

print(min(count1, count0))