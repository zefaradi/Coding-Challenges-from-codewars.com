# Equal sides of an array
# You are going to be given an array of integers. Your job is to take that array
# and find an index N where the sum of the integers to the left of N is equal to
# the sum of the integers to the right of N. If there is no index that would make
# this happen, return -1.

# For Example:
# Let's say you are given the array {1,2,3,4,3,2,1}: Your function will return
# the index 3, because at the 3rd position of the array, the sum of left side of
# the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both
# equal 6.

# Let's look at another one.
# You are given the array {1,100,50,-51,1,1}: Your function will return the index 1,
# because at the 1st position of the array, the sum of left side of the index ({1}) and the
# sum of the right side of the index ({50,-51,1,1}) both equal 1.

# Last one:
# You are given the array {20,10,-80,10,10,15,35}
# At index 0 the left side is {}
# The right side is {10,-80,10,10,15,35}
# They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
# Index 0 is the place where the left side and right side are equal.

# Note: Please remember that in most programming/scripting languages the index
# of an array starts at 0.

# Input:
# An integer array of length 0 < arr < 1000. The numbers in the array can be any
# integer positive or negative.

# Output:
# The lowest index N where the side to the left of N is equal to the side to the
# right of N. If you do not find an index that fits these rules, then you will return -1.

# Note:
# If you are given an array with multiple answers, return the lowest correct index.

def find_even_index(arr):
    length = len(arr)

    for i in range(length):
        left_sum = 0
        right_sum = 0
        # This is for if left side and right side are equal to zero
        if (i == 0):
            right_sum = 0
            for x, num in enumerate(arr):
                if x == (length-1): continue
                right_sum = right_sum + arr[x+1]
            if right_sum == left_sum:
                return(i)
                quit()
        # This is for calculating the sum of the left side
        for z in range(i):
            left_sum = left_sum + arr[z]

        # This is for calculating the sum of the right side
        for w in range(i,length):
            if w == (length-1): continue
            right_sum = right_sum + arr[w+1]

        # This is for calculating if both the left and right side are the same
        if left_sum == right_sum:
            return(i)
            quit()

        return(-1)

test = find_even_index([10,-10])
print(test)
