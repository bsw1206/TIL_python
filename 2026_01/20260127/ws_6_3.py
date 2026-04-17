# 아래 함수를 수정하시오.
def intersection_sets(set1, set2):
    if len(set1 & set2) == 0:
        return (f'공통 요소가 업습니다 \n{(len(set1 & set2), set1 & set2)}')
    return (len(set1 & set2), set1 & set2)


result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result)  # (1, {3})

result = intersection_sets({1, 2}, {3, 4})
print(result)  # (0, set())
# 출력: 공통 요소가 없습니다
