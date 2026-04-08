
from collections import deque
for tc in range(1, 11):
    N, S = map(int, input().split())
    p_lst = list(map(int, input().split()))
    adj_lst = [[] for _ in range(101)]

    for i in range(N // 2):

        fm = p_lst[i * 2]
        to = p_lst[i * 2 + 1]

        if to not in adj_lst[fm]:
            adj_lst[fm].append(to)

    visited = [0] * 101
    q = deque([S])
    
    
    
    while q:

        node = q.popleft()

        for next_node in adj_lst[node]:
            if not visited[next_node]:
                visited[next_node] = visited[node] + 1
                q.append(next_node)
    max_time = 0
    

    for j in range(1, 101):
        if visited[j] > max_time:
            max_time = visited[j]
    ans_lst = []
    for k in range(101):
        if visited[k] == max_time:
            ans_lst.append(k)


    print(f'#{tc} {max(ans_lst)}')
    