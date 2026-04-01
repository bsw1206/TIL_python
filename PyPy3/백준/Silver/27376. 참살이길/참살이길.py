import sys

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