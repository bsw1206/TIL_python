# 알정이 ㅅㅂ
# 나무 : T, 잔디 : G, 울타리 : F, 사람 : P
# N길이의 문자열
# 흥미로운 구간 : 길이가 1 이상인 도로 구간 중 그에 속한 모든 물체의 수가 3의 배수인 것을 의미함.
# 흥미로운 구간이 될 수 있는 도로의 개수 구하기


import sys
sys.stdin = open('boj_24548_도로 정보.txt')
N = int(input())
road = input()



info = {
    'T' : 0,
    'G' : 0,
    'F' : 0,
    'P' : 0,
}

# 
state_dict = {(0, 0, 0, 0): 1}
for char in road:
    info[char] += 1
    # print(info)
    # 각 알파벳의 개수를 3으로 나눈 나머지를 튜플로
    current_state = (
        info['T'] % 3,
        info['G'] % 3,
        info['F'] % 3,
        info['P'] % 3
    )
    # 딕셔너리에 이 상태가 등장한 횟수를 기록함.
    if current_state in state_dict:
        state_dict[current_state] += 1
    else:
        state_dict[current_state] = 1
print(state_dict)
result = 0

for count in state_dict.values():
    if count >= 1:
        result += (count * (count-1)) // 2
print(result)

#######################################################################

