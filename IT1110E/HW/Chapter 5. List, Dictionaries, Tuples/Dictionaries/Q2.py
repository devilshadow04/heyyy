#You are given a text. Write a program to print all the words in the text, one for each line. Words should be
#sorted in descending order of their number of occurrences in the text. Those words with the same number of
#occurrences should be sorted in lexicographic order.

d = dict()
s = input()
while True:
    words = s.split()
    for word in words:
        d[word] = d.get(word, 1) + 1
    try:
        s = input()
    except:
        break

tmp = list()
for k, v in d.items():
    tmp.append((v, k))
tmp.sort(key = lambda x: (-x[0], x[1]))

for v, k in tmp:
    print(k)