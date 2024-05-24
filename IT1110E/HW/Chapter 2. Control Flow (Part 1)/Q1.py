#Write a program to count the number of even values from a to b, inclusively.

a = int(input())
b = int(input())

if a >= b:
    print("There is no even values from a to b")
else:
    if a % 2 == 1:
        a = a + 1
    if b % 2 == 1:
        b = b - 1
    print(int(((b-a)+2)/2))