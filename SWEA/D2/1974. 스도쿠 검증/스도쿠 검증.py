T = int(input())
for tc in range(1, T + 1):
    result = 1
    lst = [list(map(int, input().split())) for _ in range(9)]
    for i in range(9):
        if len(set(lst[i])) != 9:
            result = 0
            break
    if result != 0:
        for j in range(9):
            column = []
            for k in range(9):
                column.append(lst[k][j])
            if len(set(column)) != 9:
                result = 0
                break
    if result != 0:
        for l in range(0, 9, 3):
            for l2 in range(0, 9, 3):
                squ_lst = []
                for l3 in range(3):
                    for l4 in range(3):
                        squ_lst.append(lst[l3 + l][l4 + l2])
                if len(set(squ_lst)) != 9:
                    result = 0
                    break
    print(f'#{tc} {result}')


