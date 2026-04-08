dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

ans = 0
result = False
while not result:
    # 1번 수행
    if grid[r][c] == 0:
        grid[r][c] = 2
        ans += 1
    # 2, 3번 확인 여부
    check = False
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        # 청소할 벽 찾았을 때
        if grid[nr][nc] == 0:
            check = True
            break
    # 2번 수행(청소되지 않은 빈 칸 없는 경우)
    if not check:
        back_r, back_c = r - dr[d], c - dc[d]
        if back_r < 0 or back_r >= N or back_c < 0 or back_c >= M or grid[back_r][back_c] == 1:
            result = True
            break
        r, c = back_r, back_c
    # 3번 수행(청소되지 않은 빈 칸이 존재)
    else:
        
        d -= 1
        if d == -1:
            d = 3       
        next_r, next_c = r + dr[d], c + dc[d]
        if 0 <= next_r < N and 0 <= next_c < M:
            if grid[next_r][next_c] == 0:
                r, c = next_r, next_c
                    
print(ans)