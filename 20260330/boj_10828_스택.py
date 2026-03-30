import sys
sys.stdin = open('boj_10828_스택.txt')
N = int(input())
stack = []
for _ in range(N):
    letter = input().strip()
    if 'push' in letter:
        stack.append(int(letter[5:]))
    elif letter == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    elif letter == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif letter == 'size':
        print(len(stack))
    elif letter == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
