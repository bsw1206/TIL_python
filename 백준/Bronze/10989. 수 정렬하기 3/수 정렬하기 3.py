import sys
T = int(sys.stdin.readline())
count = [0] * 10001 
for _ in range(T):
    num = int(sys.stdin.readline())
    count[num] += 1
for j in range(10001):
    if count[j] != 0:
        for _ in range(count[j]):
            print(j)