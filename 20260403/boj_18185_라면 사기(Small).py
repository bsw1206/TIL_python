# 라면매니아 교준이네 집 주변에는 N개의 라면 공장이 있다. 각 공장은 1번부터 N번까지 차례대로 번호가 부여되어 있다. 교준이는 i번 공장에서 정확하게 Ai개의 라면을 구매하고자 한다(1 ≤ i ≤ N).

# 교준이는 아래의 세 가지 방법으로 라면을 구매할 수 있다.

# i번 공장에서 라면을 하나 구매한다 : 3원
# i번 공장과 (i+1)번 공장에서 각각 라면을 하나씩 구매한다 :5원
# i번 공장과 (i+1)번 공장, (i+2)번 공장에서 각각 라면을 하나씩 구매한다 : 7원
# 최소의 비용으로 라면을 구매하고자 할 때, 교준이가 필요한 금액을 출력하는 프로그램을 작성하시오.

# 교준이가 필요한 최소 금액 출력

import sys
sys.stdin = open('boj_18185_라면 사기(Small).txt')
N = int(input())
ramen = list(map(int, input().split()))
ramen += [0, 0]
min_price = 0
for i in range(N):
    if ramen[i+1] > ramen[i+2]:
        while ramen[i] > 0 and ramen[i+1] > ramen[i+2]:
            ramen[i] -= 1
            ramen[i+1] -= 1
            min_price += 5
        while ramen[i] > 0 and ramen[i+1] > 0 and ramen[i+2] > 0:
            ramen[i] -= 1
            ramen[i+1] -= 1
            ramen[i+2] -= 1
            min_price += 7
        
    else:
        while ramen[i] > 0 and ramen[i+1] > 0 and ramen[i+2] > 0:
            ramen[i] -= 1
            ramen[i+1] -= 1
            ramen[i+2] -= 1
            min_price += 7
        while ramen[i] > 0 and ramen[i+1] > 0:
            ramen[i] -= 1
            ramen[i+1] -= 1
            min_price += 5
    while ramen[i] > 0 :
            ramen[i] -= 1
            min_price += 3

print(min_price)