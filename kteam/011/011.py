try:
    with open('011.input', 'r') as fileInp:
        ten = fileInp.readline().rstrip('\n')              #Đọc dòng thứ nhất
        tuoi = int(fileInp.readline().rstrip('\n'))        #Đọc dòng thứ hai (Con trỏ đang ở đầu dòng)

    with open('011.output', 'w') as fileOut:
        fileOut.write("20 nam nua, tuoi cua {} se la {}".format(ten, tuoi + 20))
except:
    