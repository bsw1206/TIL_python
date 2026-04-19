

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
opp_dir = {1 : 2, 2 : 1, 3 : 4, 4 : 3}

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    microbe = [list(map(int, input().split())) for _ in range(K)]
    
    for _ in range(M):

        # 수정 포인트 3: K 대신 len(microbe) 사용
        for i in range(len(microbe)):
            r, c = microbe[i][0], microbe[i][1]
            num = microbe[i][2]
            d = microbe[i][3]
            nr, nc = r + dr[d], c + dc[d]
            
            if 1 <= nr < N-1 and 1 <= nc < N-1:
                # 수정 포인트 1: 리스트의 원소를 직접 수정
                microbe[i][0], microbe[i][1] = nr, nc
            else:
                # 수정 포인트 1: 리스트의 원소를 직접 수정
                microbe[i][0], microbe[i][1] = nr, nc
                microbe[i][2] = num // 2
                microbe[i][3] = opp_dir[d]
                
        # 미생물 큰 순서 대로        
        microbe.sort(key = lambda x: (x[0], x[1], x[2]), reverse=True)
        
        i = 1
        while i < len(microbe):
            
            if microbe[i-1][0] == microbe[i][0] and microbe[i-1][1] == microbe[i][1]:
                
                
                microbe[i-1][2] += microbe[i][2]
                
                microbe.pop(i)
            else:
                i += 1
                
    sum_val = 0
    for a, b, c, d in microbe:
        sum_val += c
    print(f'#{tc} {sum_val}')