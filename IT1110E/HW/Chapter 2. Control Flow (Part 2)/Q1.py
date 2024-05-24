#Write a program that takes a positive integer n as input and returns the sum of all that number's digits.

n = input()
sum = 0

for i in n:
    sum = sum + int(i)

print(sum)