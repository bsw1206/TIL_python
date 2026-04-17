# ATM 1대, N명의 사람, i번 사람이 돈을 뽑는데 P분 소모
import sys
sys.stdin = open('boj_11399_ATM.txt')
N = int(input())
time = list(map(int, input().split()))
time.sort()
sum_val = 0
for i in range(len(time) + 1):
    for j in range(i):
        sum_val += time[j]
print(sum_val)