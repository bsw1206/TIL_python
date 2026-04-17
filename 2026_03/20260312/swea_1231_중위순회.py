import sys
sys.stdin = open('sweA_1231_중위순회.txt')


for tc in range(1, 11):
    N = int(input())
    
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    info_lst = []
    for i in range(1, N + 1):
        info = list(map(str, input().split()))
        
        if len(info) == 4:
            if left[i] == 0:
                left[i] = info[2]
            if right[i] == 0:
                right[i] = info[3]
        if len(info) == 3:
            left[i] = info[2]
        info_lst.append([info[:1]])
    print(left)
    print(right)
        
