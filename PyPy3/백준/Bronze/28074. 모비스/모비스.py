letter = input()
letter_dict = {}
result = 'NO'
for i in letter:
    if i in letter_dict.keys():
        letter_dict[i] += 1
    else:
        letter_dict[i] = 1
    if 'M' in letter_dict.keys() and 'O' in letter_dict.keys() and 'B' in letter_dict.keys() and\
    'I' in letter_dict.keys() and 'S' in letter_dict.keys():
        result = 'YES'
        break
print(result)