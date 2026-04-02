# import sys
# sys.stdin = open('boj_1764_듣보잡.txt')
# N, M = map(int, input().split())
# not_hear = {}
# for _ in range(N):
#     name = input()
#     if name not in not_hear.keys():
#         not_hear[name] = 1
#     else:
#         not_hear[name] += 1
# not_see = {}
# for _ in range(M):
#     name = input()
#     if name not in not_see.keys():
#         not_see[name] = 1
#     else:
#         not_see[name] += 1

# result = []

# for p in not_see:
#     if p in not_hear.keys():
#         result.append(p)
            
# result.sort()
# print(len(result))
# for person in result:
#     print(person)


#######################################################

import sys
sys.stdin = open('boj_1764_듣보잡.txt')
N, M = map(int, input().split())
not_hear = set(input().strip() for _ in range(N))
not_see = set(input().strip() for _ in range(M))

result = sorted(list(not_hear & not_see))

print(len(result))

for person in result:
    print(person)