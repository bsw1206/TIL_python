# 수열 전체 합이 2N 이상이 되도록
# i를 선택하여 A[i]를 max(A[i] + i, i)로 바꾸는 것
# 최소 작업 횟수를 구하기
# 그러면 제일 작은 수로 나열하여서
import sys
sys.stdin = open('두 배.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [0] + list(map(int, input().split()))

    sum_val = sum(A)
    target_sum = 2 * N
    gains = []
    for i in range(1, N + 1):
        if A[i] < 0:
            gains.append(i - A[i])
        else:
            gains.append(i)
    gains.sort(reverse=True)
    needed_sum = target_sum - sum_val
    cnt = 0

    for gain in gains:
        if needed_sum <= 0:
            break
        needed_sum -= gain
        cnt += 1
    # if needed_sum > 0:
    #     cnt += (needed_sum + N - 1) // N
    print(f'#{tc} {cnt}')
