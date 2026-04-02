T = int(input())
for i in range(1, T + 1):
    a, b = input().split()
    a = int(a)
    for x in b:
        print(x * a, end = '')
    print()