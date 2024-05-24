#Write a program to remove all consecutive duplicated characters of a given string.
#The output must be written in lowercase. The program is not case-sensitive.
#For example, in the test case below, characters 'c' and 'C' are treated as the same one, and in the output,
#the lowercase character 'c' is written out.

s = input() + " "
for i in range(len(s)-1):
    if s[i].lower() != s[i+1].lower():
        print(s[i].lower(), end = '')



