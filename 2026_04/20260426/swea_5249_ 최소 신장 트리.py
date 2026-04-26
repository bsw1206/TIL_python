import sys
sys.stdin = open('swea_5249_최소 신장 트리.txt')

# 1. 루트 노드를 찾는 함수 (Find)
def find_set(x):
    # 자기 자신이 부모라면 그게 바로 루트 노드
    if parents[x] == x:
        return x
    # 경로 압축(Path Compression) 기법: 
    # 루트 노드를 찾으면서 만나는 모든 노드의 부모를 바로 루트로 바꿔버림 (탐색 속도 대폭 향상)
    parents[x] = find_set(parents[x])
    return parents[x]

# 2. 두 트리를 하나로 합치는 함수 (Union)
def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)
    
    # 이미 같은 루트를 공유한다면 합칠 필요 없음 (이 코드는 사실 호출 전 검사해서 생략 가능)
    if root_x == root_y:
        return
    
    # 더 작은 번호를 가진 노드를 부모로 설정 (일관성을 위해)
    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y


T = int(input())
for tc in range(1, T + 1):
    # V: 마지막 노드 번호 (0번부터 시작하므로 총 노드 개수는 V + 1개)
    # E: 간선의 개수
    V, E = map(int, input().split())
    
    # 크루스칼은 인접 리스트 대신 간선 리스트만 있으면 됩니다.
    edges = []
    for _ in range(E):
        n1, n2, weight = map(int, input().split())
        # 나중에 정렬하기 쉽도록 가중치(weight)를 튜플의 첫 번째에 둡니다.
        edges.append((weight, n1, n2))
        
    # 가중치를 기준으로 오름차순 정렬 (가장 가벼운 간선부터 확인하기 위해)
    edges.sort()
    
    # Union-Find를 위한 부모 리스트 초기화 (처음엔 모두 자기 자신이 부모)
    parents = [i for i in range(V + 1)]
    
    sum_val = 0 # 가중치 합계
    cnt = 0     # 연결된 간선의 개수
    
    # 정렬된 간선을 하나씩 꺼내면서 확인
    for weight, n1, n2 in edges:
        # 두 노드의 최상위 부모(루트)가 다르다면 = 연결해도 사이클이 생기지 않는다면!
        if find_set(n1) != find_set(n2):
            union(n1, n2)      # 두 노드를 연결
            sum_val += weight  # 가중치 누적
            cnt += 1           # 간선 개수 1 증가
            
            # 신장 트리의 특징: 간선의 개수는 항상 (전체 노드 수 - 1)개
            # 총 노드가 V+1개이므로 간선을 V개 찾았다면 완성된 것! (조기 종료)
            if cnt == V:
                break
                
    print(f'#{tc} {sum_val}')