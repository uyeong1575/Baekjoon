import sys
input = sys.stdin.readline

# s, k ,h = map(int, input().split())

# if s+k+h < 100:
#     min_val = min(s, k, h)
#     if min_val == s:
#         print('Soongsil')
#     elif min_val == k:
#         print('Korea')
#     else:
#         print('Hanyang')
# else:
#     print('OK')


# 입력을 리스트로 받음
scores = list(map(int, input().split()))
universities = ['Soongsil', 'Korea', 'Hanyang']

if sum(scores) >= 100:
    print('OK')
else:
    # 최솟값의 인덱스를 찾아 해당 학교 이름을 출력
    min_index = scores.index(min(scores))
    print(universities[min_index])