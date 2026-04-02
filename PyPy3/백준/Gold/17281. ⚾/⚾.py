
import sys

from itertools import permutations
input = sys.stdin.readline
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
max_val = 0

for i in permutations(range(1, 9)):
    i = list(i)
    order = i[:3] + [0] + i[3:]
    sum_val = 0
    cur_person = 0
    
    
    for inning in lst:
        out_cnt = 0
        b1, b2, b3 = 0, 0, 0
        
        while out_cnt < 3:
            player_result = inning[order[cur_person]]
            if player_result == 4:
                sum_val += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            elif player_result == 3:
                sum_val += b1 + b2 + b3
                b3 = 1
                b1, b2 = 0, 0
            elif player_result == 2:
                sum_val += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif player_result == 1:
                sum_val += b3
                b1, b2, b3 = 1, b1, b2
            elif player_result == 0:
                out_cnt += 1
            cur_person = (cur_person + 1) % 9
            
        
        if max_val < sum_val:
            max_val = sum_val
        
print(max_val)
