N, r, c = map(int, input().split())

cnt = 0

while N:
    N -= 1
    half = 2 ** N

    if r < half and c < half:
        cnt += 0

    elif r < half and c >= half:
        cnt += half * half 
        c -= half
    elif r >= half and c < half:
        cnt += half * 2 * half
        r -= half
    else:
        cnt += half * 3 * half
        r -= half
        c -= half
print(cnt)