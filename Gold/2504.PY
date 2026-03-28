import sys
input = sys.stdin.readline

def close(stack, target_string, value):
    tmp = 0
    while stack:
        top = stack.pop()

        if top == target_string:
            stack.append(value if tmp == 0 else tmp * value)
            return True
        elif top in ['(', '[']:
            return False
        else:
            tmp += top

    return False

def solve():

    input_string = input().strip()
    stack = []

    for char in input_string:
        if char == '(' or char == '[':
            stack.append(char)

        elif char == ')':
            if not close(stack, '(', 2):
                print(0)
                return
        
        elif char == ']':
            if not close(stack, '[', 3):
                print(0)
                return
                
    ans = 0
    for i in stack:
        if isinstance(i, str):
            print(0)
            return
        ans += i
    print(ans)

solve()
