T = int(input())
for tc in range(1, T + 1):
    a, b = input().split()
    changed_a = a.replace(b, 'ㅋ')
    print(f'#{tc} {len(changed_a)}')
