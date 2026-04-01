import sys

from collections import deque

def bfs(S):

    q = deque([S])
    possible_car = [S]

    left_idx, right_idx = S, S

    while q:
        current_car = q.popleft()
        current_loc = location[current_car]
        current_fuel = fuel[current_car]

        min_reach = current_loc - current_fuel
        max_reach = current_loc + current_fuel

        while left_idx > 1 and location[left_idx-1] >= min_reach:
            
            left_idx -= 1

            if not visited[left_idx]:
                visited[left_idx] = True
                q.append(left_idx)
                possible_car.append(left_idx)

        while right_idx < N and location[right_idx + 1] <= max_reach:
            
            right_idx += 1

            if not visited[right_idx]:
                visited[right_idx] = True
                q.append(right_idx)
                possible_car.append(right_idx)
    possible_car.sort()
    return possible_car


N, S = map(int, input().split())
location = [0] + list(map(int, input().split()))
fuel = [0] + list(map(int, input().split()))
visited = [False] * (N + 1)
visited[S] = True
print(*bfs(S))