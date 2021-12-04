# numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

# boards = [
# [22 ,13 ,17 ,11 , 0,
#  8 , 2 ,23 , 4 ,24,
# 21 , 9 ,14 ,16 , 7,
#  6 ,10 , 3 ,18 , 5,
#  1 ,12 ,20 ,15 ,19],

# [3 ,15 , 0 , 2 ,22,
#  9 ,18 ,13 ,17 , 5,
# 19 , 8 , 7 ,25 ,23,
# 20 ,11 ,10 ,24 , 4,
# 14 ,21 ,16 ,12 , 6],

# [14 ,21 ,17 ,24 , 4,
# 10 ,16 ,15 , 9 ,19,
# 18 , 8 ,23 ,26 ,20,
# 22 ,11 ,13 , 6 , 5,
#  2 , 0 ,12 , 3 , 7]
#  ]

# input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7
# """

from dataclasses import dataclass
from typing import List, Union


@dataclass
class Board:
    horizontal_lines: List[List[int]]
    vertical_lines: List[List[int]]

@dataclass
class Boards:
    boards: List[Board]

with open("day4_input.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    numbers = [int(n) for n in lines[0].split(',')]
    board_lines = lines[2:]
    horizontal_lines = [l.split() for l in board_lines]
    horizontal_lines = [[int(n) for n in l] for l in horizontal_lines]
    # Indexing i+5 to remove the blank line that occurs on every 6th line
    boards_horizontal = [horizontal_lines[i:i+5] for i in range(0, len(horizontal_lines), 6)]
    boards_vertical = [list(zip(*board)) for board in boards_horizontal]
    boards_vertical = [[list(l) for l in board] for board in boards_vertical]
    board_list = Boards([Board(h, v) for (h, v) in zip(boards_horizontal, boards_vertical)])

def winner(board: Board) -> bool: 
    horizontal_win = any([len(l) == 0 for l in board.horizontal_lines])
    vertical_win = any([len(l) == 0 for l in board.vertical_lines])
    return horizontal_win or vertical_win

def remove_number_from_board(number: int, board: Board):
    vertical_lines = board.vertical_lines
    horizontal_lines = board.horizontal_lines
    for l in vertical_lines:
        if number in l:
            l.remove(number)

    for l in horizontal_lines:
        if number in l:
            l.remove(number)
        
    return board 

def get_remaining_numbers(board: Board) -> List[int]:
    remaining_numbers = [num for line in board.horizontal_lines for num in line]
    return remaining_numbers

def part1(numbers: List[int], board_list: Boards) -> Union[None, int]:
    
    for i, n in enumerate(numbers):
        for j, board in enumerate(board_list.boards):
            number_in_board = any([n in l for l in board.horizontal_lines])
            if number_in_board:
                remove_number_from_board(n, board)

            if winner(board):
                remaining_numbers = get_remaining_numbers(board)
                return n * sum(remaining_numbers)

print(part1(numbers, board_list))
