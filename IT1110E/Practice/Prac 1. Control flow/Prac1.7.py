# One way of computing square roots is Newton's method. Suppose that you want to know the square root
#of a. If you start with (almost) any estimate x, then you can get a better estimate with the formula:
#y = (x + a/x)/2
# Given a non-negative number a, compute the square root of that number using Newton's method with the precision
#of 0.0000001

a = int(input("Enter your number: "))
x = 50
while x > 0:
    root = (x+a/x)/2
    if (abs(x-root) < 0.0000001):
        break
    x = root

print(root)

