#Given a string, write a recursive function is_palindrome(str) to check if it is palindrome or not.
#The function returns 'YES' if the input string is palindrome. Otherwise, the function returns 'NO'.
#A string is said to be palindrome if the reverse of the string is the same as string, where spaces are ignored.

def reverse_string(str):
    if len(str) == 1:
        return str
    else:
        return str[len(str) - 1] + reverse_string(str[0 : (len(str) - 1)])

def is_palindrome(str):
    if str.lower().replace(" ", "") == reverse_string(str).lower().replace(" ", ""):
        return "YES"
    else:
        return "NO"

print(is_palindrome('malayalam'))
print(is_palindrome('Bach khoa Ha Noi'))
print(is_palindrome('borrow or rob'))

