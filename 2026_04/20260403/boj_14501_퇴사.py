import sys
sys.stdin = open('boj_14501_퇴사.txt')
def dfs(day, sum_val):
    global max_val

    if day > N:
        return
    if day == N:
        max_val = max(max_val, sum_val)
        return

    
    dfs(day + date[day][0], sum_val + date[day][1])
    
    dfs(day + 1, sum_val)


N = int(input())
date = [list(map(int, input().split())) for _ in range(N)]
max_val = 0
dfs(0, 0)
print(max_val)