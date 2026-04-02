
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
rank = [list(map(int, input().split())) for _ in range(N)]


rank.sort(reverse=True, key=lambda x: (x[1], x[2], x[3]))


target_idx = 0
for i in range(N):
    if rank[i][0] == K:
        target_idx = i
        break


for i in range(N):

    if rank[i][1:] == rank[target_idx][1:]:
        print(i + 1)  
        break