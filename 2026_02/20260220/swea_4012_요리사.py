import sys
sys.stdin = open('swea_4012_요리사.txt')
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     food_lst = []
#     for r in range(N):
#         for c in range(N):
#             if arr[r] != arr[c]:
#                 food_lst.append([arr[r][c] + arr[c][r], r, c])
#     min_val = 40000
#     for i in range(len(food_lst)):
#         for j in range(len(food_lst)):
#             if i != j:
#                 if food_lst[i][1] == food_lst[j][2] and food_lst[i][2] == food_lst[j][1]:
#                     continue
#                 else:
#                     taste = abs(food_lst[i][0]-food_lst[j][0])
            
#                 if min_val > taste:
#                     min_val = taste
#     print(f'#{tc} {min_val}')


from itertools import combinations

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # 1. 0부터 N-1까지의 식재료 번호 리스트
    ingredients = list(range(N))
    min_diff = float('inf')

    # 2. N/2개를 선택하는 모든 조합을 구함
    for team_a in combinations(ingredients, N // 2):
        # 3. 나머지를 team_b로 설정
        team_b = [i for i in ingredients if i not in team_a]
        
        sum_a = 0
        sum_b = 0
        
        # 4. 각 팀 내부의 시너지 합 계산 (2개씩 짝지어 더함)
        for i, j in combinations(team_a, 2):
            sum_a += matrix[i][j] + matrix[j][i]
            
        for i, j in combinations(team_b, 2):
            sum_b += matrix[i][j] + matrix[j][i]
            
        # 5. 최솟값 갱신
        diff = abs(sum_a - sum_b)
        if diff < min_diff:
            min_diff = diff

    print(f'#{tc} {min_diff}')
