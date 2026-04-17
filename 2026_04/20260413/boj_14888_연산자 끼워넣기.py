

def dfs(idx, cur_val, plus, minus, multiply, divide):
    global min_val, max_val

    # 모든 숫자를 다 계산한 경우 (종료 조건)
    if idx == N:
        min_val = min(min_val, cur_val)
        max_val = max(max_val, cur_val)
        return

    # 더하기
    if plus > 0:
        dfs(idx + 1, cur_val + n_lst[idx], plus - 1, minus, multiply, divide)
    # 빼기
    if minus > 0:
        dfs(idx + 1, cur_val - n_lst[idx], plus, minus - 1, multiply, divide)
    # 곱하기
    if multiply > 0:
        dfs(idx + 1, cur_val * n_lst[idx], plus, minus, multiply - 1, divide)
    # 나누기 (파이썬 음수 나눗셈 처리 주의: int() 사용)
    if divide > 0:
        dfs(idx + 1, int(cur_val / n_lst[idx]), plus, minus, multiply, divide - 1)



import sys
sys.stdin = open('boj_14888_연산자 끼워넣기.txt')
input = sys.stdin.readline

N = int(input())
n_lst = list(map(int, input().split()))
p, mi, mu, div = map(int, input().split())


min_val = int(1e9)
max_val = -float('inf')

dfs(1, n_lst[0], p, mi, mu, div)

print(max_val)
print(min_val)