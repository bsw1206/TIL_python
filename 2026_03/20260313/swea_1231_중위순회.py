import sys
sys.stdin = open('swea_1231_중위순회.txt')

def inorder(input_node):
    node = int(input_node)

    if node:
        
        inorder(data[node][2])

        print(f'{data[node][1]}', end = '')

        inorder(data[node][3])

        
for tc in range(1, 11):
    N = int(input())
    data = [input().split() for _ in range(N)]

    data.insert(0, [0, 0, 0, 0])

    for i in data:
        if len(i) == 2:
            i.extend(['0', '0'])
        elif len(i) == 3:
            i.extend(['0'])
        
    print(f'#{tc}', end = ' ')
    inorder(data[1][0])
    print()

    