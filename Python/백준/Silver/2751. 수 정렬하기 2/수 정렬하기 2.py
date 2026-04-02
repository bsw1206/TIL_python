import sys

# input() 대신 sys.stdin.readline을 사용해야 빠릅니다.
N = int(sys.stdin.readline())
num = []

for _ in range(N):
    # 입력받은 값을 정수(int)로 변환하여 리스트에 추가
    num.append(int(sys.stdin.readline()))

# 정렬 (O(N log N))
num.sort()

# 출력
for i in num:
    print(i)