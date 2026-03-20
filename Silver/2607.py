import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

target_word = words[0]
similar_count = 0
    
for i in range(1, n):
    compare_word = words[i]
    
    target_list = list(target_word)
    remain_word = [] # 기준 단어에 없는 글자 리스트
    
    for char in compare_word:
        if char in target_list:
            target_list.remove(char)
        else:
            remain_word.append(char)
    
    # target에 1 이하로 남거 remain에 1이하로 남으면 비슷
    if len(target_list) <= 1 and len(remain_word) <= 1:
        similar_count += 1
            
print(similar_count)

