import sys
sys.stdin = open('swea_5204_병합 정렬.txt')

def merge(left, right):
    global cnt
    
    cnt += 1 if left[-1] > right[-1] else 0
    
    merged_arr = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged_arr.append(left[left_idx])
            left_idx += 1
        else:
            merged_arr.append(right[right_idx])
            right_idx += 1

    merged_arr.extend(left[left_idx:])
    merged_arr.extend(right[right_idx:])
    return merged_arr


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2

    left_lst = arr[:mid]
    right_lst = arr[mid:]

    left_sorted = merge_sort(left_lst)
    right_sorted = merge_sort(right_lst)

    return merge(left_sorted, right_sorted)
    
    
T  = int(input())
for tc in range(1, T + 1):
    N = int(input())
    L = list(map(int, input().split()))
    cnt = 0
    L_sort = merge_sort(L)
    result = L_sort[N // 2]
    print(f'#{tc} {result} {cnt}')
