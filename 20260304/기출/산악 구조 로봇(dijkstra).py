import heapq
import sys
sys.stdin = open('산악 구조 로봇.txt')
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dijkstra():
    distance = [[float('inf')] * N for _ in range(N)]

    distance[0][0] = 0

    q = [(0, 0, 0)]

    while q:
        c_cost, r, c = heapq.heappop(q) # q에서 가장 누적 비용이 적은 위치를 꺼낸다.
        # heappop 자체가 튜플의 첫 요소인 숫자에서 가장 작은 값을 반환함.
        # 그래서 c_cost의 위치를 무조건 맨 앞에 해야 함!
        # heappush를 할 때에도 new_cost위치를 고정시켜야 함.
        if c_cost > distance[r][c]: # 예전에 큐에 넣었던 자료이면 continue
            continue    

        if r == N-1 and c == N-1: # 목적지에 도착시 바로 종료!
            return c_cost
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0<= nr < N and 0 <= nc < N:
                if ground[nr][nc] > ground[r][c]:
                    cost = (ground[nr][nc] - ground[r][c]) * 2
                    
                elif ground[nr][nc] == ground[r][c]:
                    cost = 1
                else:
                    cost = 0
                
                new_cost = c_cost + cost
                
                if distance[nr][nc] > new_cost:
                    distance[nr][nc] = new_cost
                    heapq.heappush(q, (new_cost, nr, nc))
    return distance[N-1][N-1]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ground = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {dijkstra()}')