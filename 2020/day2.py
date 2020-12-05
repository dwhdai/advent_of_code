import re


def read_passwords(filepath):
    """[summary]

    Args:
        filepath: string, path to passwords file

    Returns:
        min, max, letter, password: lists containing each extracted
        value
    """

    with open(filepath) as f:
        raw = f.read().splitlines()

    min = [int(str.split("-")[0]) for str in raw]
    max = [int(str.split("-")[1].split(" ", maxsplit=1)[0]) for str in raw]
    letter = [str.split(" ")[1][0:1] for str in raw]
    password = [str.split(" ")[2] for str in raw]

    return min, max, letter, password


def count_occurrences(letter, password):
    """Counts the number of times a given letter occurs
    in the password

    Returns:
        int: occurrences of letter in given password
    """

    num_occurrences = len(re.findall(letter, password))

    return num_occurrences


def count_valid_passwords(filepath):
    """Given a list of passwords and the policy, return the number of 
    passwords that satisfy its policy

    Returns:
        list: a list object containing string values. Each value is 
        formatted like [min-max] [letter]: [password], where min/max
        are the number of times that "letter" needs to appear in 
        "password". If the password satisfies the min/max requirements,
        then it is valid.
    """
    min, max, letter, password = read_passwords(filepath)

    counter = 0

    for i in range(0, len(min)):

        letter_occurrences = count_occurrences(letter[i], password[i])

        if letter_occurrences >= min[i] and letter_occurrences <= max[i]:
            counter += 1

    return counter


print("Part1:", count_valid_passwords("./day2_input.txt"))

def count_valid_passwords2(filepath):
    """Given an input file of passwords and policies, return the number
    of passwords that satisfy its policy.

    For part 2, the policy states that the password must contain exactly
    one instance of the letter in one of the positions indicated by
    min and max.

    Args:
        filepath (str): filepath

    Returns:
        counter (int): count of valid passwords
    """

    min, max, letter, password = read_passwords(filepath)

    counter = 0

    for i in range(0, len(min)):

        if (password[i][min[i]-1] == letter[i]) ^ (password[i][max[i]-1] == letter[i]):
            counter += 1

    return counter

print("Part 2:", count_valid_passwords2("./day2_input.txt"))