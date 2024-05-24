#Write a function that returns the mirror image of a string (contains lowercase characters only)
#if that mirror image is still a valid string. Otherwise, return "NOT POSSIBLE".

#Note: b, d, i, o, p, q, v, w, x are characters with the mirror images still valid English characters

#Example: Input: void, Output: biov

pos_let = 'bdiopqvwx'
s = input()

def possible(s):
    for i in s:
        if i in pos_let:
            continue
        else:
            return False
    return True

result = ''
if possible(s) is False:
    print("NOT POSSIBLE")
else:
    for i in range(len(s)):
        if s[i] == 'i' or s[i] == 'o' or s[i] == 'v' or s[i] == 'w' or s[i] == 'x':
            result = s[i] + result
        if s[i] == 'b':
            result = 'd' + result
        if s[i] == 'd':
            result = 'b' + result
        if s[i] == 'p':
            result = 'q' + result
        if s[i] == 'q':
            result = 'p' + result
    print(result)
