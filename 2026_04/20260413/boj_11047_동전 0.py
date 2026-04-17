import sys
sys.stdin = open('boj_11047_동전 0.txt')
N, K = map(int, input().split())
n_lst = []
result = 0
for i in range(N):
    n_lst.append(int(input()))
for i in range(N-1, -1, -1):
    if n_lst[i] <= K:
        result += K // n_lst[i]
        K -= (n_lst[i] * (K // n_lst[i]))
print(result)