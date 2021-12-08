#!/usr/bin/env python3
import math
import operator
import re
from collections import Counter
from pathlib import Path


def part1(contents):
    # lengths of busy segments for 1478 digits
    lengths_1478 = frozenset((2, 4, 3, 7))

    total_digits_counter = 0
    for line in contents.split('\n'):
        patterns_str, possible_digits_str = map(str.strip, line.split('|'))

        lengths = map(len, map(str.strip, possible_digits_str.split()))
        total_digits_counter += sum(x in lengths_1478 for x in lengths)

    print(f'Part1: total: {total_digits_counter}')


def part2(contents):
    # the digits 1 4 7 8 can be easily determined as busy (easy to find);

    total_sum = 0
    for line in contents.split('\n'):
        signals_segments = [set() for _ in range(10)]
        patterns_str, possible_digits_str = map(str.strip, line.split('|'))

        # look for digit 1,4,7,8 digits to fill signals_segments_map;
        # iterate from the digi 8 (has 7 segments)
        pairs = [(p, len(p)) for p in map(str.strip, patterns_str.split())]

        # set 1, 4, 7 & 8 digits firstly: map num_of_segments -> digit;
        # idx - digit, v - set of segments/chars
        well_kwnown_digits = {2: 1, 4: 4, 3: 7, 7: 8}
        for p, plen in pairs:
            digit = well_kwnown_digits.get(plen)
            if digit is not None:
                signals_segments[digit] = set(p)

        # look for the rest digits based on the known ones defined above
        for p, plen in pairs:
            digit = well_kwnown_digits.get(plen)
            if digit is not None:
                continue

            pset = set(p)
            if plen == 5:
                # 2 3 or 5
                diff_len = len(pset - signals_segments[1])
                if diff_len == 3:
                    # 3
                    signals_segments[3] = pset
                else:
                    diff_len = len(pset - signals_segments[4])
                    if diff_len == 3:
                        # 2
                        signals_segments[2] = pset
                    else:
                        # 5
                        signals_segments[5] = pset

            else:
                # plen == 6 (0 6 or 9)
                diff_len = len(pset - signals_segments[4])
                if diff_len == 2:
                    # 9
                    signals_segments[9] = pset
                elif diff_len == 3:
                    # 6 or 0
                    diff_len = len(pset - signals_segments[7])
                    if diff_len == 3:
                        # 0
                        signals_segments[0] = pset
                    else:
                        # 6
                        signals_segments[6] = pset

        # now define numbers after | sign
        dec = 1000
        sum_ = 0
        for displayed_digit in possible_digits_str.split():
            i = signals_segments.index(set(displayed_digit))
            sum_ += i * dec

            dec //= 10

        # acc all here
        total_sum += sum_

    print(f'Part2; total: {total_sum}')


if __name__ == '__main__':
    contents = Path('input.txt').read_text().strip()

    # contents = Path('input_sample.txt').read_text().strip()

    part1(contents)
    part2(contents)
