arr = [69, 10, 30, 2, 16, 8, 31, 22]
def merge(left, right):
    
    result = [0] * (len(left) + len(right))
    l = r = 0
    
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] = right[r]
            r += 1
    while l < len(left):
        result[l+r] = left[l]
        l += 1
    while r < len(right):
        result[l+r] = right[r]
        r += 1
    return result

def merge_sort(li):
    
    if len(li) == 1:
        return li
    
    mid = len(li) // 2
    
    left = li[:mid]
    right = li[mid:]

    left_lst = merge_sort(left)
    right_lst = merge_sort(right)
    
    merge_lst = merge(left_lst, right_lst)
    return merge_lst

sorted_arr = merge_sort(arr)
print(sorted_arr)