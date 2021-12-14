#!/usr/bin/env python3
from collections import defaultdict
from pathlib import Path


def get_path_nums(map_, from_, to_):
    ret_nums = 0

    stack = [(from_, set((from_,)))]
    while stack:
        node, visited = stack.pop()
        if node == to_:
            ret_nums += 1
            continue

        for node_ in map_.get(node):
            if node_ in visited and node_ == node_.lower():
                continue

            stack.append((node_, visited | set((node_,))))

    return ret_nums


def part1(contents):
    lines = filter(len, map(str.strip, contents.split('\n')))

    map_ = defaultdict(set)
    for line in lines:
        from_, to_ = map(str.strip, line.split('-'))
        if to_ != 'start':
            map_[from_].add(to_)
        if from_ != 'start':
            map_[to_].add(from_)

    n = get_path_nums(map_, 'start', 'end')
    print(f'Part1; n = {n}')


def part2(contents):
    pass


if __name__ == '__main__':
    contents = Path('input.txt').read_text().strip()

    # contents = Path('input_sample.txt').read_text().strip()

    part1(contents)
    part2(contents)
