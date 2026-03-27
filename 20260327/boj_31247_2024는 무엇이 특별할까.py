# 특별한 수?
import sys
sys.stdin = open('boj_31247_2024는 무엇이 특별할까.txt')
# T = int(input())
# for tc in range(T):
#     N, K = map(int, input().split())
#     if N > 1 and K >= N // 2:
#         print(0)
        
#     else:
#         n = 2
        
#         cnt = 0
#         while n < N:

#             divisor_lst = []
#             for num in range(1, n + 1):
#                 if n % num == 0:
#                     divisor_lst.append(num)
#             even, odd = [], []
#             for i in divisor_lst:
#                 if i % 2 == 0:
#                     even.append(i)
#                 else:
#                     odd.append(i)
#             if len(even) == K * len(odd):
#                 cnt += 1
#             n += 1
#         if N == 1:
#             if K == 0:
#                 print(1)
#             else:
#                 print(cnt)
#         else:

#             print(cnt)

#############################################################################
import sys

T = int(sys.stdin.readline())
for tc in range(T):
    N, K = map(int, sys.stdin.readline().split())
    if K >= 60:
        print(0)
    else:
        total_multiples = N // (2 ** K)
        even_multiples = N // (2 ** (K + 1))
        result = total_multiples - even_multiples    
        print(result) 
        
    
    