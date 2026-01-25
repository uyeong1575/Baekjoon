a, b = map(str, input().split())

rev_a = a[::-1]
rev_b = b[::-1]

a = int(rev_a)
b = int(rev_b)

if a>=b:
    print(rev_a)
else:
    print(rev_b)
