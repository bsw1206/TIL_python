import sys
sys.stdin = open('swea_1267_작업순서.txt')

for tc in range(1, 11):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
    
    # 방문 여부 파악
    visited = [0] * (V + 1)
    tree = [[] for _ in range(V + 1)]
    
    # 인접 리스트 생성
    for i in range(E):
        p, c = data[i*2], data[i*2+1]
        tree[p].append(c)
        visited[c] += 1 # 방문 처리
        
    # 큐 생성
    q = []
    # 방문한 적이 없는 i를 모두 넣음
    for i in range(1, V + 1):
        if visited[i] == 0:
            q.append(i)
            
    result = []
    
    # 큐가 빌 때까지 반복
    while q:
        curr = q.pop(0)   # 현재 할 작업 꺼내기
        result.append(curr)  # 결과값에 추가
        
        # 현재 작업을 끝냈으니, 이 작업 다음에 해야 할 작업들을 확인
        for next_node in tree[curr]:
            visited[next_node] -= 1  # 선행 작업 하나 끝났으니 -1 차감
            
            # 만약 선행 작업이 모두 끝났다면(진입 차수가 0이 되었다면) 큐에 추가
            if visited[next_node] == 0:
                q.append(next_node)
                
    print(f'#{tc}', *result) 