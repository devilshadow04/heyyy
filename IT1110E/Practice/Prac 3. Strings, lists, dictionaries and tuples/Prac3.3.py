#Write a program to remove all the unneccessary spaces from a string, including leading, trailing
#whitespaces and multiple whitespaces in the middle of the sentence

s = input().strip()
result = ''
for i in range(len(s)):
    if s[i] == ' ' and s[i-1] == ' ':
        continue
    else:
        result += s[i]
print(result)
