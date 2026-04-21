# D : 두께(세로), W : 가로, K : 합격기준
# A : 0, B : 1
# 같은 알파벳이 K개 이상 연속적으로 존재할때 통과함.
# 약품을 사용하면 가로줄이 모두 같은 알파벳으로 변경됨.
# 성능 검사를 통과하기 위한 최소 약품 사용 개수
# 약품 검사 안 해도 통과하는 경우는 0을 출력


import sys
sys.stdin=open('swea_2112_보호 필름.txt')

def dfs(idx, cur_val):
    global min_val
    # 가지치기
    if cur_val >= min_val:
        return
    # 두께를 다 돌았으면 최솟값 갱신
    if idx == D:
        if check():
            min_val = min(min_val, cur_val)
        return
    # 약품 안 넣었을때
    dfs(idx + 1, cur_val)
    # 원래 상태 저장
    original_row = film[idx][:]
    # A약품 사용
    film[idx] = [0] * W
    dfs(idx + 1, cur_val + 1)
    # B약품 사용
    film[idx] = [1] * W
    dfs(idx + 1, cur_val + 1)
    # 복구
    film[idx] = original_row

def check():
    for c in range(W):
        max_cnt = 1
        cnt = 1
        # 1 인덱스부터 시작
        for r in range(1, D):
            if film[r][c] == film[r-1][c]:
                # 연속되면 카운트 재기
                cnt += 1
            else:
                cnt = 1
            # K개 이상 연속되면
            if cnt >= K:
                # 달성 조건(max_cnt 갱신)
                max_cnt = cnt
                break
        # 달성 조건 못 다다르면
        if max_cnt < K:
            # 충족 X
            return False
    # 충족 0
    return True
    
T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    # 1인 경우 무조건 성공이므로
    if K == 1:
        print(f'#{tc} 0')
        continue
    # 나올수 있는 최대가 K임.
    min_val = K
    dfs(0, 0)
    
    print(f'#{tc} {min_val}')
