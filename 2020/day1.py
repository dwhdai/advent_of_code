# Advent of Code 2020 - Day 1

def read_expense_report(input_file):
    """ Given a file path, read in the file as a list object,
    separated by line breaks.

    Returns:
        list: list of ints
    """

    with open(input_file) as f:
        expense_report = f.read().splitlines()

    # Convert to integer
    expense_report = [int(x) for x in expense_report]

    return expense_report


def find_two_entries(expense_report, sum = 2020):
    """From the inputted list expense_report, first find
    the two elements that sum up to 2020, then multiply 
    these two elements. 
    Args:
        expense_report (list, integer): list of integer elements
        sum (int): the desired sum

    Returns:
        int: the product of the two elements
    """

    # For a list of length n, denote i to indicate the ith
    # element from i = 1 to n.

    # We wish to find the two elements that add up to 2020

    # To do this, we can iterate through each element i,
    # and subtract the ith element from 2020.

    # If the difference exists in the remaining elements,
    # then the two elements are ith element and the difference

    for element in expense_report:

        difference = sum - element

        if difference in expense_report:

            return element * difference

    return "No solution"



def find_three_entries(expense_report, sum = 2020):
    """Similar to find_two_entries, but instead we find 
    three entries that add up to 2020, and then 
    multiply them.

    Args:
        expense_report (list, integer): list of integer elements

    Returns:
        [type]: [description]
    """
    
    for i in range(0, len(expense_report)):

        difference = sum - expense_report[i]

        # Use find_two_entries to determine if there are two elements
        # in the remaining list that add up to the difference value

        remaining = expense_report[i:]
        product1 = find_two_entries(remaining, sum = difference)
        
        if product1 != "No solution":

            return expense_report[i] * product1

    return "No solution"

expense_report = read_expense_report("./2020/day1_input.txt")
part1 = find_two_entries(expense_report)
part2 = find_three_entries(expense_report)

print(part1, part2)