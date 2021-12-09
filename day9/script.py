#!/usr/bin/env python3
from functools import reduce
from pathlib import Path


def part1(contents):
    mtx = []
    for i, rowline in enumerate(map(str.strip, contents.split('\n'))):
        mtx.append(list(map(int, rowline)))

    m, n = len(mtx), len(mtx[0])

    risk_level_sum = 0
    for i in range(m):
        for j in range(n):
            adjacent_locations = []
            # i, j - 1
            # i, j + 1
            # i - 1, j
            # i + 1, j
            if j > 0:
                adjacent_locations.append(mtx[i][j - 1])

            if j < n - 1:
                adjacent_locations.append(mtx[i][j + 1])

            if i > 0:
                adjacent_locations.append(mtx[i - 1][j])

            if i < m - 1:
                adjacent_locations.append(mtx[i + 1][j])

            if mtx[i][j] < min(adjacent_locations):
                risk_level_sum += mtx[i][j] + 1

    print(f'Part1: total risk level: {risk_level_sum}')


def part2(contents):
    mtx = []
    for i, rowline in enumerate(map(str.strip, contents.split('\n'))):
        mtx.append(list(map(int, rowline)))

    m, n = len(mtx), len(mtx[0])

    # look for low points
    low_points = []
    for i in range(m):
        for j in range(n):
            adjacent_locations = []
            # i, j - 1
            # i, j + 1
            # i - 1, j
            # i + 1, j
            if j > 0:
                adjacent_locations.append(mtx[i][j - 1])

            if j < n - 1:
                adjacent_locations.append(mtx[i][j + 1])

            if i > 0:
                adjacent_locations.append(mtx[i - 1][j])

            if i < m - 1:
                adjacent_locations.append(mtx[i + 1][j])

            if mtx[i][j] < min(adjacent_locations):
                low_points.append((mtx[i][j], i, j))

    # look for basins
    basin_sizes = []
    for tup in low_points:
        stack = [tup]

        visited_coords = set()
        basin_size = 1  # low point itself
        while stack:
            low_point, i, j = stack.pop()

            # move down
            ii = i
            while ii < m and mtx[ii][j] < 9:
                if (
                    mtx[ii][j] > low_point
                    and mtx[ii][j] != 9
                    and (ii, j) not in visited_coords
                ):
                    print(f'appending from down {mtx[ii][j]}')
                    stack.append((mtx[ii][j], ii, j))
                    basin_size += 1
                    visited_coords.add((ii, j))
                ii += 1

            # move up
            ii = i
            while ii > -1 and mtx[ii][j] < 9:
                if (
                    mtx[ii][j] > low_point
                    and mtx[ii][j] != 9
                    and (ii, j) not in visited_coords
                ):
                    print(f'appending from up {mtx[ii][j]}')
                    stack.append((mtx[ii][j], ii, j))
                    basin_size += 1
                    visited_coords.add((ii, j))
                ii -= 1

            # move right
            jj = j
            while jj < n and mtx[i][jj] < 9:
                if (
                    mtx[i][jj] > low_point
                    and mtx[i][jj] != 9
                    and (i, jj) not in visited_coords
                ):
                    print(f'appending from right {mtx[i][jj]}')
                    stack.append((mtx[i][jj], i, jj))
                    basin_size += 1
                    visited_coords.add((i, jj))
                jj += 1

            # move left
            jj = j
            while jj > -1 and mtx[i][jj] < 9:
                if (
                    mtx[i][jj] > low_point
                    and mtx[i][jj] != 9
                    and (i, jj) not in visited_coords
                ):
                    print(f'appending from left {mtx[i][jj]}')
                    stack.append((mtx[i][jj], i, jj))
                    basin_size += 1
                    visited_coords.add((i, jj))
                jj -= 1

        print(f'tup: {tup} ; basin size: {basin_size}')
        print('*' * 10)
        basin_sizes.append(basin_size)

    # find three largest basins and multiply
    basin_sizes = sorted(basin_sizes)[-3:]
    result = reduce(lambda res, x: res * x, basin_sizes, 1)
    print(f'Part2: multiplier of 3 biggest basins: {result}')


if __name__ == '__main__':
    contents = Path('input.txt').read_text().strip()

    # contents = Path('input_sample.txt').read_text().strip()

    part1(contents)
    part2(contents)
