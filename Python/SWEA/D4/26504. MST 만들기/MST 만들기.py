T = int(input())
for tc in range(1, T + 1):


    N = int(input())
    
    n_lst = list(map(int, input().split()))
    
    # 오름차순으로 정렬
    n_lst.sort()

    # MST 완성하려면 N - 1개의 간선 필요
    min_cost = sum(n_lst[:N-1])

    # 최댓값 지정
    max_cost = 0
    idx = 0

    # idx가 1, 3, 6, 10...순으로 정렬됨. 
    # 1번 노드부터 N-1번 노드까지
    for step in range(1, N):
        
        max_cost += n_lst[idx]
        
        # 다음 그룹의 시작 인덱스로 넘어가기
        # 사이클에 해당되는 인덱스 건너뛰기
        idx += step
    
    print(f'{min_cost} {max_cost}')