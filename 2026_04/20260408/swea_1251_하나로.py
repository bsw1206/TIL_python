# E과 각 해저터널의 길이L의 제곱의 곱 (E * L^2)만큼 지불
import sys
sys.stdin = open('swea_1251_하나로.txt')
from heapq import heappush, heappop

def prim(tax):

    pq = [(0, 0)] # 0번 노드부터 MST 구성

    visited = [0] * N # 방문 여부 확인
    
    min_cost = 0

    

    while pq:

        cost, node = heappop(pq)

        if visited[node]:
            continue
        
        visited[node] = 1
        
        min_cost += cost
        

        # 모든 섬에 다 연결될 수 있으므로
        for next_node in range(N):
            if visited[next_node]:
                continue

            # 거리 계산 필요함.
            
            next_cost = (((x_lst[next_node] - x_lst[node]) ** 2) +  ((y_lst[next_node] - y_lst[node]) ** 2)) * tax

            heappush(pq, (next_cost, next_node))

    return round(min_cost)


T = int(input())
for tc in range(1, T + 1):
    
    N = int(input())
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    tax = float(input())

    min_val = prim(tax)
    print(f'#{tc} {min_val}')