import sys
sys.stdin = open('swea_26504_MST만들기.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = 0
    n_lst = list(map(int, input().split()))
    
    
    n_lst.sort()
    min_cost = sum(n_lst[:N-1])

    max_cost = 0
    idx = 0

    for step in range(1, N):
        max_cost += n_lst[idx]
        idx += step
    
    print(f'{min_cost} {max_cost}')

