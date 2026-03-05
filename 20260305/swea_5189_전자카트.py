
import sys
sys.stdin = open('swea_5189_전자카트.txt')

def dfs(current_loc, sum_val, cnt):
    global min_val

    if sum_val >= min_val: # 가지치기
        return
    if cnt == N - 1:
        # 사무실로 돌아왔을 때의 합계로 더함.
        sum_val += arr[current_loc][0]
        min_val = min(min_val, sum_val)
        return

    for i in range(1, N):
        if not visited[i]:
		        # 방문 여부 파악
            visited[i] = True
            dfs(i, sum_val + arr[current_loc][i], cnt + 1)
            visited[i] = False
            

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_val = float('inf')
    visited = [False] * N
    
    # 출발점을 미리 찍고 시작
    dfs(0, 0, 0)
    print(f'#{tc} {min_val}')