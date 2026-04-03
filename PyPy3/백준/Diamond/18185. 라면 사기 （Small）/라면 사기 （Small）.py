import sys

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