import sys
sys.stdin = open('swea_10580_전봇대.txt')





T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cable = [list(map(int, input().split())) for _ in range(N)]

    cable.sort(key = lambda x: x[0])
    cnt = 0

    for i in range(N):
        for j in range(i + 1, N):
            if cable[i][1] > cable[j][1]:
                cnt += 1
    print(f'#{tc} {cnt}')



  
             