#Write a function to remove all consecutive duplicates in a list and return the new list

def remove_duplicates(s):
    lst = []
    for i in range(len(s)):
        if s[i] == s[i-1]:
            continue
        else:
            lst.append(s[i])
    return lst

print(remove_duplicates([1, 0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4, 5, 5]))
