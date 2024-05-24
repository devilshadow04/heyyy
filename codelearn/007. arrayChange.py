#Cho một mảng các số nguyên. Trên mỗi lần di chuyển, bạn được phép tăng chính xác từng phần tử của
#nó thêm 1. Tìm số lần di chuyển tối thiểu cần thiết để có được một chuỗi tăng dần từ đầu vào.

def arrayChange(a):
    count = 0
    for i in range(len(a)-1):
        while a[i] >= a[i+1]:
            a[i+1] += 1
            count += 1
    return count

print(arrayChange([1, 1, 1]))

