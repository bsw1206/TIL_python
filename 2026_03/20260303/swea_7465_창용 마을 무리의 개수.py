import sys
sys.stdin = open('swea_7465_창용 마을 무리의 개수.txt')
from collections import deque

def bfs(i):
    visited[i] = True # 방문 처리
    q = deque([i]) # queue 지정

    while q:
        cur = q.popleft() # 제일 왼쪽 변수 뽑음.
        for neighbor in data[cur]: # 현재 위치의 연결되어 있는 곳을 돌기.
            if not visited[neighbor]: # 방문하지 않은 곳이면?
                visited[neighbor] = True # 방문처리
                q.append(neighbor) # 연결된 곳에서 다시 그 사람과 연결된 사람을 찾기

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [[] for _ in range(N + 1)]
    for i in range(M):
        p1, p2 = map(int, input().split())
        data[p1].append(p2)
        data[p2].append(p1)
        # 인접 리스트 만드는 중
    visited = [False] * (N + 1) # 방문 여부 파악하는 리스트
    group_cnt = 0 # group개수 파악

    for i in range(1, N + 1):
        if not visited[i]: # 아직 방문하지 않은 곳이면 카운트 1 더함.
            group_cnt += 1
            bfs(i) 
    print(f'#{tc} {group_cnt}')

