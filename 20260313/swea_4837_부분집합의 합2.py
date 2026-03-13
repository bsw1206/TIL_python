# 부분집합의 길이와 합이 들어맞는 조건의 부분집합 개수를 출력하는 프로그램

# 흠... 그러면 재귀를 통해서 인덱스를 넣고 리스트에 append하는 것을 통해서 넣고 아닌 경우에는 pop을 통해서 빼기
import sys
sys.stdin = open('swea_4837_부분집합의 합.txt')

def dfs(idx, lst):
    global result
    
    if idx == 12:
        if len(lst) == N and sum(lst) == K:
            result += 1
        return

    lst.append(n_lst[idx])
    dfs(idx + 1, lst)

    lst.pop()
    dfs(idx + 1, lst)
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    n_lst = list(range(1, 13))
    result = 0
    dfs(0, [])
    print(f'#{tc} {result}')