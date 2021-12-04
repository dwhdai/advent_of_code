from dataclasses import dataclass
from typing import List, Union, Tuple


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

def part1(numbers: List[int], board_list: Boards) -> Union[None, Tuple[ int, int ]]:
    for n in numbers:
        for i, board in enumerate(board_list.boards):
            number_in_board = any([n in l for l in board.horizontal_lines])
            if number_in_board:
                remove_number_from_board(n, board)

            if winner(board):
                remaining_numbers = get_remaining_numbers(board)
                return i, n * sum(remaining_numbers)

def part2(numbers: List[int], board_list: Boards):
    n_boards = len(board_list.boards)
    board_won = []

    for n in numbers:
        for i, board in enumerate(board_list.boards):
            number_in_board = any([n in l for l in board.horizontal_lines])
            if number_in_board:
                remove_number_from_board(n, board)
            if winner(board):
                if i not in board_won:
                    board_won.append(i)
                if len(board_won) == n_boards:
                    remaining_numbers = get_remaining_numbers(board)
                    return board_won[-1], n * sum(remaining_numbers)

if __name__ == "__main__":
    print(part1(numbers, board_list))
    print(part2(numbers, board_list))





