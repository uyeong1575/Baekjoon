from collections import Counter

s = input()
count = Counter(s)

odd_s = []
for c in count:
    if count[c]%2 != 0: # 홀수라면
        odd_s.append(c)

if len(odd_s) > 1:
    print("I'm Sorry Hansoo")
else:
    left = []

    if len(odd_s) == 1:
        mid = odd_s[0]
    else:
        mid = ''

    for c in sorted(count):
        left.append(c*(count[c]//2))
    left = ''.join(left)

    right = left[::-1]
    print(left+mid+right)

    