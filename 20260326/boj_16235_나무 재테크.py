# N * N
# (r,c) , r과 c는 1부터 시작한다.
# S2D2 : 칸에 들어있는 양분을 조사하여 상도에게 전송하고, 모든 칸에 대해서 조사함.
# M개의 나무를 구매해 땅에 심음. 1칸에 여러 개의 나무 잇을 수 있음.
# 봄에는 나이가 1증가, 1칸에 여러 개의 나무가 있으면, 나이가 어린 나무부터 양분을 먹는다. / 땅에 양분이 없으면 바로 죽음.
# 여름에는 봄에 죽은 나무가 양분으로 변한다. 죽은 나무의 나이를 2로 나눈 값이 양분으로 추가됨. 소수점 아래는 버림.
# 가을에는 나무가 번식, 번식하는 나무는 나이가 5의 배수, 인접한 8개의 칸에는 나이가 1인 나무가 생김. 
# 겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가, 양분의 양은 주어짐.
# K년이 지난 후 살아있는 나무의 개수는?
# tree_info의 [0, 1]은 나무의 위치(x, y)의미, 마지막 정수는 나무의 나이
# N은 간격, M은 나무의 수, K는 총 지나간 연수
# 나무를 어디다 심을지 정하기
# 사계절 마다 조건 정하기(0,1,2,3반복)-> 
import sys
sys.stdin = open('boj_16235_나무 재테크.txt')
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
    # 봄, 여름
    for r in range(N):
        for c in range(N):
            if tree_info[r][c]:
                survived_trees = deque()
                dead_tree = 0
                for age in tree_info[r][c]:
                    # 양분 충분한가?
                    if grid[r][c] >= age:
                        grid[r][c] -= age
                        # 나이 먹음
                        survived_trees.append(age + 1)
                    else: 
                        # 죽이고 양분 주기
                        dead_tree += age // 2
                
                tree_info[r][c] = survived_trees
                # 양분 주기
                grid[r][c] += dead_tree

    # 가을
    for r in range(N):
        for c in range(N):
            if tree_info[r][c]:
                for age in tree_info[r][c]:
                    if age % 5 == 0:
                        for i in range(8):
                            nr, nc = r + dr[i], c + dc[i]
                            if 0<= nr < N and 0<= nc < N:
                                # 아기 나무 심기
                                tree_info[nr][nc].appendleft(1)
            # 겨울 : 양분 추가                    
            grid[r][c] += arr[r][c]
            
result = 0
for r in range(N):
    for c in range(N):
        result += len(tree_info[r][c])
print(result)