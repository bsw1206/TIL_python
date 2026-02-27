import sys
sys.stdin = open('swea_1227_미로2.txt')
sys.setrecursionlimit(10000)
def dfs(r, c, finish):
    if (r, c) == finish:
        return True
    
    maze[r][c] = 1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0<= nr < 100 and 0<= nc < 100 and maze[nr][nc] != 1:
            if dfs(nr, nc, finish):
                return 1
    return 0





for _ in range(1, 11):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(100)]
    
    for r in range(100):
        for c in range(100):
            if maze[r][c] == 3:

                print(f'#{tc} {dfs(1, 1, (r, c))}')
                break