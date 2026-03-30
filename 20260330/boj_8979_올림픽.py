# 올림픽 순위 정하기

# 한 국가의 등수 = 자신보다 더 잘한 나라 수 + 1
# 예) 1등, 공동 2등이 있으면 3등은 없고, 4등이 나옴.
# 어느 국가가 몇 등을 했는지 알려주는 프로그램

# N, K : 국가의 수, 등수를 알고 싶은 국가
import sys
sys.stdin = open('boj_8979_올림픽.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
rank = [list(map(int, input().split())) for _ in range(N)]

# 1. 메달 순으로 내림차순 정렬
rank.sort(reverse=True, key=lambda x: (x[1], x[2], x[3]))

# 2. 정렬된 리스트에서 K 국가가 몇 번째(인덱스)에 있는지 찾기
target_idx = 0
for i in range(N):
    if rank[i][0] == K:
        target_idx = i
        break

# 3. K 국가와 메달 수가 똑같은 첫 번째 국가 찾기
for i in range(N):
    # 메달 수(1번 인덱스부터 끝까지)가 K 국가와 같다면
    if rank[i][1:] == rank[target_idx][1:]:
        print(i + 1)  # 인덱스는 0부터 시작하므로 +1을 해야 등수가 됨
        break