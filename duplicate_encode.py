# Duplicate Encoder

# The goal of this exercise is to convert a string to a new string where each
# character in the new string is "(" if that character appears only once in the
# original string, or ")" if that character appears more than once in the original
# string. Ignore capitalization when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("

# Notes

# Assertion messages may be unclear about what they display in some languages.
# If you read "...It Should encode XXX", the "XXX" is the expected result, not
# the input!

def duplicate_encode(word):
    word = word.lower()
    new_word = list(word)
    for i, letter in enumerate(new_word):
        count = 0
        for a in word:
            if new_word[i] == a:
                count = count + 1
        if count == 1:
            new_word[i] = '('
        elif count > 1:
            new_word[i] = ')'

    return("".join(map(str, new_word)))

test = duplicate_encode('(( @')
print(test)
