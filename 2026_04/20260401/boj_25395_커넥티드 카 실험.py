# 1부터 N까지 번호가 매겨진 N대의 카를 일렬로 배치, i번 커넥티드 카의 초기 위치와 연료량 제공
# 1만큼의 연료로 1만큼 거리 이동 가능, 연료 모두 소비시 이동할 수 없음.
# 사물에 연결될 가능성이 있는 카를 전부 구해보기
# S번 카를 사물 인터넷에 먼저 연결 -> 다른 카에게 사물 인터넷 전파 목적


# 위치와 연료량이 순서대로 제공되는데, 
# 그러면 i번째 차의 위치와 연료량을 더한 것이 i+1번째 차의 위치보다 작으면 결과값에서 제외
# 또한 i번째 차의 위치에서 연료량을 뺐을 때 i-1번째 차의 위치보다 크면 i-1을 결과값에서 제외
# 아니면 결과값에 S를 미리 추가해놓고, while not result라는 조건을 걸어서 앞뒤가 
import sys
sys.stdin = open('boj_25395_커넥티드 카 실험.txt')
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