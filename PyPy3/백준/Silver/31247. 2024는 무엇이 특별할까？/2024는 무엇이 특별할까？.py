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