import sys
sys.stdin = open('몬스터 마스터.txt')

def dfs(r, c, cur_time, idx):
    global min_time

    if cur_time > min_time:
        return
    if idx == len(lst):
        min_time = min(min_time, cur_time)
        return
    
    for i in range(len(lst)):
        if not visited[i]:
            target, target_r, target_c = lst[i]
            if target < 0:
                if catch[abs(target)]:
                    
                    visited[i] = True
                    dfs(target_r, target_c, cur_time + abs(target_r - r) + abs(target_c - c), idx + 1)
                    visited[i] = False
            elif target > 0:
                visited[i] = True
                catch[target] = True
                dfs(target_r, target_c, cur_time + abs(target_r - r) + abs(target_c - c), idx + 1)
                visited[i] = False
                catch[target] = False
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    town = [list(map(int, input().split())) for _ in range(N)]

    lst = []

    min_time = float('inf')

    for r in range(N):
        for c in range(N):
            if town[r][c] != 0:
                lst.append((town[r][c], r, c))

    catch = [False] * 5
    visited = [False] * len(lst)

    dfs(0, 0, 0, 0)
    print(f'#{tc} {min_time}')


##################################################################################

import sys
sys.stdin = open('몬스터 마스터.txt')

def dfs(r, c, current_time, visited_mask, catch_mask, visited_cnt):
    global min_time

    # 1. 가지치기: 크거나 '같을' 때도 잘라주면 미세하게 더 빠릅니다.
    if current_time >= min_time: 
        return
        
    # 2. 종료 조건: 모든 목표를 방문했을 때
    if visited_cnt == target_count: 
        min_time = min(min_time, current_time)
        return 

    for i in range(target_count):
        # 비트마스크 검사: i번째 비트가 0인지 확인 (방문 안 했나?)
        if not (visited_mask & (1 << i)): 
            target, tr, tc = lst[i]

            # 타켓이 손님이고 아직 해당 몬스터(비트)를 잡지 못한 경우
            if target < 0 and not (catch_mask & (1 << abs(target))): 
                continue 

            time = abs(tr - r) + abs(tc - c) 
            
            # 다음 재귀로 넘겨줄 몬스터 포획 상태 계산
            # 몬스터면 해당 몬스터 번호의 비트를 1로 켜고, 아니면 그대로 둠
            nxt_catch_mask = catch_mask | (1 << target) if target > 0 else catch_mask

            # 3. 재귀 호출
            # 인자로 새로운 상태(visited_mask | (1 << i))를 넘기므로 
            # 재귀가 끝나고 돌아왔을 때 False로 초기화해 줄 필요가 없습니다!
            dfs(tr, tc, current_time + time, visited_mask | (1 << i), nxt_catch_mask, visited_cnt + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    town = [list(map(int, input().split())) for _ in range(N)]

    lst = []
    for r in range(N):
        for c in range(N):
            if town[r][c] != 0:
                lst.append((town[r][c], r, c))
                
    target_count = len(lst)
    min_time = float('inf')
    
    # visited_mask, catch_mask 모두 0(아무것도 켜지지 않은 상태)으로 시작
    dfs(0, 0, 0, 0, 0, 0)
    
    print(f'#{tc} {min_time}')