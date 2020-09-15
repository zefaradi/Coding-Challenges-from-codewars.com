# Human Readable Time

# Description:
# Write a function, which takes a non-negative integer (seconds) as input and
# returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
#
# You can find some examples in the test fixtures.

def make_readable(seconds):
    hours = seconds/3600
    hours2 = int(hours)
    minutes = hours - hours2
    minutes2 = minutes * 60
    minutes3 = int(minutes2)
    seconds = minutes2 - minutes3
    seconds2 = round(seconds * 60)

    return ("%02d:%02d:%02d" % (hours2, minutes3, seconds2))

test = make_readable(3600)
print(test)
