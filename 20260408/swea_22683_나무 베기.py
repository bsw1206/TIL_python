import sys
sys.stdin = open('swea_22683_나무 베기.txt')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(cur_val, r, c, cut, dir):

    global min_val

    if cur_val >= min_val:
        return
    
    if field[r][c] == 'Y':
        min_val = min(min_val, cur_val)
        return
    
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            turn_diff = abs(dir - i)
            turn_cost = min(turn_diff, 4 - turn_diff)
            # 나무를 벨 수 있을 때
            if field[nr][nc] == 'T':
                if cut > 0:
                    visited[nr][nc] = True
                    # 현재비용 + 전진(1) + 회전비용 + 나무베기(1)
                    dfs(cur_val + 1 + turn_cost, nr, nc, cut - 1, i)
                    visited[nr][nc] = False
            
            # 평지나 도착점일 때 (나무가 아닐 때)
            else:
                visited[nr][nc] = True
                # 현재비용 + 전진(1) + 회전비용
                dfs(cur_val + 1 + turn_cost, nr, nc, cut, i)
                visited[nr][nc] = False
            

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    field = [list(input()) for _ in range(N)]
    # print(field)
    min_val = float('inf')
    visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if field[r][c] == 'X':
                dfs(0, r, c, K, 0)
                break
    if min_val == float('inf'):
        min_val = -1
    print(f'#{tc} {min_val}')