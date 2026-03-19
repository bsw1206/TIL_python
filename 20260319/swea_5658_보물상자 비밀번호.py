# 보물상자에 걸려 있는 자물쇠를 여는데, 
# 자물쇠의 비밀번호는 보물 상자에 적힌 숫자로 만들 수 있는 모든 수 중, K번째로 큰 수를 10진수로 만든 수이다.
# 보물상자의 비밀번호를 출력하는 프로그램.
# N은 4의 배수, 8이상 28이하의 정수이다.


# 11일때 1개더 12일때 2개더(11- 12 + (N//4))
# list에서 
import sys
sys.stdin = open('swea_5658_보물상자 비밀번호.txt')
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    num = input()
    
    n_lst = []
    for i in range(len(num)):
        n_lst.append(num[i:i+(N//4)])
        if len(n_lst[i]) != N // 4:
            n_lst[i] = num[i:i+(N//4)] + num[:i-N+(N//4)]
    
    for i in range(len(n_lst)):
        n_lst[i] = int(n_lst[i], 16)
    
    n_lst = set(n_lst)
    n_lst = list(n_lst)
    n_lst.sort(reverse=True)

    print(f'#{tc} {n_lst[K-1]}')
