
def find_set(parent, x):
    if parent[x] != x:
        parent[x] = find_set(parent, parent[x])
    
    return parent[x]

def union(parent, rank, x, y):
    ref_x = find_set(parent, x)
    ref_y = find_set(parent, y)

    if ref_x == ref_y:
        return
    
    if ref_x > ref_y:
        parent[ref_y] = ref_x
    elif ref_y > ref_x:
        parent[ref_x] = ref_y
    else:
        parent[ref_x] = ref_y
        rank[ref_x] += 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))


    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)

    for i in range(M):
        p1, p2 = lst[i * 2], lst[i * 2 + 1]
        union(parent, rank, p1, p2)
    result = set()
    for i in range(1, N + 1):
        result.add(find_set(parent, i))
    print(f'#{tc} {len(result)}')
