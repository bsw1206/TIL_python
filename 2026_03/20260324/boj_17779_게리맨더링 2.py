import sys
sys.stdin = open('boj_17779_게리맨더링 2.txt')


def check_val(x, y, d1, d2):
    # 1. 마름모의 꼭짓점들이 격자(N x N)를 벗어나는지 확인
    # 맨 아래 꼭짓점의 행(x + d1 + d2)이 N을 넘어가면 안 됨
    if x + d1 + d2 >= N:
        return float('inf')
    # 왼쪽 꼭짓점과 오른쪽 꼭짓점의 열이 범위를 벗어나면 안 됨
    if y - d1 < 0 or y + d2 >= N:
        return float('inf')

    # 구역별 인구수를 누적할 리스트 (매번 sum()을 하는 것보다 빠릅니다)
    sum_val = [0, 0, 0, 0, 0] 

    for r in range(N):
        for c in range(N):
            # 5번 구역 (작성하신 훌륭한 수식 그대로 사용!)
            if (x + y <= r + c <= x + y + 2 * d2) and (x - y <= r - c <= x - y + 2 * d1):
                sum_val[4] += arr[r][c]
            # 1번 구역
            elif 0 <= r < x + d1 and 0 <= c <= y:
                sum_val[0] += arr[r][c]
            # 2번 구역
            elif 0 <= r <= x + d2 and y < c < N:
                sum_val[1] += arr[r][c]
            # 3번 구역
            elif x + d1 <= r < N and 0 <= c < y - d1 + d2:
                sum_val[2] += arr[r][c]
            # 4번 구역
            elif x + d2 < r < N and y - d1 + d2 <= c < N:
                sum_val[3] += arr[r][c]
            
    return max(sum_val) - min(sum_val)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_val = float('inf')

# 완전 탐색 진행
for x in range(N):
    for y in range(N):
        # d1, d2는 반드시 1 이상이어야 함
        for d1 in range(1, N): 
            for d2 in range(1, N):
                min_val = min(min_val, check_val(x, y, d1, d2))

print(min_val)