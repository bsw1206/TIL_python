import sys
input = sys.stdin.readline
N, M = map(int, input().split())
not_hear = set(input().strip() for _ in range(N))
not_see = set(input().strip() for _ in range(M))

result = sorted(list(not_hear & not_see))

print(len(result))

for person in result:
    print(person)