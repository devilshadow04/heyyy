#Cho một chuỗi ký tự alphabet, hãy chuyển đổi chuỗi này thành dữ liệu có thể truyền trực tiếp giữa các
#máy tính.

def text_to_binary(n):
    result = ''
    for i in n.strip():
        bin_i = bin(ord(i)).replace('0b', '')
        if len(bin_i) < 8:
            bin_i = (8-len(bin_i)) * '0' + bin_i
        result = result + bin_i + " "
    return result.rstrip()

print(text_to_binary('Hasagi'))