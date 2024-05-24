#Write a program to display such a pattern for n number of rows using a number that will start with the
#number 1 and the first and the last number of each row will be 1.

n = int(input())

for i in range(1, n+1):
    print((n-i+1) * " ", end = '')
    for j in range(1, i):
        print(j, end = '')
    for k in range(i, 0, -1):
        print(k, end = '')
    print()
