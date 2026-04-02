import sys

input = sys.stdin.readline

N, K = map(int, input().split())

dp = [0] * (K + 1)
for _ in range(N):
    w, v = map(int, input().split())
    for j in range(K, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)


print(dp[K])