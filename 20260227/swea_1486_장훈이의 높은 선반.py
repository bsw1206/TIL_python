import sys
sys.stdin = open('swea_1486_장훈이의 높은 선반.txt')
from itertools import combinations
T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    min_diff = float('inf')
    
    for i in range(1, N + 1):
        for S in combinations(height, i):
            sum_height = sum(S)
            
            if sum_height >= B:
                min_diff = min(min_diff, sum_height - B)

    print(f'#{tc} {min_diff}') 



###################################################################################

def dfs(i, height):
    if sum > height:
        return True
    if i > N:
        return
    











T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))