# 정류장에 교체용 충전지가 있는 교환기가 있음.
# 충전지마다 최대로 운행 가능한 정류장 수 정해져 있음.
# 목적지에 도착하는데 필요한 최소한의 교환횟수를 출력
# 출발지의 배터리 장착은 교환횟수에서 제외

# 흠...
# 가능한 이동거리를 저장
# 
import sys
sys.stdin = open('swea_5208_전기버스2.txt')

T = int(input())
for tc in range(1, T + 1):
    
    charge_lst = list(map(int, input().split()))
   
    # 출발점 지정
    end = charge_lst.pop(0)
    
    # 인덱스 맞추기
    charge_lst = [0] + charge_lst
    cnt = 0
    
    # 현재 위치
    cur_loc = 1
    
    while cur_loc < end: # 끝날 때까지
    
		    # 현재 위치와 충전량이 도착 위치보다 크면?
        if cur_loc + charge_lst[cur_loc] >= end:
            break # 종료
        possible = [] # 충전을 할수 있는 위치 저장
        
        # 현재 위치와 현재 위치에서 갈 수 있는 범위까지 비교
        for next in range(cur_loc + 1, cur_loc + charge_lst[cur_loc] + 1):
            
            # 더 효율적인 위치 찾고,
            if next + charge_lst[next] > cur_loc + charge_lst[cur_loc]:
                # 가능한 범위 추가
                possible.append((next + charge_lst[next], next))
            max_val = 0
            next_loc = 0
            # 제일 많이 갈 수 있는 위치 찾기
            for val, idx in possible:
                if max_val < val:
                    max_val = val
                    next_loc = idx
            cur_loc = next_loc
        # 여기까지 온거면 충전을 한번 했음.
        cnt += 1

        
    print(f'#{tc} {cnt}')
