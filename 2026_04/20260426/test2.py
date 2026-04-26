from collections import deque
def bfs(node):
    q = deque([node])

    visited[node] = True
    print(node, end=' ')
    while q:
        cur_node = q.popleft()

        for neighbor in adj_lst[cur_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
                print(neighbor, end= ' ')
import sys
sys.stdin = open('input.txt')
V, E = map(int, input().split())
n_lst = list(map(int, input().split()))
adj_lst = [[] for _ in range(V + 1)]
for i in range(E):
    p1, p2 = n_lst[i * 2], n_lst[i * 2 + 1]
    adj_lst[p1].append(p2)
    adj_lst[p2].append(p1)
visited = [False] * (V + 1)
bfs(1)
print()