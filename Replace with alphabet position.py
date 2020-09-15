# Replace With Alphabet Position

# In this kata you are required to, given a string, replace every letter with its
# position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.

# Example
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

import string
alphabets = dict(zip(string.ascii_lowercase, range(1,27)))

def alphabet_position(text):
    text = text.lower()
    lst = list(text)
    lst2 = []
    for i in lst:
        for k, v in alphabets.items():
            if i == k:
                lst2.append(v)
    final_text = " ".join(map(str, lst2))
    return (final_text)

test = alphabet_position("The sunset sets at twelve o' clock.")
print(test)
