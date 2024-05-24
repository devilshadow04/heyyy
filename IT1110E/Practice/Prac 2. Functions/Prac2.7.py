#Write a recursive function to compute the sum of digits of a number

def sum_of_digits(n):
    if n <= 9:
        return n
    else:
        return sum_of_digits(n//10) + n % 10

n = int(input())
print(sum_of_digits(n))