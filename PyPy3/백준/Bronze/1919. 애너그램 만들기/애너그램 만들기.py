l1 = input()
l2 = input()
l1_lst = {}
l2_lst = {}
for i in l1:
    if i not in l1_lst:
        l1_lst[i] = 1
    else:
        l1_lst[i] += 1
for i in l2:
    if i not in l2_lst:
        l2_lst[i] = 1
    else:
        l2_lst[i] += 1

result = 0
for word, num in l1_lst.items():
    if word in l2_lst.keys():
        result += abs(num - l2_lst[word])
    else:
        result += num
for word, num in l2_lst.items():
    if word not in l1_lst.keys():
        result += num

print(result)