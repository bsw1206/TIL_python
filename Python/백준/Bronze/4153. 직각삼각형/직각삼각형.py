while True:
    try:
        a, b, c = list(map(int, input().split()))
        if a > b and a > c:
            if (a * a) == ((b * b) + (c * c)):
                print('right')
            else:
                print('wrong')
        elif b > a and b > c:
            if (b * b) == ((c * c) + (a * a)):
                print('right')
            else:
                print('wrong')
        elif c > b and c > a:
            if (c * c) == ((b * b) + (a * a)):
                print('right')
            else:
                print('wrong')
    except:
        if (a, b, c) == (0, 0, 0):
            break