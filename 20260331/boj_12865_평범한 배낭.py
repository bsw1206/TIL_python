# 최대한 가치있게 배낭 사용
# N개의 물건 : 각각 무게 W와 가치 V를 가짐
# 최대 K만큼의 무게만을 넣을 수 있는 배낭
# 가치의 최댓값?
import sys
sys.stdin = open('boj_12865_평범한 배낭.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
items = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(K + 1)]

# 1번 물건부터 N번 물건까지 차례대로 수첩 채우기
for i in range(1, N + 1):
    weight = items[i][0]
    value = items[i][1]
    # 배당 무게의 한도를 1부터 K까지 늘리며 확인
    for j in range(1, K + 1):
        if j < weight:
            # 못 넣을때, 위의까지의 최적해를 그대로 가져옴.
            dp[i][j] = dp[i-1][j]
        # 넣을 수 있으면, 안 넣고 그대로 쓰기, 현재 물건 넣고 남은 무게만큼 윗줄에서 컨닝하기 중 큰 값
        else:
            dp[i][j] = max(dp[i-1][j], value + dp[i-1][j-weight])

# 수첩의 맨 오른쪽 아랫값이 최종 정답
print(dp[N][K])


# 1차원 DP 예시 (Python)
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0] * (K + 1)

for _ in range(N):
    w, v = map(int, input().split())
    # 뒤에서부터 계산해야 이전 물건의 결과가 중복 반영되지 않음
    for j in range(K, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[K])
