'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    find = "th"
    stri = len(word)
    th = len(find)
    if (stri == 0 or stri < th):
        return 0
        
    if (word[0:th] == find):
        return count_th(word[th - 1 :]) + 1
        
    return count_th(word[th - 1:])
