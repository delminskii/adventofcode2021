#!/usr/bin/env python3

from collections import defaultdict
from itertools import cycle
from pathlib import Path
from string import ascii_uppercase


def part1(numbers):
    n = len(numbers)

    acc = 0
    for i in range(1, n):
        prev = numbers[i - 1]
        curr = numbers[i]
        acc += curr > prev

    print(f'Part1: {acc}')


def part2(nubmers):
    n = len(numbers)

    acc = 0
    prev_three_lines_sum = 0
    for i in range(n-2):
        curr_three_lines_sum = sum(numbers[i:i+2+1])
        acc += curr_three_lines_sum > prev_three_lines_sum

        prev_three_lines_sum = curr_three_lines_sum

    # -1 cause we want respecting prev_three_lines_sum 
    print(f'Part2: {acc-1}')




if __name__ == '__main__':
    lines = Path('input.txt').read_text().split('\n')
    lines = filter(len, map(str.strip, lines))
    numbers = list(map(int, lines))

    part1(numbers)
    part2(numbers)
