# n은 총 쌓는 박스 수
# w는 가로로 쌓는 박스의 개수
# num : 꺼내려는 박스의 번호
# 결과값으로 최소 몇개의 박스를 꺼내야 하는지?

# 만약에 딱 나눠서 떨어져
# 그러면 출력값이 

def solution(n, w, num):
    n -= 1
    num -= 1
    
    r_num = num // w
    if r_num % 2 == 0:
        c_num = num % w
    else:
        c_num = w - 1 - (num % w)
    r_last = n // w
    if r_last % 2 == 0:
        c_last = n % w
    else:
        c_last = w - 1 - (n % w)
    top_r = r_last
    if r_last % 2 == 0:
        if c_num > c_last:
            top_r -= 1
    else:
        if c_num < c_last:
            top_r -= 1
    return top_r - r_num + 1