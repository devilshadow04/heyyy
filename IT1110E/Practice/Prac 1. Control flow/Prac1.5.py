#Write a program to check if an integer is a prime number or not

import math
n = int(input("Enter the number: "))
if n <= 1:
    print("not prime")
elif n == 2:
    print("prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("{} is not a prime number, because {} is a factor of {}".format(n, i, n))
            break
        if i == n-1:
            print ("n is a prime number")



