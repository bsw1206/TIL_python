import sys
sys.stdin = open('swea_1267_작업순서.txt')
def dfs(i):
    # 방문처리
    visited[i] = True
    # 이웃을 도는 과정
    for neighbor in tree[i]:
        # tree값이 방문하지 않은 곳이면?
        if not visited[neighbor]:
            # 다시 찾아
            dfs(neighbor)
    # result에 i 추가
    result.append(i)


for tc in range(1, 11):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
    # 방문 여부
    visited = [False] * (V + 1)
    # 트리 작성
    tree = [[] for _ in range(V + 1)]
    for i in range(E):
        # parent가 인덱스 값, c가 p 안의 값    
        p, c = data[i*2], data[i*2+1]
        tree[p].append(c)

    result = []
    # 정점을 돌면서
    for i in range(1, V + 1):
        # 방문하지 않은 곳이면 DFS 함수 돌리기
        if not visited[i]:
            dfs(i)
    print(f'#{tc}', *result[::-1])    
    