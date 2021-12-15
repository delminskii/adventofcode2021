#!/usr/bin/env python3
from pathlib import Path
from queue import Queue


class Matrix:
    def __init__(self, contents):
        self._mtx = []

        lines = filter(len, map(str.strip, contents.split('\n')))
        for line in lines:
            self._mtx.append([int(x) for x in line])

        # # it's square
        self.size = len(self._mtx)

    def print(self):
        for i in range(self.size):
            print(''.join(map(str, self._mtx[i])))

    def get(self, i, j):
        return self._mtx[i][j]

    def get_adjacent_coords(self, i, j):
        ret_coords = []

        #   x
        # x   1
        #   2
        # down and right moves only
        coords = ((i, j + 1), (i + 1, j))

        for i, j in coords:
            if all(-1 < x < self.size for x in (i, j)):
                ret_coords.append((i, j))

        return ret_coords


def part1(contents):
    def h(curr, end):
        return abs(curr[0] - end[0]) + abs(curr[1] + end[1])

    mtx = Matrix(contents)
    start, end = (0, 0), (mtx.size - 1, mtx.size - 1)

    # solve it using A*
    q = Queue()
    q.put(start)
    path = {start: 0}

    while q:
        curr = q.get()
        if curr == end:
            break

        for nb_node in mtx.get_adjacent_coords(*curr):
            weight = path[curr] + mtx.get(*nb_node)
            if nb_node not in path or weight < path[nb_node]:
                path[nb_node] = weight
                # priority = weight + h(curr, end)
                # print(f'node: {nb_node}; priority: {priority}')
                q.put(nb_node)

    risk_val = path.get(end)
    print(f'Part1: risk = {risk_val}')


def part2(contents):
    pass


if __name__ == '__main__':
    contents = Path('input.txt').read_text().strip()

    # contents = Path('input_sample.txt').read_text().strip()

    part1(contents)
    part2(contents)
