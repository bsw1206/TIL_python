def ordered_difference_sets(set1, set2):
    if len(set1 - set2) > len(set2 - set1):
        return (set2 - set1, set1 - set2)
    else:
        return (set1 - set2, set2 - set1)
# 예시 실행
result = ordered_difference_sets({1, 2, 3, 4}, {3, 4, 5, 6})
print("결과:", result)  # 출력: ({1, 2}, {5, 6})

result = ordered_difference_sets({1, 2, 3, 4}, {1, 2, 3})
print("결과:", result)  # 출력: (set(), {4})
