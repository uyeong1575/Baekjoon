x, y, w, h = map(int, input().split())
a = [None]*2

if w-x<=x:
    a[0] = w-x
else:
    a[0] = x

if h-y<=y:
    a[1] = h-y
else:
    a[1] = y

print(f'{min(a)}')

