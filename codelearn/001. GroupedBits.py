#Given an integer n, count the number of groups of consecutive 1 bits in its binary representation.

def dec_to_bin(n):
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    else:
        return str(dec_to_bin(n//2)) + str(n % 2)

def groupedBits(n):
    bin = list(dec_to_bin(n))
    count = 0

    if n == 1:
        count = 1
    if n > 1:
        if int(bin[0]) == 1:
            count += 1
        for i in range(len(bin)-1):
            if int(bin[i]) == 0 and int(bin[i + 1]) == 1:
                count += 1
    return count

n = int(input())
print(groupedBits(n))