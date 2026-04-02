a, b = map(int, input().split())
c = int(input())
hour = a + ((b + c)//60)
minutes = (b + c) % 60
if hour < 24:
    print(hour, minutes)
else:
    print(hour - 24, minutes)