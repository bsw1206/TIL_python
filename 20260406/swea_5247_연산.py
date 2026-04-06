import sys
sys.stdin = open('swea_5247_연산.txt')
from collections import deque
def bfs(start, end):

    # 시작 값과 계산 횟수 저장(처음엔 0회)
    q = deque([(start, 0)])

    visited = set([start]) # 방문된 숫자를 계산하고 중복 계산 방지

    while q:

        num, cnt = q.popleft()

        if num == end:
            return cnt

        next_cnt = cnt + 1


        # 4가지 연산에 대한 경우를 모두 생각함. 따라서 next_num을 새로 정의해야 됨.
        # 더하기 1
        next_num = num + 1
        # 숫자 범위에 해당 여부, 계산한 숫자 확인 여부
        
        # 더하기 1
        if 1 <= next_num <= 1e6 and next_num not in visited:
            visited.add(next_num)
            q.append((next_num, next_cnt))
        
        # 빼기 1
        next_num = num - 1
        if 1 <= next_num <= 1e6 and next_num not in visited:
            visited.add(next_num)
            q.append((next_num, next_cnt))
        
        # 고바기 2
        next_num = num * 2
        if 1 <= next_num <= 1e6 and next_num not in visited:
            visited.add(next_num)
            q.append((next_num, next_cnt))
        
        # 빼기 10
        next_num = num - 10
        if 1 <= next_num <= 1e6 and next_num not in visited:
            visited.add(next_num)
            q.append((next_num, next_cnt))


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = bfs(N, M)
    
    
    print(f'#{tc} {result}')