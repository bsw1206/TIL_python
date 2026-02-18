N, M = map(int, input().split())
r, c = map(int, input().split())
T = int(input())
cur_x = (r + T) % (2 * N)
if cur_x > N:
    x = 2 * N - cur_x
else:
    x = cur_x
cur_y = (c + T) % (2 * M)
if cur_y > M:
    y = 2 * M - cur_y
else:
    y = cur_y
print(x, y)
