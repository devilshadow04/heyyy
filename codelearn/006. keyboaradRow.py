#Cho một danh sách words bao gồm các từ, trả về các từ có thể gõ được bằng cách sử dụng các chữ cái
# trong bảng chữ cái và chỉ trên một hàng của bàn phím QWERTY:

def row1(words):
    list = "qwertyuiopQWERTYUIOP"
    for i in words:
        if i in list:
            continue
        else:
            return False
    return True

def row2(words):
    list = "asdfghjklASDFGHJKL"
    for i in words:
        if i in list:
            continue
        else:
            return False
    return True
def row3(words):
    list = "zxcvbnmZXCVBNM"
    for i in words:
        if i in list:
            continue
        else:
            return False
    return True
def keyboardRow(words):
    result = []
    for i in words:
        if row1(i) or row2(i) or row3(i) is True:
            result.append(i)
    return result

print(keyboardRow(["Hello", "Alaska", "Dad", "Peace"]))
