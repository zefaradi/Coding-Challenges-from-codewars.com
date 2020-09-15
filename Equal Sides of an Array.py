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
