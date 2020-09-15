# Description

# Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns
# the same string with all even indexed characters in each word upper cased, and
# all odd indexed characters in each word lower cased. The indexing just explained
# is zero based, so the zero-ith index is even, therefore that character should be upper cased.

# The passed in string will only consist of alphabetical characters and spaces(' ').
# Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

# Examples:
# to_weird_case('String'); # => returns 'StRiNg'
# to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'

def to_weird_case(string):
    new_word = string.split()
    new_word2 = []
    for word in new_word:
        length = len(word)
        new_word3 = list(word)
        for i in range(0,length,2):
            new_word3[i] = word[i].upper()
        new_word2.append(new_word3)

    final_word = [''.join(x) for x in new_word2]
    return(" ".join(map(str, final_word)))


test = to_weird_case('This is a test')
print(test)
