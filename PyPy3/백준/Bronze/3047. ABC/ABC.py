lst = sorted(map(int, input().split()))
letter = input()

result = [0, 0, 0]
dict = {'A' : 0,
        'B' : 1,
        'C' : 2}

for i in range(3):
    result[i] = lst[dict[letter[i]]]

print(*result)