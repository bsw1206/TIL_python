import sys
sys.stdin = open('swea_1486_장훈이의 높은 선반.txt')
from itertools import combinations
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    n_lst = list(map(int, input().split()))
    min_val = float('inf')
    for k in range(1, N + 1):
        for subset in combinations(n_lst, k):
            current_height = sum(subset)
            if current_height >= M:
                min_val = min(min_val, current_height - M)
    print(f'#{tc} {min_val}')
