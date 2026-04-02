T = int(input())
for i in range(1 , T + 1):
    calculate = list(input().split())
    num = float(calculate[0])
    for x in range(1, len(calculate)):
        if calculate[x] == '@':
            num *= 3
        elif calculate[x] == '%':
            num += 5
        elif calculate[x] == '#':
            num -= 7
    print(f'{num:.2f}')