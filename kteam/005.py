#Viết chương trình nhập vào từ bàn phím một số bất kỳ ở hệ thập phân và hiển thị ra màn hình số đó
#ở hệ bát phân (Có xử lý ngoại lệ đầu vào).

a = input()
try:
    print("So thap phan %d trong he bat phan la %o" % (int(a), int(a)))
except:
    print("Dinh dang dau vao khong hop le")

