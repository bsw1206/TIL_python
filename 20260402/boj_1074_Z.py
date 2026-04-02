# N, r, c가 주어지고, r행 c열을 몇 번째로 방문했는지 구하기
# Z 모양으로 움직이는 로직 짠 뒤에 3번 움직이면 이동하는 코드를 구현해야 하는데
# 먼저 1칸 오른쪽으로 위로 ((2의 cnt-1승) - 1)칸 움직이네

# 아니면 차라리 7번 움직이는 로직을 만들고

# 안 쓴거는 다 2의 2승 -1
# 아래, 위, 아래, 아래(2의 3승 -1), 아래, 위, 아래, 위(2의 3승 -1)
# 4범위를 돌면서 
# 맨 처음에는 2 * 2의 좌상,우상,좌하,우하
# 두번쨰는 4 * 4의 좌상, 우상, 좌하, 우하
import sys
sys.stdin = open('boj_1074_Z.txt')

   


N, r, c = map(int, input().split())

cnt = 0

while N:
    N -= 1
    half = 2 ** N

    if r < half and c < half:
        cnt += 0

    elif r < half and c >= half:
        cnt += half * half 
        c -= half
    elif r >= half and c < half:
        cnt += half * 2 * half
        r -= half
    else:
        cnt += half * 3 * half
        r -= half
        c -= half
print(cnt)
