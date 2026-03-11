import sys
sys.stdin = open('swea_5207_이진 탐색.txt')


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A.sort() # 정렬 
    
    result = 0

    for i in B:
        flag = 0 # 좌우를 지정(0은 시작, 1은 왼쪽으로, 2는 오른쪽으로)
        l, r = 0, len(A)- 1 # 처음, 끝 지정
        
        while l <= r: # 탐색 실패 조건
            m = (l + r) // 2 # 중간값 지정
            if i == A[m]: # 원하는 값 발견?
                result += 1 
                break

            elif i > A[m]:
                if flag == 2: # 번갈아 갔는지 여부 확인
                    break
                l = m + 1
                flag += 2
            else:
                if flag == 1: 
                    break
                r = m - 1
                flag == 1
        
    print(f'#{tc} {result}')