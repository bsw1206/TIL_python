# 줄기세포 : 가로, 세로 크기가 1인 정사각형 형태
# 생명력 수치 : X 시간 동안 비활성 상태, X 시간 지나는 순간 활성 상태가 됨.
# X 시간 동안 살아있을 수 있으며, X 시간 지나면 죽음.
# 번식하는 방향에 이미 줄기 세포가 존재하는 경우 해당 방향으로 추가적으로 번식하지 않음.
# 두개 이상의 줄기 세포가 하나의 셀에 동시에 번식하려고 하면 생명력 수치가 높은 줄기 세포가 해당 그리드 셀을 차지함.
# 살아있는 줄기 세포 프로그램 작성하기.

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
import sys
sys.stdin = open('swea_5653_줄기세포배양.txt')
# 죽은 상태, 비활성 상태, 활성 상태 3가지가 존재
# 비활성 상태 여부, 경과 시간
# 1. 비활성/활성/사망 여부, 현재 시간을 저장하고,(비활성 : 0, 활성 : 1, 죽음 : 2) 
# 예시 arr[r][c] == 1 -> arr[r][c] = [arr[r][c], 0, arr[r][c]]
# [index_value, condition, remain_time]
# 2. 비활성에서 남는 시간이 0이 되면 상하좌우에 현재 가운데 인덱스와 비활성 상태를 부여. 죽은 상태라면 continue
# 3. 번식을 했는데 현재 범위 밖이라면 확장을 하고 번식시킴.
# 4. 활성 상태에서 남는 시간이 0이 되면 죽음 상태로 바꿈.
# 여기서 idx를 어케 정해야 할까? -> 만약에 
# def cell():
#     new_arr = []
#     for j in range(N):
#         new_arr.append([[0] + arr[j] + [0]])
  
    
#     for _ in range(K):
#         new_arr = [[0] * M] + new_arr
#         new_arr.append([0] * M)
#         N, M = N + 2, M + 2
#         for r in range(N):
#             for c in range(M):
#                 new_arr[r][c][2] -= 1
#                 if new_arr[r][c][2] == 0:
#                     if new_arr[r][c][1] == 0:
#                         for i in range(4):
#                             nr, nc = r + dr[i], c + dc[i]
#                             if new_arr[nr][nc][1] == 0:
#                                 if new_arr[nr][nc][1] > new_arr[r][c][1]:
#                                     continue
#                                 else:
#                                     new_arr[nr][nc] = [new_arr[r], 0, new_arr[r]]
#                     if new_arr[r][c][1] == 1:
#                         new_arr[r][c] == [new_arr[r][c][0], 2, 0]

# T = int(input())
# for tc in range(1, T + 1):
#     N, M, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     for r in range(N):
#         for c in range(M):
#             if arr[r][c] > 0:
#                 arr[r][c] = [arr[r][c], 0, arr[r][c]]
#             else:
#                 arr[r][c] = [0, 2, 0]
#     cell()
#     cnt = 0
#     for r in range(N):
#         for c in range(N):
#             if arr[r][c][1] != 2:
#                 cnt += 1
#     print(f'#{tc} {cnt}')


##############################################################################################



dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    
    # 1. 넉넉한 크기의 2차원 배열 미리 생성 (최대 확장 범위 고려)
    GRID_SIZE = 400
    CENTER = 150
    
    # 0은 빈칸. 세포가 있으면 [X(생명력), 상태(0:비활성, 1:활성, 2:죽음), 남은시간]
    arr = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    
    # 탐색 시간을 줄이기 위한 바운딩 박스 (세포가 존재하는 구역)
    min_r, max_r = CENTER, CENTER + N - 1
    min_c, max_c = CENTER, CENTER + M - 1
    
    # 2. 중앙에 초기 세포 배치
    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(M):
            if row[c] > 0:
                # [생명력, 0(비활성), 초기 남은시간은 생명력과 동일]
                arr[CENTER + r][CENTER + c] = [row[c], 0, row[c]]

    # 3. K시간 동안 배양 시작
    for _ in range(K):
        # 이번 턴에 확장될 수 있는 최대 범위 계산용
        nxt_min_r, nxt_max_r = min_r, max_r
        nxt_min_c, nxt_max_c = min_c, max_c
        
        # 동시 번식 경쟁을 위한 임시 2차원 배열 (여기에는 생명력 X값만 기록)
        breed_candidates = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        
        # 세포가 있는 영역만 탐색!
        for r in range(min_r, max_r + 1):
            for c in range(min_c, max_c + 1):
                if arr[r][c] == 0: 
                    continue
                
                X, state, remain_time = arr[r][c]
                
                # 죽은 세포는 건너뜀
                if state == 2:
                    continue
                    
                # 비활성 상태
                if state == 0:
                    remain_time -= 1
                    if remain_time == 0:
                        arr[r][c] = [X, 1, X] # 활성 상태(1)로 전환, 타이머 리셋
                    else:
                        arr[r][c][2] = remain_time
                        
                # 활성 상태
                elif state == 1:
                    # 활성 상태가 된 '첫 시간'에만 상하좌우 번식 (타이머가 막 리셋되어 X일 때)
                    if remain_time == X:
                        for i in range(4):
                            nr, nc = r + dr[i], c + dc[i]
                            # 맵을 벗어나지 않고, 기존 본 배열에 세포가 없는 빈 칸일 때만 번식 시도
                            if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE:
                                if arr[nr][nc] == 0:
                                    # 동시에 번식하려는 다른 세포보다 생명력이 큰 경우만 임시 배열 갱신
                                    if X > breed_candidates[nr][nc]:
                                        breed_candidates[nr][nc] = X
                                        
                                        # 바운딩 박스(탐색 범위) 갱신
                                        nxt_min_r = min(nxt_min_r, nr)
                                        nxt_max_r = max(nxt_max_r, nr)
                                        nxt_min_c = min(nxt_min_c, nc)
                                        nxt_max_c = max(nxt_max_c, nc)
                    
                    remain_time -= 1
                    if remain_time == 0:
                        arr[r][c] = [X, 2, 0] # 남은 시간 다 되면 죽음 상태(2)로 전환
                    else:
                        arr[r][c][2] = remain_time
        
        # 4. 임시 배열에 모인 '새로 번식할 세포'들을 본 배열에 확정 도장 찍기
        for r in range(nxt_min_r, nxt_max_r + 1):
            for c in range(nxt_min_c, nxt_max_c + 1):
                if breed_candidates[r][c] > 0:
                    new_X = breed_candidates[r][c]
                    arr[r][c] = [new_X, 0, new_X] # 새로운 세포는 비활성 상태로 세팅
        
        # 다음 턴을 위해 바운딩 박스 확정
        min_r, max_r = nxt_min_r, nxt_max_r
        min_c, max_c = nxt_min_c, nxt_max_c

    # 5. K시간 후, 살아있는(비활성+활성) 세포 카운트
    cnt = 0
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            if arr[r][c] != 0 and arr[r][c][1] != 2: # 빈 칸이 아니고, 죽은 상태(2)가 아니면
                cnt += 1
                
    print(f'#{tc} {cnt}')