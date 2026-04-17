import sys
sys.stdin = open('swea_4837_부분집합의 합.txt')
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    result = 0
    # arr = []
    # for i in range(1, 13):
    #     arr.append(i)
    arr = list(range(1, 13))
    for i in range(1 << len(arr)):
        lst = []
        for j in range(len(arr)):
            if i & (1 << j):
                lst.append(arr[j])
        if len(lst) == N:
            if sum(lst) == K:
                result += 1
    print(f'#{tc} {result}')
    
