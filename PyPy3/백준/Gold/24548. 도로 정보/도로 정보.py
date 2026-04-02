import sys

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

    current_state = (
        info['T'] % 3,
        info['G'] % 3,
        info['F'] % 3,
        info['P'] % 3
    )

    if current_state in state_dict:
        state_dict[current_state] += 1
    else:
        state_dict[current_state] = 1
result = 0

for count in state_dict.values():
    if count >= 1:
        result += (count * (count-1)) // 2
print(result)
