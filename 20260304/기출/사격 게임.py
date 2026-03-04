import sys
sys.stdin = open('사격 게임.txt')
def dfs(balloons, current_score):
    global max_score
    if not balloons: # 풍선 존재 x
        max_score = max(current_score, max_score)
        return
    
    for i in range(len(balloons)):
        score = 0

        if 0 < i < len(balloons) - 1: # 가운데 경우
            score += balloons[i-1] * balloons[i + 1]
        elif i == 0 and len(balloons) > 1: # 왼쪽 끝
            score += balloons[i + 1]
        elif i > 0 and i == len(balloons) - 1: # 오른쪽 끝
            score += balloons[i-1]
        elif len(balloons) == 1: # 하나 남았을 때
            score += balloons[i]
				# 터뜨린 위치 제외
        new_balloons = balloons[:i] + balloons[i + 1:]
        dfs(new_balloons, current_score + score)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    balloons = list(map(int, input().split()))
    max_score = 0
    
    dfs(balloons, 0)
    print(f'#{tc} {max_score}')