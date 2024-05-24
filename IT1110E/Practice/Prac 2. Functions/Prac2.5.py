#Write a recursive function to print the nth Fibonacci number, given a positve integer n.
#Assume that the 1st and the 2nd Fibonacci numbers are 1.

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))