# N 의 두배이상으로 맞추는 건데 
# 각 인덱스의 숫자를 변경시킬수 있는 경우는 max(A[i] + i, i) 중 큰값 설정하기
# 최소 카운트를 계산하는 방법

# 일단 목표 합계를 정하고 
# 리스트의 합이 목표 합계를 넘어가는 경우를 생각함.
# 각 리스트마다 합을 해주는 경우를 생각함.

# 합을 제일 많이 해주는 경우를 우선적으로 생각해주는 것이 카운트를 줄이는 방법?
# 그러면 얼마나 합을 해줘야 하는지를 각 인덱스 마다 계산하고 뒤집어서 정렬한 뒤에 앞에서 세면서 카운트 매기기
import sys
sys.stdin = open('두배.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    n_lst = list(map(int, input().split()))
    n_lst.insert(0, 0)
    target = N * 2
    sum_val = sum(n_lst)

    cnt = 0
    if sum_val > target:
        print(f'#{tc} {cnt}')
        continue
    change_lst = []
    for i in range(1, len(n_lst)):
        new_val = max(n_lst[i] + i, i)
        change_lst.append(new_val - n_lst[i])
        
    change_lst.sort(reverse=True)

    for j in change_lst:
        sum_val += j
        cnt += 1
        if sum_val >= target:
            break
    print(f'#{tc} {cnt}')