import re


def import_passports(filepath):
    """Given a filepath of passport data, return a list of dictionaries
    containing the passport data.

    Args:
        filepath (string): File to path

    Returns:
        passports[list]: A list of dictionaries containing the passport data.
        Each list element is a dictionary that represents the data for one
        passport. Each passport dictionary may have up to 8 elements: 
        byr (birth year), iyr (issue year), eyr (expiration year), hgt (height),
        hcl (hair colour), ecl (eye colour), pid (passport ID), cid (country ID) 
    """

    with open(filepath) as f:
        raw_passports = f.read().split("\n\n")

    # Convert to dictionary object
    passports = list()

    for raw_passport in raw_passports:

        clean_passport = dict()

        # Replace newline character with spaces
        passport_fields = raw_passport.replace("\n", " ").split(" ")

        for field in passport_fields:
            field_split = field.split(":")
            key = field_split[0]
            val = field_split[1]

            clean_passport[key] = val

        passports.append(clean_passport)

    return passports


def validate_data(passport):
    """Given a passport, check that the data fields are all valid

    1. 1920 <= byr <= 2002
    2. 2010 <= iyr <= 2020
    3. 2020 <= eyr <= 2030
    4. 150cm/59in <= hgt <= 193cm/76in
    5. hcl: a # followed by exactly six characters 0-9 or a-f
    6. ecl: exactly one of: amb blu brn gry grn hzl oth
    7. pid: a nine-digit number, including leading zeroes

    Returns:
        valid (boolean): True if all fields of passport are valid
    """

    byr = 1920 <= int(passport["byr"]) <= 2002
    iyr = 2010 <= int(passport["iyr"]) <= 2020
    eyr = 2020 <= int(passport["eyr"]) <= 2030

    hgt_val = int(re.sub("[^0-9]", "", passport["hgt"]))
    if "in" in passport["hgt"]:
        hgt = 59 <= hgt_val <= 76
    else:
        hgt = 150 <= hgt_val <= 193

    hcl = re.match("^#[0-9a-f]{6}$", passport["hcl"]) != None

    ecl = passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    pid = re.match("^[0-9]{9}$", passport["pid"]) != None

    valid = all([byr, iyr, eyr, hgt, hcl, ecl, pid])

    return valid


def check_passport_fields(passport, required_fields=["byr",
                                                     "iyr",
                                                     "eyr",
                                                     "hgt",
                                                     "hcl",
                                                     "ecl",
                                                     "pid"]):
    """Given a passport, check that it contains all the necessary fields. If so,
    it is considered valid, otherwise invalid.

    Args:
        passport (dictionary): Dictionary containing various passport fields

    Returns:
        valid (boolean): Whether passport is valid or invalid
    """

    keys = passport.keys()

    valid = all([k in keys for k in required_fields])

    return valid


def count_valid1(passports):
    """Given a list of passports, return the number of passports that are 
    considered valid.

    Args:
        passports (list): list of dictionaries

    Returns:
        num_valid[int]: number of valid passports
    """

    num_valid = 0

    for passport in passports:
        num_valid += check_passport_fields(passport)

    return num_valid

def count_valid2(passports):
    """Given a list of passports, return the number of passports that are 
    considered valid.

    Args:
        passports (list): list of dictionaries

    Returns:
        num_valid[int]: number of valid passports
    """

    num_valid = 0

    for passport in passports:
        if check_passport_fields(passport):
            num_valid += validate_data(passport)

    return num_valid


passports = import_passports("./day4_input.txt")
print("Part1:", count_valid1(passports))
print("Part2:", count_valid2(passports))
