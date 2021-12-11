#!/usr/bin/env python3
from pathlib import Path


def line_is_corrupted(line) -> tuple:
    bracket_pairs = '()[]{}<>'

    open_brackets = list((br for br in bracket_pairs[::2]))
    close_brackets = list((br for br in bracket_pairs[1::2]))

    # key - close bracket, value - open bracket
    close_pairs = dict(zip(close_brackets, open_brackets))

    stack = []
    for i, br in enumerate(line):
        if br in open_brackets:
            stack.append(br)
        else:
            open_bracket = stack.pop()
            if open_bracket != close_pairs.get(br):
                return True, br, i

    return False, None, -1


def part1(contents):
    lines = filter(len, map(str.strip, contents.split('\n')))
    CLOSE_BRACKETS_SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137}

    total_syntax_error_score = 0
    for line in lines:
        is_corrupted, on_char, _ = line_is_corrupted(line)
        if is_corrupted:
            total_syntax_error_score += CLOSE_BRACKETS_SCORES.get(on_char, 0)

    print(f'Part1: score: {total_syntax_error_score}')


def part2(contents):
    lines = filter(len, map(str.strip, contents.split('\n')))
    bracket_pairs = '()[]{}<>'

    CLOSE_BRACKETS_SCORES = dict((ch, i + 1) for i, ch in enumerate(')]}>'))

    open_brackets = list((br for br in bracket_pairs[::2]))
    close_brackets = list((br for br in bracket_pairs[1::2]))

    # key - open bracket, value - close bracket
    open_pairs = dict(zip(open_brackets, close_brackets))

    scores = []
    for line in lines:
        is_corrupted, _, _ = line_is_corrupted(line)
        if is_corrupted:
            continue

        # a string expecting to be line as complete
        stack = []
        for br in line:
            if br in open_brackets:
                stack.append(br)
            else:
                stack.pop()

        completing_brackets = ''.join(open_pairs.get(br) for br in stack[::-1])

        # calc score
        score = 0
        for br in completing_brackets:
            score = 5 * score + CLOSE_BRACKETS_SCORES.get(br)
        scores.append(score)

    middle_index = len(scores) // 2
    scores.sort()
    print(f'Part2: {scores[middle_index]}')


if __name__ == '__main__':
    contents = Path('input.txt').read_text().strip()

    # contents = Path('input_sample.txt').read_text().strip()

    part1(contents)
    part2(contents)
