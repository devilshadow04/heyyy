#You are given a text. A word is a sequence of non-blank consecutive characters. Words are separated by
#one or more spaces or end-of-line characters. For each word from this text, you have to count how many times
#it has occurred earlier in this text.

d = dict()
s = input()
while True:
    s.split()
    for word in s.split():
        d[word] = d.get(word, 0) + 1
        print(d[word] - 1, end = ' ')
    try:
        s = input()
    except:
        break
