import sys
sys.stdin = open('swea_1238_Contact.txt')
from collections import deque
for tc in range(1, 11):
    N, S = map(int, input().split())
    p_lst = list(map(int, input().split()))
    adj_lst = [[] for _ in range(101)]

    for i in range(N // 2):
        # 1. 인접 리스트 생성
        fm = p_lst[i * 2]
        to = p_lst[i * 2 + 1]

        if to not in adj_lst[fm]:
    
            adj_lst[fm].append(to)
    
    # 2. BFS

    # 방문 여부
    visited = [0] * 101
    # 시작 노드
    q = deque([S])
    
    # 2-1. 방문 처리와 동시에 얼마나 떨어져 있는지 파악하기 위함
    visited[S] = 1
    
    while q:
        # 2-2. 시작 노드와 연결되어있는 노드를 모두 도는 과정
        node = q.popleft()
        # 현재 node와 연결되어 있는 node
        for next_node in adj_lst[node]:
            # 방문하지 않은 곳이면,
            if not visited[next_node]:
                # 방문처리를 하긴 하는데 현재 위치에서 1만큼 더함.
                visited[next_node] = visited[node] + 1
                q.append(next_node)

    # 3. 답 찾기

    # 제일 오래 걸린 노드들을 찾음.
    max_time = 0
    for j in range(1, 101):
        if visited[j] > max_time:
            max_time = visited[j]

    # # 3-1. 거꾸로 돌면서 제일 멀리 떨어진 노드 찾자마자 종료
    # for k in range(99, -1, -1):
    #     if visited[k] == max_time:
    #         print(f'#{tc} {k}')
    #         break
    
    # 3-2. 제일 멀리 떨어진 노드를 다 모으고 최댓값 출력
    ans_lst = []
    for k in range(101):
        if visited[k] == max_time:
            ans_lst.append(k)


    print(f'#{tc} {ans_lst[-1]}')
    