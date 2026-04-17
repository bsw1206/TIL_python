# 야구 시뮬레이션
# 3아웃되면 이닝 교체
# 안타, 2루타, 3루타, 홈런, 아웃 5가지 경우 존재
# 도착하지 못하면 주자 사라짐
# 첫째줄에는 이닝 수 
# 둘째줄에는 각 선수가 각 이닝에서 얻는 결과가 1번 이닝부터 N번 이닝까지 순서대로 주어짐.
# 안타 : 1, 2루타 : 2, 3루타 : 3, 홈런 : 4, 아웃 : 0
# 얻을 수 있는 최대 점수를 출력


# 모든 시뮬레이션을 생각할 수는 있는데, 최댓값은 어떻게 생각하지?
# 아웃카운트, 
import sys
sys.stdin = open('boj_17281_야구.txt')
from itertools import permutations
input = sys.stdin.readline
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
max_val = 0

for i in permutations(range(1, 9)):
    i = list(i)
    # 4번 타자는 0으로 고정하고 나머지 모든 경우를 생각
    order = i[:3] + [0] + i[3:]
    # 합계랑 현재 대기 타자를 지정
    sum_val = 0
    cur_person = 0
    
    
    for inning in lst:
        out_cnt = 0
        b1, b2, b3 = 0, 0, 0
        
        while out_cnt < 3:
            
            player_result = inning[order[cur_person]]
            # 홈런
            if player_result == 4:
                sum_val += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            # 3루타
            elif player_result == 3:
                sum_val += b1 + b2 + b3
                b3 = 1
                b1, b2 = 0, 0
            # 2루타
            elif player_result == 2:
                sum_val += b2 + b3
                b1, b2, b3 = 0, 1, b1
            # 안타
            elif player_result == 1:
                sum_val += b3
                b1, b2, b3 = 1, b1, b2
            # 아웃
            elif player_result == 0:
                out_cnt += 1
            cur_person = (cur_person + 1) % 9
            
        
        if max_val < sum_val:
            max_val = sum_val
        
print(max_val)
