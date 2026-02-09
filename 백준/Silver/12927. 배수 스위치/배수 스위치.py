lamp = [0] + list(input())
count = 0
N = len(lamp)
for i in range(1, N):
    if lamp[i] == 'Y':
        count += 1    
        for j in range(i, N, i):
            if lamp[j] == 'Y':
                lamp[j] = 'N'
            else:
                lamp[j] = 'Y'
        

print(count)