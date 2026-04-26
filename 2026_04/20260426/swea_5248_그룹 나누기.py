import sys
sys.stdin = open('swea_5248_그룹 나누기.txt')
from collections import deque

def bfs(node):
    q = deque([node]) 
    visited[node] = True
    while q:
        cur_node = q.popleft()
        for neighbor in adj_lst[cur_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor) 
T = int(input()) 
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    m_lst = list(map(int, input().split()))

    adj_lst = [[] for _ in range(N + 1)]

    for i in range(M):
        p1, p2 = m_lst[i * 2], m_lst[i * 2 + 1]
        adj_lst[p1].append(p2)
        adj_lst[p2].append(p1)
    visited = [False] * (N + 1)

    cnt = 0

    for i in range(1, N + 1):
        if not visited[i]:
            cnt += 1

            bfs(i)
    print(f'#{tc} {cnt}')