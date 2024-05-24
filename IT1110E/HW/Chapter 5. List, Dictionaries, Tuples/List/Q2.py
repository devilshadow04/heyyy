#Write a program to find the element closest in magnitude to a given number in an array.
n = int(input())
num = input()
a = int(input())
elements = list(map(int, num.split()))
min = elements[0]
min_diff = abs(elements[0] - a)

for i in range(1, n):
    if abs(elements[i] - a) <= min_diff:
        min = elements[i]
        min_diff = abs(elements[i] - a)

print(min)