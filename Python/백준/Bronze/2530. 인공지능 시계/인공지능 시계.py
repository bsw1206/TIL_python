a, b, c = list(map(int, input().split()))
d = int(input())
total_seconds = (a * 3600) + (b * 60) + c + d
hour = total_seconds // 3600
second = total_seconds % 3600
minutes = second // 60
real_second = second % 60
real_hour = hour % 24
print(real_hour, minutes, real_second)