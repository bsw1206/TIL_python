# N * N 지도, 각 칸엔 높이가 적혀져있음.
# 지나갈 수 있는 길의 개수
# 자나가려면 모든 칸의 높이가 같아야 함.
# 경사로를 놓을 수 있음. 경사로의 높이는 1이고, 길이는 L이다
# 개수는 많아서 부족하지는 않음.(높은 칸과 낮은 칸을 연결함.)
# 경사로를 놓을 낮은 칸의 높이는 모두 같다.(낮은 칸이 L개만큼 연속되어야함.)
# 경사로를 놓을 때 높은 곳과 낮은 곳의 높이 차이는 1
# 경사로를 놓다가 범위를 벗어나는 경우

# arr를 정의하고 
# 위, 아래, 좌, 우로 가는 경우를 모두 생각해야 할거 같은데...
# 가로, 세로를 훑는 게 더 나을라나?
# 가로 리스트를 정의하고 뒤집은 것도 정의하자.
import sys
sys.stdin = open('boj_14890_경사로.txt')
N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

reversed_arr =[row[::-1] for row in arr]
    
print(arr)
print(reversed_arr)