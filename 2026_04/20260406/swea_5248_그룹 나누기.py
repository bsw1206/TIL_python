import sys
sys.stdin = open('swea_5248_그룹 나누기.txt')
from collections import deque
def bfs(cur_node):

    q = deque([cur_node])
    visited[cur_node] = True
    while q:
        node = q.popleft()

        for neighbor in adj_lst[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)



T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    n_lst = list(map(int, input().split()))

    # 인접 리스트
    adj_lst = [[] for _ in range(N + 1)]
    
    for i in range(M):
        p1, p2 = n_lst[2 * i], n_lst[2 * i + 1]
        # 서로 추가하는 방식
        adj_lst[p1].append(p2)
        adj_lst[p2].append(p1)
    # 방문여부 파악
    visited = [False] * (N + 1)
    # 출력값
    cnt = 0

    for i in range(1, N + 1):
        # 새로운 그룹 발견하면 cnt 추가
        if not visited[i]:
            cnt += 1

            bfs(i)
    
    print(f'#{tc} {cnt}')