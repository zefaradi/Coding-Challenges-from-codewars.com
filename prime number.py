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
