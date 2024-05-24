#Write a function remove_duplicates(lst) that receives a given list as input and returns another
#list that contains those elements that appear in the input list only once.
#These elements should be displayed in the order in which they appear in the input list.

def remove_duplicates(lst):
    result = []
    for i in lst:
        if lst.count(i) == 1:
            result.append(i)
    return result

print(remove_duplicates([4, 3, 5, 2, 5, 1, 3, 5]))
