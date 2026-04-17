import math

# 원점 찍기
origin_x, origin_y = 0, 0

# 점 리스트
x, y = 1, 2
# 지점의 정보를 저장하는 리스트

power = 100

distance = math.sqrt((x - origin_x) ** 2 + (y - origin_y) ** 2)
print(distance)
# 각도 계산
angle_radians = math.atan2(y - origin_y, x - origin_x)
print(angle_radians)
angle_degrees = math.degrees(angle_radians)
print(angle_degrees)