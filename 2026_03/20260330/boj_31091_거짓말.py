# N명의 사람
# 자신을 포함하여 몇 명 이상 혹은 몇 명 이하의 사람이 거짓말을 하고 있다고 각 사람은 말한다.

# 1명 이상
import sys
sys.stdin = open('boj_31091_거짓말.txt')

N = int(input())
lst = list(map(int, input().split()))

# up[num] = num명 이상이 거짓말이라고 말한 사람의 수
up = [0] * (N + 1)
down = [0] * (N + 1)
for num in lst:
    if num > 0:
        up[num] += 1
    else:
        down[-num] += 1

ans = []

# 거짓말쟁이가 0명일때부터 가정한다. 
# 따라서 "1~N명이 거짓말쟁이다."라고 말한 사람은 모두 거짓말쟁이가 된다.
# 거짓말 하는 사람들
up_liars = sum(up[1:])
# 반대로 down_liar는 없다.
# 거짓말 안 하는 사람들
down_liars = 0
# L : 총 거짓말 하는 사람의 수
for L in range(N + 1):
    # 같다는 의미는 내가 판단한 것이 맞다는 의미
    if up_liars + down_liars == L:
        ans.append(L)

    # L 다음에는 L + 1이 온다. 'L + 1명 이상'이라고 말한 사람은 L에서는 거짓말이였지만, 이젠 진실을 말한다.
    if L + 1 <= N:
        up_liars -= up[L + 1]
    # 반대로 L에서는 진실이었지만, L + 1에서는 거짓말이다.
    if L <= N:
        down_liars += down[L]

print(len(ans))
# 어차피 거짓말쟁이가 적은 순서대로 나열하므로 sort할 필요 xX
print(*ans)


