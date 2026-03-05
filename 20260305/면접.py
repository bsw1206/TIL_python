# N 개의 문제중에 무조건 M개를 맞췄음. 
# 연속해서 K개를 맞출 때 카운터가 0으로 리셋되고 전체 점수가 2배
# 총점이 최소인 경우 구하기


# counter = 0
# 최소가 되는 경우?
# 틀린 문제 지정
# 틀리기 전까지 배치할 수 있는 최대 문제수는 ?
# 반드시 보너스를 받아야하는 문제의 개수는?
# 모든 문제를 안전하게 배치할 수 있는 경우는??
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    min_val = float('inf')

    incorrect = N - M
    
    group = incorrect + 1

    correct_range = (K - 1) * group

    if M <= correct_range:
        print(f'#{tc} {M}')
        continue
    else:
        bonus_needed = M - correct_range
        bonus_group = bonus_needed

        score = 0

        for i in range(bonus_needed):
            score = (score + K) * 2
        
        remain = K - M

        score += remain * 



    
    





