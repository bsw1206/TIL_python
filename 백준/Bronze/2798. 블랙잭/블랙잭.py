a, b = map(int, input().split())
num_list = list(map(int, input().split()))

result = 0

for i in range(a):
    for j in range(i + 1, a):
        for k in range(j + 1, a):
            
            # 3장의 합 계산
            sum_list = num_list[i] + num_list[j] + num_list[k]
            
            # M(b)을 넘지 않으면서, 기존 최대값보다 크면 갱신
            if sum_list <= b:
                if sum_list > result:
                    result = sum_list

# 반복문이 다 끝난 뒤에 결과 출력 (들여쓰기 없음!)
print(result)