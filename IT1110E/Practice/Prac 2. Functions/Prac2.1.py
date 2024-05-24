#In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive
#divisors, that is, the sum of its positive divisors excluding the number itself.
#Write a function to check whether a number is a perfect number or not

def sum_of_divisors(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum = sum + i
    return sum

n = int(input())
if n == sum_of_divisors(n):
    print("perfect number")
else:
    print("not perfect number")

