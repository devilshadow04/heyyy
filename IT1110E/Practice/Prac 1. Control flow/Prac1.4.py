# The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows:
#start with any positive integer n. If the previous term is even, the next term is one half of the previous term.
#If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that no
#matter what value of n, the sequence will always reach 1.
# For instance, starting with n = 12, one gets the sequence 12, 6, 3, 10, 5, 16, 8, 4, 2, 1.
# Given the starting number, print the value of all the numbers in its path to 1

n = int(input("Enter your first number: "))
print(n, end = " ")
while n != 1:
    if n % 2 == 0:
        n = int(n/2)
    else:
        n = 3*n + 1
    print(n, end = " ")

