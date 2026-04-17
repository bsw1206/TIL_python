# N개의 컨테이너를 M대의 트럭으로 운반
# 트럭당 한 개, 
# 이동한 화물의 총 증량이 최대가 되도록 컨테이너를 옮겼을 때
# 옮겨진 화물의 전체 무게가 얼마인지 출력하는 프로그램
# 한 개도 옮길 수 없는 경우 0 출력

import sys
sys.stdin = open('swea_5201_컨테이너 운반.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    weight_lst = list(map(int, input().split()))
    possible_lst = list(map(int, input().split()))
    
    # 화물 무게랑, 트럭 적재량을 둘다 뒤집기
    weight_lst.sort(reverse = True) 
    possible_lst.sort(reverse = True)
    # print(n_lst)
    # print(m_lst)
    sum_val = 0
        
    for p in possible_lst:
        for w in range(len(weight_lst)):
            # 적재 가능량이 가장 무거운 화물(맨 앞 인덱스 화물)을 담을 수 있다?
            if p >= weight_lst[w]:
                # 합계에 추가
                sum_val += weight_lst.pop(w)
                break # 다음 적재 가능 여부를 찾으러 떠나기
    
    print(f'#{tc} {sum_val}')