#Write a function to find the greatest commmon divisor of 2 positive integers



def gcd(a, b):
    if a % b == 0:
        return b
    for i in range(int(b/2), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

a = int(input())
b = int(input())
print(gcd(a, b))
