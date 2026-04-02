from collections import deque
dr = [-1, 1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, -1, 1, -1, 1, 1, -1]
N, M, K = map(int, input().split())
grid = [[5] * N for _ in range(N)]
arr = [list(map(int, input().split())) for _ in range(N)]
tree_info = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, age = map(int, input().split())
    tree_info[r-1][c-1].append(age)


for year in range(K):
    for r in range(N):
        for c in range(N):
            if tree_info[r][c]:
                survived_trees = deque()
                dead_tree = 0
                for age in tree_info[r][c]:
                    if grid[r][c] >= age:
                        grid[r][c] -= age
                        survived_trees.append(age + 1)
                    else: 
                        dead_tree += age // 2
                tree_info[r][c] = survived_trees
                grid[r][c] += dead_tree
    for r in range(N):
        for c in range(N):
            if tree_info[r][c]:
                for age in tree_info[r][c]:
                    if age % 5 == 0:
                        for i in range(8):
                            nr, nc = r + dr[i], c + dc[i]
                            if 0<= nr < N and 0<= nc < N:
                                tree_info[nr][nc].appendleft(1)
            grid[r][c] += arr[r][c]
            
result = 0
for r in range(N):
    for c in range(N):
        result += len(tree_info[r][c])
print(result)