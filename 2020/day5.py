def import_seats(filepath):
    """Given filepath, import seats data as a list

    Args:
        filepath (string): filepath

    Returns:
        seats (list): list of seats, where each element is a length-10
        string denoting the seat
    """

    with open(filepath) as f:
        seats = f.read().splitlines()

    return seats


def get_row(seat):
    """Given a length-10 seat code, decode and return the row number.
    The first 7 letters of the seat code pertain to the row, and can take
    F or B values. If F, represents front half; B represents back half.
    The plane has a total of 128 rows, and each row is identified by the 7-letter
    code.

    Args:
        seat (string): 10 letter string, containing F or B, L or R

    Returns:
        min_row_num (int): row number
    """

    row_code = seat[0:7]
    min_row_num = 1
    max_row_num = 128

    for letter in row_code:
        if letter == "F":
            max_row_num -= (max_row_num - min_row_num + 1) / 2
        elif letter == "B":
            min_row_num += (max_row_num - min_row_num + 1) / 2

    return min_row_num - 1


def get_column(seat):
    """Given a length-10 seat code, decode and return the column number.
    The last 3 letters of the seat code pertain to the column, and can take
    L or R values. If L, represents left half; R represents right half.
    The plane has a total of 8 columns, and each column is identified by the 3-letter
    code.

    Args:
        seat (string): 10 letter string, containing F or B, L or R

    Returns:
        min_column_num (int): column number
    """

    column_code = seat[7:10]
    min_column_num = 1
    max_column_num = 8
    
    for letter in column_code:
        if letter == "L":
            max_column_num -= (max_column_num - min_column_num + 1) / 2
        elif letter == "R":
            min_column_num += (max_column_num - min_column_num + 1) / 2

    return min_column_num - 1

def calculate_seat_id(row, column):

    seat_id = row * 8 + column

    return seat_id

def calculate_all_seat_ids(seats):
    """Given a list of seats, calculate all seat IDs
    """
    
    seat_ids = []
    row = int()
    column = int()
    
    for seat in seats:
        row = get_row(seat)
        column = get_column(seat)
        seat_id = calculate_seat_id(row, column)
        seat_ids.append(seat_id)    
        
    return seat_ids


def find_my_seat(seat_ids):
    """Given a list of seat IDs, find my seat ID. My seat ID should be
    the one that is missing from the sequence of seat IDs, where 
    my_seat_id +/- 1 both exist

    Args:
        seat_ids (list): list of seat_ids

    Returns:
        my_seat_id (int): my seat ID
    """
    
    # Sort seat_ids
    seat_ids.sort()
    
    # For each sorted list element, find the element where element + 1
    # does not exist
    my_seat_id = int()
    for id in seat_ids:
        if id + 1 not in seat_ids:
            return id + 1

    return "Not Found"


seats = import_seats("./day5_input.txt")
seat_ids = calculate_all_seat_ids(seats)
print("Part 1:", max(seat_ids))

print("Part 2:", find_my_seat(seat_ids))