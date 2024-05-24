#Write a function digit_sum_greater(a, b) that takes two positive integers a, b as input and returns
#'YES' if the sum of all a's digits is strictly greater than the sum of all b's digits. Otherwise, the function returns 'NO'

def sum_of_digits(a):
    sum = 0
    for i in str(a):
        sum = sum + int(i)
    return sum

def digit_sum_greater(a, b):
    if sum_of_digits(a) > sum_of_digits(b):
        return "YES"
    return "NO"