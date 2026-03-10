# 24시간 운영 / 0시부터 다음날 0시 이전까지 
# 최대한 많은 화물차가 싣고 내릴 수 있도록 하면, 최대 몇 대의 화물차가 이용할 수 있는지 알아내는 것
# 작업 시작 시간과 완료 시간이 표시됨, 앞 작업의 종료와 동시에 다음 작업 시작 가능

# 이 문제는 끝나는 시각을 우선으로 정렬을 하게 되면 시작 시간이 다르고 종료 시간이 같은 것을 분리 가능
# 가장 일찍 끝나는 일인 맨 앞자리의 일을 먼저 처리하고 종료 시간을 저장함.
# 그리고 종료 시간이 다음 일의 시작 시간보다 적거나 같다면 일을 포함시킨다.

import sys
sys.stdin = open('swea_5202_화물 도크.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    time_lst = [list(map(int, input().split())) for _ in range(N)]
    
    # 종료 시간 순으로 정렬
    time_lst.sort(key= lambda x : x[1]) 

    # 맨 처음일은 무조건 하기
    cnt = 1
    
    # 처음 일의 종료시간 젖아
    end = time_lst[0][1]

    # 맨 앞의 일을 뺌
    time_lst.pop(0)

    
    for t in range(len(time_lst)):
        
        # 앞의 일의 종료 시간이 현재 일의 시작시간보다 느리다?
        if time_lst[t][0] >= end:
            # 이 일도 진행시켜
            cnt += 1
            # 종료시간 갱신
            end = time_lst[t][1]
    print(f'#{tc} {cnt}')