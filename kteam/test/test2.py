count = 0
f = open("info1110.txt")
result = []
while True:
    line = f.readline()
    count += 1
    line_lst = line.strip().split(", ")
    if len(line_lst) == 2:
        name = line_lst[0]
        mark = line_lst[1]
        try:
            mark = int(mark)
            result.append((name, mark))
        except:
            continue

    if count >= 10:
        break
print(result)
f.close()