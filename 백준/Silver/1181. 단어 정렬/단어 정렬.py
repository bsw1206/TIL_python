N = int(input())
word_list = list()
for i in range(N):
    a = str(input())
    word_list.append(a)
word_list = list(set(word_list))
word_list.sort(key=lambda x: (len(x),x))

for j in word_list:
        print(j)