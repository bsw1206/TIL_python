import sys 
sys.stdin = open('swea_5205_퀵 정렬.txt')

def patition(arr, start, end):

    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] < pivot:

            i += 1
            
            if i != j:

                arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]

    return i + 1

def quick_sort(arr, start, end):

    if start < end:
        pivot_idx = patition(arr, start, end)

        quick_sort(arr, start, pivot_idx-1)
        quick_sort(arr, pivot_idx + 1, end)

    




T = int(input())
for tc in range(1, T + 1):
    
    N = int(input())
    n_lst = list(map(int, input().split()))
    quick_sort(n_lst, 0, len(n_lst) - 1)
    result = n_lst[N // 2]
    print(f'#{tc} {result}')
