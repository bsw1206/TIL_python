# N개의 숫자가 적힌 게임 판 존재, 연산자 카드를 끼워넣어 다양한 결과값을 구해보기
# 연산자의 우선순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산함 !!
# 주어진 연산자 카드를 사용하여 수식을 계산할 때
# 그 결과가 최대가 되는 수식과 최소가 되는 수식을 찾고, 두 값의 차이를 출력하기!!

def dfs(idx, p, mi, mu, d, cal_val):
    global max_val, min_val

    # 계산 횟수가 끝나면 최댓값, 최솟값 갱신
    if idx == N:
        max_val = max(max_val, cal_val)
        min_val = min(min_val, cal_val)
        return
    
    # 여기서는 4가지 연산 종류를 독립적인 상황으로 분류하고 재귀를 사용하므로 4개의 if가 필요함.
    if p > 0:
        dfs(idx + 1, p-1, mi, mu, d, cal_val + n_lst[idx])
    if mi > 0:
        dfs(idx + 1, p, mi-1, mu, d, cal_val - n_lst[idx])
    if mu > 0:
        dfs(idx + 1, p, mi, mu-1, d, cal_val * n_lst[idx])
    if d > 0:
        dfs(idx + 1, p, mi, mu, d-1, int(cal_val / n_lst[idx]))






import sys
sys.stdin = open('swea_4008_숫자 만들기.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    

    p, mi, mu, d = map(int, input().split())
    n_lst = list(map(int, input().split()))

    # 연산 값이 -1억이상 1억 이하이므로 초기 최대, 최솟값을 다음과 같이 지정
    max_val = -10e8
    min_val = 10e8
    # 초기 인덱스는 1, n_lst의 첫번째 수를 들고 감.
    dfs(1, p, mi, mu, d, n_lst[0])
    print(f'#{tc} {max_val - min_val}')