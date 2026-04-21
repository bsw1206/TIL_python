import sys
sys.stdin = open('나무의 키.txt')
# 최대한 고르게 뿌리는 것이 일반적
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = list(map(int, input().split()))

    max_height = max(tree)
    total_diff = [max_height - h for h in tree]
    
    if sum(total_diff) == 0:
        print(f'#{tc} 0')
        continue
    
    one = 0
    two = 0
    for diff in total_diff:
        if diff % 2 == 1:
            one += 1
        two += diff // 2

    while two > one + 1:
        two -= 1
        one += 2
    if two >= one:
        print(f'#{tc} {two * 2}')
    else:
        print(f'#{tc} {one * 2 - 1}')

