T = int(input())
for i in range (T):
    a = int(input())
    b = int(input())
    
    sum_lst = []
    for l in range(1, b + 1):
        
        sum_lst.append(l)
    for k in range(a):
        
        for j in range (1 ,b):
            sum_lst[j] += sum_lst[j-1]
    print(sum_lst[-1])