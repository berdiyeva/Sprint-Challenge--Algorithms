'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    
    # base case is if length is 0
    # if the first 2 characters == "th", add 1 and cut off first letter, recurse
    # else do same thing but dont add 1
    if len(word) == 0:
        return 0
    if word[0:2] == "th":
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])

print(count_th(""))
print(count_th("abcthxyz"))
print(count_th("abcthefthghith"))
print(count_th("thhtthht"))
print(count_th("THtHThth"))   