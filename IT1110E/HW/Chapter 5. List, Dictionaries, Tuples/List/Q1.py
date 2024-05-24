#Given a sequence of integers, print out all the elements that are strictly larger than the previous one.
#The program should print 'NONE' if such an element does not exist.

n = input()
num = n.split()
sequence = list(map(int, num))
list = []
for i in range(1, len(sequence)):
    if sequence[i] > sequence[i-1]:
        list.append(sequence[i])
if list == []:
    print("NONE")
else:
    for i in range(len(list)):
        print(list[i], end = ' ')