#Write a recursive function to convert decimal number (positive integer) to string of binary number

def dec_to_bin(n):
    if n == 1:
        return 1
    else:
        return str(dec_to_bin(n//2)) + str(n % 2)

print(dec_to_bin(456))
