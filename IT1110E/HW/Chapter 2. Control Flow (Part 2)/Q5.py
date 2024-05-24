#Write a program to check whether a number can be expressed as the sum of two prime numbers.
def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sum_of_two_prime(n):
    for i in range(1,n):
        if prime(i) and prime(n-i):
            return True
    return False

n = int(input())
for i in range(n):
    x= int(input())
    if sum_of_two_prime(x):
        print("YES")
    else:
        print("NO")