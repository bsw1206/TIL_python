a, b, c = list(map(int, input().split()))
climb = ((c-b) + (a-b) -1) // (a-b)
print(climb)