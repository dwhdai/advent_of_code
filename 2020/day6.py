import string

def import_responses(filepath):
    """Given a filepath, read in the text file containing the responses
    as a list object. Each element in the list is also a list object,
    representing the responses from one group. Within each group, there
    may be 1 or more individual string elements representing the responses
    from each person in the group.

    Args:
        filepath (string): path to input file

    Returns:
        responses (list): list of lists containing responses from each group
    """

    with open(filepath) as f:
        groups = f.read().split("\n\n")
        responses = [group.split("\n") for group in groups]

    return responses


def count_yes(group):
    """Given a group's responses, count the number of questions to which
    anyone answered "yes"

    Args:
        group (list): list object where each element is an individual's response

    Returns:
        count (int): number of questions where >=1 person answered "yes"
    """

    collapsed = "".join(group)
    count = len(set(collapsed))

    return count

def count_all_yes(group):
    """Given a group's responses, count the number of questions to which
    EVERYONE answered "yes"

    Args:
        group (list): list object where each element is an individual's response

    Returns:
        count (int): number of questions where everyone answered "yes"
    """

    # initialize intersection to be all lowercase characters
    all_yes = set(string.ascii_lowercase)
    for response in group:
        all_yes = all_yes.intersection(set(response))

    return len(all_yes)


def group_count(responses):
    """Given a list of responses, for each group, count the number of questions
    to which anyone answered "yes".

    Args:
        responses (list): list of responses for all groups

    Returns:
        counts (list): number of "yes" questions for each group
    """

    counts = [count_yes(group) for group in responses]

    return counts

def group_all_count(responses):
    """Given a list of responses, for each group, count the number of questions
    to which everyone answered "yes".

    Args:
        responses (list): list of responses for all groups

    Returns:
        counts (list): number of "yes" questions for each group
    """

    counts = [count_all_yes(group) for group in responses]

    return counts


if __name__ == "__main__":
    responses = import_responses("./day6_input.txt")
    print("Part 1:", sum(group_count(responses)))
    print("Part 2:", sum(group_all_count(responses)))
