# N * N 배열의 마을에서 
# 한기는 0,0에서 시작
# 한번에 최대 4명의 의뢰를 수락하여 진행
# 손님 : -1~-4 / 몬스터 : 1~4
# 한번 움직일때 시간 1 소요
# 몬스터 전달 순서는 상관 x
# 해당 몬스터 먼저 잡은 뒤에 손님 방문하면 됨.
# 효율적으로 움직여 포획과 전달을 끝낼 최단 시간 구하기


# 일단 4방향 정의 -> 를 할 필요가 있을까?
# 최단 거리의 몬스터를 일단 먼저 잡아야 함.
# 최단 거리의 손님이나 몬스터를 파악. -> 손님 의뢰 몬스터가 잡혔다면
# 몬스터 잡힘 여부는 0으로 갱신후에 손님의 절댓값이 배열에 존재하지 않을 때로 생각
import sys
sys.stdin = open('몬스터 마스터.txt')
def dfs(r, c, current_time, visited_cnt):

    global min_time

    if current_time > min_time:
        return
    if visited_cnt == len(lst):
        min_time = min(min_time, current_time)
        return 


    for i in range (len(lst)):
        if not visited[i]:

            target = lst[i][0]

            dr, dc = lst[i][1], lst[i][2]


            if target < 0 and not catch[abs(target)]:
                continue
            time = abs(dr - r) + abs(dc - c)
            visited[i] = True
            if target > 0:
                catch[target] = True

            dfs(dr, dc, current_time + time, visited_cnt + 1)
            visited[i] = False
            if target > 0:
                catch[target] = False


T = int(input())

for tc in range(1, T + 1):

    N = int(input())

    town = [list(map(int, input().split())) for _ in range(N)]

    lst = []

    min_time = float('inf')
    for r in range(N):

        for c in range(N):

            if town[r][c] != 0:

                lst.append((town[r][c], r, c))
    catch = [False] * 5
    visited = [False] * len(lst)
    dfs(0,0,0,0)
    print(f'#{tc} {min_time}')