#Viết chương trình nhập vào từ bàn phím một số bất kỳ ở hệ thập phân và hiển thị ra màn hình số đó
#ở hệ bát phân.

def dec_to_oct(n):
    if n < 8:
        return n
    else:
        return str(dec_to_oct(n//8)) + str(n % 8)

n = int(input())
print("So thap phan {} trong he bat phan la {}".format(n, dec_to_oct(n)))

