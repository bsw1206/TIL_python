

import sys
sys.stdin = open('input2.txt')
T = int(input())
for tc in range(1, T + 1):
    hexadecimal = input().strip()
    # print(hexadecimal)
    change_lst = {
        '0' : '0000',
        '1' : '0001',
        '2' : '0010',
        '3' : '0011',
        '4' : '0100',
        '5' : '0101',
        '6' : '0110',
        '7' : '0111',
        '8' : '1000',
        '9' : '1001',
        'A' : '1010',
        'B' : '1011',
        'C' : '1100',
        'D' : '1101',
        'E' : '1110',
        'F' : '1111',
    }
    real_num = []
    for i in hexadecimal:
        real_num.append(change_lst[i])
    # 2진수로 변환하는 과정
    real_num = ''.join(real_num)
    # 결과값 지정
    result = []
    idx = 0
    while idx <= len(real_num):
        # 7개씩 자르기
        chunk = real_num[idx : idx+ 7]
        if chunk == '0000000':
            idx += 4
        else:
            result.append(int(chunk, 2))
            idx += 7
    
    print(f'#{tc}', *result)


