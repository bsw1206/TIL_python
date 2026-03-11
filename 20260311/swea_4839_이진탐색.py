import sys
sys.stdin = open('swea_4839_이진탐색.txt')

def binary_search(num, l, r, c):
    if num <= c:
        r = c
        c = int((l + r) / 2)
    else:
        l = c
        c = int((l + r) / 2)
    return num
T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    result = 0
    l, r = 1, P
    c = int((l + r) / 2)
    c1, c2 = c, c
    r1, r2 = r, r
    while c1 != A and c2 != B:
        binary_search(A, l, r1, c1)
        binary_search(B, l, r2, c2)
    
    if c1 == A and c2 != B:
        result = 'A'
    elif c1 != A and c2 == B:
        result = 'B'
    if c1 == A and c2 == B:
        result = 0
    

    print(f'#{tc} {result}')



#################################################
# 수정

import sys
sys.stdin = open('swea_4839_이진탐색.txt')

def count_binary_search(total_pages, target):
    # 처음과 끝 페이지 지정
    l = 1
    r = total_pages
    # 카운트 지정
    count = 0
    
    # 처음 값이 역전하면 종료
    while l <= r:
        # 가운뎃 값 지정
        c = int((l + r) / 2)
        # 계산 횟수 증가
        count += 1
        
        if c == target: # 목표값을 찾았을 때
            return count  # 횟수 반환
        # 처음, 끝 값을 가운뎃 값으로 갱신
        elif c > target: 
            r = c        
        else:
            l = c    

    return count

T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    
    
    count_A = count_binary_search(P, A)
    count_B = count_binary_search(P, B)
    
    # B가 찾는 데 더 오래 걸리면 B, 반대면 A
    if count_A < count_B:
        result = 'A'
    elif count_A > count_B:
        result = 'B'
    else:
        result = 0
        
    print(f'#{tc} {result}')