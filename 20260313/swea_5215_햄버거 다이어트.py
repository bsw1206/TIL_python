import sys
sys.stdin = open('swea_5215_햄버거 다이어트.txt')

# 햄버거의 맛은 최대한 유지하면서 정해진 칼로리를 넘지 않는 햄버거를 주문하여 먹으려 함.
# 가장 맛에 대한 점수가 높은 햄버거의 점수를 출력

def dfs(idx, cur_score, cur_cal):
    global max_score

    if cur_cal > L:
        return
    if idx == N:
        max_score = max(max_score, cur_score)
        return

    score, cal = arr[idx][0], arr[idx][1]

    dfs(idx + 1, cur_score + score, cur_cal + cal)

    dfs(idx + 1, cur_score, cur_cal)

T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_score = 0

    dfs(0, 0, 0)

    print(f'#{tc} {max_score}')