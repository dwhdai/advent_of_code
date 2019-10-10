import numpy as np


def captcha(x):
    """Captcha function for Day 1 of 2017 Advent of Code
    
    Arguments:
        x {str} -- input number as a string
    
    Returns:
        int -- return calculated sum as an int
    """

    first_digit = x[0:1]

    x = x + first_digit

    matches = np.zeros(0)

    for i in range(0, len(x) - 1, 1):
        if x[i] == x[i + 1]:
            matches = np.append(matches, int(x[i]))
         
    sum = np.sum(matches)
    return sum


print(captcha("1122"))
print(captcha("1111"))
print(captcha("1234"))
print(captcha("9121212129"))
