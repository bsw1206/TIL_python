# n미터, k개의 신호등 존재
# 시작점 좌표 0, 끝점 좌표가 n인 수직선
# 신호등은 정수 좌표점에만 존재함, 빨간 불과 초록 불, 총 2가지의 상태
# i번째 신호등은 빨간불과 초록불이 t초동안 번갈아 가면서 켜진다.
# s초 이후에 처음으로 빨간 불에서 초록 불이 된다.
# 시속 1m/s로 이동, 각 신호등의 좌표와 주기가 주어질 때 참살이길을 가장 빠르게 완주하는 경우의 수!

# 신호등의 좌표 : x, 주기 : t, 주행 시작한 이후 처음으로 빨간 불에서 초록불이 되는 시간 : s
import sys
sys.stdin = open('boj_27376_참살이길.txt')
n, k = map(int, input().split())
lights = []
for _ in range(k):
    lights.append(tuple(map(int,input().split())))

lights.sort(key=lambda x : x[0])

cur_time = 0
cur_loc = 0
for x, t, s in lights:
    cur_time += (x - cur_loc)
    cur_loc = x
    
    if cur_time < s:
        cur_time += (s - cur_time)
    else:
        diff = cur_time - s
        if (diff // t) % 2:

            cur_time += (t - (diff % t))
cur_time += n - cur_loc
print(cur_time)