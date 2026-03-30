# N * N 2차원 리스트에서 (x1,y1)부터 (x2,y2)까지 합을 구하는 프로그램 작성.
import sys
sys.stdin = open('boj_11660_구간 합 구하기5.txt')
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# for i in range(M):
#     X1, Y1, X2, Y2 = map(int, input().split())
    
        
#     x1, y1, x2, y2 = X1 - 1, Y1 - 1, X2 - 1, Y2 - 1
#     sum_val = 0
    
#     for r in range(x1, x2 + 1):
#         for c in range(y1, y2 + 1):
#             if x1 == x2 and y1 == y2:
#                 sum_val = arr[r][c]
#                 break
#             sum_val += arr[r][c]
#     print(sum_val)
##################################################################################
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
print(dp)
# 2. M개의 쿼리 처리
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    
    # 누적 합 배열을 이용해 O(1)의 속도로 구간 합 도출
    ans = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(ans)