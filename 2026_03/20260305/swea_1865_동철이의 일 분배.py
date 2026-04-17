# N명의 직원, 해야할 일 N개
# 직원들 번호 : 1~N, 해야할 일 번호 : 1~N
# i번 직원이 j번 일을 하면 성공할 확률? Pi,j
# 주어진 일이 모두 성공할 확률의 최댓값 구하기
# N개의 줄의 i번째 줄에 i번째 사람이 일을 할때 성공할 확률을 나열함.

# 일을 했는지 안 했는지 여부를 나타낼 확인 리스트 제작
# for 문을 돌면서 숫자의 / 100 을 합계 리스트에 담음.
# 다시 함수를 돌기
# 최댓값을 0으로 지정해놓고
# 만약에 확인리스트에 False가 없으면 최댓값 비교
import sys
sys.stdin = open('swea_1865_동철이의 일 분배.txt')
def dfs(cnt, sum_val):
    global max_val
    
    if sum_val <= max_val:
        return 
    
    if cnt == N:
        max_val = max(max_val, sum_val)
        return

    
    for j in range(N):
        if not check_lst[j]:
            
            check_lst[j] = True
            
            dfs(cnt + 1, sum_val * (work_lst[cnt][j] / 100))
    
            check_lst[j] = False
        



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    work_lst = [list(map(int, input().split())) for _ in range(N)]
    check_lst = [False] * N
    max_val = 0
    dfs(0, 1)
    result = max_val * 100
    print(f'#{tc}', f"{result:.6f}")