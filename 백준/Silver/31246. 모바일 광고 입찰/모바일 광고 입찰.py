import sys
input = sys.stdin.readline
N, K = map(int, input().split())


sub_lst = []
for _ in range(N):
    A, B = map(int, input().split())
    sub_lst.append(B - A)
sub_lst.sort()
ans = max(0, sub_lst[K-1])
print(ans)