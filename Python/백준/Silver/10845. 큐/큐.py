import sys


T = int(sys.stdin.readline())
num_lst = []

for i in range(T):
    word = str(input())
    if word[0:4] == 'push':
        num_lst.append(word[5:])
        
    elif word[0:5] == 'front':
        if num_lst == []:
            print(-1)
        else:
            print(num_lst[0])
        
    elif word[0:4] == 'size':
        print(len(num_lst))
    elif word[0:5] == 'empty':
        if len(num_lst) == 0:
            print(1)
        else:
            print(0)
    elif word[0:3] == 'pop':
        if len(num_lst) == 0:
            print(-1)
        else:
            pop_num = num_lst.pop(0)
            print(pop_num)
    elif word[0:4] == 'back':
        if len(num_lst) == 0:
            print(-1)
        else:    
            print(num_lst[-1])