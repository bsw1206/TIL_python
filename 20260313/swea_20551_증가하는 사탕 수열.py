import sys
sys.stdin = open('swea_20551_증가하는 사탕 수열.txt')
def check(A, B, C, cnt):
    
    
    if C <= 2:
        return -1
    elif B <= 1:
        return -1
    else:
        if B >= C:
            cnt += B - C + 1
            B = C - 1
        if A >= B:
            cnt += A - B + 1
        return cnt

T = int(input())
for tc in range(1, T + 1):
    A, B, C = map(int, input().split())
    
    print(f'#{tc} {check(A, B, C, 0)}')