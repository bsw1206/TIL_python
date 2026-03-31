# i번쨰 줄의 j번째 숫자? i번 층의 j번 위치에 있는 차의 정보를 나타냄.
# -1인 경우에는 비어있는 곳이고, r인 경우에는 r번째 손님이 찾아가는 차라는 의미
# 모든 손님이 차를 찾는데 걸리는 시간을 구하는 프로그램
import sys
sys.stdin = open('boj_3699_주차 빌딩.txt')

T = int(input())
for tc in range(T):
    h, l = map(int, input().split())
    info = []
    time = 0
    for _ in range(h):
        info.append(list(map(int, input().split())))
    cur_r, cur_c = 0, 0
    target = 1
    max_val = 0
    for r in range(h):
        for c in range(l):
             if max_val < info[r][c]:
                 max_val = info[r][c]
    while target < max_val + 1:
        for r in range(h):
            for c in range(l):
                if info[r][c] == target:
                    time += min(abs(c - cur_c), ((c + 2) % l)) * 5 + abs(cur_r - r) * 10
                    target += 1
                    cur_r, cur_c = r, c
                    break
    print(time)