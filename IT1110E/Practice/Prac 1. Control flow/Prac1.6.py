#Print a shape that looks like the one below, given the height
#Example: n = 3
#__/\__
#_/  \_
#/    \

n = int(input("Enter your number: "))
for i in range(1, n+1):
    print ((n-i)*"_" + "/" + (i-1)*2*" " + "\\" + (n-i)*"_")

