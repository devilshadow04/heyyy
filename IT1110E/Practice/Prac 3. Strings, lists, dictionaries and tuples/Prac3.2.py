#In naming convention of some languages, variables are often named using Camel case convention
#(for example: ArrayOfNumber), while in other languages (including Python),
#variables are named using Snake case convention (for example: array_of_number)

#Write a program to convert a string from Snake case to Camel case

s = input()
result = s[0].upper()
for i in range(1, len(s)):
    if s[i-1] == '_':
        result += s[i].upper()
    else:
        result += s[i]

print(result.replace('_', ''))