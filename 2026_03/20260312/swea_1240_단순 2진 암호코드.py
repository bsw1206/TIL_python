# 8개의 숫자로 구성
# 숫자 하나는 7개의 비트로 암호화 -> 가로 길이는 56이다.
# 올바른 암호코드인지 판별하는 프로그램 -> 올바를 경우, 암호코드에 포함된 숫자의 합을 출력
# 잘못된 암호코드는 0 출력
# N, M = 세로, 가로 크기(1<=N<=50, 56<=M<100)
import sys
sys.stdin = open('swea_1240_단순 2진 암호코드.txt')
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pw_info = [input() for _ in range(N)]
    rule = {
         '0001101' : 0,
         '0011001' : 1,
         '0010011' : 2,
         '0111101' : 3,
         '0100011' : 4,
         '0110001' : 5,
         '0101111' : 6,
         '0111011' : 7,
         '0110111' : 8,
         '0001011' : 9,
    }
    code_str = ''
    for i in range(N):
        if '1' in pw_info[i]: # 암호가 있는 줄을 찾기
            for j in range(M -1, -1, -1):
                if pw_info[i][j] == '1': 
                    # 암호의 뒷 자리가 다 1이므로 1로 끝나는 지점부터 56번째 앞 지점을 지정
                    code_str = pw_info[i][j - 55 : j + 1]
                    break
            break
    num = []
    for i in range(0, 56, 7):
        num.append(rule[code_str[i : i + 7]]) # 암호 쪼개고 정수로 바꾸어 리스트에 넣기
    # idx 짝수 홀수 번갈아 넣기
    odd_num, even_num = 0, 0
    for i in range(8):
        if i % 2 == 0:
            odd_num += num[i]
        else:
            even_num += num[i]
    # 합계 계산
    sum_val = odd_num * 3 + even_num
    if sum_val % 10 == 0:
        print(f'#{tc} {sum(num)}')
    else:
        print(f'#{tc} 0')

 

            