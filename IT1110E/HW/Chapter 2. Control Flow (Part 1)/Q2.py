#Write a Python program to find the largest of three numbers.

a = int(input())
b = int(input())
c = int(input())

if a > b:
    if c > a:
        print(c)
    else:
        print(a)
else:
    if c > b:
        print(c)
    else:
        print(b)