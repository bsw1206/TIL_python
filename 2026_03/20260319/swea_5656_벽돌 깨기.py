# 벽돌을 깨는 게임을 한다.
# N번 쏠 수 있고, W * H 배열로 주어짐.
# 가운데 포함해서 상하좌우 idx-1만큼 벽돌이 제거됨.

# 밑으로 떨어지는 함수를 정의
# 4방향으로 갈라지는 함수를 정의
# 최적의 경우를 생각하는 함수를 정의

# 벽돌의 개수를 파악하는 cnt, 델타 값, if문 : arr[r][c]에서 0이 아닌 수를 만났을 때
# 남아있는 최소의 벽돌 수를 구하기
# 현재 벽돌이 다 깨지면 더 이상 할 필요 없다.
import sys
sys.stdin = open('swea_5656_벽돌 깨기.txt')

from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# depth : 4
# branch : 12
def recur(cnt, remain_blocks, now_arr):
    global min_val
    if cnt == N or remain_blocks == 0:
        min_val = min(min_val, remain_blocks)
        return
    
    for col in range(W):
        # 연쇄 작용
        # col에 구슬을 쏘기 전 상태를 복사
        # 복사된 리스트의 col 자리에 구슬을 떨군다
        
        copy_arr = [row[:] for row in now_arr]
        row = -1
        for r in range(H):
            if copy_arr[r][col]:
                row = r # 폭발이 시작되는 점
                break
        if row == -1: # 벽돌 발견하지 못했을 경우
            continue 
        
        q = deque([(row, col, copy_arr[row][col])]) # 연쇄작용 고려하여 갯수도 같이 가져야 함.
        now_reamin_blocks = remain_blocks - 1 # 남아있는 벽돌
        copy_arr[row][col] = 0

        # 주변 벽돌을 파괴
        while q:
            r, c, p = q.popleft()
            
            for k in range(1, p):
                for i in range(4):
                    nr, nc = r + k * dr[i], c + k * dc[i]
                    # 범위 밖이면 pass
                    if nr < 0 or nr >= H or nc < 0 or nc >= W:
                        continue
                    # 벽돌이 없으면 pass
                    if copy_arr [nr][nc] == 0:
                        continue
                    q.append((nr, nc, copy_arr[nr][nc]))
                    copy_arr[nr][nc] = 0
                    now_reamin_blocks -= 1
        # 빈칸 메우기
        for c in range(W): # 가로 다 보기
            idx = H -1 # 맨 아래
            for i in range(H - 1, -1, -1):
                if copy_arr[i][c]: # 벽돌이 있다면
                    copy_arr[i][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[i][c] # 위치 바꾸기
                    idx -= 1 # 인덱스 바꾸기

        # 다음 구슬로 이동
        recur(cnt + 1, now_reamin_blocks, copy_arr)

T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_val = 1e9
    blocks = 0
    for r in range(H):
        for c in range(W):
            if arr[r][c]:
                blocks += 1
    recur(0, blocks, arr)

    print(f'#{tc} {min_val}')
    