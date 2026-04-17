N = int(input())
for i in range(1, N + 1):
    lst = [' '] * (N - i) + ['*'] * i
    print(''.join(lst))