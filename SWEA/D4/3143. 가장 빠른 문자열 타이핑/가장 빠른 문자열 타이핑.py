T = int(input())
for tc in range(1, T + 1):
    a, b = input().split()
    a = a.replace(b, '5')
    print(f'#{tc} {len(a)}')