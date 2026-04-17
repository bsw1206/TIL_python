import sys
sys.stdin = open('boj_12015_가장 긴 증가하는 부분 수열 2.txt')




from bisect import bisect_left

# 입력 속도 향상을 위해 readline 사용 권장
input = sys.stdin.readline
N = int(input())
num_lst = list(map(int, input().split()))

# LIS 배열 초기화 (가장 첫 번째 숫자를 넣어두고 시작)
lis_list = [num_lst[0]]

# 두 번째 숫자부터 끝까지 단 한 번만 순회 (O(N))
for i in range(1, N):
    target = num_lst[i]
    
    # [조건 1] target이 lis_list의 맨 마지막 숫자보다 크다면?
    if target > lis_list[-1]:
        # 수열이 더 길어질 수 있으므로 lis_list 맨 끝에 추가 (append)
        lis_list.append(target)
        
    # [조건 2] target이 lis_list의 맨 마지막 숫자보다 작거나 같다면?
    else:
        # 이분 탐색으로 target이 들어갈 수 있는 크기 순서상의 적절한 위치(인덱스)를 찾음 (O(log N))
        idx = bisect_left(lis_list, target)
        
        # 찾은 위치(idx)의 기존 값을 target으로 교체
        lis_list[idx] = target

# lis_list의 최종 길이가 우리가 구하는 정답
print(len(lis_list))