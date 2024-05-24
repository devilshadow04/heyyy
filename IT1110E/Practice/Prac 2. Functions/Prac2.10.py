#Write a lambda function to find the greatest commmon divisor of 2 positive integers.
#Suggestion: use recursive method; you can try to write normal function first and translate it into lambda function

gcd = lambda a, b: b if a % b == 0 else (gcd(a-b, b) if a >= b else gcd(a, b-a))

