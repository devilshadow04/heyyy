#Write a function to_uppercase(str) to convert a given string to all uppercase if it contains
#at least 2 uppercase characters in the first 4 characters.

def to_uppercase(str):
    count = 0
    for i in range(4):
        if str[i].isupper() == True:
            count = count + 1
        if count == 2:
            return str.upper()
            break
    return str

print(to_uppercase('aBZ2 Da@s hi'))
print(to_uppercase('aBz    da@s hi'))