# Is a number prime?

# Define a function that takes an integer argument and returns logical value true
# or false depending on if the integer is a prime.

# Per Wikipedia, a prime number (or a prime) is a natural number greater than 1
# that has no positive divisors other than 1 and itself.

# Requirements

# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive. You may be given
# negative numbers as well (or 0).

# NOTE on performance: There are no fancy optimizations required, but still the
# most trivial solutions might time out. Numbers go up to 2^31 (or similar, depends
# on language version). Looping all the way up to n, or n/2, will be too slow.

# Example
# is_prime(1)  /* false */
# is_prime(2)  /* true  */
# is_prime(-1) /* false */

def is_prime(num):
    if (num < 2):
        return (False)
    elif (num == 2):
        return (True)
    sq = int((num)**(0.5) + 1)
    for n in range(2,sq):
        if (num % n == 0):
            return False
            break
    return True

test = is_prime(100**100)
print(test)
