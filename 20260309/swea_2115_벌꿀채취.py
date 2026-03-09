# 벌꿀 양이 주어짐.
# 두 명의 일꾼이 존재
# 벌통의 수 M이 주어질 때, 각각의 일꾼은 가로로 연속되도록 M개의 벌통을 선택함.
# 선택한 벌통에서 꿀을 채취할 수 있음. 그러나 서로 벌통이 겹치면 안됨.
# 하나의 벌통에서 채취한 꿀은 하나의 용기에 담아야 함.
# 두 일꾼이 채취할 수 있는 꿀의 최대 양은 C이다.
# 꿀의 양의 제곱만큼 수익이 생김.
# 수익의 합이 최대가 되는 경우를 찾고, 그 때의 최대 수익을 출력하는 코드 작성

# 이건 일단 슬라이싱을 통해서 M,C를 고려해 최대가 되는 수익을 미리 표시하는 것이 좋을 듯 한데
# N-M+1 * N 범위의 값을 생성해서 각 시작 위치에서 벌꿀을 담았을 때 발생하는 최대 수익을 미리 저장
# 그리고 벌꿀 통을 배치하는 경우를 생각
# 가지치기도 해줘야 할듯 하고, 
# 현재 인덱스와, 현재 벌꿀의 양, 현재의 수익을 변수로 삼음.
# for문을 돌려야 하나.
# 

# 리스트 겹치면 안되는 것은 어떻게 생각할 수 있을까?
# 그냥 안 겹치는 경우를 생각해볼까?
# 

def find_max_honey_sum(idx, cur_honey, cur_honey_profit):
    global max_honey_profit
    # 최대 담을 수 있는 꿀의 양보다 많아지면 다시 돌아감
    if cur_honey > C:
        return
    # 현재 인덱스 위치가 벌통의 크기에 도달하면
    if idx == len(honey_lst):
        # 최대 이익값을 갱신
        max_honey_profit = max(max_honey_profit, cur_honey_profit)
        return
    # 현재 인덱스의 꿀의 양을 추가하는 경우
    find_max_honey_sum(idx + 1, cur_honey + honey_lst[idx], cur_honey_profit + honey_lst[idx] ** 2)
    # 추가하지 않는 경우
    find_max_honey_sum(idx + 1, cur_honey, cur_honey_profit )
    
    
import sys
sys.stdin = open('swea_2115_벌꿀채취.txt')
T = int(input())
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total_max_val = 0
    max_honey_lst = [[0] * (N - M + 1) for _ in range(N)]
    # 각 벌통에 담을 수 있는 최대의 꿀을 담을 리스트
    for r in range(N):
        for c in range(N - M + 1):
            # 벌통의 크기
            honey_lst = arr[r][c : c + M]
            # 최댓값 미리 지정
            max_honey_profit = 0
            # DFS 돌리기
            find_max_honey_sum(0, 0, 0)
            # 리스트에 최대 이익을 남기는 경우를 추가
            max_honey_lst[r][c] = max_honey_profit
    for r1 in range(N):
        for c1 in range(N-M+1):
            # 일꾼 1의 수익
            p1 = max_honey_lst[r1][c1]
            # 여기서 일꾼 2는 무조건 일꾼 1의 뒤에 올 수 밖에 없는데
            # 어차피 일꾼 1이 처음부터 돌기 때문에
            # 일꾼의 순서가 중요하지 않은 이번 경우는 상관이 없음. 
            for r2 in range(r1, N):
                s_c2 = 0
                if r1 == r2: # 일꾼 1, 2의 벌통의 행이 같은 경우
                    # c2의 시작위치를 c1과 겹치지 않게 설정
                    s_c2 = c1 + M
                    # c2를 다음과 같이 설정
                    for c2 in range(s_c2, N - M + 1):
                        # 일꾼 2의 수익
                        p2 = max_honey_lst[r2][c2]
                        # 출력 결과값을 갱신
                        total_max_val = max(total_max_val, p1 + p2)
                else: # 행이 겹치치 않는 경우
                    for c2 in range(N- M + 1): # 열의 전 범위 순회
                        p2 = max_honey_lst[r2][c2]
                        total_max_val = max(total_max_val, p1 + p2) # 갱신
    print(f'#{tc} {total_max_val}')


