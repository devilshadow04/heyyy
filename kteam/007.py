#Viết chương trình làm tròn số thập phân A đến B chữ số sau dấu phẩy. A và B được nhập bất kỳ từ bàn
# phím. Hiển thị số A sau khi được làm tròn ra màn hình (Có xử lý ngoại lệ đầu vào).

a = input()
b = input()

try:
    print("{:.{}f}".format(float(a), int(b)))
except:
    print("Dinh dang dau vao khong hop le")