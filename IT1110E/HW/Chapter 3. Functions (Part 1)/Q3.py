#Write a function reverse(n) that takes a positive integer as input are print n in the reverse order.

def reverse(n):
    reverse = 0
    k = 1
    for i in str(n):
        reverse = reverse + int(i) * k
        k = k * 10
    return reverse

n = int(input("Enter your number: "))
print(reverse(n))
