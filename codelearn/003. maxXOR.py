#Cho 2 số nguyên l và r, tìm giá trị lớn nhất của a xor b, trong đó a và b thoả mãn các điều kiện sau:
#l <= a <= b <= r

def bin_to_dec(n):
    for i in n:
        if i == 1:
            break
        if i == 0:
            del(i)
    dec = 0
    for i in range(len(str(n))):
        dec += 2**(len(str(n))-i-1) * int(str(n)[i])
    return dec
def xor(a, b):
    result_bin = ''
    bin_a = str(bin(a).replace('0b', ''))
    bin_b = str(bin(b).replace('0b', ''))
    if len(bin_a) < len(bin_b):
        bin_a = (len(bin_b) - len(bin_a)) * '0' + bin_a
    else:
        bin_b = (len(bin_a) - len(bin_b)) * '0' + bin_a

    for i in range(len(bin_a)):
        if bin_a[i] == bin_b[i]:
            result_bin += str(0)
        else:
            result_bin += str(1)
    return bin_to_dec(result_bin)

def maxxor(l, r):
    max = xor(l, r)
    for a in range(l, r+1):
        for b in range(a, r+1):
            if xor(a, b) >= max:
                max = xor(a, b)
    return max

print(maxxor(1, 1000))
