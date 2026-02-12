import sys
input = sys.stdin.readline

while True:
    arr = list(map(str, input().split()))

    if 'w' in arr:
        print('chunbae')
        break
    elif 'b' in arr:
        print('nabi')
        break
    elif 'g' in arr:
        print('yeongcheol')
        break
