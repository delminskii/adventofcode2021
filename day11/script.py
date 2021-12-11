#!/usr/bin/env python3
from pathlib import Path


class Matrix:
    def __init__(self, contents):
        self._mtx = []
        lines = filter(len, map(str.strip, contents.split('\n')))
        for line in lines:
            self._mtx.append([int(x) for x in line])

        # it's square
        self.size = len(self._mtx)

    def print(self):
        for i in range(self.size):
            print(''.join(map(str, self._mtx[i])))

    def _get_adjacent_coords(self, i, j):
        # 1 2 3
        # 4   5
        # 6 7 8
        coords = (
            (i - 1, j - 1),
            (i - 1, j),
            (i - 1, j + 1),
            (i, j - 1),
            (i, j + 1),
            (i + 1, j - 1),
            (i + 1, j),
            (i + 1, j + 1),
        )
        coords = filter(
            lambda tup: all(-1 < x < self.size for x in tup), coords
        )
        return coords

    def _get_next_for(self, num):
        rotated = False

        num += 1
        rotated = num > 9
        if rotated:
            num = 0

        return rotated, num

    def make_step1(self):
        ret_flashes_number = 0

        # ie visited already
        untouchable_coords = set()

        queue = []

        for i in range(self.size):
            for j in range(self.size):
                rotated, value = self._get_next_for(self._mtx[i][j])
                self._mtx[i][j] = value

                if rotated:
                    untouchable_coords.add((i, j))
                    queue.append((i, j))

        while queue:
            ret_flashes_number += 1

            i, j = queue.pop(0)
            for adji, adjj in self._get_adjacent_coords(i, j):
                rotated, value = self._get_next_for(self._mtx[adji][adjj])
                self._mtx[adji][adjj] = value

                if rotated:
                    untouchable_coords.add((adji, adjj))
                    queue.append((adji, adjj))

        for i, j in untouchable_coords:
            self._mtx[i][j] = 0

        return ret_flashes_number

    def make_step2(self):
        # ie visited already
        untouchable_coords = set()

        queue = []

        for i in range(self.size):
            for j in range(self.size):
                rotated, value = self._get_next_for(self._mtx[i][j])
                self._mtx[i][j] = value

                if rotated:
                    untouchable_coords.add((i, j))
                    queue.append((i, j))

        while queue:
            i, j = queue.pop(0)
            for adji, adjj in self._get_adjacent_coords(i, j):
                rotated, value = self._get_next_for(self._mtx[adji][adjj])
                self._mtx[adji][adjj] = value

                if rotated:
                    untouchable_coords.add((adji, adjj))
                    queue.append((adji, adjj))

        for i, j in untouchable_coords:
            self._mtx[i][j] = 0

        # the octopuses will all flash simultaneously
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) not in untouchable_coords:
                    return False

        return True


def part1(contents):
    NSTEPS = 100
    m = Matrix(contents)

    total_flashes = 0
    for _ in range(NSTEPS):
        flashes_num = m.make_step1()
        total_flashes += flashes_num
        # print(f'step: {_} ; flashes: {flashes_num}')

    print(f'Part1; total flashes: {total_flashes}')


def part2(contents):
    # based on part1
    m = Matrix(contents)

    # What is the first step during which all octopuses flash?
    first_step = 1
    while 1:
        all_octopuses_flash = m.make_step2()
        if all_octopuses_flash:
            break

        first_step += 1

    print(f'Part2: first step: {first_step}')


if __name__ == '__main__':
    contents = Path('input.txt').read_text().strip()

    # contents = Path('input_sample.txt').read_text().strip()
    # contents = """11111
    # 19991
    # 19191
    # 19991
    # 11111"""

    part1(contents)
    part2(contents)
