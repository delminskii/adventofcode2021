#!/usr/bin/env python3
from collections import defaultdict
from pathlib import Path


def get_parsed(contents):
    ret_mappings = dict()
    template, mappings = map(str.strip, contents.split('\n\n'))

    for m in map(str.strip, mappings.split('\n')):
        from_, to_ = map(str.strip, m.split('->'))
        ret_mappings[from_] = to_

    return template, ret_mappings


def part1(contents):
    template, mappings = get_parsed(contents)

    NSTEPS = 10
    for step in range(NSTEPS):
        pieces = (template[i : i + 2] for i in range(len(template) - 1))
        pieces = [
            '%s%s%s' % (p[0], mappings[p], p[1]) if p in mappings else p
            for p in pieces
        ]

        n = len(pieces[0])
        temp = pieces[0]
        for i in range(len(pieces) - 1):
            overlap_bitmask = [False] * n

            curr_p, next_p = pieces[i], pieces[i + 1]
            for j in range(n):
                if j == 1:
                    break

                overlap_bitmask[j] = curr_p[n - j - 1] == next_p[j]
                if not overlap_bitmask[j]:
                    break

            for b, ch in zip(overlap_bitmask, next_p):
                temp += (ch, '')[b]

        template = temp

    # calc most & least freqs
    freqs = defaultdict(int)
    for ch in template:
        freqs[ch] += 1
    __import__('pprint').pprint(freqs)

    most_common_value, least_common_value = -1, float('inf')
    for v in freqs.values():
        most_common_value = max(most_common_value, v)
        least_common_value = min(least_common_value, v)

    print(f'Part1: diff: {most_common_value - least_common_value}')


def part2(contents):
    pass


if __name__ == '__main__':
    # contents = Path('input.txt').read_text().strip()

    contents = Path('input_sample.txt').read_text().strip()

    part1(contents)
    part2(contents)
