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


def check_passport(passport, required_fields = ["byr",
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


def count_valid(passports):
    """Given a list of passports, return the number of passports that are 
    considered valid.

    Args:
        passports (list): list of dictionaries

    Returns:
        num_valid[int]: number of valid passports
    """
    
    num_valid = 0
    
    for passport in passports:
        num_valid += check_passport(passport)    
    
    return num_valid


passports = import_passports("./day4_input.txt")
print(count_valid(passports))
