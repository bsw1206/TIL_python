import sys
sys.stdin = open('baby_gin_game.txt')

T = int(input())
for tc in range(1, T + 1):
    result = False
    num = list(map(int, input()))

    num.sort()
    
    cnt = 0
    
    for i in range(0, len(num), 3):
    
        if num[i] == num[i + 1] - 1 and num[i] == num[i + 2] - 2:
            cnt += 1
    
        elif num[i] == num[i + 1] and num[i] == num[i + 2]:
            cnt += 1
    
    if cnt == 2:
        result = True
    
    print(f'#{tc} {result}')

###################################################################
# 위 코드가 문제가 있었음. 예를 들어서 123123을 정렬하면 
# 112233이 되는데 이러면 원래의 run을 깨버림.
# 이를 수정한 코드

import sys
sys.stdin = open('baby_gin_game.txt')

T = int(input())
for tc in range(1, T + 1):
    num = list(map(int, input()))
    
    
    counts = [0] * 12 
    for n in num:
        counts[n] += 1
        
    i = 0
    triplets = 0
    runs = 0
    
    
    while i < 10:
    
        if counts[i] >= 3: 
            counts[i] -= 3
            triplets += 1
            continue
            
        
        if counts[i] >= 1 and counts[i + 1] >= 1 and counts[i + 2] >= 1:
            counts[i] -= 1
            counts[i + 1] -= 1
            counts[i + 2] -= 1
            runs += 1
            continue
            
        
        i += 1 

    result = (triplets + runs == 2)
    print(f'#{tc} {result}')