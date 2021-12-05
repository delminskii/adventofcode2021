#!/usr/bin/env python3
import re
from dataclasses import dataclass
from pathlib import Path


@dataclass
class BoardCell:
    value: int
    marked: bool


def _get_numbers_and_boards(contents: str) -> tuple:
    # list of lists of BoardCell objects
    ret_boards = []

    # list of random number (1st line of contents)
    ret_random_numbers = []

    # regex to extract random numbers of the 1st line
    random_numbers_re = re.compile(r'(.*,.*)')

    random_numbers_match = random_numbers_re.search(contents)
    ret_random_numbers = list(
        map(
            int,
            filter(
                len,
                map(
                    str.strip, random_numbers_match.group(1).strip().split(',')
                ),
            ),
        )
    )

    # now contents contains boards only
    board_numbers = []
    contents = random_numbers_re.sub(str(), contents).strip()
    for line in contents.split('\n'):
        line = line.strip()
        if line:
            board_numbers.append(
                list(
                    map(
                        lambda x: BoardCell(int(x), False),
                        map(str.strip, line.split()),
                    )
                )
            )
        else:
            ret_boards.append(board_numbers)
            board_numbers = []

    # take the last one as well
    ret_boards.append(board_numbers)

    return ret_random_numbers, ret_boards


def winner_found(board) -> bool:
    n_cols = 0

    # check by rows
    for i_row, rowline in enumerate(board):
        if not n_cols:
            n_cols = len(rowline)

        if all(cell.marked for cell in rowline):
            return True

    # check by cols
    for j in range(n_cols):
        marked = []
        for rowline in board:
            marked.append(rowline[j].marked)

        if all(marked):
            return True

    return False


def part1(contents):
    random_numbers, boards = _get_numbers_and_boards(contents)

    winner_is_found = False
    i_winner_board = -1

    random_number = None
    it_random_numbers = iter(random_numbers)
    while not winner_is_found:
        # look for winner board: we want board being modified so store changed
        # boards in new var
        random_number = next(it_random_numbers)
        for i, board in enumerate(boards):
            for rowline in board:
                for cell in rowline:
                    if cell.value == random_number:
                        cell.marked = True

            winner_is_found = winner_found(board)
            if winner_is_found:
                i_winner_board = i
                break

    print('Winner board:')
    list(map(print, boards[i_winner_board]))

    # calc score
    sum_unmarked = 0
    for rowline in boards[i_winner_board]:
        sum_unmarked += sum(cell.value for cell in rowline if not cell.marked)
    print(f'score: {sum_unmarked * random_number}')


def part2(xs):
    # based on part1 (copy/paste):
    random_numbers, boards = _get_numbers_and_boards(contents)

    winner_is_found = False
    last_won_board = None

    last_random_number = None
    for random_number in random_numbers:
        for board in boards:
            # we're not interested in them already (as long as we look for the
            # last winner board)
            if winner_found(board):
                continue

            # modify cells inplace
            for rowline in board:
                for cell in rowline:
                    if cell.value == random_number:
                        cell.marked = True

            # and check again
            winner_is_found = winner_found(board)
            if winner_is_found:
                last_random_number = random_number
                last_won_board = board

    print('Winner board:')
    list(map(print, last_won_board))

    # calc score
    sum_unmarked = 0
    for rowline in last_won_board:
        sum_unmarked += sum(cell.value for cell in rowline if not cell.marked)
    print(f'score: {sum_unmarked * last_random_number}')


if __name__ == '__main__':
    contents = Path('input.txt').read_text().strip()

    # contents = Path('input_sample.txt').read_text().strip()

    part1(contents)
    part2(contents)
