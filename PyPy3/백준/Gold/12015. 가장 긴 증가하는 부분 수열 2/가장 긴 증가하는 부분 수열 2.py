import sys
input = sys.stdin.readline




from bisect import bisect_left

input = sys.stdin.readline
N = int(input())
num_lst = list(map(int, input().split()))


lis_list = [num_lst[0]]


for i in range(1, N):
    target = num_lst[i]

    if target > lis_list[-1]:

        lis_list.append(target)

    else:

        idx = bisect_left(lis_list, target)
        

        lis_list[idx] = target

print(len(lis_list))