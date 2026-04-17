# 아래 함수를 수정하시오.
def remove_duplicates_to_set(lst):
    for num in lst:
        if lst.count(num) >= 2:
            lst.remove(num)
    new_set = set()
    for i in range (len(lst)):
        new_set.add(i + 1)
    return new_set
    
result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
