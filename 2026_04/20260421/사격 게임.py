# import sys

# sys.stdin = open('사격 게임.txt')

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     balloons = list(map(int, input().split()))

#     # dp[mask]: 현재 남아있는 풍선 상태가 mask일 때 얻을 수 있는 최대 점수
#     # 상태의 가짓수는 2^N개이며, 모두 0으로 초기화합니다.
#     # (mask=0 인 경우 모든 풍선을 다 터뜨린 상태이므로 점수는 0점)
#     dp = [0] * (1 << N)

#     # mask를 1부터 꽉 찬 상태((1 << N) - 1)까지 순차적으로 계산합니다.
#     # 숫자가 작은 mask(남은 풍선이 적은 상태)부터 계산되므로 바텀업이 성립합니다.
#     for mask in range(1, 1 << N):
#         max_val = 0
        
#         # 현재 mask 상태에서 터뜨릴 풍선 i를 고릅니다.
#         for i in range(N):
#             # i번째 비트가 1인지 확인 (즉, i번 풍선이 남아있는지 검사)
#             if (mask >> i) & 1:

#                 # 1. 터뜨릴 풍선(i)의 좌우 이웃을 찾습니다.
#                 left, right = -1, -1
                
#                 # 왼쪽 이웃 찾기
#                 for l in range(i - 1, -1, -1):
#                     if (mask >> l) & 1:
#                         left = balloons[l]
#                         break
                        
#                 # 오른쪽 이웃 찾기
#                 for r in range(i + 1, N):
#                     if (mask >> r) & 1:
#                         right = balloons[r]
#                         break

#                 # 2. 규칙에 따라 점수를 계산합니다.
#                 shot_score = 0
#                 if left != -1 and right != -1:
#                     shot_score = left * right
#                 elif left != -1:
#                     shot_score = left
#                 elif right != -1:
#                     shot_score = right
#                 else:
#                     shot_score = balloons[i]

#                 # 3. 현재 점수 + (i번 풍선을 터뜨리고 남은 상태에서의 최대 점수)
#                 # mask ^ (1 << i)는 항상 mask보다 작으므로 이미 dp 배열에 값이 존재합니다.
#                 val = shot_score + dp[mask ^ (1 << i)]
#                 max_val = max(max_val, val)

#         # 4. 계산된 최대 점수를 dp 배열에 저장합니다.
#         dp[mask] = max_val

#     # 모든 풍선이 살아있는 초기 상태의 최대 점수를 출력합니다.
#     print(f'#{tc} {dp[(1 << N) - 1]}')

#########################################################################################

import sys 
sys.stdin = open('사격 게임.txt')

def dfs(balloons, cur_score):
    global max_score
    if not balloons:
        max_score = max(max_score, cur_score)
        return
    
    for i in range(len(balloons)):
        score = 0

        if 0 < i < len(balloons) - 1:
            score += balloons[i-1] * balloons[i+1]
        elif i == 0 and len(balloons) > 1:
            score += balloons[i+1]
        elif i > 0 and i == len(balloons) - 1:
            score += balloons[i-1]
        elif len(balloons) == 1:
            score += balloons[i]
        new_balloons = balloons[:i] + balloons[i + 1:]
        dfs(new_balloons, cur_score + score)
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    balloons = list(map(int, input().split()))
    max_score = 0

    dfs(balloons, 0)
    print(f'#{tc} {max_score}')


#########################################################################################

