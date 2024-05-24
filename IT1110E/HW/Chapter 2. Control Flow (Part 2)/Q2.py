#Write a program to display the pattern like a diamond.

n = int(input())
i = 1
j = n + 1
while i <= n:
    print((n-i) * " " + (2*i-1) * "*")
    i += 1
while j <= 2*n:
    print((j - n) * " " + (2*(2 * n - j) - 1) * "*")
    j += 1