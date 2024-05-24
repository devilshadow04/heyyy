#Cho hai số nguyên L, R nhiệm vụ của bạn là xác định có bao nhiêu số trong phạm vi [L, R]
#mà mỗi số khi biểu diễn trong hệ nhị phân có số lượng số bit 1 là số nguyên tố

def prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
                break
            if i == n - 1:
                return True

def dec_to_bin(n):
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    else:
        return str(dec_to_bin(n//2)) + str(n % 2)

L = int(input())
R = int(input())
count = 0
for i in range(L, R+1):
    if prime(int(dec_to_bin(i).count('1'))) is True:
       count += 1
print(count)

