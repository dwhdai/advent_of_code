def import_map(filepath):
    """Given a filepath, import the map object as as a nested list.

    Returns:
        list: a 2D nested list, representing the rows of the map
        as individual list objects
    """

    with open(filepath) as f:
        map = f.read().splitlines()

    return map


def traverse_step(start_position, map_width, step_x=3, step_y=1):
    """Given a starting coordinate, return the ending coordinate
    after traversing one step of "right 3 down 1"

    Args:
        start_position[tuple]: (x coordinate, y coordinate)
        map_width[int]: the width of the map
        step_x, step_y[int]: number of steps to take in the x,y direction
    Returns:
        [int]: x coordinate, y coordinate
    """

    x_end = (start_position[0] + step_x) % map_width
    y_end = start_position[1] + step_y

    return x_end, y_end


def tree_present(map, position):
    """Given a map and position, check to see if the inputted position
    contains a tree on the map

    Args:
        map[list]: 2D list representing the map as row vectors
        position[tuple]: (x coordinate, y coordinate)
    Returns:
        tree[boolean]: True if tree present, False otherwise
    """
    x_coord = position[0] - 1
    y_coord = position[1] - 1

    tree = map[y_coord][x_coord] == "#"

    return tree


def traverse_map(map, start_position=(1, 1), step_x=3, step_y=1):
    """Given a map, traverse through the map by taking steps of 3 right
    1 down, and count the number of trees encountered. End when finished
    traversing all rows of the map.

    Args:
        map[list]: 2D list object 
        start_position[tuple]: tuple with 2 ints, representing the x and y
            coordinates of the starting position. Note: to get list indices,
            subtract 1 from the position
        step_x, step_y[int]: the number of units to traverse in x and y 
        directions per step

    Returns:
        num_trees[int]: number of trees encountered
    """

    # Define x and y positions, initialized to start_position
    x = start_position[0]
    y = start_position[1]

    # Calculate width of map
    map_width = len(map[0])

    # Initialize tree counter
    num_trees = 0

    while y - 1 < len(map):
        # Check if current position contains a tree
        # If there is, add to num_trees counter
        num_trees += tree_present(map, (x, y))

        # Iterate to next step
        x, y = traverse_step((x, y), map_width, step_x, step_y)

    return num_trees

map = import_map("./day3_input.txt")

slope1 = traverse_map(map,  step_x=1, step_y=1)
slope2 = traverse_map(map,  step_x=3, step_y=1)
slope3 = traverse_map(map,  step_x=5, step_y=1)
slope4 = traverse_map(map,  step_x=7, step_y=1)
slope5 = traverse_map(map,  step_x=1, step_y=2)
print(slope1 * slope2 * slope3 * slope4 * slope5)
