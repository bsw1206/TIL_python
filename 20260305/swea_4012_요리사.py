# 식재료를 N / 2개씩 나누어 요리
# A, B 음식의 맛 차이가 최소
# i와 j를 같이 요리하면 시너지가 남.
# 음식의 맛을 각 시너지의 합



import sys
sys.stdin = open('swea_4012_요리사.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_diff = float('inf')
    for i in range(1 << N):
        if not (i & 1):
            continue
        if i.bit_count() == N // 2:
            A_group = []
            B_group = []
            for j in range(N):
                
                if i & (1 << j):
                    A_group.append(j)
                else:
                    B_group.append(j)
            A_synergy, B_synergy = 0, 0
            for k in range(N // 2):
                for l in range(k + 1, N // 2):
                    A_synergy += arr[A_group[k]][A_group[l]] + arr[A_group[l]][A_group[k]]
                    B_synergy += arr[B_group[k]][B_group[l]] + arr[B_group[l]][B_group[k]]
            min_diff = min(min_diff, abs(A_synergy - B_synergy))
    print(f'#{tc} {min_diff}')



        
#################################################################################


import sys
sys.stdin = open('swea_4012_요리사.txt')
from itertools import combinations
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_diff = float('inf')
    ingredients = list(range(N))

    for A_group in combinations(ingredients, N // 2):
        B_group = list(set(ingredients) - set(A_group))
    
        A_synergy, B_synergy = 0, 0
        for k, l in combinations(A_group, 2):
            A_synergy += arr[k][l] + arr[l][k]
        for k, l in combinations(B_group, 2):
            B_synergy += arr[k][l] + arr[l][k]
        min_diff = min(min_diff, abs(A_synergy - B_synergy))
    print(f'#{tc} {min_diff}')