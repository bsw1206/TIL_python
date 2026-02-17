import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n_lst = list(map(int, input().split()))

# 1. 처음에만 M개 더해서 기준값 잡기 (초기 윈도우)
current_sum = sum(n_lst[:M])
max_val = current_sum

# 2. 슬라이딩 윈도우 시작 (한 칸씩 밀기)
# i는 '빠져나가는' 값의 인덱스입니다.
for i in range(N - M):
    # 다음 합 = 현재 합 - 맨 앞 숫자 + 그 다음 들어올 숫자
    current_sum = current_sum - n_lst[i] + n_lst[i + M]
    
    # 최댓값 갱신
    if max_val < current_sum:
        max_val = current_sum

print(max_val)