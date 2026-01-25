a, b, v = map(int, input().split())

if (v-a)%(a-b) == 0: 
    ans = (v-a)//(a-b) + 1
else:
    ans = (v-a)//(a-b) + 2

print(ans)