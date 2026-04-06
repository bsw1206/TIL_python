import sys
input = sys.stdin.readline
from collections import deque
def bfs(start, end):
    
    q = deque([start])
    
    visited = [-1] * 100001
    visited[start] = 0
    n_lst = [-1] * 100001
    while q:
        num = q.popleft()

        
        

        if num == end:
            cnt = visited[num]
            path = []
            temp = num
            while temp != -1:
                path.append(temp)
                temp = n_lst[temp]
            path.reverse()
            return cnt, path
        
        for next_num in (num - 1, num + 1, num * 2):
            if 0<= next_num <= 100000 and visited[next_num] == -1:
                visited[next_num] = visited[num] + 1
                n_lst[next_num] = num
                q.append((next_num))

      

N, K = map(int, input().split())
cnt, move_lst = bfs(N, K)
print(cnt)
print(*move_lst)