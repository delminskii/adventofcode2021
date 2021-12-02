#!/usr/bin/env python3

import re
from pathlib import Path


def part1(commands):
    depth, horizontal_pos = 0, 0
    pattern_re = re.compile(r'(.*?)\s*(\d+)')
    for command in commands:
        match = pattern_re.search(command)
        if match:
            cmd, value = match.groups()
            value = {
                'up': -int(value),
                'down': int(value),
                'forward': int(value),
            }.get(cmd)
            if cmd in ('up', 'down'):
                depth += value
            else:
                # forward
                horizontal_pos += value

    print(f'Part1; {depth * horizontal_pos}')


def part2(commands):
    aim_units, horizontal_pos, depth = 0, 0, 0
    pattern_re = re.compile(r'(.*?)\s*(\d+)')
    for command in commands:
        match = pattern_re.search(command)
        if match:
            cmd, value = match.groups()
            value = {
                'up': -int(value),
                'down': int(value),
                'forward': int(value),
            }.get(cmd)
            if cmd in ('up', 'down'):
                aim_units += value
            else:
                # forward
                horizontal_pos += value
                depth += value * aim_units

    print(f'Part2: {horizontal_pos * depth}')


if __name__ == '__main__':
    lines = Path('input.txt').read_text().split('\n')
    lines = filter(len, map(str.strip, lines))
    commands = list(lines)

    part1(commands)
    part2(commands)
