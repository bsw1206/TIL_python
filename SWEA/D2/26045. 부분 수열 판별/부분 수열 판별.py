#import sys 

#sys.stdin = open('swea_26045_부분 수열 판별.txt')
T = int(input())
for tc in range(1, T + 1):
    A, B = map(int, input().split())
    A_lst = list(map(int, input().split()))
    B_lst = list(map(int, input().split()))
    count = 0
    for i in range(B):
        for j in range(len(A_lst)):
            if B_lst[i] == A_lst[j]:
                A_lst = A_lst[j+1:]
                count += 1
                break
        if count == len(B_lst):
            result = 'YES'
            break
        else:
            result = 'NO'
    print(f'#{tc} {result}')
        
        
