# 컴퓨터를 연결하는 비용을 최소로 해야 함.
import heapq
import sys
sys.stdin = open('boj_1922_네트워크 연결.txt')

def prim(start_node):


    pq = ([(0, start_node)])
    total_price = 0
    

    while pq :
        
        cur_price , node = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = True
        
        total_price += cur_price

        for next_price, next_node in adj_lst[node]:
            if not visited[next_node]:
                heapq.heappush(pq, (next_price, next_node))
    return total_price
        

N = int(input())
M = int(input())
adj_lst = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(M):
    p1, p2, price = map(int, input().split())
    adj_lst[p1].append((price, p2))
    adj_lst[p2].append((price, p1))
    
print(prim(1))



