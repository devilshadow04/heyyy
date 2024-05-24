#Write a function friendly(a, b) that takes two positive integers as input and returns 'YES' if a and b
#are friendly numbers. Otherwise, the function returns 'NO'.

def sum_of_divisors(x):
    sum = 0
    for i in range(1, x):
        if x % i == 0:
            sum = sum + i
    return sum

def friendly(a, b):
    if sum_of_divisors(a) == b and sum_of_divisors(b) == a:
        return "YES"
    return "NO"