# N개의 구역, 1~N까지 번호가 매겨져 있음.
# 구역을 두 개의 선거구로 나눈다, 각 구역은 두 선거구 중 하나에 포함되어야 함.
# 한 선거구에 포함되는 구역은 모두 연결되어야 함.
# 인구 차이의 최솟값을 구하기.


# 연결되어 있지 않는 조건을 생각
# 나누는 경우를 생각
# 인구 차이의 최솟값을 찾는 경우를 생각

from itertools import combinations
import sys
from collections import deque
sys.stdin = open('boj_17471_게리맨더링.txt')

def check_group(group):
    if not group: # 연결 되지 않음.
        return False
    q = deque([group[0]])
    visited = [0] * (N + 1)
    visited[group[0]] = True # 시작점은 방문
    count = 1

    while q:
        node = q.popleft() 
        for neighbor in arr[node]:
            if neighbor in group and not visited[neighbor]: # 연결 되어있고 방문하지 않은 경우
                visited[neighbor] = True
                q.append(neighbor)
                count += 1
    if count == len(group): # 그룹 수에 도달하면
        return True 


N = int(input())
arr = [[] for _ in range(N + 1)]
p_lst = [0] + list(map(int, input().split()))
for i in range(1, N + 1):
    n_lst = list(map(int, input().split()))
    for j in range(1, len(n_lst)):
        arr[i].append(n_lst[j])
min_val = float('inf') # 최솟값 지정
num = list(range(1, N + 1))
for a in range(1, N + 1):
    for b in combinations(num, a): # 나눌 수 있는 모든 경우
        b = list(b)
        d = [x for x in num if x not in b] # 전체 범위에서 b를 제외한 리스트
        # 여기에 서로 연결되는 코드를 써야 할거 같은데,
        # 그리고 나눌 수 없는 경우에 -1을 쓰는 코드도 필요
        if check_group(b) and check_group(d): # 둘다 가능한 경우인지
            b_sum, d_sum = 0, 0
            for i in b:
                b_sum += p_lst[i]
            for j in d:
                d_sum += p_lst[j]
            sub_val = abs(d_sum - b_sum)
            min_val = min(min_val, sub_val)
if min_val == float('inf'): # 연결을 못하는 경우
    print(-1)
else:
    print(min_val)
