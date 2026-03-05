# 방향을 오른쪽과 아래만으로 지정함.
# 처음 위치를 지정 후에 이동 방향으로 1씩 증가하면서 이동
# 최대 최소를 비교함.
# 벽 충돌여부도 확인 ㄱㄱ
import sys
sys.stdin = open('swea_5188_최소합.txt')
dr = [0, 1]
dc = [1, 0]
def dfs(r, c, sum_val):
    global min_val

    if sum_val > min_val: # 가지치기
        return
    if r == N-1 and c == N-1: # 끝에 도달
        min_val = min(min_val, sum_val)
        return

    for i in range(2):
        nr, nc = r + dr[i], c + dc[i]
        if 0<= nr < N and 0<= nc < N: # 벽 충돌
            # 재귀
            dfs(nr, nc, sum_val + arr[nr][nc])
            
            

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_val = float('inf')
    # 출발점을 미리 찍고 시작
    dfs(0, 0, arr[0][0])
    print(f'#{tc} {min_val}')