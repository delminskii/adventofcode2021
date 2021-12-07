#!/usr/bin/env python3
from pathlib import Path


def part1(contents):
    numbers = list(map(int, map(str.strip, contents.split(','))))

    min_, max_ = min(numbers), max(numbers)
    pos = -1
    min_fuel = float('inf')

    for i in range(min_, max_ + 1):
        fuel = sum(abs(x - i) for x in numbers)
        if fuel < min_fuel:
            min_fuel = fuel
            pos = i

    print(f'Part1: pos: {pos}; fuel: {min_fuel}')


def part2(contents):
    numbers = list(map(int, map(str.strip, contents.split(','))))

    min_, max_ = min(numbers), max(numbers)
    pos = -1
    min_fuel = float('inf')

    for i in range(min_, max_ + 1):
        fuel = 0
        for x in numbers:
            diff = abs(x - i)

            # arithmetic progression could be used to calc it faster but leave
            # it naively as long as it works (though taking more time)

            # naive
            # fuel += sum(range(diff + 1))

            # using sum of arithmetic series
            fuel += (diff * (1 + diff)) // 2  # or bitwise shift >>1

        if fuel < min_fuel:
            min_fuel = fuel
            pos = i

    print(f'Part2: pos: {pos}; fuel: {min_fuel}')


if __name__ == '__main__':
    contents = Path('input.txt').read_text().strip()

    # contents = Path('input_sample.txt').read_text().strip()

    part1(contents)
    part2(contents)
