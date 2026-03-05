# 3 6 7 1 5 4
# 주어진 수에 대한 부분집합의 수를 구하시오.

import sys 
sys.stdin = open('input.txt')

num = list(map(int, input().split()))

n = len(num)

cnt = 0

for i in range(1 << n):
    cnt += 1
    for j in range(n):
        if i & (1 << j):
            print(num[j], end = '')
    print()
print()


print('---')
print(cnt)
