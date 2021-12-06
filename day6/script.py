#!/usr/bin/env python3
from pathlib import Path


def get_next_number(prev_number: int) -> int:
    next_number = prev_number - 1
    return 6 if next_number < 0 else next_number


def part1(contents):
    numbers = list(map(int, map(str.strip, contents.split(','))))

    NDAYS = 80
    n_zeroes = 0
    for i in range(NDAYS):
        numbers = list(map(get_next_number, numbers)) + [8] * n_zeroes
        n_zeroes = numbers.count(0)

    print(f'ndays = {NDAYS}; nfishes = {len(numbers)}')


def part2(contents):
    # being smart due ram/cpu limitation
    numbers = map(int, map(str.strip, contents.split(',')))

    counts = [0] * 9
    for n in numbers:
        counts[n] += 1

    NDAYS = 256
    for i in range(NDAYS):
        v = counts.pop(0)
        counts[6] += v
        counts.append(v)

    print(sum(counts))


if __name__ == '__main__':
    contents = Path('input.txt').read_text().strip()

    # contents = Path('input_sample.txt').read_text().strip()

    part1(contents)
    part2(contents)
