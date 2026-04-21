import sys
sys.stdin = open('swea_5643_키 순서.txt')

def dfs(node, adj, visited):
    count = 0
    # 현재 노드와 연결된(나보다 크거나/작은) 이웃들을 확인
    for neighbor in adj[node]:
        # 아직 카운트하지 않은 사람이라면
        if not visited[neighbor]:
            visited[neighbor] = True  # 방문 처리
            count += 1                # 사람 수 1명 추가
            # 그 이웃과 연결된 사람들도 마저 탐색해서 더해줌
            count += dfs(neighbor, adj, visited)
    return count

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    M = int(input())
    
    # 1. 정방향 그래프 (나보다 큰 사람을 향함)
    taller_adj = [[] for _ in range(N + 1)]
    # 2. 역방향 그래프 (나보다 작은 사람을 향함)
    shorter_adj = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        a, b = map(int, input().split())
        taller_adj[a].append(b) 
        shorter_adj[b].append(a) 

    result = 0

    
    for i in range(1, N + 1):
        
        visited_taller = [False] * (N + 1)
        visited_shorter = [False] * (N + 1)
        
        
        visited_taller[i] = True
        visited_shorter[i] = True
        
        # 정방향 탐색: 나보다 큰 사람 수 구하기
        up = dfs(i, taller_adj, visited_taller)
        # 역방향 탐색: 나보다 작은 사람 수 구하기
        down = dfs(i, shorter_adj, visited_shorter)
        
        # 회원님의 빛나는 아이디어!
        if up + down == N - 1:
            result += 1
            
    print(f'#{tc} {result}')