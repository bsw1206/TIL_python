# 여러 그룹으로 나눠서 관리하는데
# 그룹에 속한 부품들의 크기의 합이 A를 넘기지 않고, 무게의 합이 B를 넘기지 않게 한다.
# 그룹의 수를 최소화하려고 함.
import sys
sys.stdin = open('boj_24724_현대모비스와 함께하는 부품 관리.txt')
T = int(input())
for tc in range(1, T + 1):
    print(f'Material Management {tc}')
    print('Classification ---- End!')