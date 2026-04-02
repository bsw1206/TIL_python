import sys
# sys.stdin = open('boj_11723_집합.txt')
input = sys.stdin.readline

M = int(input())
S = 0  # 집합을 대신할 단 하나의 정수 (초기값 0 = 모든 비트가 꺼져있음)

for _ in range(M):
    cmd = input().split()
    
    if cmd[0] == 'all':
        # 1부터 20까지 모든 비트를 1로 켬 (이진수 111111111111111111110)
        S = (1 << 21) - 1 
    elif cmd[0] == 'empty':
        # 모든 비트를 0으로 끔
        S = 0
    else:
        op = cmd[0]
        x = int(cmd[1])
        
        if op == 'add':
            S |= (1 << x)  # x번째 비트를 1로 켬 (OR 연산)
            
        elif op == 'remove':
            S &= ~(1 << x) # x번째 비트를 0으로 끔 (AND NOT 연산)
            
        elif op == 'check':
            if S & (1 << x): # x번째 비트가 켜져 있는지 확인 (AND 연산)
                print(1)
            else:
                print(0)
                
        elif op == 'toggle':
            S ^= (1 << x)  # x번째 비트 상태를 뒤집음 (XOR 연산)