#Write a lambda function to return the maximum of three numbers. Suggestion: use ternary condition
#in Python [do_this_if_true] if [condition] else [do_this_if_true]. For example:

#f = lambda n: 0 if n % 2 == 0 else 1

f = lambda a, b: a if a >=b else b
g = lambda a, b, c: f(a, b) if f(a, b) >= f(a, c) else f(a, c)

a = int(input())
b = int(input())
c = int(input())

print(g(a, b, c))