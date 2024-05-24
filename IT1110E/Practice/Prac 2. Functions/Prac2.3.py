#Write a function to print all the prime numbers less than a given number.
#Note: you can define additional functions for better use

def prime(n):
    for i in range(1, n):
        if i == 1:
            continue
        elif i == 2:
            print(i, end = ' ')
        else:
            for j in range(2, i):
                if i % j == 0:
                    break
                if j == i-1:
                    print(i, end = ' ')

n = int(input())
prime(n)

