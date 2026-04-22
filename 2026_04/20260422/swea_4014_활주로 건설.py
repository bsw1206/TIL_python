# 경사로 높이 1
# 활주로 건설 가능한 가능성 파악
# 높이가 동일한 구간에서 건설 가능
# X : 경사로의 길이

# 일단 최대 높이에서는 못 깔으므로 패스
# 1. 현재 위치에서 그 전 높이가 1 클때, 그리고 for문 돌면서 계속 높이가 같아야 하고 막혔을때 길이가 X보다 작거나 index를 벗어났으면 실패
# 그리고 설치되어있는지 여부도 계속 파악해야 함.
# 2. K만큼 앞으로 가는 for문에서 현재 위치랑 값이 계속 같으면서 K번째 앞의 값이 높이가 1 클때 설치 가능.
# 연속되는 수가 경사로 길이보다 최소 1은 커야한다.
import sys
sys.stdin = open('swea_4014_활주로 건설.txt')

def check_line(line, N, X):
    # 경사로가 설치되었는지 확인하는 배열
    installed = [False] * N
    
    for i in range(1, N):
        # 1. 높이가 같은 경우 (통과)
        if line[i-1] == line[i]:
            continue
            
        # 2. 높이가 1 높아지는 경우 (오르막 경사로)
        elif line[i-1] + 1 == line[i]:
            # X만큼의 평지가 확보되는지 뒤로(왼쪽으로) 검사
            for j in range(1, X + 1):
                # 인덱스를 벗어나거나, 높이가 다르거나, 이미 경사로가 설치되어 있다면 불가
                if i - j < 0 or line[i-j] != line[i-1] or installed[i-j]:
                    return False
                installed[i-j] = True  # 경사로 설치 처리
                
        # 3. 높이가 1 낮아지는 경우 (내리막 경사로)
        elif line[i-1] - 1 == line[i]:
            # X만큼의 평지가 확보되는지 앞으로(오른쪽으로) 검사
            for j in range(X):
                # 인덱스를 벗어나거나, 높이가 다르거나, 이미 경사로가 설치되어 있다면 불가
                if i + j >= N or line[i+j] != line[i] or installed[i+j]:
                    return False
                installed[i+j] = True  # 경사로 설치 처리
                
        # 4. 높이 차이가 2 이상인 경우 (경사로 설치 불가)
        else:
            return False
            
    # 무사히 끝까지 도달했다면 활주로 건설 가능
    return True

T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    # 세로줄 검사를 쉽게 하기 위해 행렬을 90도 회전(전치)시킨 리스트 생성
    # 작성하셨던 grid_reverse 와 같은 역할입니다.
    grid_transposed = list(zip(*grid)) 
    
    result = 0
    
    # 가로줄 N개, 세로줄 N개 검사
    for i in range(N):
        if check_line(grid[i], N, X):           # 가로줄 검사
            result += 1
        if check_line(grid_transposed[i], N, X): # 세로줄 검사
            result += 1
            
    print(f'#{tc} {result}')