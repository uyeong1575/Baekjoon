import sys
input = sys.stdin.readline

for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    
    sec1 = h1 * 3600 + m1 * 60 + s1
    sec2 = h2 * 3600 + m2 * 60 + s2
    
    work_sec = sec2 - sec1
    
    # 다시 h, m, s로 변환
    h = work_sec // 3600
    m = (work_sec % 3600) // 60
    s = work_sec % 60
    
    print(h, m, s)