N = int(input())
div_num = 2
if N == 1:
    print()
else:
    while N > 1:
        if N % div_num == 0:
            N //= div_num
            print(div_num)
        else:
            div_num += 1