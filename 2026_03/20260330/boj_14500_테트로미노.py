import sys
sys.stdin = open('boj_14500_테트로미노.txt')

# 정사각형 4개 이어 붙인 "테트로미노"
# N*M종이에 테트로미노 하나 놓기
# 테트로미노 하나를 놓아서 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램 작성
# 회전이나 대칭도 가능
# 회전, 대칭하는 경우 -> 각각 4가지 : 총 20가지
# 총 5가지의 
# for i in range(5):
# arr
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def 볼록할철(r, c):
    global max_val
    
    for i in range(4):
        tmp_total = arr[r][c]
        is_valid = True
        for j in range(4):
            if i == j:
                continue
            nr = r + dr[j]
            nc = c + dc[j]

            if 0<= nr < N and 0<= nc < M:
                tmp_total += arr[nr][nc]
            else:
                is_valid = False
                break
        if is_valid:
            max_val = max(max_val, tmp_total)

def tetromino(idx, sum_val, r, c):
    global max_val
    
    if idx == 4:
        max_val = max(max_val, sum_val)
        return
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0<= nr < N and 0<= nc < M and not visited[nr][nc]:
            visited[nr][nc] = True
            tetromino(idx + 1, sum_val + arr[nr][nc], nr, nc)
            visited[nr][nc] = False
            
N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
max_val = 0

for r in range(N):
    for c in range(M):
        visited[r][c] = True
        tetromino(1, arr[r][c], r, c)
        visited[r][c] = False
        볼록할철(r, c)
print(max_val)
