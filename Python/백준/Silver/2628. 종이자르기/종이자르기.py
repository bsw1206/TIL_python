c, r = map(int, input().split())
s_num = int(input())
r_lst = [] + [0, r]
c_lst = [] + [0, c]
for i in range(s_num):
    rc, length = map(int, input().split())
    if rc == 0:
        r_lst.append(length)
    else:
        c_lst.append(length)

r_lst.sort()
c_lst.sort()
r_len , c_len = [], []
for i in range(1, len(r_lst)):
    r_len.append(r_lst[i]-r_lst[i-1])
for i in range(1, len(c_lst)):
    c_len.append(c_lst[i]-c_lst[i-1])



print(max(r_len) * max(c_len))