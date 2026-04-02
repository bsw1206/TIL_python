import sys
input = sys.stdin.readline
n = int(input())
n_lst = list(map(int, input().split()))
x = int(input())
n_lst.sort()
left = 0
right = n - 1
cnt = 0
while left < right:
    cur_sum = n_lst[left] + n_lst[right]

    if cur_sum == x:
        cnt += 1
        left += 1
        right -= 1
    elif cur_sum < x:
        left += 1
    else:
        right -= 1

print(cnt)