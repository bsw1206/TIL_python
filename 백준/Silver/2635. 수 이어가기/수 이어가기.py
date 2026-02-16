T = int(input())

n_lst = []
for i in range(1, T + 1):
    temp_lst = [T, i]
    while True:
        next_val = temp_lst[-2] - temp_lst[-1]
        if next_val >= 0:
            temp_lst.append(next_val)
        else:
            break
    if len(temp_lst) > len(n_lst):
        n_lst = temp_lst
print(len(n_lst))
print(*n_lst)