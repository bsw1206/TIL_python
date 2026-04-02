import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 1. 2차원 누적 합 배열 생성 (N+1 x N+1 크기로 패딩)
dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        # (1,1)부터 (i,j)까지의 누적 합 계산
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

# 2. M개의 쿼리 처리
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    
    # 누적 합 배열을 이용해 O(1)의 속도로 구간 합 도출
    ans = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(ans)