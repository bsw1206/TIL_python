import sys

info = []
for _ in range(3):
    P, Y, S = input().split()
    info.append((int(P), Y[2:], S))
info.sort(key=lambda x: x[1])
result = []
for num in info:
    result.append(num[1])
print(''.join(result))
info.sort(reverse=True, key=lambda x: x[0])
result = []
for l in info:
    result.append(l[2][:1])
print(''.join(result))