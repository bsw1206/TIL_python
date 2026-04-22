# ---------------------------------------------------------
# 1. 부분집합을 이용해 한 구간(길이 M)에서의 최대 이익을 구하는 함수
# ---------------------------------------------------------
def find_max_honey_sum(idx, cur_honey, cur_honey_profit):
    global max_honey_profit

    # [가지치기] 현재까지 채취한 꿀의 양이 제한 용량(C)을 초과하면 탐색 중단
    if cur_honey > C:
        return
    
    # [기저 조건] 구간 내의 모든 벌통(M개)을 다 확인했을 때
    if idx == len(honey_lst):
        # 기존에 구한 최대 수익과 현재 조합의 수익을 비교하여 갱신
        max_honey_profit = max(max_honey_profit, cur_honey_profit)
        return
    
    # [경우 1] 현재 인덱스의 벌통에서 꿀을 채취하는 경우
    # 꿀 양은 더해주고, 수익은 '꿀 양의 제곱'만큼 더해줌
    find_max_honey_sum(idx + 1, cur_honey + honey_lst[idx], cur_honey_profit + honey_lst[idx] ** 2)

    # [경우 2] 현재 인덱스의 벌통에서 꿀을 채취하지 않고 넘어가는 경우
    # 꿀 양과 수익은 그대로 유지
    find_max_honey_sum(idx + 1, cur_honey, cur_honey_profit)


T = int(input())
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    total_max_val = 0 # 두 일꾼이 얻을 수 있는 최종 최대 수익
    
    # 해당 좌표(r, c)에서 시작하는 길이 M짜리 구간의 최대 수익을 저장할 배열
    max_honey_lst = [[0] * (N - M + 1) for _ in range(N)]
    
    # ---------------------------------------------------------
    # 2. 모든 가능한 시작 위치에 대해 미리 최대 수익을 계산하여 저장
    # ---------------------------------------------------------
    for r in range(N):
        for c in range(N - M + 1):
            # 길이 M만큼의 벌통 구간을 슬라이싱하여 추출
            honey_lst = arr[r][c : c + M]
            max_honey_profit = 0
            
            # DFS 탐색 시작: 인덱스 0, 현재 꿀 양 0, 현재 수익 0
            find_max_honey_sum(0, 0, 0)
            
            # 탐색이 끝나면 해당 구간의 최대 수익을 배열에 기록
            max_honey_lst[r][c] = max_honey_profit
            
    # ---------------------------------------------------------
    # 3. 겹치지 않는 두 일꾼의 작업 구간을 선택하여 최대 수익 합산
    # ---------------------------------------------------------
    # 첫 번째 일꾼의 구간 선택 (r1, c1)
    for r1 in range(N):
        for c1 in range(N - M + 1):
            p1 = max_honey_lst[r1][c1] # 첫 번째 일꾼의 수익
            
            # 두 번째 일꾼의 구간 선택 (r2, c2)
            # 첫 번째 일꾼과 같은 행(r1)부터 시작하여 중복 탐색 방지
            for r2 in range(r1, N):
                s_c2 = 0
                
                # 만약 두 일꾼이 같은 행(가로줄)에 있다면
                if r1 == r2:
                    s_c2 = c1 + M # 두 번째 일꾼은 첫 번째 일꾼 구간이 끝난 이후부터 시작해야 함 (겹침 방지)
                    
                    for c2 in range(s_c2, N - M + 1):
                        p2 = max_honey_lst[r2][c2]
                        # 두 수익의 합이 기존 최대치보다 크면 갱신
                        total_max_val = max(total_max_val, p1 + p2)
                        
                # 두 일꾼이 서로 다른 행에 있다면
                else:
                    # 행이 다르므로 열(c2)은 처음(0)부터 아무 곳이나 선택 가능 (겹칠 위험 없음)
                    for c2 in range(N - M + 1):
                        p2 = max_honey_lst[r2][c2]
                        total_max_val = max(total_max_val, p1 + p2)
                        
    # 최종 결과 출력
    print(f'#{tc} {total_max_val}')