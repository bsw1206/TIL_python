# BFS로 한번 풀어봐야겠다.
# 일단 인접 행렬을 만들자.

# tree의 홀수 부분을 쭉 돌면서
# N 값과 같은 값을 발견하면
# 그 부분의 인덱스를 저장해.

# 그리고 다시 돌면서
# 

# 

import sys
sys.stdin = open('swea_5174_subtree.txt')
from collections import deque


def bfs(start_n):
    cnt = 0

    q = deque([start_n])

    while q:
        
        n = q.popleft()
        cnt += 1

        if left[n] != 0:
            q.append(left[n])
        if right[n] != 0:
            q.append(right[n])
    return cnt



T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    tree = list(map(int, input().split()))
    
    V = max(tree)

    left = [0] * (V + 1)
    right = [0] * (V + 1)
    for i in range(E):
        p, c = tree[i * 2], tree[i * 2 + 1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
    print(f'#{tc} {bfs(N)}')