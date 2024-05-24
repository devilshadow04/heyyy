#Write a program to print a string consists of every second character of the string in reverse order
#starting from the last one and with the first character in the result string capitalized
#(the other characters are lowercase)

s = input()
result = s[-1].upper()
for i in range(len(s)//2-1, -1, -1):
    result += s[2*i]
print(result)