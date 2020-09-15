# Split Strings

# Description:
# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace the
# missing second character of the final pair with an underscore ('_').

# Examples:
#
# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

def solutions(s):
    s = str(s)
    lst = list()
    length = len(s)
    if length % 2 == 0:
        for letters in range(0,length,2):
            lst.append(s[letters:(letters+2)])
        return(lst)
        quit()
    else:
        s2 = s + '_'
        length2 = len(s2)
        for letters2 in range(0,length2,2):
            lst.append(s2[letters2:(letters2+2)])
        return(lst)

test = solutions('x')
print(test)
