import sys
input = sys.stdin.readline

def call():
    return int(input())
def call2():
    return list(map(int, input().split()))
def call3():
    return set(map(int, input().split()))
call()
num_list1 = call3()
call()
num_list2 = call2()
for num in num_list2:
    if num in num_list1:
        print(1)
    else:
        print(0)